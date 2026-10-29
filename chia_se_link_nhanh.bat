@echo off
chcp 65001 >nul
title QuizAI - Chia Sẻ Link Online Bằng Pinggy
echo ======================================================================
echo       TẠO ĐƯỜNG LINK ONLINE CHO BẠN BÈ / ĐIỆN THOẠI TRUY CẬP
echo ======================================================================
echo.
echo [*] Lưu ý: Hãy đảm bảo bạn đã bật Backend và Frontend trước (file chay_he_thong.bat).
echo [*] Đang kết nối tạo link công khai qua giao thức SSH an toàn...
echo [*] Khi thành công, trên màn hình sẽ xuất hiện:
echo     - Đường link "https://xxxx.a.pinggy.io" (dành cho laptop)
echo     - Mã QR Code (dành cho điện thoại quét bằng Camera)
echo.
echo ----------------------------------------------------------------------
echo.

ssh -p 443 -R0:localhost:5173 -o StrictHostKeyChecking=no a.pinggy.io

pause
