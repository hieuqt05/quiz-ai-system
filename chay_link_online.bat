@echo off
chcp 65001 >nul
title QuizAI - Khởi Chạy Toàn Bộ Hệ Thống & Kết Nối Vercel Online
echo ======================================================================
echo          QUIZAI - KHỞI ĐỘNG HỆ THỐNG VÀ KẾT NỐI VERCEL ONLINE
echo ======================================================================
echo.
echo [*] Bước 1: Khởi chạy Backend API C# (Port 5000)...
start "QuizAI - Backend API (Port 5000)" cmd /k "cd Backend && dotnet run --urls=http://0.0.0.0:5000"

echo [*] Bước 2: Khởi chạy Frontend React Vite (Port 5173)...
start "QuizAI - Frontend Web (Port 5173)" cmd /k "cd Frontend && npm run dev"

echo [*] Đang chờ 5 giây để 2 server khởi động hoàn tất...
timeout /t 5 /nobreak >nul

echo.
echo [*] Bước 3: Mở đường hầm Cloudflare Tunnel bảo mật HTTPS...
start "QuizAI - Cloudflare Tunnel (Port 5000)" cmd /k ".\cloudflared.exe tunnel --url http://localhost:5000"

echo.
echo ======================================================================
echo  🌐 CÁC ĐƯỜNG LINK TRUY CẬP HỆ THỐNG CỦA BẠN:
echo.
echo   [1] Link Vercel Online toàn cầu (gửi Thầy Cô / xem thoại 4G):
echo       👉 https://quiz-ai-system.vercel.app
echo.
echo   [2] Link Chạy trực tiếp trên máy của bạn (Localhost):
echo       👉 http://localhost:5173
echo.
echo ======================================================================
echo.
echo [*] Đang tự động mở trang web Vercel trên trình duyệt của bạn...
start https://quiz-ai-system.vercel.app

pause
