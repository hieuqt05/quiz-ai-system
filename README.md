# QuizAI - Hệ Thống Trắc Nghiệm Online Tích Hợp AI

Dự án đã được khởi tạo hoàn chỉnh bao gồm Backend (ASP.NET Core Web API) và Frontend (React + Vite + TailwindCSS).

## 🚀 Hướng Dẫn Chạy Dự Án

### 1. Cấu hình Backend (Gemini API Key)
Mở tệp `Backend/appsettings.json` và thay thế `"YOUR_GEMINI_API_KEY_HERE"` bằng API Key thực tế của bạn từ Google AI Studio.
Nếu bạn không cập nhật API Key, tính năng tạo câu hỏi bằng AI sẽ báo lỗi 500.

### 2. Khởi chạy Backend (Lắng nghe mọi IP để máy khác kết nối được)
Mở một terminal mới, chuyển hướng vào thư mục `Backend` và chạy:
```bash
cd Backend
dotnet run --urls="http://0.0.0.0:5000"
```
*Lưu ý: Hệ thống sử dụng SQL Server LocalDB. Các bảng và dữ liệu mẫu (Tài khoản Admin) sẽ tự động được tạo khi Backend khởi chạy lần đầu tiên.*

### 3. Khởi chạy Frontend
Mở một terminal khác, chuyển hướng vào thư mục `Frontend` và chạy:
```bash
cd Frontend
npm run dev
```

---

## 🌐 HƯỚNG DẪN CHẠY TRÊN NHIỀU MÁY (MẠNG LAN / WI-FI & INTERNET)

### Cách 1: Chạy trong cùng mạng Wi-Fi / LAN (Lớp học, Phòng Lab, Cùng phòng)
1. **Lấy địa chỉ IP máy chủ (máy chạy Backend & Frontend):**
   - Mở cmd/powershell gõ `ipconfig` -> Tìm dòng **IPv4 Address** của card Wi-Fi (ví dụ: `192.168.10.234`).
2. **Khởi động Backend và Frontend như bước 2 và 3 ở trên.**
   - Frontend Vite sẽ hiển thị:
     ```
     ➜  Local:   http://localhost:5173/
     ➜  Network: http://192.168.10.234:5173/
     ```
3. **Mở tường lửa Windows (chỉ cần làm 1 lần trên máy chủ nếu máy khác không vào được):**
   - Mở **PowerShell bằng quyền Administrator** và chạy lệnh:
     ```powershell
     netsh advfirewall firewall add rule name="QuizAI_Inbound" dir=in action=allow protocol=TCP localport=5000,5173
     ```
4. **Các máy khác (Học sinh/Điện thoại/Laptop):**
   - Không cần cài đặt bất kỳ thứ gì!
   - Chỉ cần kết nối cùng mạng Wi-Fi với máy chủ, mở trình duyệt (Chrome, Safari, Edge) và truy cập:
     `http://<IP_MÁY_CHỦ>:5173` (Ví dụ: `http://192.168.10.234:5173`)

### Cách 2: Chạy qua Internet (Khác mạng Wi-Fi, 4G, hoặc khi Wi-Fi trường bật chặn LAN/AP Isolation)
Nếu máy bạn và máy bạn bè khác mạng Wi-Fi hoặc dùng 4G:
1. Mở một terminal mới, dùng **Cloudflare Tunnel** (miễn phí, không cần đăng ký tài khoản):
   ```bash
   npx cloudflared tunnel --url http://localhost:5173
   ```
   *(Hoặc dùng `npx localtunnel --port 5173`)*
2. Hệ thống sẽ sinh ra một đường link công khai (ví dụ: `https://xxx.trycloudflare.com`).
3. Gửi link đó cho bất kỳ ai trên toàn thế giới, họ có thể vào làm bài thi trực tiếp!

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
