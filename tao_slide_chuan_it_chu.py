import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

def create_presentation(output_path):
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # Modern Tech Dark Palette
    C_BG = RGBColor(11, 15, 25)
    C_CARD = RGBColor(19, 27, 46)
    C_BORDER = RGBColor(40, 53, 84)
    C_PRIMARY = RGBColor(99, 102, 241)    # Indigo
    C_CYAN = RGBColor(6, 182, 212)        # Cyan
    C_GREEN = RGBColor(16, 185, 129)      # Emerald
    C_AMBER = RGBColor(245, 158, 11)      # Amber
    C_RED = RGBColor(239, 68, 68)         # Red
    C_WHITE = RGBColor(255, 255, 255)
    C_TEXT = RGBColor(203, 213, 225)      # Slate 300
    C_MUTED = RGBColor(148, 163, 184)     # Slate 400

    FONT_TITLE = "Segoe UI"
    FONT_BODY = "Segoe UI"

    def set_background(slide):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
        bg.fill.solid()
        bg.fill.fore_color.rgb = C_BG
        bg.line.fill.background()

        top_line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, Inches(0.08))
        top_line.fill.solid()
        top_line.fill.fore_color.rgb = C_PRIMARY
        top_line.line.fill.background()

    def add_header(slide, tag, title, subtitle=""):
        set_background(slide)
        txBox = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.733), Inches(1.2))
        tf = txBox.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0

        p = tf.paragraphs[0]
        p.text = tag.upper()
        p.font.name = FONT_TITLE
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = C_CYAN
        p.space_after = Pt(2)

        p = tf.add_paragraph()
        p.text = title
        p.font.name = FONT_TITLE
        p.font.size = Pt(23)
        p.font.bold = True
        p.font.color.rgb = C_WHITE
        p.space_after = Pt(2)

        if subtitle:
            p = tf.add_paragraph()
            p.text = subtitle
            p.font.name = FONT_BODY
            p.font.size = Pt(13)
            p.font.color.rgb = C_MUTED

    def add_card(slide, left, top, width, height, title="", title_color=C_WHITE, bg_color=C_CARD, border_color=C_BORDER):
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        card.fill.solid()
        card.fill.fore_color.rgb = bg_color
        card.line.color.rgb = border_color
        card.line.width = Pt(1)

        if title:
            txBox = slide.shapes.add_textbox(left + Inches(0.25), top + Inches(0.2), width - Inches(0.5), Inches(0.4))
            tf = txBox.text_frame
            tf.word_wrap = True
            tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
            p = tf.paragraphs[0]
            p.text = title
            p.font.name = FONT_TITLE
            p.font.size = Pt(15)
            p.font.bold = True
            p.font.color.rgb = title_color
        return card

    def add_bullets(slide, left, top, width, height, items):
        txBox = slide.shapes.add_textbox(left, top, width, height)
        tf = txBox.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0

        for i, item in enumerate(items):
            p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
            p.text = item
            p.font.name = FONT_BODY
            p.font.size = Pt(13)
            p.font.color.rgb = C_TEXT
            p.space_after = Pt(8)

    # ==========================================
    # SLIDE 1: TÊN ĐỀ TÀI & TRANG BÌA
    # ==========================================
    s1 = prs.slides.add_slide(blank_layout)
    set_background(s1)
    box = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.5), Inches(1.1), Inches(10.333), Inches(5.3))
    box.fill.solid()
    box.fill.fore_color.rgb = C_CARD
    box.line.color.rgb = C_BORDER
    box.line.width = Pt(1.5)

    tx = s1.shapes.add_textbox(Inches(1.8), Inches(1.5), Inches(9.733), Inches(4.5))
    tf = tx.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0

    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.CENTER
    p.text = "BÁO CÁO ĐỒ ÁN • MÔN LẬP TRÌNH MẠNG"
    p.font.name = FONT_TITLE
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = C_CYAN
    p.space_after = Pt(14)

    p = tf.add_paragraph()
    p.alignment = PP_ALIGN.CENTER
    p.text = "QuizAI – Hệ Thống Trắc Nghiệm Online\nTích Hợp Trí Tuệ Nhân Tạo & Giám Sát Thi Đa Máy"
    p.font.name = FONT_TITLE
    p.font.size = Pt(28)
    p.font.bold = True
    p.font.color.rgb = C_WHITE
    p.space_after = Pt(16)

    p = tf.add_paragraph()
    p.alignment = PP_ALIGN.CENTER
    p.text = "Client-Server • RESTful API • TCP/IP • Xác Thực JWT • Chống Gian Lận 3 Lớp"
    p.font.name = FONT_BODY
    p.font.size = Pt(14)
    p.font.color.rgb = C_TEXT
    p.space_after = Pt(28)

    p = tf.add_paragraph()
    p.alignment = PP_ALIGN.CENTER
    p.text = "Giảng viên hướng dẫn: Bộ môn Lập Trình Mạng    |    Sinh viên: Nhóm thực hiện QuizAI"
    p.font.name = FONT_BODY
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = C_MUTED

    # ==========================================
    # SLIDE 2: LÝ DO CHỌN ĐỀ TÀI & MỤC TIÊU
    # ==========================================
    s2 = prs.slides.add_slide(blank_layout)
    add_header(s2, "01. Tổng Quan", "Lý Do Chọn Đề Tài & Mục Tiêu Dự Án", "Giải quyết bài toán tạo đề thi, chống gian lận và tối ưu hạ tầng mạng")

    add_card(s2, Inches(0.8), Inches(1.8), Inches(5.6), Inches(5.1), "Thực Trạng & Vấn Đề", C_AMBER)
    add_bullets(s2, Inches(1.1), Inches(2.5), Inches(5.0), Inches(4.0), [
        "• Soạn đề thủ công: Tốn nhiều thời gian, khó đa dạng hóa câu hỏi.",
        "• Gian lận trực tuyến: Chuyển tab tra cứu Google, nhờ ChatGPT giải hộ.",
        "• Nhìn bài thi: Thí sinh ngồi cạnh nhau có cùng đề và vị trí đáp án.",
        "• Rủi ro đường truyền: Rớt mạng Wi-Fi làm mất dữ liệu bài thi đang làm dở."
    ])

    add_card(s2, Inches(6.9), Inches(1.8), Inches(5.6), Inches(5.1), "Mục Tiêu Giải Quyết", C_GREEN)
    add_bullets(s2, Inches(7.2), Inches(2.5), Inches(5.0), Inches(4.0), [
        "• AI Gemini: Tự động sinh bộ đề 10-30 câu chuẩn xác trong vài giây.",
        "• Chống gian lận 3 lớp: Bắt chuyển tab (3 lần nộp bài), chặn PrintScreen/DevTools.",
        "• Trộn đề ngẫu nhiên: Đảo vị trí câu hỏi & 4 đáp án A, B, C, D cho từng máy.",
        "• Auto-Save Real-time: Bảo toàn dữ liệu 100% khi rớt mạng hoặc sập nguồn."
    ])

    # ==========================================
    # SLIDE 3: THÀNH VIÊN & PHÂN CÔNG CÔNG VIỆC
    # ==========================================
    s3 = prs.slides.add_slide(blank_layout)
    add_header(s3, "02. Tổ Chức", "Thành Viên & Phân Công Công Việc", "Phân chia rõ ràng trách nhiệm theo từng tầng kiến trúc hệ thống")

    add_card(s3, Inches(0.8), Inches(1.8), Inches(3.6), Inches(5.1), "Backend & Network", C_PRIMARY)
    add_bullets(s3, Inches(1.05), Inches(2.5), Inches(3.1), Inches(4.0), [
        "• Xây dựng ASP.NET Core 9 API.",
        "• Cấu hình TCP/IP, CORS & Port 0.0.0.0.",
        "• Tích hợp Gemini AI & JWT Auth.",
        "• Thiết kế Database SQL Server."
    ])

    add_card(s3, Inches(4.85), Inches(1.8), Inches(3.6), Inches(5.1), "Frontend & UI/UX", C_CYAN)
    add_bullets(s3, Inches(5.1), Inches(2.5), Inches(3.1), Inches(4.0), [
        "• Phát triển giao diện React 19 SPA.",
        "• Thiết kế Dark Mode với TailwindCSS.",
        "• Xử lý Auto-Save & Trộn đề ngẫu nhiên.",
        "• Bảng thống kê & Xuất Excel (.xlsx)."
    ])

    add_card(s3, Inches(8.9), Inches(1.8), Inches(3.6), Inches(5.1), "Security & Testing", C_GREEN)
    add_bullets(s3, Inches(9.15), Inches(2.5), Inches(3.1), Inches(4.0), [
        "• Lập trình module Chống gian lận 3 lớp.",
        "• Thiết lập SSH Tunnel (Pinggy / QR).",
        "• Kiểm thử chịu lỗi mạng & Stress test.",
        "• Đóng gói tài liệu & Slide thuyết trình."
    ])

    # ==========================================
    # SLIDE 4: TIMELINE – KẾ HOẠCH & TIẾN ĐỘ
    # ==========================================
    s4 = prs.slides.add_slide(blank_layout)
    add_header(s4, "03. Tiến Độ", "Timeline – Kế Hoạch & Tiến Độ Thực Hiện", "Quy trình phát triển phần mềm theo từng giai đoạn chuẩn chỉ")

    add_card(s4, Inches(0.8), Inches(1.8), Inches(2.7), Inches(5.1), "Giai Đoạn 1: Thiết Kế", C_PRIMARY)
    add_bullets(s4, Inches(1.0), Inches(2.5), Inches(2.3), Inches(4.0), [
        "• Phân tích yêu cầu.",
        "• Thiết kế sơ đồ mạng.",
        "• Thiết kế CSDL (ERD).",
        "• Chuẩn hóa RESTful API."
    ])

    add_card(s4, Inches(3.75), Inches(1.8), Inches(2.7), Inches(5.1), "Giai Đoạn 2: Lập Trình", C_CYAN)
    add_bullets(s4, Inches(3.95), Inches(2.5), Inches(2.3), Inches(4.0), [
        "• Viết Backend Web API.",
        "• Viết Frontend React SPA.",
        "• Tích hợp Gemini GenAI.",
        "• Mã hóa mật khẩu BCrypt."
    ])

    add_card(s4, Inches(6.7), Inches(1.8), Inches(2.7), Inches(5.1), "Giai Đoạn 3: Nâng Cấp", C_AMBER)
    add_bullets(s4, Inches(6.9), Inches(2.5), Inches(2.3), Inches(4.0), [
        "• Mạng LAN & Tunneling.",
        "• Anti-Cheat 3 lớp bảo vệ.",
        "• Auto-Save & Trộn đề.",
        "• Xuất báo cáo Excel .xlsx."
    ])

    add_card(s4, Inches(9.65), Inches(1.8), Inches(2.7), Inches(5.1), "Giai Đoạn 4: Hoàn Thiện", C_GREEN)
    add_bullets(s4, Inches(9.85), Inches(2.5), Inches(2.3), Inches(4.0), [
        "• Kiểm thử tải đa máy.",
        "• Viết tài liệu đồ án.",
        "• Đồng bộ mã nguồn GitHub.",
        "• Sẵn sàng báo cáo nghiệm thu."
    ])

    # ==========================================
    # SLIDE 5: CHỨC NĂNG HỆ THỐNG
    # ==========================================
    s5 = prs.slides.add_slide(blank_layout)
    add_header(s5, "04. Chức Năng", "Các Chức Năng Cốt Lõi Của Hệ Thống", "Đầy đủ nghiệp vụ cho Học sinh, Giáo viên và Quản trị viên")

    add_card(s5, Inches(0.8), Inches(1.8), Inches(5.6), Inches(5.1), "Phân Hệ Học Sinh (Thí Sinh)", C_CYAN)
    add_bullets(s5, Inches(1.1), Inches(2.5), Inches(5.0), Inches(4.0), [
        "• Đăng ký / Đăng nhập: Tài khoản bảo mật với JWT.",
        "• Làm bài trực tuyến: Đồng hồ đếm ngược đồng bộ Server UTC.",
        "• Trộn đề: Câu hỏi & 4 đáp án A, B, C, D đảo ngẫu nhiên.",
        "• Chống mất dữ liệu: Tự động lưu đáp án (Auto-Save) real-time.",
        "• Xem kết quả: Chấm điểm tức thì kèm giải thích chi tiết đáp án."
    ])

    add_card(s5, Inches(6.9), Inches(1.8), Inches(5.6), Inches(5.1), "Phân Hệ Quản Trị & Giáo Viên", C_PRIMARY)
    add_bullets(s5, Inches(7.2), Inches(2.5), Inches(5.0), Inches(4.0), [
        "• AI Tạo đề: Nhập văn bản/chủ đề -> Gemini AI sinh trắc nghiệm.",
        "• Kiểm duyệt: Xem trước, sửa đổi hoặc xóa câu hỏi AI.",
        "• Quản lý đề: Tạo, xuất bản, xóa đề thi (Cascade Delete).",
        "• Giám sát vi phạm: Bôi đỏ cảnh báo thí sinh rời màn hình.",
        "• Xuất Excel (.xlsx): 1-Click tải bảng điểm chuẩn Microsoft Excel."
    ])

    # ==========================================
    # SLIDE 6: CÔNG NGHỆ & KỸ THUẬT SỬ DỤNG
    # ==========================================
    s6 = prs.slides.add_slide(blank_layout)
    add_header(s6, "05. Công Nghệ", "Ngăn Xếp Công Nghệ (Technology Stack)", "Sử dụng các công nghệ hiện đại, ổn định và tối ưu hiệu năng mạng")

    add_card(s6, Inches(0.8), Inches(1.8), Inches(3.6), Inches(5.1), "Frontend Stack", C_CYAN)
    add_bullets(s6, Inches(1.05), Inches(2.5), Inches(3.1), Inches(4.0), [
        "• React 19: Xây dựng SPA mượt mà.",
        "• Vite 8: Build siêu tốc, hỗ trợ Proxy.",
        "• TailwindCSS: Giao diện Dark Mode.",
        "• Axios: Tự đính kèm JWT Bearer.",
        "• SheetJS (xlsx): Xuất bảng tính chuẩn."
    ])

    add_card(s6, Inches(4.85), Inches(1.8), Inches(3.6), Inches(5.1), "Backend Stack", C_PRIMARY)
    add_bullets(s6, Inches(5.1), Inches(2.5), Inches(3.1), Inches(4.0), [
        "• ASP.NET Core 9: Web API đa luồng.",
        "• Kestrel Server: Độ trễ phản hồi <120ms.",
        "• JWT: Xác thực phi trạng thái (Stateless).",
        "• BCrypt.Net: Băm mật khẩu có Salt.",
        "• Google Gemini API: GenAI tạo câu hỏi."
    ])

    add_card(s6, Inches(8.9), Inches(1.8), Inches(3.6), Inches(5.1), "Database & Network", C_GREEN)
    add_bullets(s6, Inches(9.15), Inches(2.5), Inches(3.1), Inches(4.0), [
        "• SQL Server LocalDB: CSDL quan hệ.",
        "• EF Core 9: Migration & Code-First.",
        "• IP Binding 0.0.0.0: Mở mạng LAN.",
        "• SSH Reverse Tunnel: Pinggy HTTPS/QR.",
        "• UTF-8 BOM: Chuẩn hóa font tiếng Việt."
    ])

    # ==========================================
    # SLIDE 7: KIẾN TRÚC HỆ THỐNG TỔNG THỂ
    # ==========================================
    s7 = prs.slides.add_slide(blank_layout)
    add_header(s7, "06. Kiến Trúc", "Kiến Trúc Hệ Thống Tổng Thể (3-Tier)", "Mô hình Client - Server 3 tầng phân tách rõ ràng trách nhiệm")

    add_card(s7, Inches(0.8), Inches(1.8), Inches(3.6), Inches(5.1), "Tầng Client (Presentation)", C_CYAN)
    add_bullets(s7, Inches(1.05), Inches(2.5), Inches(3.1), Inches(4.0), [
        "• Single Page Application (SPA).",
        "• Gửi yêu cầu qua giao thức HTTP/HTTPS.",
        "• Lưu tạm đáp án vào LocalStorage.",
        "• Xử lý xáo trộn đề trên SessionStorage.",
        "• Bắt sự kiện gian lận chuyển tab/chụp ảnh."
    ])

    add_card(s7, Inches(4.85), Inches(1.8), Inches(3.6), Inches(5.1), "Tầng Server (Business Logic)", C_PRIMARY)
    add_bullets(s7, Inches(5.1), Inches(2.5), Inches(3.1), Inches(4.0), [
        "• Tiếp nhận & điều phối RESTful API.",
        "• Kiểm tra quyền hạn bằng Middleware JWT.",
        "• Tính toán điểm số & đếm vi phạm.",
        "• Đồng bộ giờ làm bài theo UTC Server.",
        "• Kết nối Google AI Studio qua HTTPS."
    ])

    add_card(s7, Inches(8.9), Inches(1.8), Inches(3.6), Inches(5.1), "Tầng Database (Data Access)", C_GREEN)
    add_bullets(s7, Inches(9.15), Inches(2.5), Inches(3.1), Inches(4.0), [
        "• Lưu trữ bền vững dữ liệu ACID.",
        "• Bảng Users: Tài khoản & Hash BCrypt.",
        "• Bảng Exams & Questions: Ngân hàng đề.",
        "• Bảng Submissions: Điểm & Số lần vi phạm.",
        "• Bảng Details: Chi tiết từng câu trả lời."
    ])

    # ==========================================
    # SLIDE 8: CƠ CHẾ CHẠY ĐA MÁY (LAN / INTERNET)
    # ==========================================
    s8 = prs.slides.add_slide(blank_layout)
    add_header(s8, "07. Mạng Đa Máy", "Cơ Chế Chạy Đa Máy: LAN & Public Internet", "Hỗ trợ kết nối đồng thời từ máy tính, laptop và điện thoại thông minh")

    add_card(s8, Inches(0.8), Inches(1.8), Inches(5.6), Inches(5.1), "1. Mạng LAN (Phòng Lab / Wi-Fi)", C_CYAN)
    add_bullets(s8, Inches(1.1), Inches(2.5), Inches(5.0), Inches(4.0), [
        "• Lắng nghe 0.0.0.0: Bind cổng 5000 & 5173 trên mọi card mạng.",
        "• Vite Reverse Proxy: Chuyển tiếp /api/* về Backend Kestrel.",
        "• Truy cập tức thì: Máy con gõ http://192.168.x.x:5173.",
        "• Khởi động 1-Click: File chay_he_thong.bat tự tìm IP nội bộ."
    ])

    add_card(s8, Inches(6.9), Inches(1.8), Inches(5.6), Inches(5.1), "2. Public Internet (Khác mạng / 4G)", C_PRIMARY)
    add_bullets(s8, Inches(7.2), Inches(2.5), Inches(5.0), Inches(4.0), [
        "• SSH Reverse Tunnel: Pinggy mã hóa dữ liệu qua cổng 443.",
        "• Bỏ qua Firewall: Vượt qua bộ lọc AP Isolation của trường học.",
        "• Mã QR tiện lợi: Điện thoại chỉ cần bật camera quét mã để thi.",
        "• Bảo mật TLS: Mã hóa End-to-End an toàn tuyệt đối."
    ])

    # ==========================================
    # SLIDE 9: GIAO THỨC MẠNG & MÔ HÌNH TCP/IP
    # ==========================================
    s9 = prs.slides.add_slide(blank_layout)
    add_header(s9, "08. Giao Thức Mạng", "Giao Thức Mạng & Mô Hình TCP/IP", "Cơ sở lý thuyết mạng truyền thông áp dụng trong hệ thống thi cử")

    add_card(s9, Inches(0.8), Inches(1.8), Inches(5.6), Inches(5.1), "Tại Sao Chọn TCP Thay Vì UDP?", C_AMBER)
    add_bullets(s9, Inches(1.1), Inches(2.5), Inches(5.0), Inches(4.0), [
        "• Hướng kết nối (Connection-oriented): Đảm bảo thông suốt.",
        "• Tin cậy tuyệt đối: Có cờ báo nhận ACK và Sequence Number.",
        "• Chống mất gói tin: Tự động phát lại (Retransmission) nếu lag mạng.",
        "• Không dùng UDP: Tránh thất lạc gói tin nộp bài làm sai lệch điểm."
    ])

    add_card(s9, Inches(6.9), Inches(1.8), Inches(5.6), Inches(5.1), "Cơ Chế Bắt Tay 3 Bước (3-Way Handshake)", C_GREEN)
    add_bullets(s9, Inches(7.2), Inches(2.5), Inches(5.0), Inches(4.0), [
        "• Bước 1 (SYN): Client gửi yêu cầu kết nối kèm số Seq khởi tạo.",
        "• Bước 2 (SYN-ACK): Server xác nhận và gửi số Seq của mình.",
        "• Bước 3 (ACK): Client xác nhận hoàn tất -> Phiên TCP mở.",
        "• Ứng dụng: Mọi cuộc gọi HTTP/HTTPS đều thiết lập qua TCP."
    ])

    # ==========================================
    # SLIDE 10: GIAO THỨC WEB & RESTFUL API
    # ==========================================
    s10 = prs.slides.add_slide(blank_layout)
    add_header(s10, "09. Giao Thức Web", "Giao Thức Web & Kiến Trúc RESTful API", "Chuẩn hóa tài nguyên mạng bằng các phương thức HTTP tiêu chuẩn")

    add_card(s10, Inches(0.8), Inches(1.8), Inches(5.6), Inches(5.1), "Các Phương Thức HTTP Chuẩn", C_CYAN)
    add_bullets(s10, Inches(1.1), Inches(2.5), Inches(5.0), Inches(4.0), [
        "• GET: Lấy tài nguyên (Đọc danh sách đề, xem bảng điểm).",
        "• POST: Tạo tài nguyên mới (Đăng nhập, Bắt đầu thi, Nộp bài).",
        "• PATCH: Cập nhật một phần (Duyệt câu hỏi, cập nhật vi phạm).",
        "• DELETE: Xóa tài nguyên (Xóa vĩnh viễn đề thi kèm dữ liệu liên quan)."
    ])

    add_card(s10, Inches(6.9), Inches(1.8), Inches(5.6), Inches(5.1), "Đặc Trưng Kiến Trúc REST", C_PRIMARY)
    add_bullets(s10, Inches(7.2), Inches(2.5), Inches(5.0), Inches(4.0), [
        "• Stateless (Phi trạng thái): Mỗi request chứa đủ thông tin xác thực.",
        "• Định dạng JSON: Gọn nhẹ, tối ưu băng thông đường truyền mạng.",
        "• Mã trạng thái HTTP chuẩn: 200 OK, 201 Created, 401 Unauthorized, 403 Forbidden.",
        "• Swagger UI tích hợp: Tài liệu hóa trực quan tại /swagger."
    ])

    # ==========================================
    # SLIDE 11: HTTPS & CƠ CHẾ BẢO MẬT TLS/SSL
    # ==========================================
    s11 = prs.slides.add_slide(blank_layout)
    add_header(s11, "10. Bảo Mật Web", "Giao Thức HTTPS & Cơ Chế Hoạt Động TLS/SSL", "Bảo vệ dữ liệu thi cử chống nghe lén và giả mạo trên đường truyền")

    add_card(s11, Inches(0.8), Inches(1.8), Inches(5.6), Inches(5.1), "Quy Trình Bắt Tay TLS (TLS Handshake)", C_PRIMARY)
    add_bullets(s11, Inches(1.1), Inches(2.5), Inches(5.0), Inches(4.0), [
        "• ClientHello: Client gửi phiên bản TLS và danh sách mã hóa hỗ trợ.",
        "• ServerHello & Certificate: Server gửi chứng chỉ số chứa Public Key.",
        "• Key Exchange: Trao đổi khóa bí mật phiên (Session Key) an toàn.",
        "• Mã hóa đối xứng: Toàn bộ gói tin sau đó được mã hóa bằng AES-256."
    ])

    add_card(s11, Inches(6.9), Inches(1.8), Inches(5.6), Inches(5.1), "Tầm Quan Trọng Trong QuizAI", C_GREEN)
    add_bullets(s11, Inches(7.2), Inches(2.5), Inches(5.0), Inches(4.0), [
        "• Chống bắt gói tin (Wireshark): Kẻ nghe lén chỉ thấy dữ liệu mã hóa.",
        "• Bảo vệ Token & Mật khẩu: Không bị lộ mã JWT trên đường truyền Wi-Fi.",
        "• Bảo vệ Gemini API Key: Kênh HTTPS ngăn chặn rò rỉ khóa bí mật.",
        "• Toàn vẹn dữ liệu: Đảm bảo đáp án của thí sinh không bị sửa đổi trên mạng."
    ])

    # ==========================================
    # SLIDE 12: XÁC THỰC JWT & CHÍNH SÁCH CORS
    # ==========================================
    s12 = prs.slides.add_slide(blank_layout)
    add_header(s12, "11. An Ninh Mạng", "Cơ Chế Xác Thực JWT & Chính Sách CORS", "Xác thực người dùng phi trạng thái và kiểm soát truy cập nguồn chéo")

    add_card(s12, Inches(0.8), Inches(1.8), Inches(5.6), Inches(5.1), "Xác Thực JWT (JSON Web Token)", C_CYAN)
    add_bullets(s12, Inches(1.1), Inches(2.5), Inches(5.0), Inches(4.0), [
        "• Cấu trúc 3 phần: Header . Payload . Signature (HMAC-SHA256).",
        "• Stateless Auth: Server không tốn RAM lưu Session hàng trăm học sinh.",
        "• Xác thực nhanh: Server dùng SecretKey kiểm tra tính hợp lệ chữ ký.",
        "• Axios Interceptor: Tự động đính kèm Bearer Token vào mọi request."
    ])

    add_card(s12, Inches(6.9), Inches(1.8), Inches(5.6), Inches(5.1), "Chính Sách Mạng CORS", C_AMBER)
    add_bullets(s12, Inches(7.2), Inches(2.5), Inches(5.0), Inches(4.0), [
        "• Same-Origin Policy: Trình duyệt mặc định chặn request khác domain/IP.",
        "• Cấu hình nới lỏng: policy.SetIsOriginAllowed(_ => true).",
        "• Chấp nhận mọi IP: Laptop, điện thoại hay IP LAN đều kết nối được.",
        "• Bảo mật an toàn: Vẫn duy trì kiểm soát nghiêm ngặt bằng JWT Token."
    ])

    # ==========================================
    # SLIDE 13: HỆ THỐNG CHỐNG GIAN LẬN ĐA TẦNG
    # ==========================================
    s13 = prs.slides.add_slide(blank_layout)
    add_header(s13, "12. Chống Gian Lận", "Hệ Thống Chống Gian Lận Đa Tầng (3 Lớp)", "Giám sát toàn diện hành vi thi cử, đảm bảo tính công bằng và minh bạch")

    add_card(s13, Inches(0.8), Inches(1.8), Inches(3.6), Inches(5.1), "Lớp 1: Chống Chuyển Tab", C_RED)
    add_bullets(s13, Inches(1.05), Inches(2.5), Inches(3.1), Inches(4.0), [
        "• Bắt visibilitychange & blur.",
        "• Cooldown 2.5s: Chống tính đúp.",
        "• Vi phạm lần 1 & 2: Cảnh báo đỏ.",
        "• Vi phạm lần 3: Thu hồi & nộp bài."
    ])

    add_card(s13, Inches(4.85), Inches(1.8), Inches(3.6), Inches(5.1), "Lớp 2: Chặn Sao Chép", C_AMBER)
    add_bullets(s13, Inches(5.1), Inches(2.5), Inches(3.1), Inches(4.0), [
        "• Chặn phím PrintScreen (chớp đen).",
        "• Khóa Ctrl+C/X/A, Ctrl+P (in).",
        "• Khóa F12 & DevTools soi đáp án.",
        "• Tắt chuột phải & chống bôi đen."
    ])

    add_card(s13, Inches(8.9), Inches(1.8), Inches(3.6), Inches(5.1), "Lớp 3: Watermark Camera", C_CYAN)
    add_bullets(s13, Inches(9.15), Inches(2.5), Inches(3.1), Inches(4.0), [
        "• In mờ chéo Họ tên & Username.",
        "• Phủ khắp nền màn hình thi.",
        "• Chụp điện thoại lộ rõ danh tính.",
        "• Ghi nhận số vi phạm về máy chủ."
    ])

    # ==========================================
    # SLIDE 14: LUỒNG DỮ LIỆU CHÍNH CỦA HỆ THỐNG
    # ==========================================
    s14 = prs.slides.add_slide(blank_layout)
    add_header(s14, "13. Luồng Dữ Liệu", "Luồng Dữ Liệu Chính Của Hệ Thống (Data Flow)", "Hai luồng xử lý cốt lõi: Xác thực tài khoản và Làm bài thi trực tuyến")

    add_card(s14, Inches(0.8), Inches(1.8), Inches(5.6), Inches(5.1), "Luồng 1: Đăng Nhập & Xác Thực", C_PRIMARY)
    add_bullets(s14, Inches(1.1), Inches(2.5), Inches(5.0), Inches(4.0), [
        "1. Client gửi POST /api/auth/login kèm thông tin đăng nhập.",
        "2. Server kiểm tra Username & so khớp mã băm mật khẩu BCrypt.",
        "3. Server tạo chuỗi JWT Token có chữ ký số -> Trả về Client.",
        "4. Client lưu Token vào LocalStorage và phân hướng theo Role."
    ])

    add_card(s14, Inches(6.9), Inches(1.8), Inches(5.6), Inches(5.1), "Luồng 2: Làm Bài Thi & Chấm Điểm", C_GREEN)
    add_bullets(s14, Inches(7.2), Inches(2.5), Inches(5.0), Inches(4.0), [
        "1. Bắt đầu: POST /api/submissions/start -> Nhận đề & Server Time.",
        "2. Làm bài: Trộn ngẫu nhiên câu hỏi & Auto-Save vào LocalStorage.",
        "3. Giám sát: Ghi nhận vi phạm chuyển tab (Tối đa 3 lần).",
        "4. Nộp bài: POST /api/submissions/submit -> Chấm điểm & hiện giải thích."
    ])

    # ==========================================
    # SLIDE 15: KẾT QUẢ ĐẠT ĐƯỢC & HIỆU NĂNG
    # ==========================================
    s15 = prs.slides.add_slide(blank_layout)
    add_header(s15, "14. Thực Nghiệm", "Kết Quả Đạt Được & Hiệu Năng Thực Tế", "Các số liệu thực nghiệm đo đạc trong quá trình kiểm thử hệ thống")

    # 4 Metric Cards
    m1 = add_card(s15, Inches(0.8), Inches(1.8), Inches(2.7), Inches(2.2), "", bg_color=C_CARD)
    tb = s15.shapes.add_textbox(Inches(0.9), Inches(2.0), Inches(2.5), Inches(1.8))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "< 120 ms"
    p.font.name = FONT_TITLE
    p.font.size = Pt(28)
    p.font.bold = True
    p.font.color.rgb = C_CYAN
    p2 = tf.add_paragraph()
    p2.text = "Thời gian phản hồi API trung bình qua giao thức HTTP"
    p2.font.name = FONT_BODY
    p2.font.size = Pt(12)
    p2.font.color.rgb = C_MUTED

    m2 = add_card(s15, Inches(3.75), Inches(1.8), Inches(2.7), Inches(2.2), "", bg_color=C_CARD)
    tb = s15.shapes.add_textbox(Inches(3.85), Inches(2.0), Inches(2.5), Inches(1.8))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "3 - 5 giây"
    p.font.name = FONT_TITLE
    p.font.size = Pt(28)
    p.font.bold = True
    p.font.color.rgb = C_PRIMARY
    p2 = tf.add_paragraph()
    p2.text = "Gemini AI sinh hoàn chỉnh 10 câu hỏi kèm giải thích"
    p2.font.name = FONT_BODY
    p2.font.size = Pt(12)
    p2.font.color.rgb = C_MUTED

    m3 = add_card(s15, Inches(6.7), Inches(1.8), Inches(2.7), Inches(2.2), "", bg_color=C_CARD)
    tb = s15.shapes.add_textbox(Inches(6.8), Inches(2.0), Inches(2.5), Inches(1.8))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "100%"
    p.font.name = FONT_TITLE
    p.font.size = Pt(28)
    p.font.bold = True
    p.font.color.rgb = C_GREEN
    p2 = tf.add_paragraph()
    p2.text = "Bảo toàn dữ liệu khi rớt mạng Wi-Fi hoặc F5 tải lại trang"
    p2.font.name = FONT_BODY
    p2.font.size = Pt(12)
    p2.font.color.rgb = C_MUTED

    m4 = add_card(s15, Inches(9.65), Inches(1.8), Inches(2.7), Inches(2.2), "", bg_color=C_CARD)
    tb = s15.shapes.add_textbox(Inches(9.75), Inches(2.0), Inches(2.5), Inches(1.8))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "Chuẩn .XLSX"
    p.font.name = FONT_TITLE
    p.font.size = Pt(26)
    p.font.bold = True
    p.font.color.rgb = C_AMBER
    p2 = tf.add_paragraph()
    p2.text = "Xuất bảng điểm Excel độ rộng chuẩn, triệt tiêu lỗi ###"
    p2.font.name = FONT_BODY
    p2.font.size = Pt(12)
    p2.font.color.rgb = C_MUTED

    h_box = add_card(s15, Inches(0.8), Inches(4.3), Inches(11.55), Inches(2.6), "Tính Năng Hoàn Thiện Thực Tế", C_WHITE)
    add_bullets(s15, Inches(1.1), Inches(4.9), Inches(11.0), Inches(1.8), [
        "✓ Chạy ổn định trên nhiều máy cùng lúc (Mạng LAN & Internet qua Pinggy).",
        "✓ Hệ thống chống gian lận hoạt động mượt mà, phân loại rõ thí sinh trung thực và vi phạm.",
        "✓ Bảng thống kê giáo viên có biểu đồ phổ điểm và xuất file Excel sắc nét.",
        "✓ 100% mã nguồn lưu trữ và đồng bộ liên tục trên GitHub."
    ])

    # ==========================================
    # SLIDE 16: KẾT LUẬN & ĐỊNH HƯỚNG PHÁT TRIỂN
    # ==========================================
    s16 = prs.slides.add_slide(blank_layout)
    add_header(s16, "15. Kết Luận", "Kết Luận & Định Hướng Phát Triển Cuối Kỳ", "Đóng góp thực tiễn của đề tài và kế hoạch nâng cấp trong giai đoạn tiếp theo")

    add_card(s16, Inches(0.8), Inches(1.8), Inches(5.6), Inches(5.1), "Kết Luận Đạt Được", C_GREEN)
    add_bullets(s16, Inches(1.1), Inches(2.5), Inches(5.0), Inches(4.0), [
        "• Hoàn thành trọn vẹn kiến trúc mạng Client-Server.",
        "• Vận dụng xuất sắc các giao thức TCP/IP, HTTP, HTTPS & JWT.",
        "• Giải quyết triệt để vấn đề gian lận và rớt mạng khi thi cử.",
        "• Ứng dụng thực tiễn cao: Sẵn sàng dùng cho lớp học và kỳ thi."
    ])

    add_card(s16, Inches(6.9), Inches(1.8), Inches(5.6), Inches(5.1), "Định Hướng Cuối Kỳ", C_CYAN)
    add_bullets(s16, Inches(7.2), Inches(2.5), Inches(5.0), Inches(4.0), [
        "• WebSocket / SignalR: Chế độ thi đấu đối kháng trực tiếp (Kahoot Mode).",
        "• AI Camera: Giám sát nhận diện khuôn mặt qua webcam.",
        "• Docker Container: Đóng gói toàn bộ Backend & DB vào Container.",
        "• Cloud Deployment: Triển khai lên máy chủ đám mây với tên miền riêng."
    ])

    prs.save(output_path)
    print(f"Presentation saved successfully to {output_path}")

if __name__ == "__main__":
    out_file = os.path.join(os.path.dirname(__file__), "slide_thuyet_trinh_QuizAI_final.pptx")
    create_presentation(out_file)
