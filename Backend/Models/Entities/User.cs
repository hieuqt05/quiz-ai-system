using System.ComponentModel.DataAnnotations;

namespace QuizApi.Models.Entities;

public class User
{
    public int UserId { get; set; }

    [Required, MaxLength(100)]
    public string Username { get; set; } = string.Empty;

    [Required, MaxLength(200)]
    public string Email { get; set; } = string.Empty;

    [Required]
    public string PasswordHash { get; set; } = string.Empty;

    [MaxLength(200)]
    public string FullName { get; set; } = string.Empty;

    public UserRole Role { get; set; } = UserRole.STUDENT;

    public bool IsActive { get; set; } = true;

    public DateTime CreatedAt { get; set; } = DateTime.UtcNow;

    public DateTime? LastLoginAt { get; set; }

    // Navigation properties
    public ICollection<Exam> CreatedExams { get; set; } = [];
    public ICollection<Submission> Submissions { get; set; } = [];
}

public enum UserRole
{
    STUDENT,
    TEACHER,
    ADMIN
}
