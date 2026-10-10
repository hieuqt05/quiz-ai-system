using System.ComponentModel.DataAnnotations;

namespace QuizApi.Models.DTOs;

// ---- AUTH ----
public record RegisterRequest(
    [Required, MinLength(3), MaxLength(100)] string Username,
    [Required, EmailAddress] string Email,
    [Required, MinLength(6)] string Password,
    [Required, MaxLength(200)] string FullName
);

public record LoginRequest(
    [Required] string Username,
    [Required] string Password
);

public record AuthResponse(
    string Token,
    string RefreshToken,
    UserDto User
);

// ---- USER ----
public record UserDto(
    int UserId,
    string Username,
    string Email,
    string FullName,
    string Role,
    bool IsActive,
    DateTime CreatedAt
);

// ---- EXAM ----
public record CreateExamRequest(
    [Required, MaxLength(300)] string Title,
    string Description,
    int DurationMinutes,
    decimal PassScore,
    string Category
);

public record ExamDto(
    int ExamId,
    string Title,
    string Description,
    int DurationMinutes,
    decimal PassScore,
    string Status,
    string Category,
    int QuestionCount,
    DateTime CreatedAt,
    string CreatorName
);

public record ExamDetailDto(
    int ExamId,
    string Title,
    string Description,
    int DurationMinutes,
    decimal PassScore,
    string Status,
    string Category,
    DateTime CreatedAt,
    List<QuestionDto> Questions
);

// ---- QUESTION ----
public record CreateQuestionRequest(
    [Required] string QuestionText,
    string Explanation,
    string Difficulty,
    [Required] List<CreateOptionRequest> Options
);

public record CreateOptionRequest(
    [Required, MaxLength(1)] string OptionLabel,
    [Required] string OptionText,
    bool IsCorrect
);

public record QuestionDto(
    int QuestionId,
    string QuestionText,
    string Explanation,
    string Difficulty,
    string SourceType,
    string Status,
    int OrderIndex,
    List<OptionDto> Options
);

public record OptionDto(
    int OptionId,
    string OptionLabel,
    string OptionText,
    bool IsCorrect
);

// ---- AI ----
public record AIGenerateRequest(
    [Required] int ExamId,
    [Required] string InputType, // DOCUMENT_TEXT | TOPIC
    [Required] string Content,
    [Range(1, 30)] int NumQuestions = 10,
    string Difficulty = "MEDIUM"
);

public record AIGenerateResponse(
    bool Success,
    int GeneratedCount,
    int PendingReview,
    string? ErrorMessage,
    List<QuestionDto>? Questions
);

// ---- AI Internal ----
public record AIQuestionItem(
    string QuestionText,
    string Difficulty,
    string Explanation,
    List<AIOptionItem> Options
);

public record AIOptionItem(
    string Label,
    string Text,
    bool IsCorrect
);

public record AIRawResponse(List<AIQuestionItem> Questions);

// ---- SUBMISSION ----
public record StartSubmissionRequest(
    [Required] int ExamId
);

public record SubmitAnswerRequest(
    [Required] int QuestionId,
    int? SelectedOptionId
);

public record SubmitExamRequest(
    [Required] int SubmissionId,
    [Required] List<SubmitAnswerRequest> Answers
);

public record SubmissionResultDto(
    int SubmissionId,
    string ExamTitle,
    decimal TotalScore,
    int TotalQuestions,
    int CorrectAnswers,
    int TimeTaken,
    string Status,
    DateTime SubmittedAt,
    List<AnswerResultDto> Details
);

public record AnswerResultDto(
    int QuestionId,
    string QuestionText,
    string Explanation,
    string? SelectedLabel,
    string CorrectLabel,
    bool IsCorrect,
    List<OptionDto> Options
);

// ---- STATS ----
public record ExamStatsDto(
    int ExamId,
    string ExamTitle,
    int TotalAttempts,
    decimal AverageScore,
    decimal PassRate,
    decimal HighestScore,
    decimal LowestScore
);
