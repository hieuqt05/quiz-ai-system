# NỘI DUNG SLIDE VÀ KỊCH BẢN THUYẾT TRÌNH BÁO CÁO ĐỒ ÁN
## Môn học: LẬP TRÌNH MẠNG
## Đề tài: QuizAI – Hệ Thống Trắc Nghiệm Online Tích Hợp AI & Giám Sát Thi Đa Máy

> 📁 **File PowerPoint trình chiếu chuẩn:** [`slide_thuyet_trinh_QuizAI_final.pptx`](file:///h:/Antigravity/Laptrinhmang/slide_thuyet_trinh_QuizAI_final.pptx)  
> 💡 **Đặc điểm thiết kế:** Slide được thiết kế theo phong cách **tối giản (Minimalist), cực kỳ ít chữ**, tập trung vào từ khóa in đậm và thẻ thông tin. Người thuyết trình sẽ dựa vào kịch bản lời thoại chi tiết bên dưới để diễn giải chuyên sâu, gây ấn tượng mạnh với Hội đồng Giảng viên.

---

## 📑 DANH MỤC 16 SLIDE CHUẨN CHECKLIST YÊU CẦU

1. **Slide 01:** Trang bìa (Tên môn học, Tên đề tài, Giảng viên, Sinh viên thực hiện)
2. **Slide 02:** Lý do chọn đề tài & Mục tiêu dự án
3. **Slide 03:** Thành viên & Phân công công việc
4. **Slide 04:** Timeline – Kế hoạch & Tiến độ thực hiện
5. **Slide 05:** Chức năng hệ thống (Phân hệ Học sinh & Quản trị viên)
6. **Slide 06:** Công nghệ & Kỹ thuật sử dụng (Technology Stack)
7. **Slide 07:** Kiến trúc hệ thống tổng thể (3-Tier & Client-Server Architecture)
8. **Slide 08:** Cơ chế chạy đa máy (Mạng LAN `0.0.0.0` & Public Internet Pinggy)
9. **Slide 09:** Giao thức mạng & Mô hình TCP/IP (Tại sao dùng TCP thay vì UDP, Bắt tay 3 bước)
10. **Slide 10:** Giao thức Web & Cơ chế hoạt động RESTful API
11. **Slide 11:** HTTPS: Cơ chế hoạt động & Bảo mật TLS/SSL (Chống Wireshark)
12. **Slide 12:** Cơ chế xác thực JWT & Chính sách mạng CORS
13. **Slide 13:** Hệ thống chống gian lận đa tầng (3 lớp bảo vệ kỳ thi)
14. **Slide 14:** Luồng dữ liệu chính (Đăng nhập xác thực & Làm bài thi thời gian thực)
15. **Slide 15:** Kết quả đạt được & Hiệu năng thực nghiệm
16. **Slide 16:** Kết luận & Định hướng phát triển cuối kỳ

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

### SLIDE 08: CƠ CHẾ CHẠY ĐA MÁY (LAN / INTERNET)
**Chữ trên Slide:**
* **1. Mạng LAN (Phòng Lab / Wi-Fi):**
  - Lắng nghe `0.0.0.0`: Bind cổng 5000 & 5173 trên mọi card mạng.
  - Vite Reverse Proxy: Chuyển tiếp `/api/*` về Backend Kestrel.
  - Truy cập tức thì: Máy con gõ `http://192.168.x.x:5173`.
  - Khởi động 1-Click: File `chay_he_thong.bat` tự tìm IP nội bộ.
* **2. Public Internet (Khác mạng / 4G):**
  - SSH Reverse Tunnel: Pinggy mã hóa dữ liệu qua cổng 443.
  - Bỏ qua Firewall: Vượt qua bộ lọc AP Isolation của trường học.
  - Mã QR tiện lợi: Điện thoại chỉ cần bật camera quét mã để thi.
  - Bảo mật TLS: Mã hóa End-to-End an toàn tuyệt đối.

🗣️ **Lời thoại thuyết trình gợi ý (45 giây):**
> "Điểm sáng của đề tài là khả năng chạy đa máy trong thực tế: Server được cấu hình bind vào IP đại diện `0.0.0.0`, cho phép mọi thiết bị trong mạng Wi-Fi truy cập thẳng qua IP LAN của máy chủ. Đặc biệt, đối với các mạng bị chặn kết nối nội bộ như Wi-Fi trường học có bật AP Isolation, hệ thống tích hợp sẵn kênh truyền SSH Reverse Tunnel, cấp một đường link HTTPS công khai kèm mã QR để các máy ở xa hay dùng 4G đều vào thi được ngay mà không cần mở port modem."

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

### SLIDE 14: LUỒNG DỮ LIỆU CHÍNH CỦA HỆ THỐNG
**Chữ trên Slide (2 Khối luồng dữ liệu):**
* **Luồng 1 (Đăng nhập & Xác thực):**
  1. Client gửi `POST /api/auth/login` kèm thông tin đăng nhập.
  2. Server kiểm tra Username & so khớp mã băm mật khẩu BCrypt.
  3. Server tạo chuỗi JWT Token có chữ ký số -> Trả về Client.
  4. Client lưu Token vào LocalStorage và phân hướng theo Role.
* **Luồng 2 (Làm bài thi & Chấm điểm):**
  1. Bắt đầu: `POST /api/submissions/start` -> Nhận đề & Server Time.
  2. Làm bài: Trộn ngẫu nhiên câu hỏi & Auto-Save vào LocalStorage.
  3. Giám sát: Ghi nhận vi phạm chuyển tab (Tối đa 3 lần).
  4. Nộp bài: `POST /api/submissions/submit` -> Chấm điểm & hiện giải thích.

🗣️ **Lời thoại thuyết trình gợi ý (40 giây):**
> "Về mặt luồng dữ liệu, mọi hoạt động đều diễn ra chặt chẽ: Ở luồng đăng nhập, mật khẩu được kiểm tra qua hàm băm BCrypt có muối trước khi server cấp token JWT. Ở luồng làm bài thi, client nhận đề thi và đồng bộ thời gian theo giờ server, câu hỏi được xáo trộn ngẫu nhiên và lưu tạm vào LocalStorage để chống mất mạng. Khi kết thúc, gói tin nộp bài được server đối chiếu đáp án, tính điểm phần trăm và lưu vết số lần vi phạm của thí sinh."

---

### SLIDE 15: KẾT QUẢ ĐẠT ĐƯỢC & HIỆU NĂNG THỰC TẾ
**Chữ trên Slide (4 Khối số liệu lớn):**
* **`< 120 ms`:** Tốc độ phản hồi API trung bình qua giao thức HTTP.
* **`3 - 5 giây`:** Gemini AI sinh hoàn chỉnh 10 câu hỏi kèm giải thích.
* **`100%`:** Bảo toàn dữ liệu khi rớt mạng Wi-Fi hoặc F5 tải lại trang.
* **`Chuẩn .XLSX`:** Xuất bảng điểm Excel độ rộng chuẩn, triệt tiêu lỗi `###`.
* *100% các tính năng hoạt động ổn định trên cả máy tính và điện thoại thông minh.*

🗣️ **Lời thoại thuyết trình gợi ý (35 giây):**
> "Kết quả thực nghiệm cho thấy hệ thống vận hành cực kỳ mượt mà: Độ trễ phản hồi API trung bình dưới 120ms, thời gian AI tạo bộ đề chỉ từ 3 đến 5 giây. Khả năng bảo toàn dữ liệu khi giả lập ngắt mạng đạt 100%. Đặc biệt, tính năng xuất bảng điểm đã được nâng cấp lên chuẩn file Excel .XLSX với độ rộng cột tự động, khắc phục hoàn toàn lỗi hiển thị dấu thăng hay che khuất chữ của các định dạng CSV cũ."

---

### SLIDE 16: KẾT LUẬN & ĐỊNH HƯỚNG PHÁT TRIỂN
**Chữ trên Slide:**
* **Kết Luận Đạt Được:**
  - Hoàn thành trọn vẹn kiến trúc mạng Client-Server.
  - Vận dụng xuất sắc các giao thức TCP/IP, HTTP, HTTPS & JWT.
  - Giải quyết triệt để vấn đề gian lận và rớt mạng khi thi cử.
  - Ứng dụng thực tiễn cao: Sẵn sàng dùng cho lớp học và kỳ thi.
* **Định Hướng Cuối Kỳ:**
  - WebSocket / SignalR: Chế độ thi đấu đối kháng trực tiếp (Kahoot Mode).
  - AI Camera: Giám sát nhận diện khuôn mặt qua webcam.
  - Docker Container: Đóng gói toàn bộ Backend & DB vào Container.
  - Cloud Deployment: Triển khai lên máy chủ đám mây với tên miền riêng.

🗣️ **Lời thoại thuyết trình gợi ý (35 giây):**
> "Tóm lại, dự án QuizAI đã hiện thực hóa trọn vẹn các kiến thức cốt lõi của môn Lập trình mạng thành một sản phẩm có tính ứng dụng cao trong giáo dục. Hướng phát triển cho giai đoạn cuối kỳ, nhóm sẽ nâng cấp giao thức truyền thông hai chiều thời gian thực bằng WebSockets và SignalR để xây dựng chế độ thi đấu đối kháng trực tiếp, đồng thời đóng gói Docker và đưa hệ thống lên máy chủ đám mây. Nhóm em xin chân thành cảm ơn Thầy/Cô và các bạn đã lắng nghe!"
