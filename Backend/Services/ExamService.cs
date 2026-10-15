using Microsoft.EntityFrameworkCore;
using QuizApi.Data;
using QuizApi.Models.DTOs;
using QuizApi.Models.Entities;

namespace QuizApi.Services;

public interface IExamService
{
    Task<List<ExamDto>> GetPublishedExamsAsync();
    Task<List<ExamDto>> GetAllExamsAsync();
    Task<ExamDetailDto?> GetExamDetailAsync(int examId, bool includeAllQuestions = false);
    Task<ExamDto> CreateExamAsync(CreateExamRequest request, int createdBy);
    Task<bool> PublishExamAsync(int examId);
    Task<bool> ArchiveExamAsync(int examId);
    Task<bool> DeleteExamAsync(int examId);
    Task<QuestionDto> AddQuestionAsync(int examId, CreateQuestionRequest request, int createdBy);
    Task<bool> ApproveQuestionAsync(int questionId);
    Task<bool> RejectQuestionAsync(int questionId);
    Task<List<QuestionDto>> GetPendingQuestionsAsync(int? examId = null);
}

public class ExamService(AppDbContext db) : IExamService
{
    public async Task<List<ExamDto>> GetPublishedExamsAsync()
    {
        return await db.Exams
            .Where(e => e.Status == ExamStatus.PUBLISHED)
            .Include(e => e.Creator)
            .Include(e => e.Questions.Where(q => q.Status == QuestionStatus.APPROVED))
            .Select(e => MapToDto(e))
            .ToListAsync();
    }

    public async Task<List<ExamDto>> GetAllExamsAsync()
    {
        return await db.Exams
            .Include(e => e.Creator)
            .Include(e => e.Questions)
            .Select(e => MapToDto(e))
            .ToListAsync();
    }

    public async Task<ExamDetailDto?> GetExamDetailAsync(int examId, bool includeAllQuestions = false)
    {
        var exam = await db.Exams
            .Include(e => e.Creator)
            .Include(e => e.Questions.Where(q => includeAllQuestions || q.Status == QuestionStatus.APPROVED))
            .ThenInclude(q => q.Options)
            .FirstOrDefaultAsync(e => e.ExamId == examId);

        if (exam == null) return null;

        var questions = exam.Questions
            .OrderBy(q => q.OrderIndex)
            .Select(q => MapQuestionToDto(q))
            .ToList();

        return new ExamDetailDto(
            exam.ExamId, exam.Title, exam.Description,
            exam.DurationMinutes, exam.PassScore,
            exam.Status.ToString(), exam.Category,
            exam.CreatedAt, questions
        );
    }

    public async Task<ExamDto> CreateExamAsync(CreateExamRequest request, int createdBy)
    {
        var exam = new Exam
        {
            Title = request.Title,
            Description = request.Description,
            DurationMinutes = request.DurationMinutes,
            PassScore = request.PassScore,
            Category = request.Category,
            CreatedBy = createdBy,
            Status = ExamStatus.DRAFT
        };

        db.Exams.Add(exam);
        await db.SaveChangesAsync();
        await db.Entry(exam).Reference(e => e.Creator).LoadAsync();

        return MapToDto(exam);
    }

    public async Task<bool> PublishExamAsync(int examId)
    {
        var exam = await db.Exams.FindAsync(examId);
        if (exam == null) return false;
        exam.Status = ExamStatus.PUBLISHED;
        exam.PublishedAt = DateTime.UtcNow;
        await db.SaveChangesAsync();
        return true;
    }

    public async Task<bool> ArchiveExamAsync(int examId)
    {
        var exam = await db.Exams.FindAsync(examId);
        if (exam == null) return false;
        exam.Status = ExamStatus.ARCHIVED;
        await db.SaveChangesAsync();
        return true;
    }

