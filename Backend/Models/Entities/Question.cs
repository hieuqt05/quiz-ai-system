using System.ComponentModel.DataAnnotations;

namespace QuizApi.Models.Entities;

public class Question
{
    public int QuestionId { get; set; }

    public int ExamId { get; set; }

    public int? GeneratedBy { get; set; }

    public string QuestionText { get; set; } = string.Empty;

    public string Explanation { get; set; } = string.Empty;

    public DifficultyLevel Difficulty { get; set; } = DifficultyLevel.MEDIUM;

    public SourceType SourceType { get; set; } = SourceType.MANUAL;

    public QuestionStatus Status { get; set; } = QuestionStatus.APPROVED;

    public int OrderIndex { get; set; } = 0;

    public DateTime CreatedAt { get; set; } = DateTime.UtcNow;

    // Navigation
    public Exam Exam { get; set; } = null!;
    public User? GeneratedByUser { get; set; }
    public ICollection<Option> Options { get; set; } = [];
    public ICollection<SubmissionDetail> SubmissionDetails { get; set; } = [];
}

public enum DifficultyLevel { EASY, MEDIUM, HARD }
public enum SourceType { AI, MANUAL }
public enum QuestionStatus { PENDING, APPROVED, REJECTED }
