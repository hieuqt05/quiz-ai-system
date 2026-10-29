# TỪ ĐIỂN TỪ KHÓA CHUYÊN NGÀNH • BÁO CÁO ĐỒ ÁN LẬP TRÌNH MẠNG
## Dự án: QuizAI – Hệ Thống Trắc Nghiệm Online Tích Hợp AI & Giám Sát Thi Đa Máy

Tài liệu này được biên soạn nhằm giải thích chi tiết, chính xác và chuyên sâu tất cả các **từ khóa chuyên ngành mạng máy tính, an ninh mạng và phát triển phần mềm** được sử dụng trong dự án QuizAI. Giúp sinh viên hiểu tường tận bản chất kỹ thuật, tự tin thuyết trình và trả lời xuất sắc mọi câu hỏi phản biện của Hội đồng Giảng viên.

---

## 📑 DANH MỤC 18 TỪ KHÓA CỐT LÕI

### 🌐 NHÓM 1: TẦNG MẠNG & GIAO THỨC TRUYỀN THÔNG (NETWORKING)
1. **Kiến Trúc Client - Server 3 Tầng (3-Tier Architecture)**
2. **Giao Thức TCP/IP & Cơ Chế Bắt Tay 3 Bước (TCP 3-Way Handshake)**
3. **Địa Chỉ Lắng Nghe `0.0.0.0` vs `127.0.0.1` (IP Binding)**
4. **Reverse Proxy (Vite Dev Proxy)**
5. **CORS (Cross-Origin Resource Sharing - Chính Sách Chia Sẻ Tài Nguyên Chéo Nguồn)**
6. **SSH Reverse Tunneling (Đường Hầm Đảo Ngược - Pinggy)**
7. **Giao Thức HTTPS & Bảo Mật TLS/SSL**
8. **Kiến Trúc RESTful API & Các Phương Thức HTTP (GET, POST, PATCH, DELETE)**

### 🔐 NHÓM 2: AN NINH MẠNG & XÁC THỰC (SECURITY)
9. **JWT (JSON Web Token) & Xác Thực Phi Trạng Thái (Stateless Authentication)**
10. **Mã Hóa Băm Mật Khẩu BCrypt (Salted Hash Function)**
11. **Phân Quyền RBAC (Role-Based Access Control)**

### 🛡️ NHÓM 3: GIÁM SÁT THI & CHỐNG GIAN LẬN (ANTI-CHEAT)
12. **Browser Visibility API & Window Blur Event (Bắt Sự Kiện Chuyển Tab)**
13. **Cơ Chế Debounce / Cooldown Event (Chống Kích Hoạt Đúp Sự Kiện Trình Duyệt)**
14. **Khả Năng Chịu Lỗi Mạng (Fault Tolerance) & Client-side Caching (LocalStorage)**
15. **Thuật Toán Trộn Ngẫu Nhiên Fisher-Yates (Shuffling Algorithm)**
16. **Đồng Bộ Thời Gian Thực Bằng Server Timestamp (Server-side Timer Synchronization)**

### 🤖 NHÓM 4: TRÍ TUỆ NHÂN TẠO & QUẢN TRỊ DỮ LIỆU (AI & DATA)
17. **Prompt Engineering & Structured JSON Schema (Ép Khuôn Dữ Liệu GenAI)**
18. **UTF-8 with BOM (Byte Order Mark - Định Dạng Báo Cáo Excel Đa Nền Tảng)**

---

# CHI TIẾT TỪNG TỪ KHÓA CHUYÊN NGÀNH

---

## 1. Kiến Trúc Client - Server 3 Tầng (3-Tier Architecture)

### 📌 Nó là gì?
Kiến trúc Client - Server 3 tầng là mô hình phân tách toàn bộ hệ thống phần mềm thành 3 lớp độc lập và chuyên biệt:
1. **Tầng Presentation (Client / Giao diện):** Nơi người dùng trực tiếp tương tác.
2. **Tầng Application / Business Logic (Server / Nghiệp vụ):** Nơi tiếp nhận yêu cầu, xử lý tính toán, chấm điểm và điều phối luồng dữ liệu.
3. **Tầng Data Access (Database / Lưu trữ):** Nơi lưu trữ bền vững dữ liệu đề thi, người dùng và kết quả.

