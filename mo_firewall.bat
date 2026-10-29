@echo off
chcp 65001 >nul
title Mở Port Tường Lửa Cho QuizAI
echo ======================================================================
echo         TỰ ĐỘNG MỞ CỔNG TƯỜNG LỬA (PORT 5000 VÀ 5173)
echo ======================================================================
echo.
echo Đang thêm quy tắc cho phép các máy khác kết nối đến Port 5000 và 5173...
netsh advfirewall firewall delete rule name="QuizAI_Inbound" >nul 2>&1
netsh advfirewall firewall add rule name="QuizAI_Inbound" dir=in action=allow protocol=TCP localport=5000,5173

if %errorlevel% equ 0 (
    echo.
    echo [THÀNH CÔNG] Đã mở cổng tường lửa cho QuizAI thành công!
    echo Bây giờ các máy khác cùng mạng Wi-Fi đã có thể kết nối vào máy bạn.
) else (
    echo.
    echo [LỖI] Bạn cần nhấn CHUỘT PHẢI vào file này và chọn "Run as administrator"!
)
echo.
pause
