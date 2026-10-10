using System.Security.Claims;
using Microsoft.AspNetCore.Mvc;
using QuizApi.Models.DTOs;
using QuizApi.Services;

namespace QuizApi.Controllers;

[ApiController]
[Route("api/[controller]")]
public class AuthController(IAuthService authService) : ControllerBase
{
    [HttpPost("register")]
    public async Task<IActionResult> Register([FromBody] RegisterRequest request)
    {
        if (!ModelState.IsValid) return BadRequest(ModelState);

        var user = await authService.RegisterAsync(request);
        if (user == null)
            return Conflict(new { message = "Username hoặc Email đã tồn tại." });

        return Ok(new { message = "Đăng ký thành công!", user });
    }

    [HttpPost("login")]
    public async Task<IActionResult> Login([FromBody] LoginRequest request)
    {
        var result = await authService.LoginAsync(request);
        if (result == null)
            return Unauthorized(new { message = "Tên đăng nhập hoặc mật khẩu không đúng." });

        return Ok(result);
    }

    [HttpGet("me")]
    [Microsoft.AspNetCore.Authorization.Authorize]
    public IActionResult Me()
    {
        var userId = User.FindFirst(ClaimTypes.NameIdentifier)?.Value;
        var username = User.FindFirst(ClaimTypes.Name)?.Value;
        var role = User.FindFirst(ClaimTypes.Role)?.Value;
        var fullName = User.FindFirst("fullName")?.Value;
        var email = User.FindFirst(ClaimTypes.Email)?.Value;

        return Ok(new { userId, username, role, fullName, email });
    }
}
