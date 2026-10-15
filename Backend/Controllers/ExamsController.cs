using System.Security.Claims;
using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Mvc;
using QuizApi.Models.DTOs;
using QuizApi.Services;

namespace QuizApi.Controllers;

[ApiController]
[Route("api/[controller]")]
public class ExamsController(IExamService examService) : ControllerBase
{
    private int CurrentUserId => int.Parse(User.FindFirst(ClaimTypes.NameIdentifier)?.Value ?? "0");

    [HttpGet]
    public async Task<IActionResult> GetPublished()
    {
        var exams = await examService.GetPublishedExamsAsync();
        return Ok(exams);
    }

    [HttpGet("all")]
    [Authorize(Roles = "TEACHER,ADMIN")]
    public async Task<IActionResult> GetAll()
    {
        var exams = await examService.GetAllExamsAsync();
        return Ok(exams);
    }

    [HttpGet("{id}")]
    [Authorize]
    public async Task<IActionResult> GetDetail(int id)
    {
        var isAdmin = User.IsInRole("TEACHER") || User.IsInRole("ADMIN");
        var exam = await examService.GetExamDetailAsync(id, isAdmin);
        if (exam == null) return NotFound();
        return Ok(exam);
    }

    [HttpPost]
    [Authorize(Roles = "TEACHER,ADMIN")]
    public async Task<IActionResult> Create([FromBody] CreateExamRequest request)
    {
        if (!ModelState.IsValid) return BadRequest(ModelState);
        var exam = await examService.CreateExamAsync(request, CurrentUserId);
        return CreatedAtAction(nameof(GetDetail), new { id = exam.ExamId }, exam);
    }

    [HttpPatch("{id}/publish")]
    [Authorize(Roles = "TEACHER,ADMIN")]
    public async Task<IActionResult> Publish(int id)
    {
        var success = await examService.PublishExamAsync(id);
        if (!success) return NotFound();
        return Ok(new { message = "Đề thi đã được công bố." });
    }

    [HttpPatch("{id}/archive")]
    [Authorize(Roles = "ADMIN")]
    public async Task<IActionResult> Archive(int id)
    {
        var success = await examService.ArchiveExamAsync(id);
        if (!success) return NotFound();
        return Ok(new { message = "Đề thi đã được lưu trữ." });
    }

    [HttpDelete("{id}")]
    [Authorize(Roles = "TEACHER,ADMIN")]
    public async Task<IActionResult> Delete(int id)
    {
        var success = await examService.DeleteExamAsync(id);
        if (!success) return NotFound(new { message = "Không tìm thấy đề thi cần xóa." });
        return Ok(new { message = "Đã xóa đề thi thành công." });
    }

    [HttpPost("{examId}/questions")]
    [Authorize(Roles = "TEACHER,ADMIN")]
    public async Task<IActionResult> AddQuestion(int examId, [FromBody] CreateQuestionRequest request)
    {
        if (!ModelState.IsValid) return BadRequest(ModelState);
        var question = await examService.AddQuestionAsync(examId, request, CurrentUserId);
        return Ok(question);
    }

    [HttpGet("questions/pending")]
    [Authorize(Roles = "TEACHER,ADMIN")]
    public async Task<IActionResult> GetPendingQuestions([FromQuery] int? examId)
    {
        var questions = await examService.GetPendingQuestionsAsync(examId);
        return Ok(questions);
    }

    [HttpPatch("questions/{questionId}/approve")]
    [Authorize(Roles = "TEACHER,ADMIN")]
    public async Task<IActionResult> ApproveQuestion(int questionId)
    {
        var success = await examService.ApproveQuestionAsync(questionId);
        if (!success) return NotFound();
        return Ok(new { message = "Câu hỏi đã được duyệt." });
    }

    [HttpPatch("questions/{questionId}/reject")]
    [Authorize(Roles = "TEACHER,ADMIN")]
    public async Task<IActionResult> RejectQuestion(int questionId)
    {
        var success = await examService.RejectQuestionAsync(questionId);
        if (!success) return NotFound();
        return Ok(new { message = "Câu hỏi đã bị từ chối." });
    }
}
