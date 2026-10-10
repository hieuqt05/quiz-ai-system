using Microsoft.EntityFrameworkCore;
using QuizApi.Data;
using QuizApi.Models.DTOs;
using QuizApi.Models.Entities;

namespace QuizApi.Services;

public interface IStatsService
{
    Task<ExamStatsDto?> GetExamStatsAsync(int examId);
    Task<List<SubmissionResultDto>> GetExamSubmissionsAsync(int examId);
    Task<List<UserDto>> GetAllUsersAsync();
    Task<bool> ToggleUserActiveAsync(int userId);
}

public class StatsService(AppDbContext db) : IStatsService
{
    public async Task<ExamStatsDto?> GetExamStatsAsync(int examId)
    {
        var exam = await db.Exams.FindAsync(examId);
        if (exam == null) return null;

        var submissions = await db.Submissions
            .Where(s => s.ExamId == examId && s.Status == SubmissionStatus.COMPLETED)
            .ToListAsync();

        if (submissions.Count == 0)
            return new ExamStatsDto(examId, exam.Title, 0, 0, 0, 0, 0);

        var avgScore = submissions.Average(s => (double)s.TotalScore);
        var passRate = submissions.Count(s => s.TotalScore >= exam.PassScore) * 100.0 / submissions.Count;

        return new ExamStatsDto(
            examId, exam.Title,
            submissions.Count,
            Math.Round((decimal)avgScore, 2),
            Math.Round((decimal)passRate, 2),
            submissions.Max(s => s.TotalScore),
            submissions.Min(s => s.TotalScore)
        );
    }

    public async Task<List<SubmissionResultDto>> GetExamSubmissionsAsync(int examId)
    {
        var submissions = await db.Submissions
            .Include(s => s.Exam)
            .Include(s => s.User)
            .Where(s => s.ExamId == examId && s.Status == SubmissionStatus.COMPLETED)
            .OrderByDescending(s => s.SubmittedAt)
            .ToListAsync();

        return submissions.Select(s => new SubmissionResultDto(
            s.SubmissionId, $"{s.User.FullName} ({s.User.Username})",
            s.TotalScore, s.TotalQuestions, s.CorrectAnswers,
            s.TimeTaken, s.Status.ToString(),
            s.SubmittedAt ?? DateTime.UtcNow, []
        )).ToList();
    }

    public async Task<List<UserDto>> GetAllUsersAsync()
    {
        return await db.Users
            .Select(u => new UserDto(u.UserId, u.Username, u.Email, u.FullName,
                u.Role.ToString(), u.IsActive, u.CreatedAt))
            .ToListAsync();
    }

    public async Task<bool> ToggleUserActiveAsync(int userId)
    {
        var user = await db.Users.FindAsync(userId);
        if (user == null) return false;
        user.IsActive = !user.IsActive;
        await db.SaveChangesAsync();
        return true;
    }
}
