namespace QuizApi.Models.Entities;

public class Submission
{
    public int SubmissionId { get; set; }

    public int UserId { get; set; }

    public int ExamId { get; set; }

    public DateTime StartedAt { get; set; } = DateTime.UtcNow;

    public DateTime? SubmittedAt { get; set; }

    public decimal TotalScore { get; set; } = 0;

    public int TotalQuestions { get; set; } = 0;

    public int CorrectAnswers { get; set; } = 0;

    public int TimeTaken { get; set; } = 0; // seconds

    public SubmissionStatus Status { get; set; } = SubmissionStatus.IN_PROGRESS;

    // Navigation
    public User User { get; set; } = null!;
    public Exam Exam { get; set; } = null!;
    public ICollection<SubmissionDetail> Details { get; set; } = [];
}

public enum SubmissionStatus { IN_PROGRESS, COMPLETED, TIMEOUT }
