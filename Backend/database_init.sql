IF OBJECT_ID(N'[__EFMigrationsHistory]') IS NULL
BEGIN
    CREATE TABLE [__EFMigrationsHistory] (
        [MigrationId] nvarchar(150) NOT NULL,
        [ProductVersion] nvarchar(32) NOT NULL,
        CONSTRAINT [PK___EFMigrationsHistory] PRIMARY KEY ([MigrationId])
    );
END;
GO

BEGIN TRANSACTION;
CREATE TABLE [Users] (
    [UserId] int NOT NULL IDENTITY,
    [Username] nvarchar(100) NOT NULL,
    [Email] nvarchar(200) NOT NULL,
    [PasswordHash] nvarchar(max) NOT NULL,
    [FullName] nvarchar(200) NOT NULL,
    [Role] nvarchar(max) NOT NULL,
    [IsActive] bit NOT NULL,
    [CreatedAt] datetime2 NOT NULL,
    [LastLoginAt] datetime2 NULL,
    CONSTRAINT [PK_Users] PRIMARY KEY ([UserId])
);

CREATE TABLE [Exams] (
    [ExamId] int NOT NULL IDENTITY,
    [CreatedBy] int NOT NULL,
    [Title] nvarchar(300) NOT NULL,
    [Description] nvarchar(max) NOT NULL,
    [DurationMinutes] int NOT NULL,
    [PassScore] decimal(5,2) NOT NULL,
    [Status] nvarchar(max) NOT NULL,
    [Category] nvarchar(200) NOT NULL,
    [CreatedAt] datetime2 NOT NULL,
    [PublishedAt] datetime2 NULL,
    CONSTRAINT [PK_Exams] PRIMARY KEY ([ExamId]),
    CONSTRAINT [FK_Exams_Users_CreatedBy] FOREIGN KEY ([CreatedBy]) REFERENCES [Users] ([UserId]) ON DELETE NO ACTION
);

CREATE TABLE [AIGenerationLogs] (
    [LogId] int NOT NULL IDENTITY,
    [RequestedBy] int NOT NULL,
    [ExamId] int NULL,
    [InputType] nvarchar(max) NOT NULL,
    [InputContent] nvarchar(max) NOT NULL,
    [QuestionsRequested] int NOT NULL,
    [QuestionsGenerated] int NOT NULL,
    [RawAIResponse] nvarchar(max) NOT NULL,
    [TokensUsed] int NOT NULL,
    [Status] nvarchar(max) NOT NULL,
    [ErrorMessage] nvarchar(max) NULL,
    [CreatedAt] datetime2 NOT NULL,
    CONSTRAINT [PK_AIGenerationLogs] PRIMARY KEY ([LogId]),
    CONSTRAINT [FK_AIGenerationLogs_Exams_ExamId] FOREIGN KEY ([ExamId]) REFERENCES [Exams] ([ExamId]) ON DELETE SET NULL,
    CONSTRAINT [FK_AIGenerationLogs_Users_RequestedBy] FOREIGN KEY ([RequestedBy]) REFERENCES [Users] ([UserId]) ON DELETE NO ACTION
);

CREATE TABLE [Questions] (
    [QuestionId] int NOT NULL IDENTITY,
    [ExamId] int NOT NULL,
    [GeneratedBy] int NULL,
    [QuestionText] nvarchar(max) NOT NULL,
    [Explanation] nvarchar(max) NOT NULL,
    [Difficulty] nvarchar(max) NOT NULL,
    [SourceType] nvarchar(max) NOT NULL,
    [Status] nvarchar(max) NOT NULL,
    [OrderIndex] int NOT NULL,
    [CreatedAt] datetime2 NOT NULL,
    CONSTRAINT [PK_Questions] PRIMARY KEY ([QuestionId]),
    CONSTRAINT [FK_Questions_Exams_ExamId] FOREIGN KEY ([ExamId]) REFERENCES [Exams] ([ExamId]) ON DELETE CASCADE,
    CONSTRAINT [FK_Questions_Users_GeneratedBy] FOREIGN KEY ([GeneratedBy]) REFERENCES [Users] ([UserId]) ON DELETE SET NULL
);

CREATE TABLE [Submissions] (
    [SubmissionId] int NOT NULL IDENTITY,
    [UserId] int NOT NULL,
    [ExamId] int NOT NULL,
    [StartedAt] datetime2 NOT NULL,
    [SubmittedAt] datetime2 NULL,
    [TotalScore] decimal(5,2) NOT NULL,
    [TotalQuestions] int NOT NULL,
    [CorrectAnswers] int NOT NULL,
    [TimeTaken] int NOT NULL,
    [Status] nvarchar(max) NOT NULL,
    CONSTRAINT [PK_Submissions] PRIMARY KEY ([SubmissionId]),
    CONSTRAINT [FK_Submissions_Exams_ExamId] FOREIGN KEY ([ExamId]) REFERENCES [Exams] ([ExamId]) ON DELETE NO ACTION,
    CONSTRAINT [FK_Submissions_Users_UserId] FOREIGN KEY ([UserId]) REFERENCES [Users] ([UserId]) ON DELETE NO ACTION
);

