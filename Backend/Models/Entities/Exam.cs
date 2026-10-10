using System.ComponentModel.DataAnnotations;

namespace QuizApi.Models.Entities;

public class Exam
{
    public int ExamId { get; set; }

    public int CreatedBy { get; set; }

    [Required, MaxLength(300)]
    public string Title { get; set; } = string.Empty;

    public string Description { get; set; } = string.Empty;

    public int DurationMinutes { get; set; } = 30;

    public decimal PassScore { get; set; } = 50;

    public ExamStatus Status { get; set; } = ExamStatus.DRAFT;

    [MaxLength(200)]
    public string Category { get; set; } = string.Empty;

    public DateTime CreatedAt { get; set; } = DateTime.UtcNow;

    public DateTime? PublishedAt { get; set; }

    // Navigation
    public User Creator { get; set; } = null!;
    public ICollection<Question> Questions { get; set; } = [];
    public ICollection<Submission> Submissions { get; set; } = [];
}

public enum ExamStatus
{
    DRAFT,
    PUBLISHED,
    ARCHIVED
}
