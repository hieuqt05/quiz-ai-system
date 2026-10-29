# NỘI DUNG SLIDE VÀ KỊCH BẢN THUYẾT TRÌNH BÁO CÁO ĐỒ ÁN
## Môn học: LẬP TRÌNH MẠNG
## Đề tài: QuizAI – Hệ Thống Trắc Nghiệm Online Tích Hợp AI & Giám Sát Thi Đa Máy

> 📁 **File PowerPoint trình chiếu chuẩn:** [`slide_thuyet_trinh_QuizAI_final.pptx`](file:///h:/Antigravity/Laptrinhmang/slide_thuyet_trinh_QuizAI_final.pptx)  
> 💡 **Đặc điểm thiết kế:** Slide được thiết kế theo phong cách **tối giản (Minimalist), cực kỳ ít chữ**, tập trung vào từ khóa in đậm và thẻ thông tin. Người thuyết trình sẽ dựa vào kịch bản lời thoại chi tiết bên dưới để diễn giải chuyên sâu, gây ấn tượng mạnh với Hội đồng Giảng viên.

---

## 📑 DANH MỤC 17 SLIDE BÁO CÁO ĐỒ ÁN CUỐI KỲ

1. **Slide 01:** Trang bìa (Báo cáo đồ án cuối kỳ • Lập trình mạng)
2. **Slide 02:** Lý do chọn đề tài & Mục tiêu dự án
3. **Slide 03:** Thành viên & Phân công công việc
4. **Slide 04:** Timeline – Kế hoạch & Tiến độ thực hiện
5. **Slide 05:** Chức năng hệ thống (Phân hệ Thí sinh & Quản trị viên/Giáo viên)
6. **Slide 06:** Ngăn xếp công nghệ toàn diện (Technology Stack)
7. **Slide 07:** Kiến trúc hệ thống tổng thể (3-Tier & Client-Server Architecture)
8. **Slide 08:** Cơ chế triển khai mạng (Mạng LAN `0.0.0.0` & Cloud Production Vercel)
9. **Slide 09:** Giao thức mạng & Mô hình TCP/IP (Tại sao dùng TCP thay vì UDP, Bắt tay 3 bước)
10. **Slide 10:** Giao thức Web & Kiến trúc RESTful API
11. **Slide 11:** HTTPS: Cơ chế hoạt động & Bảo mật TLS/SSL (Chống Wireshark)
12. **Slide 12:** Cơ chế xác thực JWT & Chính sách mạng CORS
13. **Slide 13:** Hệ thống chống gian lận đa tầng (3 lớp bảo vệ kỳ thi)
14. **Slide 14:** Luồng dữ liệu cốt lõi (Xác thực, Làm bài thi & AI sinh đề)
15. **Slide 15:** Kết quả đạt được & Đo lường hiệu năng thực nghiệm
16. **Slide 16:** Kết luận đồ án cuối kỳ & Hướng mở rộng tương lai
17. **Slide 17:** Lời cảm ơn Hội đồng & Thông tin Demo trực tuyến

---

# CHI TIẾT NỘI DUNG SLIDE & LỜI THOẠI THUYẾT TRÌNH (SPEAKER NOTES)

---

### SLIDE 01: TRANG BÌA
**Chữ trên Slide (Rất ít chữ):**
* **BÁO CÁO ĐỒ ÁN • MÔN LẬP TRÌNH MẠNG**
* **QuizAI – Hệ Thống Trắc Nghiệm Online Tích Hợp AI & Giám Sát Thi Đa Máy**
* *Client-Server • RESTful API • TCP/IP • Xác Thực JWT • Chống Gian Lận 3 Lớp*
* Giảng viên hướng dẫn: Bộ môn Lập Trình Mạng | Sinh viên thực hiện: Nhóm QuizAI

🗣️ **Lời thoại thuyết trình gợi ý (35 giây):**
> "Kính chào Thầy/Cô và các bạn. Hôm nay, nhóm em xin phép được báo cáo đồ án môn Lập trình mạng với đề tài: **QuizAI – Hệ thống trắc nghiệm trực tuyến tích hợp trí tuệ nhân tạo và giám sát thi đa máy**. Dự án này được chúng em xây dựng nhằm áp dụng thực tiễn các kiến thức mạng máy tính cốt lõi như mô hình Client-Server, giao thức truyền tin tin cậy TCP, kiến trúc RESTful API, bảo mật HTTPS và xác thực phi trạng thái JWT, đồng thời tích hợp mô hình GenAI Gemini để tự động hóa ngân hàng đề thi."

---

### SLIDE 02: LÝ DO CHỌN ĐỀ TÀI & MỤC TIÊU
**Chữ trên Slide:**
* **Thực trạng & Vấn đề:**
  - Soạn đề thủ công: Tốn thời gian, khó đa dạng hóa câu hỏi.
  - Gian lận trực tuyến: Chuyển tab tra Google, nhờ ChatGPT giải hộ.
  - Nhìn bài thi: Thí sinh ngồi cạnh nhau có cùng đề và vị trí đáp án.
  - Rủi ro đường truyền: Rớt mạng Wi-Fi làm mất dữ liệu bài thi đang làm dở.
* **Mục tiêu QuizAI:**
  - Gemini AI: Tự động sinh bộ đề 10-30 câu chuẩn xác trong 3-5 giây.
  - Chống gian lận 3 lớp: Bắt chuyển tab (3 lần nộp bài), chặn PrintScreen/DevTools.
  - Trộn đề ngẫu nhiên: Đảo vị trí câu hỏi & 4 đáp án A, B, C, D cho từng máy.
  - Auto-Save Real-time: Bảo toàn dữ liệu 100% khi rớt mạng hoặc sập nguồn.

🗣️ **Lời thoại thuyết trình gợi ý (40 giây):**
> "Xuất phát từ thực tế thi cử trực tuyến, nhóm nhận thấy 3 vấn đề nhức nhối: Thứ nhất, giáo viên mất nhiều công sức biên soạn đề thi; Thứ hai, học sinh rất dễ gian lận bằng cách chuyển tab hoặc nhìn bài bạn bên cạnh; Thứ ba, đường truyền mạng chập chờn có thể làm mất trắng kết quả thi của thí sinh. Mục tiêu của QuizAI là giải quyết triệt để các rào cản này bằng AI tạo đề tự động, hệ thống giám sát chống gian lận đa tầng và cơ chế tự phục hồi dữ liệu khi rớt mạng."

---

### SLIDE 03: THÀNH VIÊN & PHÂN CÔNG CÔNG VIỆC
**Chữ trên Slide (3 Cột):**
* **Backend & Network:** Xây dựng ASP.NET Core 9 API • Cấu hình TCP/IP, CORS & Port 0.0.0.0 • Tích hợp Gemini AI & JWT Auth • Thiết kế Database SQL Server.
* **Frontend & UI/UX:** Phát triển giao diện React 19 SPA • Thiết kế Dark Mode với TailwindCSS • Xử lý Auto-Save & Trộn đề ngẫu nhiên • Bảng thống kê & Xuất Excel (.xlsx).
* **Security & Testing:** Lập trình module Chống gian lận 3 lớp • Thiết lập SSH Tunnel (Pinggy / QR) • Kiểm thử chịu lỗi mạng & Stress test • Đóng gói tài liệu & Slide thuyết trình.

🗣️ **Lời thoại thuyết trình gợi ý (30 giây):**
> "Để dự án đạt hiệu quả cao nhất, nhóm phân chia công việc theo đúng các tầng kiến trúc mạng: Mảng Backend đảm nhiệm việc xử lý luồng dữ liệu, cấu hình mạng và kết nối AI; Mảng Frontend chịu trách nhiệm về giao diện SPA, cơ chế tự động lưu và xuất báo cáo điểm; Mảng Bảo mật và Kiểm thử phụ trách việc giám sát chống gian lận và thử nghiệm kết nối đa máy."

---

### SLIDE 04: TIMELINE – KẾ HOẠCH & TIẾN ĐỘ THỰC HIỆN
**Chữ trên Slide (4 Khối mốc thời gian):**
* **Giai đoạn 1 (Thiết kế):** Phân tích yêu cầu • Sơ đồ mạng • Thiết kế CSDL ERD • Chuẩn hóa RESTful API.
* **Giai đoạn 2 (Lập trình):** Viết Backend Web API • Viết Frontend React SPA • Tích hợp Gemini GenAI • Mã hóa BCrypt.
* **Giai đoạn 3 (Nâng cấp):** Mạng LAN & Tunneling • Anti-Cheat 3 lớp bảo vệ • Auto-Save & Trộn đề • Xuất báo cáo Excel .xlsx.
* **Giai đoạn 4 (Hoàn thiện):** Kiểm thử tải đa máy • Viết tài liệu đồ án • Đồng bộ mã nguồn GitHub • Sẵn sàng nghiệm thu.

🗣️ **Lời thoại thuyết trình gợi ý (30 giây):**
> "Quy trình phát triển của nhóm bám sát mô hình phát triển phần mềm chuẩn: Khởi đầu từ việc phân tích sơ đồ mạng và thiết kế cơ sở dữ liệu, tiếp đến là lập trình các module cốt lõi, nâng cấp các tính năng an ninh mạng và cuối cùng là kiểm thử đa máy trên thực tế để nghiệm thu sản phẩm."

---

### SLIDE 05: CHỨC NĂNG HỆ THỐNG
**Chữ trên Slide:**
* **Phân hệ Học sinh (Thí sinh):**
  - Đăng ký / Đăng nhập: Tài khoản bảo mật với JWT.
  - Làm bài trực tuyến: Đồng hồ đếm ngược đồng bộ Server UTC.
  - Trộn đề: Câu hỏi & 4 đáp án A, B, C, D đảo ngẫu nhiên.
  - Chống mất dữ liệu: Tự động lưu đáp án (Auto-Save) real-time.
  - Xem kết quả: Chấm điểm tức thì kèm giải thích chi tiết đáp án.
* **Phân hệ Quản trị & Giáo viên:**
  - AI Tạo đề: Nhập văn bản/chủ đề -> Gemini AI sinh trắc nghiệm.
  - Kiểm duyệt: Xem trước, sửa đổi hoặc xóa câu hỏi AI.
  - Quản lý đề: Tạo, xuất bản, xóa đề thi (Cascade Delete).
  - Giám sát vi phạm: Bôi đỏ cảnh báo thí sinh rời màn hình.
  - Xuất Excel (.xlsx): 1-Click tải bảng điểm chuẩn Microsoft Excel.

🗣️ **Lời thoại thuyết trình gợi ý (40 giây):**
> "Về mặt chức năng, hệ thống cung cấp đầy đủ nghiệp vụ cho cả hai phía: Phía thí sinh được trải nghiệm giao diện thi trực quan, có cơ chế xáo trộn đề chống nhìn bài và tự động lưu câu trả lời phòng ngừa sự cố mạng. Phía giáo viên được hỗ trợ tạo đề thi tự động bằng AI, duyệt câu hỏi, giám sát vi phạm gian lận thời gian thực và xuất toàn bộ bảng điểm lớp học ra file Excel chỉ với 1 cú click chuột."

---

### SLIDE 06: CÔNG NGHỆ & KỸ THUẬT SỬ DỤNG
**Chữ trên Slide (3 Khối):**
* **Frontend Stack:** React 19 SPA • Vite 8 Build • TailwindCSS Dark Mode • Axios Interceptor • SheetJS (xlsx) Export.
* **Backend Stack:** ASP.NET Core 9 Web API • Kestrel Server (<120ms) • JWT Stateless Auth • BCrypt.Net Salted Hash • Google Gemini GenAI.
* **Database & Network:** SQL Server LocalDB • EF Core 9 Code-First • IP Binding `0.0.0.0` • SSH Reverse Tunnel (Pinggy / QR Code) • UTF-8 BOM tiếng Việt.

🗣️ **Lời thoại thuyết trình gợi ý (35 giây):**
> "Hệ thống sử dụng ngăn xếp công nghệ hiện đại nhằm tối ưu hóa hiệu năng mạng: Frontend dùng React 19 kết hợp Vite cho tốc độ tải trang cực nhanh; Backend sử dụng ASP.NET Core 9 chạy trên nền Kestrel Server với độ trễ phản hồi dưới 120ms; Cơ sở dữ liệu SQL Server đảm bảo tính toàn vẹn ACID; cùng các công nghệ mạng tiên tiến như SSH Tunneling và chuẩn xuất bảng tính SheetJS."

---

### SLIDE 07: KIẾN TRÚC HỆ THỐNG TỔNG THỂ (3-TIER)
**Chữ trên Slide:**
* **Tầng Client (Presentation):** Single Page Application (SPA) • Gửi request qua giao thức HTTP/HTTPS • Caching LocalStorage & SessionStorage • Bắt sự kiện gian lận chuyển tab/chụp ảnh.
* **Tầng Server (Business Logic):** Tiếp nhận & điều phối RESTful API • Middleware kiểm tra JWT • Tính toán điểm số & đếm vi phạm • Đồng bộ giờ UTC Server • Gọi Google AI Studio qua HTTPS.
* **Tầng Database (Data Access):** Lưu trữ bền vững dữ liệu ACID • Bảng Users (Hash BCrypt) • Bảng Exams & Questions • Bảng Submissions (Lưu điểm & Số lần vi phạm) • Bảng Details.

🗣️ **Lời thoại thuyết trình gợi ý (40 giây):**
> "QuizAI tuân thủ mô hình 3 tầng Client-Server chuẩn mực: Tầng Client tương tác trực tiếp với người dùng và quản lý bộ nhớ đệm cục bộ; Tầng Server đóng vai trò trung tâm xử lý nghiệp vụ, kiểm tra tính hợp lệ của token và chấm điểm độc lập; Tầng Database đảm bảo dữ liệu đề thi và lịch sử làm bài được lưu trữ bền vững, tuyệt đối không cho phép Client kết nối trực tiếp vào Database nhằm loại bỏ nguy cơ lộ dữ liệu."

---

### SLIDE 08: CƠ CHẾ TRIỂN KHAI MẠNG: LAN & CLOUD PRODUCTION
**Chữ trên Slide:**
* **1. Mạng LAN (Phòng Lab / Wi-Fi):**
  - Lắng nghe `0.0.0.0`: Bind cổng 5000 & 5173 trên mọi card mạng.
  - Vite Reverse Proxy: Chuyển tiếp ngầm `/api/*` về Backend Kestrel.
  - Mở Firewall Windows: Lệnh netsh mở port cho các máy con kết nối.
  - Truy cập tức thì: Học sinh mở `http://192.168.x.x:5173`.
  - Khởi động 1-Click: File `chay_he_thong.bat` tự tìm IP nội bộ.
* **2. Cloud Production (Vercel & Cloudflare):**
  - Tên miền chính thức: `https://quiz-ai-system.vercel.app/`.
  - CDN Toàn cầu: Vercel Edge Network tải giao diện siêu tốc.
  - Cloudflare HTTPS Tunnel: Kết nối an toàn không cần mở port modem.
  - Vượt qua rào cản mạng: Chạy mượt mà trên 4G/5G và mạng ngoài trường.
  - CI/CD Tự động: Commit code lên GitHub tự động cập nhật hệ thống.

🗣️ **Lời thoại thuyết trình gợi ý (45 giây):**
> "Điểm sáng của đề tài là khả năng triển khai linh hoạt ở cả hai môi trường: Ở môi trường nội bộ, server bind vào IP `0.0.0.0` để phục vụ phòng máy trường học với độ trễ tối thiểu. Đồng thời, nhóm đã đưa thành công hệ thống lên đám mây Production tại địa chỉ `https://quiz-ai-system.vercel.app/` kết hợp cùng đường hầm bảo mật Cloudflare. Điều này giúp hệ thống hoạt động thông suốt trên toàn bộ thiết bị di động, mạng 4G/5G từ xa mà hoàn toàn không phụ thuộc vào việc cấu hình mạng hay mở cổng modem."

---

### SLIDE 09: GIAO THỨC MẠNG & MÔ HÌNH TCP/IP
**Chữ trên Slide:**
* **Tại sao chọn TCP thay vì UDP?**
  - Hướng kết nối (Connection-oriented): Đảm bảo thông suốt.
  - Tin cậy tuyệt đối: Có cờ báo nhận ACK và Sequence Number.
  - Chống mất gói tin: Tự động phát lại (Retransmission) nếu lag mạng.
  - Không dùng UDP: Tránh thất lạc gói tin nộp bài làm sai lệch điểm.
* **Cơ chế Bắt tay 3 bước (TCP 3-Way Handshake):**
  - Bước 1 (SYN): Client gửi yêu cầu kết nối kèm số Seq khởi tạo.
  - Bước 2 (SYN-ACK): Server xác nhận và gửi số Seq của mình.
  - Bước 3 (ACK): Client xác nhận hoàn tất -> Phiên TCP mở.
  - Ứng dụng: Mọi cuộc gọi HTTP/HTTPS đều thiết lập qua TCP.

🗣️ **Lời thoại thuyết trình gợi ý (40 giây):**
> "Dưới góc độ môn Lập trình mạng, bài thi trắc nghiệm đặt ra yêu cầu tuyệt đối về tính toàn vẹn dữ liệu. Giao thức TCP với cơ chế bắt tay 3 bước SYN, SYN-ACK, ACK và tự động truyền lại gói tin khi có sự cố nghẽn mạng là sự lựa chọn bắt buộc. Nếu sử dụng giao thức UDP, gói tin nộp bài của thí sinh có thể bị thất lạc trên đường truyền dẫn đến việc bài làm bị mất điểm hoặc không thể chấm điểm."

---

### SLIDE 10: GIAO THỨC WEB & RESTFUL API
**Chữ trên Slide:**
* **Các Phương Thức HTTP Tiêu Chuẩn:**
  - `GET`: Lấy tài nguyên (Đọc danh sách đề, xem bảng điểm).
  - `POST`: Tạo tài nguyên mới (Đăng nhập, Bắt đầu thi, Nộp bài).
  - `PATCH`: Cập nhật một phần (Duyệt câu hỏi, cập nhật vi phạm).
  - `DELETE`: Xóa tài nguyên (Xóa vĩnh viễn đề thi kèm dữ liệu liên quan).
* **Đặc Trưng Kiến Trúc REST:**
  - Stateless (Phi trạng thái): Mỗi request chứa đủ thông tin xác thực.
  - Định dạng JSON: Gọn nhẹ, tối ưu băng thông đường truyền mạng.
  - Mã trạng thái HTTP chuẩn: 200 OK, 201 Created, 401 Unauthorized, 403 Forbidden.
  - Swagger UI tích hợp: Tài liệu hóa trực quan tại `/swagger`.

🗣️ **Lời thoại thuyết trình gợi ý (35 giây):**
> "Hệ thống chuẩn hóa toàn bộ giao tiếp mạng theo kiến trúc RESTful API. Dữ liệu được coi là các tài nguyên và thao tác thông qua các phương thức HTTP rõ ràng: GET để truy vấn, POST để tạo mới bài nộp, PATCH để duyệt câu hỏi và DELETE để xóa đề thi. Định dạng JSON gọn nhẹ giúp tiết kiệm tối đa băng thông mạng và tương thích với mọi thiết bị client."

---

### SLIDE 11: HTTPS & CƠ CHẾ BẢO MẬT TLS/SSL
**Chữ trên Slide:**
* **Quy trình Bắt tay TLS (TLS Handshake):**
  - ClientHello: Client gửi phiên bản TLS và danh sách mã hóa hỗ trợ.
  - ServerHello & Certificate: Server gửi chứng chỉ số chứa Public Key.
  - Key Exchange: Trao đổi khóa bí mật phiên (Session Key) an toàn.
  - Mã hóa đối xứng: Toàn bộ gói tin sau đó được mã hóa bằng AES-256.
* **Tầm quan trọng trong QuizAI:**
  - Chống bắt gói tin (Wireshark): Kẻ nghe lén chỉ thấy dữ liệu mã hóa.
  - Bảo vệ Token & Mật khẩu: Không bị lộ mã JWT trên đường truyền Wi-Fi.
  - Bảo vệ Gemini API Key: Kênh HTTPS ngăn chặn rò rỉ khóa bí mật.
  - Toàn vẹn dữ liệu: Đảm bảo đáp án của thí sinh không bị sửa đổi trên mạng.

🗣️ **Lời thoại thuyết trình gợi ý (40 giây):**
> "Để bảo vệ kỳ thi trước các cuộc tấn công mạng, giao thức HTTPS với lớp bảo mật TLS là yếu tố sống còn. Quá trình bắt tay TLS sẽ thiết lập một khóa phiên đối xứng AES-256. Dù kẻ tấn công cùng phòng thi có sử dụng phần mềm Wireshark để bắt gói tin mạng, họ cũng chỉ thấy các khối dữ liệu mã hóa ngẫu nhiên, hoàn toàn không thể đọc trộm được đề thi, token đăng nhập hay can thiệp sửa đổi đáp án của thí sinh."

---

### SLIDE 12: XÁC THỰC JWT & CHÍNH SÁCH MẠNG CORS
**Chữ trên Slide:**
* **Xác thực JWT (JSON Web Token):**
  - Cấu trúc 3 phần: `Header . Payload . Signature` (HMAC-SHA256).
  - Stateless Auth: Server không tốn RAM lưu Session hàng trăm học sinh.
  - Xác thực nhanh: Server dùng `SecretKey` kiểm tra tính hợp lệ chữ ký.
  - Axios Interceptor: Tự động đính kèm Bearer Token vào mọi request.
* **Chính sách mạng CORS:**
  - Same-Origin Policy: Trình duyệt mặc định chặn request khác domain/IP.
  - Cấu hình nới lỏng: `policy.SetIsOriginAllowed(_ => true)`.
  - Chấp nhận mọi IP: Laptop, điện thoại hay IP LAN đều kết nối được.
  - Bảo mật an toàn: Vẫn duy trì kiểm soát nghiêm ngặt bằng JWT Token.

🗣️ **Lời thoại thuyết trình gợi ý (35 giây):**
> "Cơ chế xác thực JWT Stateless giúp máy chủ không cần tốn bộ nhớ RAM lưu session của từng thí sinh, chỉ cần giải mã chữ ký số là xác định được danh tính. Đồng thời, cấu hình chính sách CORS nới lỏng cho phép các thiết bị di động hay laptop mang IP mạng LAN khác nhau đều gửi được dữ liệu về máy chủ mà không bị trình duyệt chặn theo chính sách cùng nguồn gốc."

---

### SLIDE 13: HỆ THỐNG CHỐNG GIAN LẬN ĐA TẦNG (3 LỚP)
**Chữ trên Slide (3 Cột):**
* **Lớp 1 (Chống chuyển tab):** Bắt `visibilitychange` & `blur` • Cooldown 2.5s chống tính đúp • Vi phạm lần 1 & 2: Cảnh báo đỏ • **Vi phạm lần 3: Tự động thu hồi & nộp bài ngay.**
* **Lớp 2 (Chặn sao chép):** Chặn phím `PrintScreen` (chớp đen màn hình) • Khóa `Ctrl+C/X/A`, `Ctrl+P` (in) • Khóa `F12` & DevTools soi đáp án • Tắt chuột phải & chống bôi đen văn bản.
* **Lớp 3 (Watermark Camera):** In mờ chéo Họ tên & Username thí sinh • Phủ khắp nền màn hình bài thi • Chụp ảnh điện thoại lộ rõ danh tính • Ghi nhận số vi phạm gửi về máy chủ.

🗣️ **Lời thoại thuyết trình gợi ý (45 giây):**
> "Hệ thống chống gian lận của QuizAI được xây dựng 3 lớp vững chắc: Lớp 1 phát hiện hành vi rời màn hình hoặc bấm Alt+Tab. Nhờ cơ chế cooldown 2.5 giây, mỗi lần chuyển tab chỉ tính đúng 1 lần vi phạm: thí sinh được cảnh báo ở lần 1, lần 2 và đúng lần thứ 3 bài thi sẽ tự động bị thu hồi. Lớp 2 vô hiệu hóa toàn bộ phím tắt chụp màn hình, in ấn, phím F12 mở DevTools và chuột phải. Lớp 3 là Watermark in chéo tên thí sinh lên màn hình, nếu dùng điện thoại chụp ảnh lại thì danh tính người chụp cũng sẽ in rõ trên câu hỏi."

---

### SLIDE 14: LUỒNG DỮ LIỆU CỐT LÕI (DATA FLOW)
**Chữ trên Slide (3 Cột):**
* **Luồng 1 (Xác thực):** 1. Gửi `POST /auth/login` • 2. So khớp BCrypt Hash • 3. Ký số JWT Token • 4. Lưu vào LocalStorage • 5. Phân quyền Admin/User.
* **Luồng 2 (Thi & Chấm điểm):** 1. Bắt đầu: Nhận đề thi • 2. Client: Trộn đề & Auto-Save • 3. Giám sát: Đếm chuyển tab • 4. Nộp bài: Gửi danh sách chọn • 5. Chấm điểm & hiện giải thích.
* **Luồng 3 (AI Sinh đề thi):** 1. Giáo viên nhập chủ đề/tài liệu • 2. Backend gửi Prompt tới Gemini • 3. Nhận phản hồi JSON câu hỏi • 4. Giáo viên duyệt & chỉnh sửa • 5. Lưu vào ngân hàng CSDL.

🗣️ **Lời thoại thuyết trình gợi ý (45 giây):**
> "Về mặt luồng dữ liệu, hệ thống chia làm 3 quy trình chính: Ở luồng xác thực, mật khẩu được kiểm tra qua hàm băm BCrypt có muối trước khi server cấp JWT Token có chữ ký số. Ở luồng làm bài thi, client nhận đề thi và đồng bộ thời gian theo server, câu hỏi được xáo trộn ngẫu nhiên và lưu tạm vào LocalStorage để chống mất mạng. Và ở luồng tạo đề, giáo viên chỉ cần nhập tài liệu hoặc chủ đề, backend sẽ gọi Gemini API để nhận về cấu trúc JSON câu hỏi, giáo viên có toàn quyền kiểm duyệt trước khi lưu vào ngân hàng đề thi."

---

### SLIDE 15: KẾT QUẢ ĐẠT ĐƯỢC & ĐO LƯỜNG HIỆU NĂNG
**Chữ trên Slide (4 Khối số liệu & 1 Bảng điểm nhấn):**
* **`< 120 ms`:** Tốc độ phản hồi API trung bình qua giao thức HTTP/HTTPS.
* **`3 - 5 giây`:** Gemini AI sinh hoàn chỉnh 10-20 câu hỏi kèm 4 đáp án & giải thích.
* **`100%`:** Bảo toàn dữ liệu bài làm khi rớt mạng Wi-Fi hoặc F5 tải lại trang.
* **`Chuẩn .XLSX`:** Xuất bảng điểm Excel tự căn chỉnh độ rộng cột, triệt tiêu lỗi `###`.
* **Điểm nổi bật:** Chạy thực tế trên đám mây Production `https://quiz-ai-system.vercel.app/`, hỗ trợ đa thiết bị an toàn, 100% mã nguồn đồng bộ trên GitHub.

🗣️ **Lời thoại thuyết trình gợi ý (40 giây):**
> "Kết quả đo lường thực tế chứng minh hiệu năng vượt trội: Độ trễ phản hồi API trung bình dưới 120ms, AI tạo bộ đề hoàn chỉnh chỉ trong 3 đến 5 giây. Khả năng bảo toàn dữ liệu khi giả lập ngắt mạng đạt 100%. Bảng điểm xuất ra file Excel .XLSX tự động căn chỉnh kích thước cột hoàn hảo. Đặc biệt, hệ thống đã chạy ổn định trên môi trường đám mây Production tại địa chỉ quiz-ai-system.vercel.app cho phép bất kỳ ai cũng có thể truy cập thi thử trực tiếp."

---

### SLIDE 16: KẾT LUẬN & HƯỚNG MỞ RỘNG TƯƠNG LAI
**Chữ trên Slide:**
* **Kết Luận Đạt Được:**
  - Hoàn thành trọn vẹn kiến trúc mạng Client-Server 3 tầng chuẩn chỉ.
  - Vận dụng xuất sắc kiến thức: TCP/IP, HTTP/HTTPS, REST, CORS & JWT.
  - Giải quyết triệt để vấn đề gian lận thi cử và mất bài khi rớt mạng.
  - Tích hợp thành công GenAI Gemini tạo đề thi thông minh tự động.
  - Triển khai thành công lên môi trường đám mây Vercel Production.
* **Hướng Phát Triển Tương Lai:**
  - WebSocket / SignalR: Chế độ thi đấu đối kháng trực tiếp (Kahoot Mode).
  - AI Camera Proctoring: Nhận diện khuôn mặt & phát hiện quay cóp qua webcam.
  - Mobile Application: Đóng gói app đa nền tảng Flutter / React Native.
  - Microservices Architecture: Tách riêng dịch vụ AI Generator và Auth Service.
  - Database Clustering: Nhân bản CSDL tăng khả năng chịu tải hàng nghìn thí sinh.

🗣️ **Lời thoại thuyết trình gợi ý (40 giây):**
> "Tóm lại, dự án QuizAI đã hiện thực hóa trọn vẹn mục tiêu của môn học Lập trình mạng thành một sản phẩm có tính ứng dụng cao trong giáo dục và thi cử trực tuyến. Trong tương lai, nhóm dự kiến sẽ mở rộng giao thức hai chiều thời gian thực với WebSocket và SignalR để phát triển chế độ thi đối kháng như Kahoot, đồng thời tích hợp webcam AI để nhận diện khuôn mặt thí sinh theo thời gian thực."

---

### SLIDE 17: Q&A / CẢM ƠN HỘI ĐỒNG & GIẢNG VIÊN
**Chữ trên Slide:**
* **LỜI CẢM ƠN:** Cảm Ơn Quý Thầy Cô & Hội Đồng Đã Lắng Nghe!
* **Hệ thống trực tuyến:** `https://quiz-ai-system.vercel.app/`
* **Mã nguồn dự án:** `https://github.com/hieuqt05/quiz-ai-system`
* *Nhóm xin sẵn sàng lắng nghe nhận xét và trả lời các câu hỏi từ Hội Đồng!*

🗣️ **Lời thoại thuyết trình gợi ý (20 giây):**
> "Dưới đây là link trải nghiệm trực tuyến của hệ thống và toàn bộ mã nguồn trên GitHub. Nhóm em xin chân thành cảm ơn Quý Thầy/Cô và Hội đồng đã chú ý lắng nghe bài báo cáo. Nhóm em rất mong nhận được những góp ý quý báu và xin sẵn sàng trả lời các câu hỏi từ Thầy/Cô!"
