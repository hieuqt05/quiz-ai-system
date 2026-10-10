using Microsoft.EntityFrameworkCore;
using QuizApi.Data;
using QuizApi.Models.DTOs;
using QuizApi.Models.Entities;

namespace QuizApi.Services;

public interface IQuizService
{
    Task<int> StartSubmissionAsync(int userId, int examId);
    Task<SubmissionResultDto?> SubmitExamAsync(SubmitExamRequest request, int userId);
    Task<SubmissionResultDto?> GetResultAsync(int submissionId, int userId);
    Task<List<SubmissionResultDto>> GetUserHistoryAsync(int userId);
}

public class QuizService(AppDbContext db) : IQuizService
{
    public async Task<int> StartSubmissionAsync(int userId, int examId)
    {
        // Check if already in progress
        var existing = await db.Submissions.FirstOrDefaultAsync(
            s => s.UserId == userId && s.ExamId == examId && s.Status == SubmissionStatus.IN_PROGRESS);

        if (existing != null) return existing.SubmissionId;

        var exam = await db.Exams
            .Include(e => e.Questions.Where(q => q.Status == QuestionStatus.APPROVED))
            .FirstOrDefaultAsync(e => e.ExamId == examId && e.Status == ExamStatus.PUBLISHED);

        if (exam == null) throw new InvalidOperationException("Exam not found or not published.");

        var submission = new Submission
        {
            UserId = userId,
            ExamId = examId,
            StartedAt = DateTime.UtcNow,
            TotalQuestions = exam.Questions.Count,
            Status = SubmissionStatus.IN_PROGRESS
        };

        db.Submissions.Add(submission);
        await db.SaveChangesAsync();
        return submission.SubmissionId;
    }

    public async Task<SubmissionResultDto?> SubmitExamAsync(SubmitExamRequest request, int userId)
    {
        var submission = await db.Submissions
            .Include(s => s.Exam)
            .FirstOrDefaultAsync(s => s.SubmissionId == request.SubmissionId && s.UserId == userId);

        if (submission == null || submission.Status != SubmissionStatus.IN_PROGRESS) return null;

        var questionIds = request.Answers.Select(a => a.QuestionId).ToList();
        var questions = await db.Questions
            .Include(q => q.Options)
            .Where(q => questionIds.Contains(q.QuestionId))
            .ToListAsync();

        int correct = 0;
        var details = new List<SubmissionDetail>();

        foreach (var answer in request.Answers)
        {
            var question = questions.FirstOrDefault(q => q.QuestionId == answer.QuestionId);
            if (question == null) continue;

            bool isCorrect = false;
            if (answer.SelectedOptionId.HasValue)
            {
                var selectedOpt = question.Options.FirstOrDefault(o => o.OptionId == answer.SelectedOptionId.Value);
                isCorrect = selectedOpt?.IsCorrect ?? false;
            }

            if (isCorrect) correct++;

            details.Add(new SubmissionDetail
            {
                SubmissionId = submission.SubmissionId,
                QuestionId = answer.QuestionId,
                SelectedOptionId = answer.SelectedOptionId,
                IsCorrect = isCorrect
            });
        }

        submission.CorrectAnswers = correct;
        submission.TotalQuestions = questions.Count;
        submission.TotalScore = questions.Count > 0
            ? Math.Round((decimal)correct / questions.Count * 100, 2)
            : 0;
        submission.SubmittedAt = DateTime.UtcNow;
        submission.TimeTaken = (int)(submission.SubmittedAt.Value - submission.StartedAt).TotalSeconds;
        submission.Status = SubmissionStatus.COMPLETED;

        db.SubmissionDetails.AddRange(details);
        await db.SaveChangesAsync();

        return await BuildResultDto(submission, questions, details);
    }

    public async Task<SubmissionResultDto?> GetResultAsync(int submissionId, int userId)
    {
        var submission = await db.Submissions
            .Include(s => s.Exam)
            .Include(s => s.Details)
                .ThenInclude(d => d.Question)
                    .ThenInclude(q => q.Options)
            .FirstOrDefaultAsync(s => s.SubmissionId == submissionId && s.UserId == userId);

        if (submission == null) return null;

        var questions = submission.Details.Select(d => d.Question).ToList();
        return await BuildResultDto(submission, questions, submission.Details.ToList());
    }

    public async Task<List<SubmissionResultDto>> GetUserHistoryAsync(int userId)
    {
        var submissions = await db.Submissions
            .Include(s => s.Exam)
            .Where(s => s.UserId == userId && s.Status == SubmissionStatus.COMPLETED)
            .OrderByDescending(s => s.SubmittedAt)
            .ToListAsync();

        return submissions.Select(s => new SubmissionResultDto(
            s.SubmissionId, s.Exam.Title, s.TotalScore,
            s.TotalQuestions, s.CorrectAnswers, s.TimeTaken,
            s.Status.ToString(), s.SubmittedAt ?? DateTime.UtcNow,
            []
        )).ToList();
    }

    private static Task<SubmissionResultDto> BuildResultDto(
        Submission submission, List<Question> questions, List<SubmissionDetail> details)
    {
        var answerResults = questions.Select(q =>
        {
            var detail = details.FirstOrDefault(d => d.QuestionId == q.QuestionId);
            var correctOption = q.Options.FirstOrDefault(o => o.IsCorrect);
            var selectedOption = detail?.SelectedOptionId.HasValue == true
                ? q.Options.FirstOrDefault(o => o.OptionId == detail.SelectedOptionId)
                : null;

            return new AnswerResultDto(
                q.QuestionId, q.QuestionText, q.Explanation,
                selectedOption?.OptionLabel,
                correctOption?.OptionLabel ?? "",
                detail?.IsCorrect ?? false,
                q.Options.OrderBy(o => o.OptionLabel)
                         .Select(o => new OptionDto(o.OptionId, o.OptionLabel, o.OptionText, o.IsCorrect))
                         .ToList()
            );
        }).ToList();

        return Task.FromResult(new SubmissionResultDto(
            submission.SubmissionId,
            submission.Exam?.Title ?? "",
            submission.TotalScore,
            submission.TotalQuestions,
            submission.CorrectAnswers,
            submission.TimeTaken,
            submission.Status.ToString(),
            submission.SubmittedAt ?? DateTime.UtcNow,
            answerResults
        ));
    }
}
