using System.IdentityModel.Tokens.Jwt;
using System.Security.Claims;
using System.Text;
using Microsoft.EntityFrameworkCore;
using Microsoft.IdentityModel.Tokens;
using QuizApi.Data;
using QuizApi.Models.DTOs;
using QuizApi.Models.Entities;

namespace QuizApi.Services;

public interface IAuthService
{
    Task<AuthResponse?> LoginAsync(LoginRequest request);
    Task<UserDto?> RegisterAsync(RegisterRequest request);
    UserDto? GetUserFromToken(string token);
}

public class AuthService(AppDbContext db, IConfiguration config) : IAuthService
{
    public async Task<UserDto?> RegisterAsync(RegisterRequest request)
    {
        if (await db.Users.AnyAsync(u => u.Username == request.Username || u.Email == request.Email))
            return null;

        var user = new User
        {
            Username = request.Username,
            Email = request.Email,
            PasswordHash = BCrypt.Net.BCrypt.HashPassword(request.Password),
            FullName = request.FullName,
            Role = UserRole.STUDENT
        };

        db.Users.Add(user);
        await db.SaveChangesAsync();

        return MapToDto(user);
    }

    public async Task<AuthResponse?> LoginAsync(LoginRequest request)
    {
        var user = await db.Users.FirstOrDefaultAsync(u => u.Username == request.Username);
        if (user == null || !user.IsActive) return null;
        if (!BCrypt.Net.BCrypt.Verify(request.Password, user.PasswordHash)) return null;

        user.LastLoginAt = DateTime.UtcNow;
        await db.SaveChangesAsync();

        var token = GenerateJwtToken(user);
        return new AuthResponse(token, Guid.NewGuid().ToString(), MapToDto(user));
    }

    public UserDto? GetUserFromToken(string token)
    {
        // simplified - in prod use token validation
        return null;
    }

    private string GenerateJwtToken(User user)
    {
        var jwtSettings = config.GetSection("JwtSettings");
        var key = new SymmetricSecurityKey(Encoding.UTF8.GetBytes(jwtSettings["SecretKey"]!));
        var creds = new SigningCredentials(key, SecurityAlgorithms.HmacSha256);

        var claims = new[]
        {
            new Claim(ClaimTypes.NameIdentifier, user.UserId.ToString()),
            new Claim(ClaimTypes.Name, user.Username),
            new Claim(ClaimTypes.Email, user.Email),
            new Claim(ClaimTypes.Role, user.Role.ToString()),
            new Claim("fullName", user.FullName)
        };

        var token = new JwtSecurityToken(
            issuer: jwtSettings["Issuer"],
            audience: jwtSettings["Audience"],
            claims: claims,
            expires: DateTime.UtcNow.AddHours(24),
            signingCredentials: creds
        );

        return new JwtSecurityTokenHandler().WriteToken(token);
    }

    private static UserDto MapToDto(User user) => new(
        user.UserId, user.Username, user.Email,
        user.FullName, user.Role.ToString(), user.IsActive, user.CreatedAt
    );
}