    public async Task<bool> DeleteExamAsync(int examId)
    {
        var exam = await db.Exams.FindAsync(examId);
        if (exam == null) return false;

        // 1. Xóa chi tiết bài nộp và bài nộp liên quan
        var submissions = await db.Submissions
            .Where(s => s.ExamId == examId)
            .Include(s => s.Details)
            .ToListAsync();

        if (submissions.Count != 0)
        {
            db.SubmissionDetails.RemoveRange(submissions.SelectMany(s => s.Details));
            db.Submissions.RemoveRange(submissions);
        }

        // 2. Xóa các lựa chọn (options) và câu hỏi thuộc đề thi
        var questions = await db.Questions
            .Where(q => q.ExamId == examId)
            .Include(q => q.Options)
            .ToListAsync();

        if (questions.Count != 0)
        {
            db.Options.RemoveRange(questions.SelectMany(q => q.Options));
            db.Questions.RemoveRange(questions);
        }

        // 3. Gỡ liên kết đề thi khỏi nhật ký tạo câu hỏi AI (nếu có)
        var aiLogs = await db.AIGenerationLogs.Where(l => l.ExamId == examId).ToListAsync();
        foreach (var log in aiLogs)
        {
            log.ExamId = null;
        }

        // 4. Xóa đề thi
        db.Exams.Remove(exam);
        await db.SaveChangesAsync();
        return true;
    }

    public async Task<QuestionDto> AddQuestionAsync(int examId, CreateQuestionRequest request, int createdBy)
    {
        var question = new Question
        {
            ExamId = examId,
            GeneratedBy = createdBy,
            QuestionText = request.QuestionText,
            Explanation = request.Explanation,
            Difficulty = Enum.Parse<DifficultyLevel>(request.Difficulty, true),
            SourceType = SourceType.MANUAL,
            Status = QuestionStatus.APPROVED,
            OrderIndex = await db.Questions.CountAsync(q => q.ExamId == examId)
        };

        db.Questions.Add(question);
        await db.SaveChangesAsync();

        foreach (var opt in request.Options)
        {
            db.Options.Add(new Option
            {
                QuestionId = question.QuestionId,
                OptionLabel = opt.OptionLabel,
                OptionText = opt.OptionText,
                IsCorrect = opt.IsCorrect
            });
        }

        await db.SaveChangesAsync();
        await db.Entry(question).Collection(q => q.Options).LoadAsync();

        return MapQuestionToDto(question);
    }

    public async Task<bool> ApproveQuestionAsync(int questionId)
    {
        var q = await db.Questions.FindAsync(questionId);
        if (q == null) return false;
        q.Status = QuestionStatus.APPROVED;
        await db.SaveChangesAsync();
        return true;
    }

    public async Task<bool> RejectQuestionAsync(int questionId)
    {
        var q = await db.Questions.FindAsync(questionId);
        if (q == null) return false;
        q.Status = QuestionStatus.REJECTED;
        await db.SaveChangesAsync();
        return true;
    }

    public async Task<List<QuestionDto>> GetPendingQuestionsAsync(int? examId = null)
    {
        var query = db.Questions
            .Include(q => q.Options)
            .Where(q => q.Status == QuestionStatus.PENDING);

        if (examId.HasValue)
            query = query.Where(q => q.ExamId == examId.Value);

        return await query.Select(q => MapQuestionToDto(q)).ToListAsync();
    }

    private static ExamDto MapToDto(Exam e) => new(
        e.ExamId, e.Title, e.Description, e.DurationMinutes,
        e.PassScore, e.Status.ToString(), e.Category,
        e.Questions.Count(q => q.Status == QuestionStatus.APPROVED),
        e.CreatedAt, e.Creator?.FullName ?? ""
    );

    private static QuestionDto MapQuestionToDto(Question q) => new(
        q.QuestionId, q.QuestionText, q.Explanation,
        q.Difficulty.ToString(), q.SourceType.ToString(),
        q.Status.ToString(), q.OrderIndex,
        q.Options.OrderBy(o => o.OptionLabel)
                 .Select(o => new OptionDto(o.OptionId, o.OptionLabel, o.OptionText, o.IsCorrect))
                 .ToList()
    );
}
