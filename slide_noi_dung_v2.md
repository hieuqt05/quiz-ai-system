# NỘI DUNG SLIDE VÀ KỊCH BẢN THUYẾT TRÌNH GIỮA KỲ
## Môn học: LẬP TRÌNH MẠNG
## Đề tài: QuizAI – Hệ Thống Trắc Nghiệm Online Tích Hợp Trí Tuệ Nhân Tạo

---

> 💡 **File trình chiếu trực tiếp:** Mở file [`slide_thuyet_trinh.html`](file:///h:/Antigravity/Laptrinhmang/slide_thuyet_trinh.html) trên trình duyệt Chrome/Edge/Cốc Cốc để trình chiếu toàn màn hình (nhấn phím `F`). Bạn cũng có thể nhấn nút **"In / PDF"** để xuất ra file PDF nộp cho giáo viên!

---

## 📑 DANH MỤC 17 SLIDE THEO CHECKLIST YÊU CẦU

1. **Slide 01:** Trang bìa (Tên môn học, Tên đề tài, Giảng viên, Sinh viên thực hiện)
2. **Slide 02:** Lý do chọn đề tài & Mục tiêu dự án
3. **Slide 03:** Thành viên & Phân công công việc
4. **Slide 04:** Timeline – Kế hoạch & Tiến độ thực hiện
5. **Slide 05:** Phác thảo thiết kế AI & Prompt Engineering
6. **Slide 06:** Chức năng hệ thống (Học sinh, Giáo viên, Quản trị viên)
7. **Slide 07:** Ngăn xếp công nghệ sử dụng (Technology Stack)
8. **Slide 08:** Kiến trúc hệ thống tổng thể (3-Tier & Client-Server Architecture)
9. **Slide 09:** Các giao thức mạng áp dụng (Mô hình TCP/IP, TCP 3-Way Handshake)
10. **Slide 10:** Giao thức Web & Cơ chế hoạt động RESTful API
11. **Slide 11:** HTTPS: Cơ chế hoạt động & Bảo mật TLS/SSL
12. **Slide 12:** Cơ chế xác thực JWT & Chính sách mạng CORS
13. **Slide 13:** Luồng dữ liệu 1: Đăng nhập & Xác thực tài khoản
14. **Slide 14:** Luồng dữ liệu 2: Tự động sinh câu hỏi bằng AI
15. **Slide 15:** Luồng dữ liệu 3: Làm bài thi & Chấm điểm thời gian thực
16. **Slide 16:** Kết quả đạt được & Giao diện thực tế
17. **Slide 17:** Kết luận & Định hướng phát triển cuối kỳ

---

# CHI TIẾT NỘI DUNG VÀ LỜI THOẠI TỪNG SLIDE (SPEAKER NOTES)

---

### SLIDE 01: TRANG BÌA
- **Tiêu đề:** QuizAI – HỆ THỐNG TRẮC NGHIỆM ONLINE TÍCH HỢP TRÍ TUỆ NHÂN TẠO
- **Môn:** Lập Trình Mạng
- **Sinh viên thực hiện:** Nguyễn Văn Tèo & Nhóm
- **GitHub:** https://github.com/hieuqt05/quiz-ai-system

🗣️ **Lời thoại thuyết trình gợi ý:**
> "Kính chào Thầy/Cô và các bạn. Hôm nay, nhóm em xin phép được báo cáo tiến độ đồ án giữa kỳ môn Lập trình mạng với đề tài: **QuizAI – Hệ thống trắc nghiệm online tích hợp trí tuệ nhân tạo**. Đề tài này được nhóm xây dựng nhằm áp dụng thực tiễn các kiến thức mạng máy tính như mô hình Client-Server, giao thức truyền tin TCP, kiến trúc RESTful API, giao thức bảo mật HTTPS/TLS và cơ chế xác thực JWT, đồng thời kết hợp mô hình AI Gemini để giải quyết bài toán tự động hóa đề thi."

---

### SLIDE 02: LÝ DO CHỌN ĐỀ TÀI & MỤC TIÊU
- **Thực trạng:**
  - Giáo viên mất nhiều thời gian biên soạn ngân hàng câu hỏi thủ công.
  - Các hệ thống thi trắc nghiệm cũ thiếu tính năng tự động hóa và thiếu giải thích chi tiết đáp án.
  - Đòi hỏi đường truyền ổn định, tin cậy cao, không được mất mát gói tin khi nộp bài.
- **Giải pháp (QuizAI):**
  - Tích hợp Google Gemini AI tự động sinh câu hỏi từ chủ đề hoặc bài giảng.
  - Xây dựng Web API RESTful đa luồng, độ trễ thấp.
  - Áp dụng các chuẩn an ninh mạng (HTTPS, BCrypt, JWT).

🗣️ **Lời thoại thuyết trình gợi ý:**
> "Về lý do chọn đề tài, xuất phát từ thực tế công tác giáo dục hiện nay: việc biên soạn đề thi trắc nghiệm đòi hỏi rất nhiều thời gian và công sức. Nhóm nhận thấy tiềm năng to lớn của các mô hình GenAI như Gemini trong việc tạo sinh nội dung câu hỏi. Đặc biệt, dưới góc độ môn Lập trình mạng, một hệ thống thi online đặt ra yêu cầu rất cao về sự tin cậy trong truyền thông dữ liệu: không được phép thất lạc câu trả lời của thí sinh, bảo mật đề thi chống nghe lén và cơ chế đồng bộ thời gian thực giữa máy khách và máy chủ."

---

### SLIDE 03: THÀNH VIÊN & PHÂN CÔNG CÔNG VIỆC
- **Nguyễn Văn Tèo (Trưởng nhóm):** Thiết kế kiến trúc tổng thể, Backend REST API, Database EF Core, quản lý luồng dữ liệu & mạng.
- **Thành viên 02 (Frontend Dev):** Xây dựng giao diện React SPA, đếm ngược thời gian, responsive TailwindCSS, xử lý HTTP Axios.
- **Thành viên 03 (AI Integration):** Tích hợp Google Gemini API, Prompt Engineering, cơ chế Retry & Exponential Backoff.
- **Thành viên 04 (Testing & Network Analysis):** Bắt gói tin Wireshark, kiểm thử tải API, tài liệu kỹ thuật & slide.

🗣️ **Lời thoại thuyết trình gợi ý:**
> "Về phân công công việc, nhóm đã phân chia rõ ràng các mảng: bạn phụ trách kiến trúc mạng và backend API, bạn phụ trách phía client giao diện người dùng, bạn chuyên trách việc kết nối API trí tuệ nhân tạo bên thứ ba và bạn phụ trách kiểm thử bắt gói tin cũng như lập tài liệu."

---

### SLIDE 04: TIMELINE – KẾ HOẠCH & TIẾN ĐỘ THỰC HIỆN
- **Tuần 1 - 2:** Khảo sát yêu cầu, thiết kế Database ERD (7 bảng) & thiết kế Endpoints.
- **Tuần 3 - 4:** Lập trình Backend ASP.NET Core 9, bảo mật JWT Bearer, mã hóa mật khẩu BCrypt.
- **Tuần 5 - 6:** Tích hợp Gemini AI, xây dựng Frontend React + Vite, hoàn thiện trang làm bài thi.
- **Tuần 7:** Kiểm thử mạng, bắt gói tin HTTP/HTTPS, kiểm thử xử lý sự cố rớt mạng.
- **Tuần 8 (Hiện tại):** Báo cáo giữa kỳ, chuẩn bị kế hoạch phát triển cuối kỳ.

🗣️ **Lời thoại thuyết trình gợi ý:**
> "Về tiến độ, nhóm đã bám sát lộ trình 5 giai đoạn: từ khảo sát thiết kế cơ sở dữ liệu và các luồng mạng, cho đến xây dựng API, tích hợp AI, kiểm thử độ ổn định truyền thông và hiện tại nhóm đã hoàn thành 100% mục tiêu giai đoạn giữa kỳ."

---

### SLIDE 05: PHÁC THẢO THIẾT KẾ AI & PROMPT ENGINEERING
- **Model:** Google Gemini Flash (`gemini-3.8-flash`) qua REST API.
- **Prompt:** Thiết lập System Instructions ràng buộc nghiêm ngặt chỉ trả về JSON hợp lệ (Không trả markdown).
- **Cấu trúc sinh câu hỏi:** Tiêu đề câu hỏi, 4 đáp án (A, B, C, D), đáp án đúng, giải thích chi tiết (`explanation`), độ khó.
- **Human-in-the-Loop:** AI sinh -> Lưu DB trạng thái `PENDING` -> Giáo viên duyệt `APPROVED` mới đưa vào đề thi.
- **Xử lý sự cố mạng:** Exponential Backoff Retry (thử lại 3 lần nếu gặp lỗi mạng 429/503).

🗣️ **Lời thoại thuyết trình gợi ý:**
> "Điểm sáng tạo của hệ thống là khả năng tạo đề bằng AI. Tuy nhiên, AI có thể sinh thông tin chưa chuẩn (hallucination). Vì vậy, nhóm thiết kế theo mô hình Human-in-the-Loop: khi giáo viên yêu cầu, AI sinh câu hỏi nhưng sẽ được lưu ở trạng thái chờ duyệt (Pending). Giáo viên kiểm tra, tinh chỉnh rồi mới phê duyệt đưa vào ngân hàng đề thi. Đồng thời hệ thống có cơ chế Exponential Backoff để chống lỗi nghẽn mạng hoặc quá tải API."

---

### SLIDE 06: CHỨC NĂNG HỆ THỐNG
- **Học sinh:** Đăng ký, làm bài thi có đếm ngược, tự động nộp bài khi hết giờ, xem điểm tức thì, xem giải thích chi tiết, xem lịch sử thi.
- **Giáo viên:** Quản lý đề thi (tạo, sửa, xóa), sinh câu hỏi AI, duyệt câu hỏi, xem thống kê phổ điểm.
- **Quản trị viên:** Quản lý tài khoản người dùng, giám sát nhật ký AI (`AIGenerationLogs`), thống kê toàn trường.

🗣️ **Lời thoại thuyết trình gợi ý:**
> "Về mặt chức năng, hệ thống hỗ trợ 3 vai trò rõ rệt: Học sinh có trải nghiệm làm bài trơn tru với đồng hồ đếm ngược được đồng bộ từ server; Giáo viên có công cụ tạo đề thi truyền thống lẫn tự động bằng AI; và Admin có quyền quản trị toàn diện."

---

### SLIDE 07: CÔNG NGHỆ SỬ DỤNG (TECH STACK)
- **Backend:** C# ASP.NET Core 9.0 Web API, Entity Framework Core 9, SQL Server LocalDB.
- **Frontend:** React 19, Vite, Tailwind CSS, Axios, React Router v7.
- **Security:** JWT (JSON Web Token), BCrypt.Net.
- **AI Service:** Google Gemini API (với HttpClientFactory).

🗣️ **Lời thoại thuyết trình gợi ý:**
> "Về công nghệ: Nhóm lựa chọn ASP.NET Core 9 – một trong những framework backend có hiệu năng xử lý I/O mạng cao nhất hiện nay, kết hợp với React 19 và Vite ở phía Frontend để mang lại trải nghiệm SPA nhanh và mượt mà nhất."

---

### SLIDE 08: KIẾN TRÚC HỆ THỐNG TỔNG THỂ (3-TIER ARCHITECTURE)
- **Client Tier:** Trình duyệt web (Port 5173), tương tác người dùng, gửi yêu cầu HTTP/HTTPS.
- **Server Tier:** ASP.NET Core Web API (Port 5000), gồm Controllers, Services, EF Core DbContext.
- **Database & External Services:** SQL Server (7 bảng) và Google Gemini AI Cloud Service.

🗣️ **Lời thoại thuyết trình gợi ý:**
> "Hệ thống được thiết kế theo mô hình 3 tầng chuẩn mực: Client Tier độc lập hoàn toàn với Server Tier, giao tiếp với nhau thuần túy qua giao thức HTTP RESTful API sử dụng dữ liệu JSON. Nhờ đó, backend có thể dễ dàng mở rộng phục vụ thêm ứng dụng Mobile sau này mà không cần thay đổi logic xử lý mạng."

---

### SLIDE 09: CÁC GIAO THỨC MẠNG ÁP DỤNG (TCP/IP STACK)
- **Application Layer:** HTTP / HTTPS, REST API, JSON format.
- **Transport Layer:** Giao thức **TCP (Transmission Control Protocol)**.
- **Lý do chọn TCP:**
  - Độ tin cậy tuyệt đối (Reliable Delivery).
  - Cơ chế bắt tay 3 bước (3-Way Handshake: SYN -> SYN-ACK -> ACK).
  - Đảm bảo đúng thứ tự phân đoạn dữ liệu, cơ chế báo nhận ACK và phát lại (Retransmission) khi có sự cố đường truyền.

🗣️ **Lời thoại thuyết trình gợi ý:**
> "Dưới góc độ Lập trình mạng, nhóm áp dụng mô hình phân tầng TCP/IP. Tại tầng truyền vận (Transport Layer), hệ thống bắt buộc sử dụng TCP thay vì UDP. Bởi vì trong bài toán thi cử, việc mất gói tin là điều tối kỵ – nếu một đáp án của thí sinh bị rớt gói tin trên đường truyền thì kết quả bài thi sẽ bị sai lệch. Cơ chế 3-way handshake và kiểm soát luồng của TCP đảm bảo dữ liệu gửi đến máy chủ luôn toàn vẹn và đúng thứ tự."

---

### SLIDE 10: GIAO THỨC WEB & RESTFUL API
- **HTTP Methods:**
  - `GET`: Lấy dữ liệu (Stateless, an toàn, có thể cache).
  - `POST`: Tạo mới dữ liệu (Đăng nhập, tạo đề, nộp bài, gọi AI).
  - `PATCH`: Cập nhật từng phần (Duyệt câu hỏi, publish đề thi).
  - `DELETE`: Xóa tài nguyên (Xóa đề thi rác).
- **HTTP Status Codes:** `200 OK`, `201 Created`, `401 Unauthorized`, `403 Forbidden`, `404 Not Found`, `500 Internal Error`.
- **Stateless Principle:** Máy chủ không lưu session trong RAM, mỗi request tự mang đủ thông tin xác thực qua Header `Authorization`.

🗣️ **Lời thoại thuyết trình gợi ý:**
> "Tại tầng ứng dụng, nhóm xây dựng chuẩn RESTful Web API. Nhóm tuân thủ chặt chẽ việc sử dụng các động từ HTTP tương ứng với hành vi nghiệp vụ và trả về các mã trạng thái chuẩn quốc tế như 200, 201, 401 hoặc 403. Tính chất không trạng thái (Stateless) giúp máy chủ tiết kiệm bộ nhớ và dễ dàng mở rộng theo chiều ngang (load balancing)."

---

### SLIDE 11: HTTPS: CƠ CHẾ HOẠT ĐỘNG & BẢO MẬT TLS/SSL
- **Bản chất:** HTTP chạy trên nền tầng bảo mật TLS (Transport Layer Security) tại cổng 443.
- **Mục tiêu an ninh:**
  - Confidentiality (Tính bí mật): Mã hóa chống nghe lén dữ liệu bài thi (Sniffing).
  - Integrity (Tính toàn vẹn): Mã băm MAC chống sửa đổi nội dung điểm số trên đường truyền.
  - Authentication (Xác thực danh tính): Chứng chỉ số SSL/TLS ngăn chặn tấn công Man-in-the-Middle (MitM).
- **Quy trình bắt tay TLS Handshake:** Client Hello -> Server Hello (kèm Certificate) -> Xác thực khóa & Trao đổi Pre-Master Secret -> Thiết lập Session Key đối xứng (AES) -> Truyền tải an toàn.

🗣️ **Lời thoại thuyết trình gợi ý:**
> "Để bảo vệ dữ liệu trong môi trường mạng công cộng, hệ thống sử dụng giao thức HTTPS. Quy trình TLS Handshake diễn ra gồm 4 bước chính: hai bên thương lượng phiên bản và bộ mã hóa, server gửi chứng chỉ số công khai, client xác thực tính hợp lệ của server và trao đổi khóa bí mật. Sau đó, toàn bộ dữ liệu bài thi được mã hóa đối xứng bằng thuật toán AES tốc độ cao, ngăn chặn hoàn toàn nguy cơ nghe lén bằng Wireshark hoặc giả mạo đường truyền."

---

### SLIDE 12: BẢO MẬT XÁC THỰC JWT & CHÍNH SÁCH MẠNG CORS
- **JWT (JSON Web Token):**
  - Gồm 3 phần: `Header.Payload.Signature`.
  - Signature được ký bằng thuật toán HMAC-SHA256 với Secret Key an toàn tại Server.
  - Client gửi kèm trong Header: `Authorization: Bearer <Token>`.
- **Cơ chế phân quyền RBAC:** Giải mã Role ngay tại Middleware không cần query DB.
- **Xử lý CORS & Reverse Proxy:** Sử dụng Reverse Proxy của Vite chuyển tiếp request `/api` sang Backend để vượt qua chính sách Same-Origin Policy an toàn.

🗣️ **Lời thoại thuyết trình gợi ý:**
> "Về khâu xác thực, nhóm sử dụng chuẩn JWT Bearer. Khi người dùng đăng nhập thành công, server cấp một chuỗi token có chữ ký số. Mọi request sau đó chỉ cần đính kèm token vào header Authorization. Server chỉ cần đối chiếu chữ ký mà không phải truy vấn lại cơ sở dữ liệu, giúp giảm tải I/O mạng đáng kể. Đối với vấn đề Cross-Origin Resource Sharing (CORS) giữa 2 port 5173 và 5000, nhóm cấu hình Reverse Proxy ngay tại Vite để đảm bảo bảo mật và luồng truyền thông suốt."

---

### SLIDE 13: LUỒNG DỮ LIỆU 1 – ĐĂNG NHẬP & XÁC THỰC
1. Client gửi `POST /api/auth/login` mang `{ username, password }`.
2. Server truy vấn User, gọi `BCrypt.Verify()` so sánh mật khẩu băm với salt.
3. Server ký số JWT Token mang các Claims (UserId, Role, FullName).
4. Client nhận `200 OK`, lưu token vào `localStorage` và đính kèm vào Axios Interceptor.

🗣️ **Lời thoại thuyết trình gợi ý:**
> "Đây là sơ đồ tuần tự của luồng xác thực: Mật khẩu của thí sinh không bao giờ được lưu dạng rõ (plaintext) trong database mà được băm bằng thuật toán BCrypt với salt ngẫu nhiên. Khi đăng nhập thành công, token được cấp và lưu trữ an toàn phía client."

---

### SLIDE 14: LUỒNG DỮ LIỆU 2 – TỰ ĐỘNG SINH CÂU HỎI AI
1. Giáo viên nhập chủ đề/văn bản -> Gửi `POST /api/ai/generate`.
2. Backend đóng gói Prompt có System Instructions JSON -> Gọi Google Gemini API qua HTTPS POST.
3. Nhận phản hồi, phân tích JSON, kiểm tra tính hợp lệ (đủ 4 options, 1 đáp án đúng).
4. Lưu vào bảng `Questions` với trạng thái `PENDING`.
5. Giáo viên kiểm duyệt -> Gửi `PATCH /api/exams/questions/{id}/approve` để xuất bản.

🗣️ **Lời thoại thuyết trình gợi ý:**
> "Ở luồng dữ liệu thứ hai, Backend đóng vai trò như một HTTP Client gọi ra dịch vụ AI bên ngoài qua giao thức HTTPS. Quy trình này được bảo vệ bởi cơ chế kiểm tra schema dữ liệu trước khi ghi vào database nhằm loại bỏ hoàn toàn các câu hỏi bị lỗi cú pháp."

---

### SLIDE 15: LUỒNG DỮ LIỆU 3 – LÀM BÀI THI & CHẤM ĐIỂM
1. Học sinh nhấn Bắt đầu -> `POST /api/submissions/start`.
2. Server trả về thời gian làm bài tính theo **đồng hồ Server (Server Time)**, triệt tiêu gian lận chỉnh giờ máy client.
3. Đồng hồ đếm ngược chạy trên giao diện; tự động trigger submit khi hết giờ.
4. Gửi `POST /api/submissions/submit` -> Server đối chiếu bảng `Options`, tính điểm phần trăm và trả về kết quả kèm giải thích chi tiết.
5. **Cơ chế chống mất mạng (Fault Tolerance):** Nếu bị rớt mạng, học sinh vào lại hệ thống sẽ tiếp tục bài thi đang dở dang (`IN_PROGRESS`).

🗣️ **Lời thoại thuyết trình gợi ý:**
> "Ở luồng làm bài thi, nhóm đặc biệt chú trọng cơ chế chống gian lận thời gian: đồng hồ đếm ngược được tính toán dựa trên timestamp của máy chủ chứ không phụ thuộc vào đồng hồ cục bộ của máy học sinh. Đồng thời, nếu học sinh gặp sự cố mạng đột ngột thì bài thi vẫn được lưu trạng thái để có thể tiếp tục làm bài mà không mất quyền lợi."

---

### SLIDE 16: KẾT QUẢ ĐẠT ĐƯỢC & DEMO GIAO DIỆN
- 100% các API RESTful hoạt động ổn định và có tài liệu Swagger đầy đủ.
- Thời gian phản hồi API trung bình < 150ms.
- Tốc độ sinh câu hỏi bằng AI: chỉ 3-5 giây cho một bộ câu hỏi hoàn chỉnh.
- Giao diện Dark Mode hiện đại, responsive mượt mà trên máy tính và điện thoại.

🗣️ **Lời thoại thuyết trình gợi ý:**
> "Sau đây là các kết quả thực nghiệm: Hệ thống đạt tốc độ phản hồi rất nhanh, trung bình dưới 150ms cho các tác vụ thi cử. Giao diện được thiết kế trực quan, hỗ trợ đầy đủ các thao tác từ làm bài thi, nộp bài, xem giải thích chi tiết cho đến các biểu đồ thống kê điểm số phục vụ giáo viên."

---

### SLIDE 17: KẾT LUẬN & ĐỊNH HƯỚNG PHÁT TRIỂN CUỐI KỲ
- **Đạt được:** Hoàn thành trọn vẹn kiến trúc mạng Client-Server, áp dụng đúng các giao thức TCP/IP, HTTP/HTTPS, bảo mật JWT và ứng dụng AI thực tế.
- **Định hướng cuối kỳ:**
  1. Tích hợp **SignalR / WebSocket** để giám sát thí sinh theo thời gian thực (real-time proctoring).
  2. Bổ sung tính năng đấu đối kháng trắc nghiệm thời gian thực (Quiz Battle qua Socket).
  3. Đóng gói Docker Container và triển khai lên Cloud Server với tên miền và chứng chỉ SSL quốc tế.

🗣️ **Lời thoại thuyết trình gợi ý:**
> "Tóm lại, trong giai đoạn giữa kỳ, nhóm em đã hoàn thành đầy đủ mục tiêu đề ra cho môn Lập trình mạng. Hướng phát triển cho giai đoạn cuối kỳ, nhóm sẽ nâng cấp giao thức truyền thông lên WebSockets/SignalR để hỗ trợ tính năng thi đấu real-time và giám sát phòng thi trực tuyến. Em xin chân thành cảm ơn Thầy/Cô và các bạn đã lắng nghe!"

---

## 🎯 CÁC CÂU HỎI PHẢN BIỆN THƯỜNG GẶP TỪ GIẢNG VIÊN & CÁCH TRẢ LỜI

**Câu 1: Tại sao đồ án này lại dùng TCP mà không dùng UDP?**
> *Trả lời:* "Dạ thưa Thầy/Cô, trong ứng dụng thi trắc nghiệm trực tuyến, yêu cầu bắt buộc là tính toàn vẹn và độ tin cậy tuyệt đối của dữ liệu. Nếu dùng UDP, do không có cơ chế bắt tay và không có báo nhận ACK, các gói tin nộp bài thi hoặc câu hỏi có thể bị thất lạc trên mạng dẫn đến sai lệch kết quả thi của thí sinh. Do đó, giao thức TCP với cơ chế 3-way handshake và tự động phát lại (retransmission) là sự lựa chọn duy nhất phù hợp."

**Câu 2: Làm sao hệ thống chống được việc học sinh sửa giờ máy tính để kéo dài thời gian làm bài?**
> *Trả lời:* "Dạ thưa Thầy/Cô, thời gian làm bài không tính theo đồng hồ trên máy Client. Khi học sinh bấm bắt đầu, Server ghi nhận `StartedAt` theo giờ UTC của máy chủ. Mỗi khi Client tương tác hoặc nộp bài, Server sẽ tính: `Thời gian còn lại = Thời lượng đề thi - (Giờ hiện tại của Server - StartedAt)`. Dù học sinh có chỉnh đồng hồ trên máy tính lùi lại bao nhiêu đi nữa thì Server vẫn tính theo mốc giờ của chính nó và tự động khóa bài khi hết hạn."

**Câu 3: HTTPS bảo vệ dữ liệu thi cử như thế nào trước kẻ nghe lén dùng Wireshark?**
> *Trả lời:* "Dạ thưa Thầy/Cô, khi chưa có HTTPS, kẻ tấn công cùng mạng Wi-Fi có thể dùng Wireshark để bắt gói tin HTTP thuần, đọc được toàn bộ đáp án và token tài khoản ở dạng rõ. Với HTTPS, quá trình bắt tay TLS sẽ thiết lập một khóa phiên đối xứng (Session Key AES). Mọi gói tin ở tầng ứng dụng đều được mã hóa trước khi đưa xuống tầng TCP, nên kẻ bắt gói tin chỉ thấy các khối dữ liệu mã hóa ngẫu nhiên, không thể giải mã được nếu không có khóa bí mật."

**Câu 4: JWT lưu ở localStorage có an toàn không và Server xác thực nó như thế nào?**
> *Trả lời:* "Dạ thưa Thầy/Cô, JWT gồm 3 phần: Header, Payload và Signature. Server xác thực bằng cách lấy Header và Payload, kết hợp với mã bí mật (Secret Key) chỉ Server biết để băm lại bằng HMAC-SHA256. Nếu chữ ký trùng khớp thì token hợp lệ. Việc này không cần truy vấn database giúp tăng tốc độ mạng. Về lưu trữ, ngoài `localStorage`, hệ thống có thể nâng cấp lưu trong `HttpOnly Cookie` để phòng chống triệt để tấn công XSS."
