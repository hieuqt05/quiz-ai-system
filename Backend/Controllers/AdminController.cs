using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Mvc;
using QuizApi.Services;

namespace QuizApi.Controllers;

[ApiController]
[Route("api/[controller]")]
[Authorize(Roles = "ADMIN")]
public class AdminController(IStatsService statsService) : ControllerBase
{
    [HttpGet("users")]
    public async Task<IActionResult> GetUsers()
    {
        var users = await statsService.GetAllUsersAsync();
        return Ok(users);
    }

    [HttpPatch("users/{userId}/toggle")]
    public async Task<IActionResult> ToggleUser(int userId)
    {
        var success = await statsService.ToggleUserActiveAsync(userId);
        if (!success) return NotFound();
        return Ok(new { message = "Cập nhật trạng thái thành công." });
    }

    [HttpGet("stats/exam/{examId}")]
    [Authorize(Roles = "TEACHER,ADMIN")]
    public async Task<IActionResult> GetExamStats(int examId)
    {
        var stats = await statsService.GetExamStatsAsync(examId);
        if (stats == null) return NotFound();
        return Ok(stats);
    }

    [HttpGet("stats/exam/{examId}/submissions")]
    [Authorize(Roles = "TEACHER,ADMIN")]
    public async Task<IActionResult> GetExamSubmissions(int examId)
    {
        var subs = await statsService.GetExamSubmissionsAsync(examId);
        return Ok(subs);
    }
}
