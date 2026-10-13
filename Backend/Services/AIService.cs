using System.Text;
using System.Text.Json;
using Microsoft.EntityFrameworkCore;
using QuizApi.Data;
using QuizApi.Models.DTOs;
using QuizApi.Models.Entities;

namespace QuizApi.Services;

public interface IAIService
{
    Task<AIGenerateResponse> GenerateQuestionsAsync(AIGenerateRequest request, int userId);
}

public class AIService(AppDbContext db, IConfiguration config, IHttpClientFactory httpClientFactory) : IAIService
{
    private readonly string _geminiApiKey = config["GeminiApiKey"] ?? "";
    private const string GeminiUrl = "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent";

    public async Task<AIGenerateResponse> GenerateQuestionsAsync(AIGenerateRequest request, int userId)
    {
        var log = new AIGenerationLog
        {
            RequestedBy = userId,
            ExamId = request.ExamId,
            InputType = Enum.Parse<AIInputType>(request.InputType, true),
            InputContent = request.Content,
            QuestionsRequested = request.NumQuestions,
            CreatedAt = DateTime.UtcNow
        };

        try
        {
            var prompt = BuildPrompt(request);
            var rawResponse = await CallGeminiAsync(prompt);

            log.RawAIResponse = rawResponse;

            var parsed = ParseAIResponse(rawResponse);
            if (parsed == null || parsed.Questions.Count == 0)
                throw new InvalidOperationException("AI không tạo được câu hỏi hợp lệ.");

            // Validate
            ValidateQuestions(parsed.Questions);

            // Save to DB
            var savedQuestions = await SaveQuestionsAsync(parsed.Questions, request.ExamId, userId);

            log.QuestionsGenerated = savedQuestions.Count;
            log.Status = AILogStatus.SUCCESS;
            db.AIGenerationLogs.Add(log);
            await db.SaveChangesAsync();

            return new AIGenerateResponse(true, savedQuestions.Count, savedQuestions.Count, null, savedQuestions);
        }
        catch (Exception ex)
        {
            log.Status = AILogStatus.FAILED;
            log.ErrorMessage = ex.Message;
            log.QuestionsGenerated = 0;
            db.AIGenerationLogs.Add(log);
            await db.SaveChangesAsync();

            return new AIGenerateResponse(false, 0, 0, ex.Message, null);
        }
    }

    private string BuildPrompt(AIGenerateRequest request)
    {
        var inputSection = request.InputType == "TOPIC"
            ? $"Chủ đề: {request.Content}"
            : $"--- NỘI DUNG ---\n{request.Content}\n--- KẾT THÚC ---";

        return $$"""
            Bạn là chuyên gia giáo dục. Hãy tạo {{request.NumQuestions}} câu hỏi trắc nghiệm độ khó {{request.Difficulty}} dựa trên:

            {{inputSection}}

            Yêu cầu bắt buộc:
            - CHỈ trả về JSON thuần, không có markdown, không có text khác.
            - Đúng {{request.NumQuestions}} câu hỏi.
            - Mỗi câu có 4 đáp án A, B, C, D và CHỈ 1 đáp án đúng (isCorrect: true).
            - Trường 'explanation' giải thích tại sao đáp án đúng là đúng.

            JSON Schema bắt buộc:
            {
              "questions": [
                {
                  "questionText": "string",
                  "difficulty": "EASY|MEDIUM|HARD",
                  "explanation": "string",
                  "options": [
                    {"label": "A", "text": "string", "isCorrect": false},
                    {"label": "B", "text": "string", "isCorrect": true},
                    {"label": "C", "text": "string", "isCorrect": false},
                    {"label": "D", "text": "string", "isCorrect": false}
                  ]
                }
              ]
            }
            """;
    }

