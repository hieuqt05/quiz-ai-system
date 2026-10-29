@echo off
chcp 65001 >nul
title QuizAI - Chia Sẻ Ra Internet (Cloudflare / Localtunnel)
echo ======================================================================
echo    CHIA SẺ HỆ THỐNG RA INTERNET (CHO MÁY KHÁC MẠNG / DÙNG 4G)
echo ======================================================================
echo.
echo Lưu ý: Hãy đảm bảo bạn đã chạy Backend và Frontend trước (hoặc chạy chay_he_thong.bat).
echo Đang tạo đường hầm bảo mật HTTPS ra Internet qua Cloudflare Tunnel...
echo.

npx cloudflared tunnel --url http://localhost:5173

if %errorlevel% neq 0 (
    echo.
    echo [THỬ LẠI BẰNG LOCALTUNNEL...]
    npx localtunnel --port 5173
)

pause
