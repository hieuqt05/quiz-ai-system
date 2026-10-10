using System.Security.Claims;
using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Mvc;
using QuizApi.Models.DTOs;
using QuizApi.Services;

namespace QuizApi.Controllers;

[ApiController]
[Route("api/[controller]")]
[Authorize(Roles = "TEACHER,ADMIN")]
public class AIController(IAIService aiService) : ControllerBase
{
    private int CurrentUserId => int.Parse(User.FindFirst(ClaimTypes.NameIdentifier)?.Value ?? "0");

    [HttpPost("generate")]
    public async Task<IActionResult> Generate([FromBody] AIGenerateRequest request)
    {
        if (!ModelState.IsValid) return BadRequest(ModelState);

        // Sanitize input length
        if (request.Content.Length > 15000)
            return BadRequest(new { message = "Nội dung quá dài (tối đa 15,000 ký tự)." });

        var response = await aiService.GenerateQuestionsAsync(request, CurrentUserId);

        if (!response.Success)
            return StatusCode(500, new { message = response.ErrorMessage });

        return Ok(response);
    }
}
