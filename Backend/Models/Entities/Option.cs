using System.ComponentModel.DataAnnotations;

namespace QuizApi.Models.Entities;

public class Option
{
    public int OptionId { get; set; }

    public int QuestionId { get; set; }

    [Required, MaxLength(1)]
    public string OptionLabel { get; set; } = string.Empty; // A, B, C, D

    public string OptionText { get; set; } = string.Empty;

    public bool IsCorrect { get; set; } = false;

    // Navigation
    public Question Question { get; set; } = null!;
    public ICollection<SubmissionDetail> SubmissionDetails { get; set; } = [];
}
