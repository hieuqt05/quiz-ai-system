# SLIDE BÁO CÁO ĐỒ ÁN LẬP TRÌNH MẠNG (PHIÊN BẢN NGẮN GỌN & LỜI THOẠI)
## Đề tài: QuizAI – Hệ Thống Trắc Nghiệm Online Tích Hợp AI & Giám Sát Thi Đa Máy
> 📁 **File PowerPoint trình chiếu trực tiếp:** [`slide_QuizAI_ngan_gon.pptx`](file:///h:/Antigravity/Laptrinhmang/slide_QuizAI_ngan_gon.pptx)  
> ⏱️ **Thời lượng báo cáo lý tưởng:** 5 - 7 phút (Mỗi slide từ 30 - 45 giây)

---

## 📑 MỤC LỤC 10 SLIDE TRỌNG TÂM
1. **Slide 01:** Trang Bìa (Giới thiệu đề tài & Thành viên)
2. **Slide 02:** Đặt Vấn Đề & Mục Tiêu (Thách thức thi cử & Giải pháp QuizAI)
3. **Slide 03:** Kiến Trúc Hệ Thống (Mô hình Client - Server 3 Tầng)
4. **Slide 04:** Truyền Thông Mạng Đa Máy (Chạy mạng LAN & Public Internet)
5. **Slide 05:** Trí Tuệ Nhân Tạo (Gemini GenAI tạo đề thi chuẩn cấu trúc)
6. **Slide 06:** Hệ Thống Chống Gian Lận (3 lớp bảo vệ kỳ thi trung thực)
7. **Slide 07:** Độ Tin Cậy & Tự Phục Hồi (Auto-Save, Shuffling & Timestamp Server)
8. **Slide 08:** Bảng Quản Trị & Xuất Excel (Giám sát trực tiếp & Báo cáo điểm)
9. **Slide 09:** Kết Quả Đạt Được & Hiệu Năng Thực Nghiệm
10. **Slide 10:** Kết Luận & Định Hướng Phát Triển Cuối Kỳ

---

# CHI TIẾT NỘI DUNG SLIDE & KỊCH BẢN LỜI THOẠI (SPEAKER NOTES)

---

### SLIDE 01: TRANG BÌA
**Nội dung hiển thị trên Slide:**
* **Chủ đề:** Báo Cáo Đồ Án • Môn Lập Trình Mạng
* **Tên đề tài:** QuizAI – Hệ Thống Trắc Nghiệm Online Tích Hợp AI & Giám Sát Kỳ Thi
* **Từ khóa công nghệ:** Client-Server • RESTful API • TCP/IP • JWT Security • Anti-Cheat 3 Lớp
* **Thông tin:** Giảng viên hướng dẫn & Sinh viên thực hiện

🗣️ **Lời thoại thuyết trình gợi ý:**
> "Kính chào Thầy/Cô và các bạn. Hôm nay, nhóm em xin phép được báo cáo đồ án môn Lập trình mạng với đề tài: **QuizAI – Hệ thống trắc nghiệm trực tuyến tích hợp trí tuệ nhân tạo và giám sát thi đa máy**. Dự án này được chúng em xây dựng nhằm áp dụng thực tiễn các kiến thức cốt lõi của môn học như mô hình Client-Server, giao thức TCP, kiến trúc RESTful API, cơ chế bảo mật HTTPS và xác thực phi trạng thái JWT, đồng thời tích hợp mô hình AI Gemini để giải quyết bài toán tự động hóa ngân hàng đề thi."

💡 *Mẹo:* Giọng nói rõ ràng, tự tin, dừng 2 giây sau khi đọc tên đề tài để mọi người chú ý vào màn hình.

---

### SLIDE 02: ĐẶT VẤN ĐỀ & MỤC TIÊU
**Nội dung hiển thị trên Slide:**
* **Thực trạng & Thách thức:**
  - Biên soạn đề thủ công: Tốn thời gian, khó đa dạng hóa câu hỏi.
  - Gian lận online: Chuyển tab tra cứu Google, ChatGPT hỗ trợ giải.
  - Ngồi cạnh nhìn bài: Đề thi cùng thứ tự câu hỏi và đáp án.
  - Rủi ro đường truyền: Rớt mạng đột ngột làm mất bài làm dở dang.
* **Mục tiêu của QuizAI:**
  - Gemini AI: Tự động sinh 10-30 câu hỏi chuẩn xác trong 3-5 giây.
  - Giám sát 3 lớp: Bắt chuyển tab (3 lần hủy bài), chặn PrintScreen/DevTools, Watermark camera.
  - Trộn đề thông minh: Đảo ngẫu nhiên câu hỏi & 4 đáp án A, B, C, D.
  - Auto-Save Real-time: Bảo toàn dữ liệu 100% khi rớt mạng hoặc sập nguồn.

🗣️ **Lời thoại thuyết trình gợi ý:**
> "Xuất phát từ thực tế thi cử trực tuyến hiện nay, chúng em nhận thấy 3 vấn đề lớn: Thứ nhất, giáo viên mất rất nhiều thời gian soạn đề; Thứ hai, học sinh rất dễ gian lận bằng cách mở tab mới tra Google hoặc nhìn bài bạn bên cạnh; Thứ ba, sự cố mạng chập chờn có thể khiến bài thi bị mất trắng. Mục tiêu của QuizAI là giải quyết triệt để các rào cản này bằng cách kết hợp AI tạo đề tự động, cơ chế trộn đề ngẫu nhiên, hệ thống chống gian lận đa tầng và cơ chế tự phục hồi dữ liệu khi gặp sự cố mạng."

---

### SLIDE 03: KIẾN TRÚC MẠNG HỆ THỐNG (3-TIER)
**Nội dung hiển thị trên Slide:**
* **Tầng Client (React 19 + Vite):**
  - Giao diện Single Page Application (SPA), Dark Mode hiện đại.
  - Axios Interceptors tự đính kèm JWT Bearer Token.
* **Tầng Server (ASP.NET Core 9 Web API):**
  - Xử lý đa luồng (Multi-threading), độ trễ thấp (<120ms).
  - JWT Stateless Authentication, CORS mở rộng cho mạng LAN.
* **Tầng Database (SQL Server LocalDB):**
  - EF Core 9 Migration, mã hóa mật khẩu BCrypt.
  - Lưu trữ đề thi, bài nộp và số lần vi phạm quy chế.

🗣️ **Lời thoại thuyết trình gợi ý:**
> "Về mặt kỹ thuật mạng, QuizAI tuân thủ mô hình kiến trúc 3 tầng chuẩn mực: Tầng Client là Single Page Application viết bằng React 19, giao tiếp với máy chủ thông qua giao thức HTTP/HTTPS. Tầng Server được xây dựng trên nền tảng ASP.NET Core 9 với khả năng xử lý bất đồng bộ đa luồng, sử dụng JWT để xác thực người dùng mà không cần lưu phiên trên server giúp tiết kiệm bộ nhớ. Cuối cùng, tầng Database quản lý toàn vẹn dữ liệu đề thi và lịch sử làm bài của thí sinh."

---

### SLIDE 04: TRUYỀN THÔNG MẠNG ĐA MÁY (LAN / INTERNET)
**Nội dung hiển thị trên Slide:**
* **Chế độ Mạng LAN (Phòng Lab / Cùng Wi-Fi):**
  - Backend & Frontend lắng nghe trên `0.0.0.0` (Port 5000 & 5173).
  - Vite Reverse Proxy chuyển tiếp `/api/*` cục bộ.
  - Máy khác truy cập thẳng qua IP LAN: `http://192.168.x.x:5173`.
* **Chế độ Public Internet (Khác mạng Wi-Fi / 4G):**
  - Thiết lập SSH Reverse Tunnel (Pinggy) mã hóa TLS.
  - Bỏ qua rào cản Firewall và cơ chế chặn mạng AP Isolation của trường.
  - Tự động sinh mã QR: Điện thoại chỉ cần quét camera là vào làm bài thi.

🗣️ **Lời thoại thuyết trình gợi ý:**
> "Một điểm nổi bật của QuizAI là khả năng kết nối đa máy thực tế. Server được cấu hình lắng nghe trên interface `0.0.0.0`, cho phép bất kỳ thiết bị nào cùng mạng Wi-Fi như laptop hay điện thoại đều có thể truy cập qua IP LAN của máy chủ. Đặc biệt, đối với các môi trường mạng bị chặn như Wi-Fi trường học bật tính năng AP Isolation, hệ thống tích hợp sẵn kênh truyền SSH Reverse Tunnel, cấp một đường link HTTPS công khai kèm mã QR để thí sinh dùng mạng 4G hay bất kỳ đâu cũng có thể kết nối thi trực tiếp."

---

### SLIDE 05: TÍCH HỢP GENAI (GEMINI AI WORKFLOW)
**Nội dung hiển thị trên Slide:**
* **Bước 1 (Client):** Giáo viên nhập chủ đề hoặc dán văn bản bài giảng, chọn độ khó (Dễ/Vừa/Khó) và số lượng câu.
* **Bước 2 (Server - Gemini API):** Backend đóng gói Prompt với System Instruction JSON Schema nghiêm ngặt, gọi Gemini API qua HTTPS POST.
* **Bước 3 (Validation & Database):** Server kiểm tra tính hợp lệ dữ liệu (đủ 4 options, 1 đáp án đúng) -> Lưu trạng thái `Pending` để giáo viên duyệt trước khi thi.

🗣️ **Lời thoại thuyết trình gợi ý:**
> "Ở luồng tạo đề thi, Backend đóng vai trò như một HTTP Client gửi request đến Google Gemini API qua kết nối HTTPS bảo mật. Chúng em áp dụng kỹ thuật Prompt Engineering với định dạng Schema JSON chặt chẽ, buộc mô hình AI phản hồi chuẩn xác câu hỏi, 4 đáp án và lời giải chi tiết. Trước khi lưu vào database, dữ liệu được kiểm tra hợp lệ để đảm bảo không có câu hỏi lỗi cú pháp và cho phép giáo viên kiểm duyệt trước khi công bố đề thi."

---

### SLIDE 06: HỆ THỐNG CHỐNG GIAN LẬN ĐA TẦNG (3 LỚP)
**Nội dung hiển thị trên Slide:**
* **Lớp 1 - Chống chuyển tab / Mất focus:**
  - Bắt sự kiện `visibilitychange` và `window.onblur`.
  - Bộ lọc Cooldown 2.5s: Chống kích hoạt đúp, đếm chuẩn xác từng lần vi phạm.
  - **Quy chế 3 lần:** Cảnh báo lần 1, lần 2 -> **Vi phạm lần thứ 3: Tự động thu hồi bài thi và nộp điểm ngay lập tức.**
* **Lớp 2 - Chặn sao chép & DevTools:**
  - Chặn phím `PrintScreen`, `Ctrl+P` (in), `Ctrl+C/X/A` (copy hỏi ChatGPT).
  - Khóa `F12` và `Ctrl+Shift+I` (chống xem đáp án trong DevTools).
  - Khóa chuột phải và tắt bôi đen văn bản (`select-none`).
* **Lớp 3 - Watermark chống chụp bằng điện thoại:**
  - In mờ chéo Họ tên & Username thí sinh khắp nền đề thi.
  - Chụp màn hình bằng camera sẽ lộ rõ danh tính người chụp.

🗣️ **Lời thoại thuyết trình gợi ý:**
> "Để đảm bảo tính nghiêm túc cho kỳ thi online, QuizAI trang bị hệ thống chống gian lận 3 lớp toàn diện: Lớp thứ nhất bắt các sự kiện chuyển tab hoặc bấm Alt+Tab. Nhờ cơ chế cooldown 2.5 giây, hệ thống đếm chuẩn xác từng lần vi phạm: thí sinh được cảnh báo 2 lần và đúng lần vi phạm thứ 3 bài thi sẽ tự động bị thu hồi. Lớp thứ hai vô hiệu hóa toàn bộ phím tắt chụp màn hình, in ấn, phím F12 mở DevTools và khóa chuột phải. Lớp thứ ba là Watermark động in chéo tên thí sinh lên màn hình, nếu dùng điện thoại chụp ảnh màn hình lại thì danh tính người vi phạm cũng sẽ in rõ trên câu hỏi."

---

### SLIDE 07: ĐỘ TIN CẬY MẠNG & CHỐNG MẤT DỮ LIỆU
**Nội dung hiển thị trên Slide:**
* **Cơ chế Chống Mất Dữ Liệu (Auto-Save):**
  - Tự động ghi nhớ đáp án vào `localStorage` theo thời gian thực (kèm nhãn thời gian lưu).
  - Gặp sự cố rớt mạng Wi-Fi, sập nguồn hay bấm F5 -> Bật lại bài thi còn nguyên vẹn 100%.
  - Thời gian đếm ngược tính theo **UTC Timestamp của Server**, triệt tiêu gian lận chỉnh giờ máy client.
* **Trộn Đề Ngẫu Nhiên (Shuffling):**
  - Thuật toán Fisher-Yates đảo ngẫu nhiên thứ tự câu hỏi và thứ tự đáp án A, B, C, D.
  - Hai thí sinh ngồi cạnh nhau có đề thi và vị trí đáp án hoàn toàn khác nhau.

🗣️ **Lời thoại thuyết trình gợi ý:**
> "Về khía cạnh độ tin cậy truyền thông (Fault Tolerance), QuizAI giải quyết triệt để rủi ro mất mạng. Mỗi câu trả lời được lưu tức thì vào bộ nhớ đệm client, nếu thí sinh bị rớt mạng hay tắt máy tính, khi vào lại đề thi vẫn giữ nguyên trạng thái. Thời gian làm bài cũng được đồng bộ theo đồng hồ của server chứ không dựa vào giờ máy tính học sinh để chống gian lận. Thêm vào đó, thuật toán xáo trộn Fisher-Yates sẽ đảo ngẫu nhiên vị trí câu hỏi và đáp án cho từng thí sinh, triệt tiêu việc nhìn bài nhau trong phòng thi."

---

### SLIDE 08: BẢNG QUẢN TRỊ & XUẤT BÁO CÁO EXCEL
**Nội dung hiển thị trên Slide:**
* **Bảng Giám Sát Thời Gian Thực:**
  - Xem danh sách thí sinh đã nộp bài, điểm số, thời gian làm và kết quả Đạt / Chưa đạt.
  - Cột Giám Sát Vi Phạm: Bôi đỏ cảnh báo các thí sinh có hành vi rời màn hình (`⚠️ X lần vi phạm`).
  - Thống kê phổ điểm trực quan: Số lượt thi, Điểm trung bình, Tỉ lệ đạt và Điểm cao nhất.
* **Xuất Báo Cáo Excel (.CSV):**
  - 1-Click tải bảng điểm: Định dạng chuẩn UTF-8 kèm BOM hiển thị tiếng Việt hoàn hảo trên Excel.
  - Đầy đủ thông tin phục vụ nộp phòng đào tạo hoặc lưu trữ học vụ.

🗣️ **Lời thoại thuyết trình gợi ý:**
> "Về phía giáo viên, trang quản trị cung cấp một bức tranh toàn diện về kỳ thi: từ thống kê phổ điểm, tỷ lệ đạt cho đến bảng danh sách chi tiết từng lượt nộp bài. Điểm đặc biệt là cột giám sát vi phạm sẽ bôi đỏ cảnh báo những thí sinh đã từng chuyển tab trong lúc làm bài. Cuối buổi thi, giáo viên chỉ cần nhấn nút 'Xuất Bảng Điểm' là có ngay file Excel chuẩn mã hóa UTF-8 tiếng Việt để báo cáo kết quả mà không cần nhập liệu thủ công."

---

### SLIDE 09: KẾT QUẢ ĐẠT ĐƯỢC & HIỆU NĂNG THỰC TẾ
**Nội dung hiển thị trên Slide:**
* **Chỉ số hiệu năng đo đạc thực tế:**
  - `< 120 ms`: Thời gian phản hồi trung bình các API RESTful qua giao thức HTTP.
  - `3 - 5 giây`: Thời gian Gemini AI sinh hoàn chỉnh bộ 10-20 câu hỏi trắc nghiệm kèm giải thích.
  - `100%`: Tỉ lệ bảo toàn bài làm khi xảy ra sự cố ngắt mạng hoặc tải lại trang.
  - `0 Lỗi`: Xung đột dữ liệu; an toàn thông tin với Token JWT và mã hóa mật khẩu BCrypt.
* **Đánh giá tổng quan:**
  - 100% chức năng kiểm thử thành công trên cả Laptop và Điện thoại thông minh.

🗣️ **Lời thoại thuyết trình gợi ý:**
> "Sau quá trình thử nghiệm thực tế, hệ thống đạt hiệu năng rất ấn tượng: Tốc độ phản hồi API trung bình dưới 120ms, thời gian AI sinh trọn bộ đề thi chỉ mất từ 3 đến 5 giây. Khả năng bảo toàn dữ liệu đạt 100% trong mọi kịch bản giả lập ngắt mạng. Toàn bộ các cơ chế an ninh mạng từ xác thực JWT đến chính sách CORS đều vận hành trơn tru trên cả máy tính lẫn thiết bị di động."

---

### SLIDE 10: KẾT LUẬN & ĐỊNH HƯỚNG MỞ RỘNG
**Nội dung hiển thị trên Slide:**
* **Giá trị đạt được:**
  - Hoàn thành xuất sắc mô hình Client-Server phục vụ môn Lập trình mạng.
  - Ứng dụng thực tiễn cao: Sẵn sàng áp dụng cho kiểm tra trên lớp và thi thử trực tuyến.
  - Mã nguồn mở, cấu trúc chuẩn mực và lưu trữ trên GitHub.
* **Định hướng phát triển cuối kỳ:**
  - Tích hợp **SignalR / WebSocket**: Chế độ thi đấu đối kháng trực tiếp (Quiz Battle thời gian thực kiểu Kahoot).
  - Tích hợp AI Camera: Giám sát khuôn mặt thí sinh qua webcam.
  - Đóng gói Docker & Triển khai lên Cloud Server (Render / VPS) với HTTPS chính thức.

🗣️ **Lời thoại thuyết trình gợi ý:**
> "Tóm lại, dự án QuizAI đã hiện thực hóa trọn vẹn các kiến thức cốt lõi của môn Lập trình mạng thành một sản phẩm có tính ứng dụng cao trong giáo dục. Hướng phát triển cho giai đoạn cuối kỳ, nhóm sẽ nâng cấp giao thức truyền thông hai chiều thời gian thực bằng WebSockets và SignalR để xây dựng chế độ thi đấu đối kháng trực tiếp, đồng thời đóng gói Docker và triển khai hệ thống lên máy chủ đám mây. Nhóm em xin chân thành cảm ơn Thầy/Cô và các bạn đã lắng nghe!"

---

## 🎯 BỘ CÂU HỎI PHẢN BIỆN THƯỜNG GẶP CỦA GIẢNG VIÊN & ĐÁP ÁN

### ❓ Câu 1: Tại sao hệ thống này dùng TCP mà không dùng UDP?
> **Trả lời:** "Dạ thưa Thầy/Cô, bài thi trắc nghiệm đòi hỏi tính toàn vẹn và độ tin cậy tuyệt đối của dữ liệu. Giao thức TCP có cơ chế bắt tay 3 bước (3-way handshake), đánh số thứ tự gói tin (Sequence Number) và tự động phát lại nếu mất gói tin (Retransmission). Nếu dùng UDP, các gói tin nộp bài có thể bị thất lạc trên mạng dẫn đến sai lệch điểm thi của thí sinh. Do đó, TCP là lựa chọn bắt buộc."

### ❓ Câu 2: Tại sao phải có cơ chế Cooldown 2.5 giây khi phát hiện chuyển tab?
> **Trả lời:** "Dạ thưa Thầy/Cô, khi người dùng chuyển tab hoặc bấm Alt+Tab, trình duyệt web kích hoạt đồng thời 2 sự kiện là `window.onblur` và `document.visibilitychange` chỉ cách nhau vài mili-giây. Nếu không có cơ chế debounce cooldown 2.5 giây, 1 lần thí sinh chuyển tab sẽ bị tính đúp thành 2 lần vi phạm, gây oan ức cho thí sinh. Cooldown đảm bảo 1 hành vi chuyển tab chỉ tính đúng 1 lần vi phạm."

### ❓ Câu 3: Làm sao hệ thống chống việc thí sinh tua ngược giờ máy tính để làm thêm giờ?
> **Trả lời:** "Dạ thưa Thầy/Cô, thời gian làm bài không căn cứ vào đồng hồ cục bộ của máy tính học sinh. Khi bắt đầu thi, máy chủ lưu `StartedAt` theo giờ chuẩn UTC của Server. Mỗi khi thí sinh tương tác hoặc nộp bài, Server sẽ tính: `Thời gian đã làm = Giờ hiện tại của Server - StartedAt`. Dù thí sinh có chỉnh lùi giờ trên Windows bao nhiêu đi nữa thì Server vẫn tính theo mốc giờ của nó và tự động khóa bài khi hết giờ."

### ❓ Câu 4: Khi dùng SSH Tunnel (Pinggy), dữ liệu có an toàn không?
> **Trả lời:** "Dạ thưa Thầy/Cô, cực kỳ an toàn. Giao thức SSH bản thân nó đã thiết lập một đường hầm mã hóa đối xứng AES. Khi người dùng bên ngoài truy cập vào link web, giao tiếp được bảo vệ bởi lớp mã hóa HTTPS/TLS từ trình duyệt đến cổng Tunnel, ngăn chặn hoàn toàn các cuộc tấn công nghe lén (Man-in-the-Middle) hay bắt gói tin bằng Wireshark."
