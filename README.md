# QuizAI - Hệ Thống Trắc Nghiệm Online Tích Hợp AI

Dự án đã được khởi tạo hoàn chỉnh bao gồm Backend (ASP.NET Core Web API) và Frontend (React + Vite + TailwindCSS).

## 🚀 Hướng Dẫn Chạy Dự Án

### 1. Cấu hình Backend (Gemini API Key)
Mở tệp `Backend/appsettings.json` và thay thế `"YOUR_GEMINI_API_KEY_HERE"` bằng API Key thực tế của bạn từ Google AI Studio.
Nếu bạn không cập nhật API Key, tính năng tạo câu hỏi bằng AI sẽ báo lỗi 500.

### 2. Khởi chạy Backend
Mở một terminal mới, chuyển hướng vào thư mục `Backend` và chạy:
```bash
cd Backend
dotnet run --urls="http://localhost:5000"
```
*Lưu ý: Hệ thống sử dụng SQL Server LocalDB. Các bảng và dữ liệu mẫu (Tài khoản Admin) sẽ tự động được tạo khi Backend khởi chạy lần đầu tiên.*

### 3. Khởi chạy Frontend
Mở một terminal khác, chuyển hướng vào thư mục `Frontend` và chạy:
```bash
cd Frontend
npm run dev
```
Trang web sẽ chạy tại địa chỉ: `http://localhost:5173/`

---

## 🔐 Tài khoản Demo

- **Admin / Giáo viên**:
  - Tên đăng nhập: `admin`
  - Mật khẩu: `Admin@123`
- **Học sinh**:
  - Bạn có thể nhấn nút "Đăng ký" trên giao diện để tự tạo một tài khoản học sinh.

---

## ✨ Tính Năng Nổi Bật

1. **AI Tạo Câu Hỏi**: Quản trị viên nhập văn bản/chủ đề, Gemini AI sẽ tự động sinh câu hỏi trắc nghiệm kèm đáp án và lời giải thích.
2. **Duyệt Câu Hỏi**: Quản trị viên kiểm duyệt, chỉnh sửa câu hỏi do AI tạo trước khi đưa vào đề thi.
3. **Làm Bài Trắc Nghiệm**: Học sinh tham gia thi với đồng hồ đếm ngược, nộp bài, xem điểm ngay lập tức.
4. **Giải Thích Chi Tiết**: Sau khi làm bài, học sinh có thể xem đáp án đúng kèm lời giải thích tại sao đáp án đó đúng.
5. **Thống Kê**: Quản trị viên xem số liệu phổ điểm, tỷ lệ đạt của từng đề thi.

---

**Lưu ý**: Hãy đảm bảo bạn đã cài đặt SQL Server hoặc SQL Server Express (localdb) trên máy để cơ sở dữ liệu có thể hoạt động được.