CREATE TABLE [Options] (
    [OptionId] int NOT NULL IDENTITY,
    [QuestionId] int NOT NULL,
    [OptionLabel] nvarchar(1) NOT NULL,
    [OptionText] nvarchar(max) NOT NULL,
    [IsCorrect] bit NOT NULL,
    CONSTRAINT [PK_Options] PRIMARY KEY ([OptionId]),
    CONSTRAINT [FK_Options_Questions_QuestionId] FOREIGN KEY ([QuestionId]) REFERENCES [Questions] ([QuestionId]) ON DELETE CASCADE
);

CREATE TABLE [SubmissionDetails] (
    [DetailId] int NOT NULL IDENTITY,
    [SubmissionId] int NOT NULL,
    [QuestionId] int NOT NULL,
    [SelectedOptionId] int NULL,
    [IsCorrect] bit NOT NULL,
    CONSTRAINT [PK_SubmissionDetails] PRIMARY KEY ([DetailId]),
    CONSTRAINT [FK_SubmissionDetails_Options_SelectedOptionId] FOREIGN KEY ([SelectedOptionId]) REFERENCES [Options] ([OptionId]) ON DELETE SET NULL,
    CONSTRAINT [FK_SubmissionDetails_Questions_QuestionId] FOREIGN KEY ([QuestionId]) REFERENCES [Questions] ([QuestionId]) ON DELETE NO ACTION,
    CONSTRAINT [FK_SubmissionDetails_Submissions_SubmissionId] FOREIGN KEY ([SubmissionId]) REFERENCES [Submissions] ([SubmissionId]) ON DELETE CASCADE
);

IF EXISTS (SELECT * FROM [sys].[identity_columns] WHERE [name] IN (N'UserId', N'CreatedAt', N'Email', N'FullName', N'IsActive', N'LastLoginAt', N'PasswordHash', N'Role', N'Username') AND [object_id] = OBJECT_ID(N'[Users]'))
    SET IDENTITY_INSERT [Users] ON;
INSERT INTO [Users] ([UserId], [CreatedAt], [Email], [FullName], [IsActive], [LastLoginAt], [PasswordHash], [Role], [Username])
VALUES (1, '2024-01-01T00:00:00.0000000Z', N'admin@quizsystem.com', N'System Administrator', CAST(1 AS bit), NULL, N'$2a$11$saLK3O868yAvkObsaCJ1j.owClbXfZXp2dZRUlWsIIWSht3Rut4TW', N'ADMIN', N'admin');
IF EXISTS (SELECT * FROM [sys].[identity_columns] WHERE [name] IN (N'UserId', N'CreatedAt', N'Email', N'FullName', N'IsActive', N'LastLoginAt', N'PasswordHash', N'Role', N'Username') AND [object_id] = OBJECT_ID(N'[Users]'))
    SET IDENTITY_INSERT [Users] OFF;

CREATE INDEX [IX_AIGenerationLogs_ExamId] ON [AIGenerationLogs] ([ExamId]);

CREATE INDEX [IX_AIGenerationLogs_RequestedBy] ON [AIGenerationLogs] ([RequestedBy]);

CREATE INDEX [IX_Exams_CreatedBy] ON [Exams] ([CreatedBy]);

CREATE INDEX [IX_Options_QuestionId] ON [Options] ([QuestionId]);

CREATE INDEX [IX_Questions_ExamId] ON [Questions] ([ExamId]);

CREATE INDEX [IX_Questions_GeneratedBy] ON [Questions] ([GeneratedBy]);

CREATE INDEX [IX_SubmissionDetails_QuestionId] ON [SubmissionDetails] ([QuestionId]);

CREATE INDEX [IX_SubmissionDetails_SelectedOptionId] ON [SubmissionDetails] ([SelectedOptionId]);

CREATE INDEX [IX_SubmissionDetails_SubmissionId] ON [SubmissionDetails] ([SubmissionId]);

CREATE INDEX [IX_Submissions_ExamId] ON [Submissions] ([ExamId]);

CREATE INDEX [IX_Submissions_UserId] ON [Submissions] ([UserId]);

CREATE UNIQUE INDEX [IX_Users_Email] ON [Users] ([Email]);

CREATE UNIQUE INDEX [IX_Users_Username] ON [Users] ([Username]);

INSERT INTO [__EFMigrationsHistory] ([MigrationId], [ProductVersion])
VALUES (N'20261010135802_InitialCreate', N'9.0.0');

UPDATE [Users] SET [PasswordHash] = N'$2a$11$HZxVrfn4FuLvQ9jhcK5yyuk6PrxkLNqbWKpvGUqz/zTLdT6QlkFwa'
WHERE [UserId] = 1;
SELECT @@ROWCOUNT;


INSERT INTO [__EFMigrationsHistory] ([MigrationId], [ProductVersion])
VALUES (N'20261010141337_UpdateModels', N'9.0.0');

ALTER TABLE [Submissions] ADD [ViolationCount] int NOT NULL DEFAULT 0;

UPDATE [Users] SET [PasswordHash] = N'$2a$11$Ri.Jb9una4mDtAZHmj/BmeIXOV60QfsMkY1AYNsBdnirum4OIIVXO'
WHERE [UserId] = 1;
SELECT @@ROWCOUNT;


INSERT INTO [__EFMigrationsHistory] ([MigrationId], [ProductVersion])
VALUES (N'20261029033333_AddViolationCount', N'9.0.0');

COMMIT;
GO