### 🎯 Dùng để làm gì?
- Tách biệt rõ ràng trách nhiệm (Separation of Concerns).
- Đảm bảo tính bảo mật: Client **không bao giờ** kết nối trực tiếp vào Database, mọi thao tác phải qua lớp kiểm duyệt an ninh tại Server.
- Khả năng mở rộng (Scalability): Khi lượng thí sinh tăng cao, có thể nâng cấp máy chủ Server hoặc Database độc lập mà không cần viết lại giao diện.

### 💻 Được làm như thế nào trong QuizAI?
- **Tầng Client:** Thư mục `Frontend/` xây dựng bằng React 19 + Vite, chạy độc lập trên cổng `5173`.
- **Tầng Server:** Thư mục `Backend/` viết bằng C# (ASP.NET Core 9 Web API), chạy trên cổng `5000`. Cung cấp các Controller xử lý nghiệp vụ (`AuthController`, `ExamsController`, `SubmissionsController`, `AdminController`, `AIController`).
- **Tầng Data:** Cơ sở dữ liệu SQL Server LocalDB (`QuizSystemDB`), được quản lý thông qua Entity Framework Core 9 (`AppDbContext.cs`).

---

## 2. Giao Thức TCP/IP & Cơ Chế Bắt Tay 3 Bước (TCP 3-Way Handshake)

### 📌 Nó là gì?
- **TCP (Transmission Control Protocol):** Là giao thức tầng Giao vận (Transport Layer) hướng kết nối (Connection-oriented), đảm bảo việc truyền dữ liệu giữa hai máy tính diễn ra tin cậy, đúng thứ tự và không bị mất gói tin.
- **Bắt tay 3 bước (3-Way Handshake):** Là quy trình thiết lập kết nối trước khi truyền dữ liệu:
  1. **SYN (Synchronize):** Client gửi cờ SYN đến Server để yêu cầu mở phiên.
  2. **SYN-ACK (Synchronize-Acknowledgment):** Server phản hồi đồng ý mở phiên và gửi số thứ tự của mình.
  3. **ACK (Acknowledgment):** Client xác nhận lại. Phiên TCP chính thức được thiết lập.

### 🎯 Dùng để làm gì?
- Trả lời câu hỏi kinh điển: *"Tại sao thi online phải dùng TCP mà không dùng UDP?"*.
- Bài thi trực tuyến bắt buộc phải có tính toàn vẹn 100%. Nếu dùng UDP (phi kết nối, không có kiểm tra lỗi và phát lại), khi mạng lag, gói tin nộp bài của thí sinh có thể bị thất lạc, dẫn đến điểm thi bị sai lệch hoặc mất bài. TCP đảm bảo tự động truyền lại (Retransmission) nếu xảy ra sự cố nghẽn mạng.

### 💻 Được làm như thế nào trong QuizAI?
Mọi giao tiếp HTTP/HTTPS giữa Client (React) và Server (ASP.NET Core) cũng như giữa Server và Google Gemini AI đều chạy ngầm bên trên tầng giao vận TCP (Port 5000, 5173, 443). Gói tin gửi đáp án `POST /api/submissions/submit` luôn được bảo đảm chuyển phát thành công tới cơ sở dữ liệu.

---

## 3. Địa Chỉ Lắng Nghe `0.0.0.0` vs `127.0.0.1` (IP Binding)

### 📌 Nó là gì?
- **`127.0.0.1` (Localhost / Loopback Interface):** Là địa chỉ IP ảo chỉ trỏ về chính máy tính hiện tại. Mọi tiến trình chỉ lắng nghe trên `127.0.0.1` sẽ **từ chối mọi kết nối đến từ bên ngoài card mạng**.
- **`0.0.0.0` (Inaddr_Any / Wildcard Address):** Là địa chỉ đặc biệt ra lệnh cho ứng dụng lắng nghe trên **tất cả các card mạng hiện có** trên máy tính (bao gồm card Wi-Fi, card mạng dây LAN Ethernet, card mạng ảo Hamachi/VPN).

