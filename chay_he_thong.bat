@echo off
chcp 65001 >nul
title QuizAI - Khởi Động Hệ Thống Đa Máy (LAN / Web)
echo ======================================================================
echo          QUIZAI - HỆ THỐNG TRẮC NGHIỆM ONLINE TÍCH HỢP AI
echo               CHẾ ĐỘ MẠNG LAN / NHIỀU MÁY KẾT NỐI
echo ======================================================================
echo.

echo [*] Đang kiểm tra các địa chỉ IP của máy bạn...
powershell -NoProfile -Command "Get-NetIPAddress -AddressFamily IPv4 | Where-Object { $_.InterfaceAlias -notmatch 'Loopback' -and $_.IPAddress -notmatch '^169\.254\.' } | ForEach-Object { Write-Host ('   - Card [' + $_.InterfaceAlias + ']: http://' + $_.IPAddress + ':5173') -ForegroundColor Green }"
echo.
echo ----------------------------------------------------------------------
echo  HƯỚNG DẪN DÀNH CHO CÁC MÁY KHÁC (HỌC SINH / ĐIỆN THOẠI):
echo   1. Kết nối vào cùng mạng Wi-Fi với máy tính này.
echo   2. Mở trình duyệt web và nhập địa chỉ IP ở trên (Ví dụ: http://192.168.x.x:5173).
echo   3. Đăng ký tài khoản và bắt đầu làm bài trắc nghiệm!
echo ----------------------------------------------------------------------
echo.

echo [*] Đang khởi chạy Backend API (Port 5000)...
start "QuizAI - Backend API (Port 5000)" cmd /k "cd Backend && dotnet run --urls=http://0.0.0.0:5000"

echo [*] Đang khởi chạy Frontend Vite (Port 5173)...
start "QuizAI - Frontend Web (Port 5173)" cmd /k "cd Frontend && npm run dev"

echo.
echo ======================================================================
echo  ĐÃ KHỞI CHẠY XONG CẢ 2 TIẾN TRÌNH TRONG 2 CỬA SỔ RIÊNG BIỆT!
echo  Nếu máy khác không kết nối được, hãy mở PowerShell (Admin) và chạy:
echo  netsh advfirewall firewall add rule name="QuizAI" dir=in action=allow protocol=TCP localport=5000,5173
echo ======================================================================
echo.
pause
