namespace QuizApi.Models.Entities;

public class SubmissionDetail
{
    public int DetailId { get; set; }

    public int SubmissionId { get; set; }

    public int QuestionId { get; set; }

    public int? SelectedOptionId { get; set; }

    public bool IsCorrect { get; set; } = false;

    // Navigation
    public Submission Submission { get; set; } = null!;
    public Question Question { get; set; } = null!;
    public Option? SelectedOption { get; set; }
}