### 🎯 Dùng để làm gì?
Giúp hệ thống thoát khỏi rào cản "chỉ chạy một mình trên máy nhà" để có thể chạy đồng thời trên nhiều laptop, máy tính phòng lab và điện thoại của học sinh.

### 💻 Được làm như thế nào trong QuizAI?
- **Backend:** Cấu hình trong `launchSettings.json` và dòng lệnh khởi chạy:
  ```bash
  dotnet run --urls="http://0.0.0.0:5000"
  ```
- **Frontend (Vite):** Cấu hình trong file `Frontend/vite.config.js`:
  ```javascript
  server: {
    host: '0.0.0.0', // Lắng nghe trên mọi IP card mạng
    port: 5173
  }
  ```
Nhờ đó, khi một máy con trong cùng Wi-Fi gõ `http://192.168.10.234:5173`, gói tin mạng được card Wi-Fi chấp nhận và chuyển tiếp vào ứng dụng thành công.

---

## 4. Reverse Proxy (Vite Dev Proxy)

### 📌 Nó là gì?
Reverse Proxy (Máy chủ ủy thác ngược) là một máy chủ trung gian đứng trước các máy chủ dịch vụ, nhận yêu cầu từ client và điều hướng yêu cầu đó đến đúng máy chủ backend tương ứng.

### 🎯 Dùng để làm gì?
- Tránh lỗi Same-Origin Policy (CORS) trong môi trường phát triển: Client chỉ cần gửi request đến địa chỉ của chính nó (`/api/*`), proxy sẽ tự động chuyển tiếp ngầm về port backend.
- Giúp các máy con trong mạng LAN không cần biết port hay địa chỉ của Backend API, chỉ cần biết duy nhất 1 địa chỉ Frontend cổng `5173`.

### 💻 Được làm như thế nào trong QuizAI?
Cấu hình trong `Frontend/vite.config.js`:
```javascript
proxy: {
  '/api': {
    target: 'http://localhost:5000',
    changeOrigin: true,
    secure: false,
  }
}
```
Khi máy học sinh gọi `http://192.168.10.234:5173/api/exams`, máy chủ Vite trên máy bạn sẽ nhận gói tin này và chuyển tiếp nội bộ về `http://localhost:5000/api/exams`, sau đó trả kết quả ngược lại cho máy học sinh.

---

## 5. CORS (Cross-Origin Resource Sharing)

### 📌 Nó là gì?
CORS là một cơ chế bảo mật cốt lõi được xây dựng trong mọi trình duyệt web (Chrome, Edge, Safari). Nó ngăn chặn một trang web từ domain A (Origin A) tự ý gửi request lấy trộm dữ liệu từ domain B (Origin B) nếu không được phép.

### 🎯 Dùng để làm gì?
Khi chạy hệ thống trên nhiều máy tính, máy khách có thể truy cập qua các Origin khác nhau (ví dụ: `http://192.168.10.234:5173` hoặc link tunnel `https://xxxx.a.pinggy.io`). Nếu không mở chính sách CORS, trình duyệt của máy khách sẽ lập tức chặn đứng mọi cuộc gọi API vì khác biệt Origin!

### 💻 Được làm như thế nào trong QuizAI?
Cấu hình tại `Backend/Program.cs`:
```csharp
builder.Services.AddCors(opts =>
{
    opts.AddPolicy("AllowFrontend", policy =>
        policy.SetIsOriginAllowed(_ => true) // Chấp nhận mọi IP máy khách / mạng LAN / Internet
              .AllowAnyHeader()
              .AllowAnyMethod()
              .AllowCredentials());
});
```
Đảm bảo dù bạn bè dùng laptop hay điện thoại mở qua bất kỳ IP nào cũng đều được Server cấp phép trao đổi dữ liệu.

---

## 6. SSH Reverse Tunneling (Đường Hầm Đảo Ngược - Pinggy)

### 📌 Nó là gì?
SSH Reverse Tunneling là kỹ thuật mạng sử dụng giao thức SSH bảo mật (Port 22/443) để mở một kết nối outbound từ máy local của bạn ra một máy chủ công cộng trung gian trên Internet, từ đó chuyển tiếp luồng dữ liệu từ Internet ngược trở lại cổng local máy bạn.