    private async Task<string> CallGeminiAsync(string prompt)
    {
        var client = httpClientFactory.CreateClient();
        var url = $"{GeminiUrl}?key={_geminiApiKey}";

        var body = new
        {
            contents = new[]
            {
                new { role = "user", parts = new[] { new { text = prompt } } }
            },
            generationConfig = new
            {
                temperature = 0.7,
                maxOutputTokens = 8192,
                responseMimeType = "application/json"
            }
        };

        var json = JsonSerializer.Serialize(body);
        HttpResponseMessage? response = null;
        int maxRetries = 3;

        for (int i = 0; i < maxRetries; i++)
        {
            var content = new StringContent(json, Encoding.UTF8, "application/json");
            response = await client.PostAsync(url, content);

            if (response.IsSuccessStatusCode)
                break;

            if (response.StatusCode == System.Net.HttpStatusCode.ServiceUnavailable || 
                (int)response.StatusCode == 429)
            {
                if (i == maxRetries - 1)
                    break; // give up
                await Task.Delay(2000 * (i + 1));
                continue;
            }
            break;
        }

        if (response == null || !response.IsSuccessStatusCode)
        {
            var err = response != null ? await response.Content.ReadAsStringAsync() : "No response";
            throw new HttpRequestException($"Gemini API lỗi {(response?.StatusCode)}: {err}");
        }

        var responseJson = await response.Content.ReadAsStringAsync();

        // Extract text from Gemini response structure
        using var doc = JsonDocument.Parse(responseJson);
        var parts = doc.RootElement
            .GetProperty("candidates")[0]
            .GetProperty("content")
            .GetProperty("parts");

        var sb = new StringBuilder();
        foreach (var part in parts.EnumerateArray())
        {
            if (part.TryGetProperty("text", out var textElem))
            {
                sb.Append(textElem.GetString());
            }
        }

        return sb.ToString();
    }

    private static AIRawResponse? ParseAIResponse(string rawText)
    {
        try
        {
            // Clean up markdown code blocks if present
            var text = rawText.Trim();
            if (text.StartsWith("```")) text = text.Split('\n').Skip(1).Aggregate((a, b) => a + "\n" + b);
            if (text.EndsWith("```")) text = text[..text.LastIndexOf("```")];

            return JsonSerializer.Deserialize<AIRawResponse>(text,
                new JsonSerializerOptions { PropertyNameCaseInsensitive = true });
        }
        catch
        {
            return null;
        }
    }

    private static void ValidateQuestions(List<AIQuestionItem> questions)
    {
        for (int i = 0; i < questions.Count; i++)
        {
            var q = questions[i];
            if (string.IsNullOrWhiteSpace(q.QuestionText))
                throw new InvalidOperationException($"Câu {i + 1}: QuestionText rỗng.");
            if (q.Options.Count != 4)
                throw new InvalidOperationException($"Câu {i + 1}: Phải có đúng 4 đáp án.");
            if (q.Options.Count(o => o.IsCorrect) != 1)
                throw new InvalidOperationException($"Câu {i + 1}: Phải có đúng 1 đáp án đúng.");
        }
    }

    private async Task<List<QuestionDto>> SaveQuestionsAsync(
        List<AIQuestionItem> aiQuestions, int examId, int userId)
    {
        var startIdx = await db.Questions.CountAsync(q => q.ExamId == examId);
        var result = new List<QuestionDto>();

        foreach (var (aiQ, idx) in aiQuestions.Select((q, i) => (q, i)))
        {
            var question = new Question
            {
                ExamId = examId,
                GeneratedBy = userId,
                QuestionText = aiQ.QuestionText,
                Explanation = aiQ.Explanation,
                Difficulty = Enum.TryParse<DifficultyLevel>(aiQ.Difficulty, true, out var d) ? d : DifficultyLevel.MEDIUM,
                SourceType = SourceType.AI,
                Status = QuestionStatus.PENDING,
                OrderIndex = startIdx + idx
            };

            db.Questions.Add(question);
            await db.SaveChangesAsync();

            var options = aiQ.Options.Select(o => new Option
            {
                QuestionId = question.QuestionId,
                OptionLabel = o.Label,
                OptionText = o.Text,
                IsCorrect = o.IsCorrect
            }).ToList();

            db.Options.AddRange(options);
            await db.SaveChangesAsync();

            result.Add(new QuestionDto(
                question.QuestionId, question.QuestionText, question.Explanation,
                question.Difficulty.ToString(), question.SourceType.ToString(),
                question.Status.ToString(), question.OrderIndex,
                options.Select(o => new OptionDto(o.OptionId, o.OptionLabel, o.OptionText, o.IsCorrect)).ToList()
            ));
        }

        return result;
    }
}
