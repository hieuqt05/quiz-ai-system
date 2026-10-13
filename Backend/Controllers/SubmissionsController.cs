using System.Security.Claims;
using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Mvc;
using QuizApi.Models.DTOs;
using QuizApi.Services;

namespace QuizApi.Controllers;

[ApiController]
[Route("api/[controller]")]
[Authorize]
public class SubmissionsController(IQuizService quizService) : ControllerBase
{
    private int CurrentUserId => int.Parse(User.FindFirst(ClaimTypes.NameIdentifier)?.Value ?? "0");

    [HttpPost("start")]
    public async Task<IActionResult> Start([FromBody] StartSubmissionRequest request)
    {
        try
        {
            var result = await quizService.StartSubmissionAsync(CurrentUserId, request.ExamId);
            return Ok(result);
        }
        catch (InvalidOperationException ex)
        {
            return BadRequest(new { message = ex.Message });
        }
    }

    [HttpPost("submit")]
    public async Task<IActionResult> Submit([FromBody] SubmitExamRequest request)
    {
        var result = await quizService.SubmitExamAsync(request, CurrentUserId);
        if (result == null) return BadRequest(new { message = "Không tìm thấy bài thi hoặc đã nộp." });
        return Ok(result);
    }

    [HttpGet("{id}/result")]
    public async Task<IActionResult> GetResult(int id)
    {
        var result = await quizService.GetResultAsync(id, CurrentUserId);
        if (result == null) return NotFound();
        return Ok(result);
    }

    [HttpGet("history")]
    public async Task<IActionResult> GetHistory()
    {
        var history = await quizService.GetUserHistoryAsync(CurrentUserId);
        return Ok(history);
    }
}
