using Microsoft.EntityFrameworkCore;
using QuizApi.Models.Entities;

namespace QuizApi.Data;

public class AppDbContext(DbContextOptions<AppDbContext> options) : DbContext(options)
{
    public DbSet<User> Users => Set<User>();
    public DbSet<Exam> Exams => Set<Exam>();
    public DbSet<Question> Questions => Set<Question>();
    public DbSet<Option> Options => Set<Option>();
    public DbSet<Submission> Submissions => Set<Submission>();
    public DbSet<SubmissionDetail> SubmissionDetails => Set<SubmissionDetail>();
    public DbSet<AIGenerationLog> AIGenerationLogs => Set<AIGenerationLog>();

    protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
    {
        optionsBuilder.ConfigureWarnings(w => w.Ignore(Microsoft.EntityFrameworkCore.Diagnostics.RelationalEventId.PendingModelChangesWarning));
        base.OnConfiguring(optionsBuilder);
    }

    protected override void OnModelCreating(ModelBuilder modelBuilder)
    {
        base.OnModelCreating(modelBuilder);

        // User
        modelBuilder.Entity<User>(e =>
        {
            e.HasKey(u => u.UserId);
            e.HasIndex(u => u.Username).IsUnique();
            e.HasIndex(u => u.Email).IsUnique();
            e.Property(u => u.Role).HasConversion<string>();
        });

        // Exam
        modelBuilder.Entity<Exam>(e =>
        {
            e.HasKey(x => x.ExamId);
            e.Property(x => x.Status).HasConversion<string>();
            e.Property(x => x.PassScore).HasColumnType("decimal(5,2)");
            e.HasOne(x => x.Creator)
             .WithMany(u => u.CreatedExams)
             .HasForeignKey(x => x.CreatedBy)
             .OnDelete(DeleteBehavior.Restrict);
        });

        // Question
        modelBuilder.Entity<Question>(e =>
        {
            e.HasKey(q => q.QuestionId);
            e.Property(q => q.Difficulty).HasConversion<string>();
            e.Property(q => q.SourceType).HasConversion<string>();
            e.Property(q => q.Status).HasConversion<string>();
            e.HasOne(q => q.Exam)
             .WithMany(x => x.Questions)
             .HasForeignKey(q => q.ExamId)
             .OnDelete(DeleteBehavior.Cascade);
            e.HasOne(q => q.GeneratedByUser)
             .WithMany()
             .HasForeignKey(q => q.GeneratedBy)
             .OnDelete(DeleteBehavior.SetNull);
        });

        // Option
        modelBuilder.Entity<Option>(e =>
        {
            e.HasKey(o => o.OptionId);
            e.HasOne(o => o.Question)
             .WithMany(q => q.Options)
             .HasForeignKey(o => o.QuestionId)
             .OnDelete(DeleteBehavior.Cascade);
        });

        // Submission
        modelBuilder.Entity<Submission>(e =>
        {
            e.HasKey(s => s.SubmissionId);
            e.Property(s => s.TotalScore).HasColumnType("decimal(5,2)");
            e.Property(s => s.Status).HasConversion<string>();
            e.HasOne(s => s.User)
             .WithMany(u => u.Submissions)
             .HasForeignKey(s => s.UserId)
             .OnDelete(DeleteBehavior.Restrict);
            e.HasOne(s => s.Exam)
             .WithMany(x => x.Submissions)
             .HasForeignKey(s => s.ExamId)
             .OnDelete(DeleteBehavior.Restrict);
        });

        // SubmissionDetail
        modelBuilder.Entity<SubmissionDetail>(e =>
        {
            e.HasKey(d => d.DetailId);
            e.HasOne(d => d.Submission)
             .WithMany(s => s.Details)
             .HasForeignKey(d => d.SubmissionId)
             .OnDelete(DeleteBehavior.Cascade);
            e.HasOne(d => d.Question)
             .WithMany(q => q.SubmissionDetails)
             .HasForeignKey(d => d.QuestionId)
             .OnDelete(DeleteBehavior.Restrict);
            e.HasOne(d => d.SelectedOption)
             .WithMany(o => o.SubmissionDetails)
             .HasForeignKey(d => d.SelectedOptionId)
             .OnDelete(DeleteBehavior.SetNull);
        });

        // AIGenerationLog
        modelBuilder.Entity<AIGenerationLog>(e =>
        {
            e.HasKey(l => l.LogId);
            e.Property(l => l.InputType).HasConversion<string>();
            e.Property(l => l.Status).HasConversion<string>();
            e.HasOne(l => l.Requester)
             .WithMany()
             .HasForeignKey(l => l.RequestedBy)
             .OnDelete(DeleteBehavior.Restrict);
            e.HasOne(l => l.Exam)
             .WithMany()
             .HasForeignKey(l => l.ExamId)
             .OnDelete(DeleteBehavior.SetNull);
        });

        // Seed admin user
        modelBuilder.Entity<User>().HasData(new User
        {
            UserId = 1,
            Username = "admin",
            Email = "admin@quizsystem.com",
            PasswordHash = BCrypt.Net.BCrypt.HashPassword("Admin@123"),
            FullName = "System Administrator",
            Role = UserRole.ADMIN,
            IsActive = true,
            CreatedAt = new DateTime(2024, 1, 1, 0, 0, 0, DateTimeKind.Utc)
        });
    }
}
