namespace QuizApi.Models.Entities;

public class AIGenerationLog
{
    public int LogId { get; set; }

    public int RequestedBy { get; set; }

    public int? ExamId { get; set; }

    public AIInputType InputType { get; set; } = AIInputType.DOCUMENT_TEXT;

    public string InputContent { get; set; } = string.Empty;

    public int QuestionsRequested { get; set; }

    public int QuestionsGenerated { get; set; }

    public string RawAIResponse { get; set; } = string.Empty;

    public int TokensUsed { get; set; }

    public AILogStatus Status { get; set; } = AILogStatus.SUCCESS;

    public string? ErrorMessage { get; set; }

    public DateTime CreatedAt { get; set; } = DateTime.UtcNow;

    // Navigation
    public User Requester { get; set; } = null!;
    public Exam? Exam { get; set; }
}

public enum AIInputType { DOCUMENT_TEXT, TOPIC }
public enum AILogStatus { SUCCESS, FAILED }