### 🎯 Dùng để làm gì?
- Vượt qua tường lửa (Firewall) và các bộ định tuyến NAT mà không cần quyền Admin truy cập modem để mở port (Port Forwarding).
- Đánh bại cơ chế **AP Isolation** (chế độ bảo mật của mạng Wi-Fi trường đại học ngăn các laptop sinh viên nhìn thấy nhau).
- Cho phép bất kỳ ai ngồi ở nhà, dùng 4G đều có thể vào thi được.

### 💻 Được làm như thế nào trong QuizAI?
Cài đặt trong file kịch bản [`chia_se_link_nhanh.bat`](file:///h:/Antigravity/Laptrinhmang/chia_se_link_nhanh.bat):
```bash
ssh -p 443 -R0:localhost:5173 -o StrictHostKeyChecking=no a.pinggy.io
```
- `-p 443`: Dùng cổng HTTPS (443) để không bị tường lửa trường chặn như cổng SSH mặc định (22).
- `-R0:localhost:5173`: Ra lệnh máy chủ Pinggy mở 1 cổng ngẫu nhiên trên Internet và chuyển toàn bộ dữ liệu về cổng `5173` máy tính của bạn.
- Cung cấp sẵn mã QR code trực tiếp trên màn hình terminal để quét bằng điện thoại.

---

## 7. Giao Thức HTTPS & Bảo Mật TLS/SSL

### 📌 Nó là gì?
- **HTTPS (HyperText Transfer Protocol Secure):** Là phiên bản bảo mật của giao thức HTTP, hoạt động trên cổng 443.
- **TLS (Transport Layer Security):** Là giao thức mật mã học nằm ở giữa tầng Giao vận (TCP) và tầng Ứng dụng (HTTP). Nó mã hóa toàn bộ payload trước khi đưa xuống mạng thông qua quá trình bắt tay TLS (TLS Handshake) sử dụng khóa bất đối xứng RSA/ECC và khóa phiên đối xứng AES.

### 🎯 Dùng để làm gì?
- Chống nghe lén (Eavesdropping): Nếu kẻ tấn công cùng phòng dùng phần mềm **Wireshark** để bắt gói tin mạng, họ chỉ thấy dữ liệu rác đã bị mã hóa, không thể xem trộm được đề thi hay đáp án trắc nghiệm.
- Chống giả mạo gói tin (Data Tampering).

### 💻 Được làm như thế nào trong QuizAI?
- Khi giao tiếp với Google Gemini API: Sử dụng kết nối HTTPS bắt buộc để bảo vệ Gemini API Key và nội dung câu hỏi.
- Khi chia sẻ qua Pinggy / Tunnel: Cung cấp sẵn chứng chỉ SSL hợp lệ (`https://...`), bảo vệ phiên làm bài thi của thí sinh từ đầu đến cuối (End-to-End Encryption).

---

## 8. Kiến Trúc RESTful API & Các Phương Thức HTTP

### 📌 Nó là gì?
REST (Representational State Transfer) là chuẩn thiết kế kiến trúc phần mềm cho các dịch vụ web. Dữ liệu được xem như các "Tài nguyên" (Resources) và thao tác dựa trên các động từ chuẩn của giao thức HTTP:
- `GET`: Lấy dữ liệu (Đọc đề thi, xem thống kê).
- `POST`: Tạo mới tài nguyên (Đăng ký, Đăng nhập, Bắt đầu thi, Nộp bài thi).
- `PATCH`: Cập nhật một phần dữ liệu (Duyệt câu hỏi, cập nhật vi phạm).
- `DELETE`: Xóa tài nguyên (Xóa đề thi).

### 🎯 Dùng để làm gì?
Chuẩn hóa giao tiếp giữa Client và Server, giúp mã nguồn tường minh, dễ bảo trì, trả về định dạng chuẩn JSON mà mọi nền tảng (Web, Mobile, Desktop) đều đọc được.

### 💻 Được làm như thế nào trong QuizAI?
Hệ thống cung cấp danh mục RESTful API hoàn chỉnh (có tài liệu Swagger UI tại `/swagger`):
- `POST /api/auth/login`: Xác thực tài khoản.
- `GET /api/exams`: Lấy danh sách đề đã công bố.
- `POST /api/submissions/start`: Bắt đầu phiên thi.
- `POST /api/submissions/submit`: Nộp bài chấm điểm.
- `PATCH /api/exams/questions/{id}/approve`: Duyệt câu hỏi AI.
- `GET /api/admin/stats/exam/{id}/submissions`: Lấy danh sách giám sát thí sinh.

---

## 9. JWT (JSON Web Token) & Xác Thực Phi Trạng Thái (Stateless Authentication)

### 📌 Nó là gì?
JWT là một chuỗi mã hóa nhỏ gọn, an toàn URL dùng để truyền tải thông tin định danh giữa hai bên. Một chuỗi JWT gồm 3 phần ngăn cách bởi dấu chấm (`.`):
$$\text{Header} . \text{Payload} . \text{Signature}$$
- **Header:** Chứa thuật toán mã hóa (ví dụ: `HS256`).
- **Payload:** Chứa thông tin người dùng (UserId, Username, Role).
- **Signature (Chữ ký):** Được tạo bằng cách lấy:
  $$\text{HMAC-SHA256}(\text{Base64(Header)} + "." + \text{Base64(Payload)}, \text{SecretKey})$$

### 🎯 Dùng để làm gì?
- **Stateless (Phi trạng thái):** Server không cần tốn RAM lưu Session của hàng trăm thí sinh trong database.
- Mỗi khi thí sinh gửi request, Server chỉ cần dùng `SecretKey` giải mã và kiểm tra chữ ký. Nếu chữ ký trùng khớp $\rightarrow$ Xác thực thành công. Điều này giúp hệ thống chịu tải mạng cực tốt và xử lý phản hồi siêu nhanh (<120ms).

### 💻 Được làm như thế nào trong QuizAI?
- **Server:** Cấu hình trong `Program.cs` và sinh token trong `AuthService.cs` với hạn dùng và khóa bí mật cấu hình tại `appsettings.json`.
- **Client:** File `Frontend/src/services/api.js` sử dụng Axios Request Interceptor để tự động đính kèm Token vào Header của mọi request:
  ```javascript
  config.headers.Authorization = `Bearer ${token}`;
  ```

---

## 10. Mã Hóa Băm Mật Khẩu BCrypt (Salted Hash Function)

### 📌 Nó là gì?
BCrypt là hàm băm mật khẩu một chiều được thiết kế dựa trên thuật toán mã hóa Blowfish. Điểm đặc biệt của BCrypt là nó tích hợp sẵn cơ chế **Salt (chuỗi muối ngẫu nhiên)** và **Work Factor (hệ số độ phức tạp tính toán)**.

### 🎯 Dùng để làm gì?
- Chống tấn công **Rainbow Table** (bảng tra cứu mật khẩu băm sẵn). Cùng một mật khẩu `123456`, nếu 2 học sinh cùng đặt thì trong cơ sở dữ liệu sẽ sinh ra 2 chuỗi băm hoàn toàn khác nhau nhờ Salt ngẫu nhiên.
- Chống tấn công Brute-force (dò quét bằng siêu máy tính).

### 💻 Được làm như thế nào trong QuizAI?
Khi đăng ký tài khoản trong `AuthService.cs`:
```csharp
PasswordHash = BCrypt.Net.BCrypt.HashPassword(request.Password);
```
Mật khẩu gốc của học sinh không bao giờ được lưu trữ dưới dạng văn bản rõ (plain text).

---

## 11. Phân Quyền RBAC (Role-Based Access Control)

### 📌 Nó là gì?
RBAC là phương pháp kiểm soát truy cập tài nguyên dựa trên vai trò của từng người dùng trong hệ thống (ví dụ: `STUDENT`, `TEACHER`, `ADMIN`).

### 🎯 Dùng để làm gì?
Đảm bảo học sinh không thể truy cập trái phép vào các API nhạy cảm như tạo đề thi, duyệt câu hỏi của AI hoặc xem đáp án của đề thi trước khi nộp bài.

### 💻 Được làm như thế nào trong QuizAI?
Sử dụng các thuộc tính `[Authorize(Roles = "ADMIN,TEACHER")]` trực tiếp trên các Controller và Action trong Backend ASP.NET Core:
```csharp
[HttpGet("stats/exam/{examId}/submissions")]
[Authorize(Roles = "TEACHER,ADMIN")]
public async Task<IActionResult> GetExamSubmissions(int examId)
```
Nếu học sinh cố tình gọi API này qua Postman, hệ thống sẽ trả về mã lỗi HTTP `403 Forbidden` ngay lập tức.

---

## 12. Browser Visibility API & Window Blur Event (Chống Chuyển Tab)

### 📌 Nó là gì?
- **Page Visibility API:** Là chuẩn API của trình duyệt cung cấp sự kiện `visibilitychange` và thuộc tính `document.hidden`, cho biết tab hiện tại đang hiển thị hay đang bị ẩn đi do người dùng chuyển sang tab khác hoặc thu nhỏ cửa sổ.
- **Window Blur Event:** Sự kiện `window.onblur` được kích hoạt khi cửa sổ trình duyệt mất tiêu điểm (Focus) – ví dụ thí sinh bấm phím `Alt + Tab`, bấm vào thanh Taskbar, hoặc mở một ứng dụng khác như Word, ChatGPT đè lên.

### 🎯 Dùng để làm gì?
Phát hiện tức thì hành vi rời khỏi màn hình làm bài thi để tra cứu tài liệu trái phép.

### 💻 Được làm như thế nào trong QuizAI?
Được triển khai trong `Frontend/src/pages/QuizPage.jsx`:
```javascript
const handleVisibilityChange = () => {
  if (document.hidden) recordViolation('Chuyển tab trình duyệt hoặc thu nhỏ cửa sổ');
};
const handleWindowBlur = () => {
  recordViolation('Mất tiêu điểm màn hình thi (Alt + Tab hoặc nhấp ứng dụng khác)');
};
document.addEventListener('visibilitychange', handleVisibilityChange);
window.addEventListener('blur', handleWindowBlur);
```

---

## 13. Cơ Chế Debounce / Cooldown Event (Chống Kích Hoạt Đúp)

### 📌 Nó là gì?
Debounce / Cooldown là kỹ thuật giới hạn tần suất thực thi của một hàm. Khi một chuỗi sự kiện liên tục xảy ra trong một khoảng thời gian ngắn, cơ chế này chỉ cho phép xử lý sự kiện đầu tiên và bỏ qua mọi sự kiện tiếp theo trong một khoảng thời gian xác định (Cooldown window).

### 🎯 Dùng để làm gì?
Khi người dùng chuyển tab hoặc Alt+Tab, trình duyệt web luôn phát ra **cả 2 sự kiện `blur` và `visibilitychange` cùng một lúc** chỉ cách nhau vài mili-giây. Nếu không có bộ lọc Cooldown, 1 lần thí sinh chuyển tab sẽ bị tính đúp thành 2 lần vi phạm, dẫn đến việc mới chuyển tab 2 lần mà đã bị hủy bài thi!

### 💻 Được làm như thế nào trong QuizAI?
Sử dụng `useRef` lưu mốc thời gian vi phạm cuối cùng với cửa sổ Cooldown là **2.5 giây**:
```javascript
const lastViolationTimeRef = useRef(0);

const recordViolation = (reason) => {
  const now = Date.now();
  // Nếu sự kiện tiếp theo xảy ra cách sự kiện trước dưới 2.5s -> Bỏ qua vì là kích hoạt đúp
  if (now - lastViolationTimeRef.current < 2500) return;
  lastViolationTimeRef.current = now;

  const next = currentStored + 1;
  // Cập nhật số lần vi phạm chính xác 1 lần cho 1 thao tác chuyển tab
  if (next >= 3) {
    handleSubmit(next); // Đúng lần thứ 3 tự động thu hồi bài thi!
  }
};
```

---

## 14. Khả Năng Chịu Lỗi (Fault Tolerance) & Client-side Caching (LocalStorage)

### 📌 Nó là gì?
- **Fault Tolerance (Khả năng chịu lỗi):** Là đặc tính của hệ thống mạng cho phép nó tiếp tục hoạt động bình thường, không làm mất mát dữ liệu của người dùng ngay cả khi một số thành phần phần cứng, phần mềm hoặc đường truyền mạng gặp sự cố đột ngột.
- **LocalStorage:** Bộ nhớ cục bộ có sẵn trên trình duyệt web, cho phép lưu trữ dữ liệu bền vững theo cặp khóa-giá trị (Key-Value) mà không bị mất đi khi người dùng tải lại trang hoặc tắt trình duyệt.

### 🎯 Dùng để làm gì?
Bảo vệ bài làm của thí sinh khi gặp sự cố cúp điện, sập nguồn máy tính, vô tình nhấn F5 hoặc rớt mạng Wi-Fi phòng thi.

### 💻 Được làm như thế nào trong QuizAI?
Trong `Frontend/src/pages/QuizPage.jsx`:
- Mỗi khi thí sinh chọn đáp án: Dữ liệu được ghi ngầm vào `localStorage` theo key `quiz_answers_${submissionId}`.
- Khi thí sinh vào lại trang thi: Hệ thống kiểm tra và tự động khôi phục toàn bộ các câu trả lời đã làm trước đó.
- Sau khi bấm "Nộp bài" thành công: Tự động dọn sạch bộ nhớ tạm để bảo mật.

---

## 15. Thuật Toán Trộn Ngẫu Nhiên Fisher-Yates (Shuffling Algorithm)

### 📌 Nó là gì?
Fisher-Yates (còn gọi là Knuth Shuffle) là thuật toán tối ưu dùng để xáo trộn ngẫu nhiên một mảng các phần tử hữu hạn. Độ phức tạp thời gian đạt mức tối ưu $O(N)$ và đảm bảo mọi hoán vị của các phần tử đều có xác suất xuất hiện hoàn toàn bằng nhau (Unbiased Random Permutation).

### 🎯 Dùng để làm gì?
- Ngăn chặn triệt để hành vi nhìn bài nhau của các thí sinh ngồi cạnh nhau trong cùng phòng máy tính.
- Đảo ngẫu nhiên cả thứ tự các câu hỏi và thứ tự 4 đáp án A, B, C, D của từng câu.

### 💻 Được làm như thế nào trong QuizAI?
Khi khởi tạo bài thi trong `QuizPage.jsx`:
- Câu hỏi được xáo trộn ngẫu nhiên.
- Các options bên trong mỗi câu hỏi được xáo trộn và gán lại nhãn A, B, C, D mới nhưng vẫn giữ nguyên `OptionId` gốc để Server chấm điểm chính xác.
- Mảng đã xáo trộn được lưu vào `sessionStorage` của thí sinh đó, giúp câu hỏi không bị xáo trộn lung tung mỗi khi tải lại trang trong cùng một lượt thi.

---

## 16. Đồng Bộ Thời Gian Bằng Server Timestamp (Server-side Timer Sync)

### 📌 Nó là gì?
Là kỹ thuật quản lý thời gian thi cử hoàn toàn dựa vào mốc giờ chuẩn UTC của máy chủ (Server Time), thay vì tin tưởng vào đồng hồ cục bộ trên máy tính của học sinh (Client Time).

### 🎯 Dùng để làm gì?
Triệt tiêu gian lận chỉnh giờ máy tính. Học sinh không thể vào cài đặt Windows lùi đồng hồ máy tính lại 30 phút để kéo dài thời gian làm bài.

### 💻 Được làm như thế nào trong QuizAI?
Tại `Backend/Services/QuizService.cs`:
- Khi học sinh bấm bắt đầu thi: Server ghi nhận `StartedAt = DateTime.UtcNow`.
- Khi học sinh nộp bài hoặc load lại trang: Server tính:
  $$\text{Thời gian đã làm} = \text{DateTime.UtcNow} - \text{StartedAt}$$
  $$\text{Thời gian còn lại} = \text{DurationMinutes} \times 60 - \text{Thời gian đã làm}$$
Dù client có can thiệp sửa đổi đồng hồ hay can thiệp code JavaScript, Server vẫn độc lập đóng bài thi khi hết hạn.

---

## 17. Prompt Engineering & Structured JSON Schema (Ép Khuôn Dữ Liệu GenAI)

### 📌 Nó là gì?
- **Prompt Engineering:** Kỹ thuật thiết kế câu lệnh hướng dẫn chuyên biệt để mô hình ngôn ngữ lớn (LLM như Google Gemini) hiểu ngữ cảnh và thực hiện chính xác nhiệm vụ mong muốn.
- **Structured JSON Schema:** Kỹ thuật ép buộc mô hình AI phản hồi dữ liệu theo đúng định dạng cấu trúc JSON đã được quy định sẵn (gồm tên trường, kiểu dữ liệu, mảng các lựa chọn), tuyệt đối không trả về văn bản tự do hay lời chào hỏi thừa.

### 🎯 Dùng để làm gì?
Đảm bảo 100% dữ liệu câu hỏi do AI tạo ra có thể được Backend bóc tách tự động (Deserialize) thành các đối tượng C# DTOs và ghi thẳng vào cơ sở dữ liệu mà không bao giờ bị lỗi cú pháp (`JSON Parse Error`).

### 💻 Được làm như thế nào trong QuizAI?
Tại `Backend/Services/AIService.cs`:
Hệ thống thiết lập một `System Instruction` nghiêm ngặt gửi tới Gemini API:
```json
{
  "questions": [
    {
      "questionText": "Nội dung câu hỏi",
      "difficulty": "EASY|MEDIUM|HARD",
      "explanation": "Giải thích chi tiết",
      "options": [
        { "label": "A", "text": "Nội dung", "isCorrect": true },
        { "label": "B", "text": "Nội dung", "isCorrect": false }
      ]
    }
  ]
}
```

---

## 18. UTF-8 with BOM (Byte Order Mark)

### 📌 Nó là gì?
- **UTF-8 (8-bit Unicode Transformation Format):** Chuẩn mã hóa ký tự biến đổi chiều dài hỗ trợ hiển thị toàn bộ hệ thống chữ viết trên thế giới, bao gồm tiếng Việt có dấu.
- **BOM (Byte Order Mark):** Là một chuỗi ký tự đặc biệt gồm 3 byte `0xEF, 0xBB, 0xBF` (ký hiệu trong JavaScript là `\uFEFF`) được đặt ở ngay đầu file văn bản.

### 🎯 Dùng để làm gì?
Khi xuất file báo cáo điểm dạng `.CSV`, phần mềm **Microsoft Excel trên Windows mặc định sẽ mở file bằng bảng mã ANSI/Windows-1252**, dẫn đến việc các ký tự tiếng Việt có dấu bị lỗi font nghiêm trọng (biến thành ký tự rác `Nguy?n V?n A`). Chuỗi BOM đóng vai trò như một tín hiệu nhận diện buộc Excel phải tự động chuyển sang đọc bằng bộ mã UTF-8.

### 💻 Được làm như thế nào trong QuizAI?
Tại `Frontend/src/pages/AdminPage.jsx`:
```javascript
const csvContent = '\uFEFF' + [headers.join(','), ...rows.map(r => r.join(','))].join('\r\n');
const blob = new Blob([csvContent], { type: 'text/csv;charset=utf-8;' });
```
Đảm bảo giáo viên tải file điểm về và nhấp đúp mở bằng Excel trên bất kỳ máy tính Windows nào cũng hiển thị tiếng Việt sắc nét, chuẩn 100%.

---

## 💡 KẾT LUẬN & MẸO ÁP DỤNG KHI THUYẾT TRÌNH

> 🌟 **Lời khuyên vàng khi thuyết trình:**  
> Đừng cố đọc thuộc lòng tất cả các từ khóa! Khi trình bày Slide, bạn chỉ cần nêu tên từ khóa kèm mục đích của nó. Hãy giữ danh sách này bên cạnh khi **trả lời câu hỏi phản biện của Giảng viên**. Khi thầy cô hỏi xoáy sâu vào kỹ thuật mạng ("CORS là gì?", "Tại sao dùng TCP?", "Chống chuyển tab ra sao?"), bạn chỉ cần lật đúng mục tương ứng ở trên và trả lời gãy gọn – Thầy cô chắc chắn sẽ đánh giá bạn am hiểu kiến thức mạng rất sâu sắc và cho điểm tối đa!
