@echo off
chcp 65001 >nul
title QuizAI - Khởi Chạy Link Online Đám Mây (Cloudflare)
echo ======================================================================
echo          QUIZAI - KHỞI ĐỘNG HỆ THỐNG VÀ PHÁT LINK ONLINE
echo ======================================================================
echo.
echo [*] Bước 1: Khởi chạy Backend API (Port 5000)...
start "QuizAI - Backend" cmd /k "cd Backend && dotnet run --urls=http://0.0.0.0:5000"

echo [*] Bước 2: Khởi chạy Frontend React (Port 5173)...
start "QuizAI - Frontend" cmd /k "cd Frontend && npm run dev"

echo [*] Đang chờ 5 giây để 2 server khởi động...
timeout /t 5 /nobreak >nul

echo [*] Bước 3: Tạo đường link Online bảo mật HTTPS (Cloudflare)...
echo ----------------------------------------------------------------------
echo  HƯỚNG DẪN:
echo  - Một cửa sổ Cloudflare sẽ hiện lên và cấp 1 đường link dạng:
echo      https://xxxx.trycloudflare.com
echo  - Bạn chỉ cần copy link đó gửi cho thầy cô hoặc mở trên điện thoại!
echo ----------------------------------------------------------------------
echo.
start "QuizAI - Cloudflare Tunnel" cmd /k ".\cloudflared.exe tunnel --url http://localhost:5173"

pause

