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
    C_BG = RGBColor(11, 15, 25)           # Dark Slate (#0B0F19)
    C_CARD = RGBColor(19, 27, 46)         # Deep Navy Card (#131B2E)
    C_BORDER = RGBColor(40, 53, 84)       # Subtle Border (#283554)
    C_PRIMARY = RGBColor(99, 102, 241)    # Indigo Accent (#6366F1)
    C_CYAN = RGBColor(6, 182, 212)        # Cyan Accent (#06B6D4)
    C_GREEN = RGBColor(16, 185, 129)      # Emerald Accent (#10B981)
    C_AMBER = RGBColor(245, 158, 11)      # Amber Accent (#F59E0B)
    C_RED = RGBColor(239, 68, 68)         # Crimson Red (#EF4444)
    C_WHITE = RGBColor(255, 255, 255)
    C_TEXT = RGBColor(203, 213, 225)      # Slate 300 Text
    C_MUTED = RGBColor(148, 163, 184)     # Slate 400 Subtitle

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
        txBox = slide.shapes.add_textbox(Inches(0.8), Inches(0.35), Inches(11.733), Inches(1.25))
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
        p.font.size = Pt(22)
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

    def add_bullets(slide, left, top, width, height, items, font_size=13):
        txBox = slide.shapes.add_textbox(left, top, width, height)
        tf = txBox.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0

        for i, item in enumerate(items):
            p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
            p.text = item
            p.font.name = FONT_BODY
            p.font.size = Pt(font_size)
            p.font.color.rgb = C_TEXT
            p.space_after = Pt(7)

    # ==========================================
    # SLIDE 1: TRANG BÌA (BÁO CÁO ĐỒ ÁN CUỐI KỲ)
    # ==========================================
    s1 = prs.slides.add_slide(blank_layout)
    set_background(s1)
    box = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.5), Inches(1.0), Inches(10.333), Inches(5.5))
    box.fill.solid()
    box.fill.fore_color.rgb = C_CARD
    box.line.color.rgb = C_BORDER
    box.line.width = Pt(1.5)

    tx = s1.shapes.add_textbox(Inches(1.8), Inches(1.35), Inches(9.733), Inches(4.8))
    tf = tx.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0

    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.CENTER
    p.text = "BÁO CÁO ĐỒ ÁN CUỐI KỲ • HỌC PHẦN LẬP TRÌNH MẠNG"
    p.font.name = FONT_TITLE
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = C_CYAN
    p.space_after = Pt(14)

    p = tf.add_paragraph()
    p.alignment = PP_ALIGN.CENTER
    p.text = "QuizAI – Hệ Thống Trắc Nghiệm Online\nTích Hợp AI & Giám Sát Thi Đa Thiết Bị"
    p.font.name = FONT_TITLE
    p.font.size = Pt(28)
    p.font.bold = True
    p.font.color.rgb = C_WHITE
    p.space_after = Pt(16)

    p = tf.add_paragraph()
    p.alignment = PP_ALIGN.CENTER
    p.text = "Client-Server • RESTful API • TCP/IP • HTTPS TLS • Anti-Cheat 3 Lớp • Cloud Deployment"
    p.font.name = FONT_BODY
    p.font.size = Pt(14)
    p.font.color.rgb = C_TEXT
    p.space_after = Pt(28)

    p = tf.add_paragraph()
    p.alignment = PP_ALIGN.CENTER
    p.text = "Giảng viên hướng dẫn: Bộ môn Lập Trình Mạng    |    Nhóm sinh viên thực hiện: QuizAI Team"
    p.font.name = FONT_BODY
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = C_MUTED

    # ==========================================
    # SLIDE 2: LÝ DO CHỌN ĐỀ TÀI & MỤC TIÊU DỰ ÁN
    # ==========================================
    s2 = prs.slides.add_slide(blank_layout)
    add_header(s2, "01. Tổng Quan", "Lý Do Chọn Đề Tài & Mục Tiêu Dự Án", "Giải quyết bài toán tạo đề thi, chống gian lận và tối ưu hạ tầng mạng")

    add_card(s2, Inches(0.8), Inches(1.8), Inches(5.6), Inches(5.1), "Thực Trạng & Vấn Đề", C_AMBER)
    add_bullets(s2, Inches(1.1), Inches(2.5), Inches(5.0), Inches(4.0), [
        "• Soạn đề thủ công: Tốn nhiều thời gian, khó đa dạng hóa câu hỏi.",
        "• Gian lận trực tuyến: Chuyển tab tra cứu Google, nhờ ChatGPT giải hộ.",
        "• Nhìn bài thi: Thí sinh ngồi cạnh nhau có cùng đề và vị trí đáp án.",
        "• Chụp trộm đề: Thí sinh dùng điện thoại hoặc phím tắt chụp màn hình.",
        "• Rủi ro đường truyền: Rớt mạng Wi-Fi làm mất sạch bài thi đang làm."
    ])

    add_card(s2, Inches(6.9), Inches(1.8), Inches(5.6), Inches(5.1), "Mục Tiêu Giải Quyết", C_GREEN)
    add_bullets(s2, Inches(7.2), Inches(2.5), Inches(5.0), Inches(4.0), [
        "• AI Gemini: Tự động sinh bộ đề 10-30 câu chuẩn xác trong 3-5 giây.",
        "• Chống gian lận 3 lớp: Bắt chuyển tab (3 lần nộp bài), chặn PrintScreen/DevTools.",
        "• Dynamic Watermark: In mờ danh tính thí sinh chống chụp ảnh bằng điện thoại.",
        "• Trộn đề Fisher-Yates: Đảo ngẫu nhiên vị trí câu hỏi & đáp án A, B, C, D.",
        "• Auto-Save Real-time: Bảo toàn 100% dữ liệu bài làm khi rớt mạng hoặc F5."
    ])

    # ==========================================
    # SLIDE 3: THÀNH VIÊN & PHÂN CÔNG CÔNG VIỆC
    # ==========================================
    s3 = prs.slides.add_slide(blank_layout)
    add_header(s3, "02. Tổ Chức", "Thành Viên & Phân Công Công Việc", "Phân chia rõ ràng trách nhiệm theo từng tầng kiến trúc hệ thống")

    add_card(s3, Inches(0.8), Inches(1.8), Inches(3.6), Inches(5.1), "Backend & Architecture", C_PRIMARY)
    add_bullets(s3, Inches(1.05), Inches(2.5), Inches(3.1), Inches(4.0), [
        "• Lập trình ASP.NET Core 9 API.",
        "• Cấu hình TCP/IP, CORS & Port 0.0.0.0.",
        "• Tích hợp Google Gemini AI.",
        "• Xác thực JWT & Mã hóa BCrypt.",
        "• Thiết kế CSDL SQL Server & EF Core."
    ])

    add_card(s3, Inches(4.85), Inches(1.8), Inches(3.6), Inches(5.1), "Frontend & UX/UI", C_CYAN)
    add_bullets(s3, Inches(5.1), Inches(2.5), Inches(3.1), Inches(4.0), [
        "• Xây dựng giao diện React 19 SPA.",
        "• Dark Mode hiện đại với TailwindCSS.",
        "• Xử lý Auto-Save & Countdown Timer.",
        "• Trộn đề ngẫu nhiên per attempt.",
        "• Bảng thống kê & Xuất Excel (.xlsx)."
    ])

    add_card(s3, Inches(8.9), Inches(1.8), Inches(3.6), Inches(5.1), "Security & Cloud DevOps", C_GREEN)
    add_bullets(s3, Inches(9.15), Inches(2.5), Inches(3.1), Inches(4.0), [
        "• Phát triển module Anti-Cheat 3 lớp.",
        "• Kỹ thuật Debounce chống đếm trùng tab.",
        "• Thiết lập Cloudflare Tunnel & HTTPS.",
        "• Triển khai đám mây Vercel Production.",
        "• Kiểm thử tải đa thiết bị & Báo cáo."
    ])

    # ==========================================
    # SLIDE 4: TIMELINE – KẾ HOẠCH & TIẾN ĐỘ THỰC HIỆN
    # ==========================================
    s4 = prs.slides.add_slide(blank_layout)
    add_header(s4, "03. Tiến Độ", "Timeline – Kế Hoạch & Tiến Độ Thực Hiện", "Quy trình phát triển chuẩn công nghiệp từ thiết kế đến triển khai thực tế")

    add_card(s4, Inches(0.8), Inches(1.8), Inches(2.7), Inches(5.1), "Giai Đoạn 1: Thiết Kế", C_PRIMARY)
    add_bullets(s4, Inches(1.0), Inches(2.5), Inches(2.3), Inches(4.0), [
        "• Khảo sát nghiệp vụ.",
        "• Thiết kế mô hình mạng.",
        "• Thiết kế CSDL (ERD).",
        "• Chuẩn hóa RESTful API."
    ])

    add_card(s4, Inches(3.75), Inches(1.8), Inches(2.7), Inches(5.1), "Giai Đoạn 2: Lập Trình", C_CYAN)
    add_bullets(s4, Inches(3.95), Inches(2.5), Inches(2.3), Inches(4.0), [
        "• Viết Backend Web API.",
        "• Viết Frontend React SPA.",
        "• Tích hợp Gemini GenAI.",
        "• Xử lý Token JWT & Auth."
    ])

    add_card(s4, Inches(6.7), Inches(1.8), Inches(2.7), Inches(5.1), "Giai Đoạn 3: Nâng Cấp", C_AMBER)
    add_bullets(s4, Inches(6.9), Inches(2.5), Inches(2.3), Inches(4.0), [
        "• Anti-Cheat 3 lớp toàn diện.",
        "• Auto-Save & Trộn đề.",
        "• Xuất Excel (.xlsx) chuẩn.",
        "• Chạy đa máy mạng LAN."
    ])

    add_card(s4, Inches(9.65), Inches(1.8), Inches(2.7), Inches(5.1), "Giai Đoạn 4: Hoàn Thiện", C_GREEN)
    add_bullets(s4, Inches(9.85), Inches(2.5), Inches(2.3), Inches(4.0), [
        "• Cloudflare Tunnel & HTTPS.",
        "• Deploy Vercel Production.",
        "• Kiểm thử tải đa thiết bị.",
        "• Nghiệm thu đồ án cuối kỳ."
    ])

    # ==========================================
    # SLIDE 5: CHỨC NĂNG HỆ THỐNG TOÀN DIỆN
    # ==========================================
    s5 = prs.slides.add_slide(blank_layout)
    add_header(s5, "04. Chức Năng", "Các Chức Năng Cốt Lõi Của Hệ Thống", "Phân quyền chặt chẽ giữa Thí sinh và Quản trị viên / Giáo viên")

    add_card(s5, Inches(0.8), Inches(1.8), Inches(5.6), Inches(5.1), "Phân Hệ Thí Sinh (Student)", C_CYAN)
    add_bullets(s5, Inches(1.1), Inches(2.5), Inches(5.0), Inches(4.0), [
        "• Đăng ký / Đăng nhập: Bảo mật xác thực qua JWT Token.",
        "• Phòng thi trực tuyến: Đồng hồ đếm ngược đồng bộ Server UTC.",
        "• Trộn đề thông minh: Đảo ngẫu nhiên câu hỏi & 4 đáp án A-B-C-D.",
        "• Auto-Save an toàn: Tự động lưu bài làm vào LocalStorage.",
        "• Xem kết quả: Chấm điểm tức thì, xem đáp án & giải thích chi tiết."
    ])

    add_card(s5, Inches(6.9), Inches(1.8), Inches(5.6), Inches(5.1), "Phân Hệ Giáo Viên & Quản Trị (Admin)", C_PRIMARY)
    add_bullets(s5, Inches(7.2), Inches(2.5), Inches(5.0), Inches(4.0), [
        "• AI Tạo đề tự động: Nhập chủ đề/tài liệu -> Gemini AI sinh đề thi.",
        "• Kiểm duyệt câu hỏi: Xem trước, chỉnh sửa, phê duyệt hoặc xóa.",
        "• Quản lý đề & Tài khoản: CRUD đề thi, kích hoạt/khóa tài khoản.",
        "• Giám sát vi phạm: Bảng theo dõi số lần gian lận rời màn hình.",
        "• Xuất báo cáo Excel: Tải file .xlsx định dạng chuẩn, không lỗi ###."
    ])

    # ==========================================
    # SLIDE 6: NGĂN XẾP CÔNG NGHỆ TOÀN DIỆN
    # ==========================================
    s6 = prs.slides.add_slide(blank_layout)
    add_header(s6, "05. Công Nghệ", "Ngăn Xếp Công Nghệ Toàn Diện (Tech Stack)", "Kết hợp công nghệ hiện đại đảm bảo hiệu năng mạng, bảo mật và độ ổn định")

    add_card(s6, Inches(0.8), Inches(1.8), Inches(3.6), Inches(5.1), "Frontend Stack", C_CYAN)
    add_bullets(s6, Inches(1.05), Inches(2.5), Inches(3.1), Inches(4.0), [
        "• React 19: Xây dựng SPA tốc độ cao.",
        "• Vite 8: Build siêu tốc, hỗ trợ Proxy.",
        "• TailwindCSS: Giao diện Dark Mode.",
        "• Axios: Tự đính kèm Bearer Token.",
        "• SheetJS (xlsx): Xuất file Excel chuẩn."
    ])

    add_card(s6, Inches(4.85), Inches(1.8), Inches(3.6), Inches(5.1), "Backend & AI Stack", C_PRIMARY)
    add_bullets(s6, Inches(5.1), Inches(2.5), Inches(3.1), Inches(4.0), [
        "• ASP.NET Core 9: Web API đa luồng.",
        "• Kestrel Server: Độ trễ cực thấp <120ms.",
        "• Google Gemini API: GenAI tạo trắc nghiệm.",
        "• JWT: Xác thực phi trạng thái (Stateless).",
        "• BCrypt.Net: Băm mật khẩu an toàn."
    ])

    add_card(s6, Inches(8.9), Inches(1.8), Inches(3.6), Inches(5.1), "Database & Cloud DevOps", C_GREEN)
    add_bullets(s6, Inches(9.15), Inches(2.5), Inches(3.1), Inches(4.0), [
        "• SQL Server LocalDB: CSDL quan hệ.",
        "• EF Core 9: Migration & Code-First.",
        "• Vercel Cloud: Hosting Frontend toàn cầu.",
        "• Cloudflare Tunnel: Kênh HTTPS bảo mật.",
        "• GitHub CI/CD: Tự động deploy khi push."
    ])

    # ==========================================
    # SLIDE 7: KIẾN TRÚC HỆ THỐNG TỔNG THỂ (3-TIER)
    # ==========================================
    s7 = prs.slides.add_slide(blank_layout)
    add_header(s7, "06. Kiến Trúc", "Kiến Trúc Hệ Thống Tổng Thể (3-Tier)", "Mô hình Client - Server 3 tầng phân tách rõ ràng trách nhiệm")

    add_card(s7, Inches(0.8), Inches(1.8), Inches(3.6), Inches(5.1), "Tầng Client (Presentation)", C_CYAN)
    add_bullets(s7, Inches(1.05), Inches(2.5), Inches(3.1), Inches(4.0), [
        "• Single Page Application (SPA).",
        "• Giao tiếp qua HTTP/HTTPS REST API.",
        "• Lưu tạm đáp án vào LocalStorage.",
        "• Xáo trộn câu hỏi trên SessionStorage.",
        "• Bắt gian lận chuyển tab & chụp ảnh."
    ])

    add_card(s7, Inches(4.85), Inches(1.8), Inches(3.6), Inches(5.1), "Tầng Server (Business Logic)", C_PRIMARY)
    add_bullets(s7, Inches(5.1), Inches(2.5), Inches(3.1), Inches(4.0), [
        "• Điều phối các Controller RESTful API.",
        "• Middleware kiểm tra chữ ký số JWT.",
        "• Tính toán điểm số & ghi nhận vi phạm.",
        "• Đồng bộ thời gian thi theo Server UTC.",
        "• Gọi Google AI Studio qua HTTPS API."
    ])

    add_card(s7, Inches(8.9), Inches(1.8), Inches(3.6), Inches(5.1), "Tầng Database (Data Access)", C_GREEN)
    add_bullets(s7, Inches(9.15), Inches(2.5), Inches(3.1), Inches(4.0), [
        "• Lưu trữ bền vững dữ liệu chuẩn ACID.",
        "• Bảng Users: Tài khoản & Hash mật khẩu.",
        "• Bảng Exams & Questions: Ngân hàng đề.",
        "• Bảng Submissions: Điểm & Số lần vi phạm.",
        "• Bảng Details: Chi tiết từng câu trả lời."
    ])

    # ==========================================
    # SLIDE 8: CƠ CHẾ TRIỂN KHAI MẠNG (LAN & CLOUD)
    # ==========================================
    s8 = prs.slides.add_slide(blank_layout)
    add_header(s8, "07. Triển Khai Mạng", "Cơ Chế Triển Khai Mạng: LAN & Cloud Production", "Hỗ trợ kết nối đồng thời từ máy tính, laptop và điện thoại thông minh")

    add_card(s8, Inches(0.8), Inches(1.8), Inches(5.6), Inches(5.1), "1. Mạng LAN (Phòng Lab / Wi-Fi)", C_CYAN)
    add_bullets(s8, Inches(1.1), Inches(2.5), Inches(5.0), Inches(4.0), [
        "• Lắng nghe 0.0.0.0: Bind cổng 5000 & 5173 trên mọi card mạng.",
        "• Vite Reverse Proxy: Chuyển tiếp ngầm /api/* về Backend Kestrel.",
        "• Mở Firewall Windows: Lệnh netsh mở port cho các máy con kết nối.",
        "• Truy cập tức thì: Học sinh mở http://192.168.x.x:5173.",
        "• Khởi động 1-Click: File chay_he_thong.bat tự tìm IP nội bộ."
    ])

    add_card(s8, Inches(6.9), Inches(1.8), Inches(5.6), Inches(5.1), "2. Cloud Production (Vercel & Cloudflare)", C_GREEN)
    add_bullets(s8, Inches(7.2), Inches(2.5), Inches(5.0), Inches(4.0), [
        "• Tên miền chính thức: https://quiz-ai-system.vercel.app/.",
        "• CDN Toàn cầu: Vercel Edge Network tải giao diện siêu tốc.",
        "• Cloudflare HTTPS Tunnel: Kết nối an toàn không cần mở port modem.",
        "• Vượt qua rào cản mạng: Chạy mượt mà trên 4G/5G và mạng ngoài trường.",
        "• CI/CD Tự động: Commit code lên GitHub tự động cập nhật hệ thống."
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
        "• Đúng thứ tự: Gói tin đến đích luôn được sắp xếp chính xác.",
        "• Không dùng UDP: Tránh thất lạc gói tin nộp bài làm sai lệch điểm."
    ])

    add_card(s9, Inches(6.9), Inches(1.8), Inches(5.6), Inches(5.1), "Cơ Chế Bắt Tay 3 Bước (3-Way Handshake)", C_GREEN)
    add_bullets(s9, Inches(7.2), Inches(2.5), Inches(5.0), Inches(4.0), [
        "• Bước 1 (SYN): Client gửi yêu cầu kết nối kèm số Seq khởi tạo.",
        "• Bước 2 (SYN-ACK): Server xác nhận và gửi số Seq của mình.",
        "• Bước 3 (ACK): Client xác nhận hoàn tất -> Phiên TCP mở.",
        "• Quá trình ngắt kết nối (4-Way Handshake): FIN -> ACK -> FIN -> ACK.",
        "• Ứng dụng: Mọi cuộc gọi HTTP/HTTPS đều thiết lập qua TCP."
    ])

    # ==========================================
    # SLIDE 10: GIAO THỨC WEB & RESTFUL API
    # ==========================================
    s10 = prs.slides.add_slide(blank_layout)
    add_header(s10, "09. Giao Thức Web", "Giao Thức Web & Kiến Trúc RESTful API", "Chuẩn hóa tài nguyên mạng bằng các phương thức HTTP tiêu chuẩn")

    add_card(s10, Inches(0.8), Inches(1.8), Inches(5.6), Inches(5.1), "Các Phương Thức HTTP Tiêu Chuẩn", C_CYAN)
    add_bullets(s10, Inches(1.1), Inches(2.5), Inches(5.0), Inches(4.0), [
        "• GET: Lấy tài nguyên (Đọc danh sách đề thi, xem bảng điểm).",
        "• POST: Tạo mới tài nguyên (Đăng ký, Đăng nhập, Bắt đầu thi, Nộp bài).",
        "• PATCH: Cập nhật một phần (Duyệt câu hỏi, cập nhật vi phạm).",
        "• DELETE: Xóa tài nguyên (Xóa đề thi kèm câu hỏi liên quan).",
        "• OPTIONS: Preflight check kiểm tra quyền CORS trước khi gửi POST."
    ])

    add_card(s10, Inches(6.9), Inches(1.8), Inches(5.6), Inches(5.1), "Đặc Trưng Kiến Trúc REST", C_PRIMARY)
    add_bullets(s10, Inches(7.2), Inches(2.5), Inches(5.0), Inches(4.0), [
        "• Stateless (Phi trạng thái): Mỗi request mang đủ thông tin xác thực.",
        "• Định dạng JSON: Gọn nhẹ, tiết kiệm băng thông đường truyền mạng.",
        "• Mã trạng thái chuẩn: 200 OK, 201 Created, 401 Unauthorized, 403 Forbidden.",
        "• Swagger UI tích hợp: Tài liệu hóa trực quan tại đường dẫn /swagger.",
        "• Khả năng mở rộng (Scalability): Dễ dàng nâng cấp và bảo trì hệ thống."
    ])

    # ==========================================
    # SLIDE 11: HTTPS & CƠ CHẾ BẢO MẬT TLS/SSL
    # ==========================================
    s11 = prs.slides.add_slide(blank_layout)
    add_header(s11, "10. Bảo Mật Web", "Giao Thức HTTPS & Cơ Chế Hoạt Động TLS/SSL", "Bảo vệ dữ liệu thi cử chống nghe lén và giả mạo trên đường truyền")

    add_card(s11, Inches(0.8), Inches(1.8), Inches(5.6), Inches(5.1), "Quy Trình Bắt Tay TLS (TLS Handshake)", C_PRIMARY)
    add_bullets(s11, Inches(1.1), Inches(2.5), Inches(5.0), Inches(4.0), [
        "• ClientHello: Gửi phiên bản TLS và danh sách mã hóa (Cipher Suites).",
        "• ServerHello & Certificate: Server gửi chứng chỉ số chứa Public Key.",
        "• Key Exchange: Trao đổi khóa bí mật phiên (Session Key) bất đối xứng.",
        "• Mã hóa đối xứng: Toàn bộ dữ liệu sau đó được mã hóa bằng AES-256.",
        "• Finished: Xác nhận kết nối bảo mật hoàn tất, bắt đầu gửi dữ liệu."
    ])

    add_card(s11, Inches(6.9), Inches(1.8), Inches(5.6), Inches(5.1), "Tầm Quan Trọng Trong QuizAI", C_GREEN)
    add_bullets(s11, Inches(7.2), Inches(2.5), Inches(5.0), Inches(4.0), [
        "• Chống bắt gói tin (Sniffing): Wireshark chỉ thấy dòng dữ liệu mã hóa.",
        "• Bảo vệ JWT Token & Pass: Không bị lộ mã xác thực trên mạng Wi-Fi công cộng.",
        "• Bảo vệ Gemini API Key: Kênh HTTPS ngăn chặn rò rỉ khóa bí mật.",
        "• Toàn vẹn dữ liệu (Integrity): Chống tấn công Man-in-the-Middle sửa đáp án.",
        "• Tương thích trình duyệt: Không bị cảnh báo 'Not Secure' màu đỏ."
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
        "• Phân quyền linh hoạt: Chứa Claim Vai trò (Admin / Student) trong Payload.",
        "• Tự động đính kèm: Axios Interceptor gán Bearer Token vào mọi request.",
        "• Tự động đăng xuất: Chuyển hướng về Login khi Token hết hạn (401)."
    ])

    add_card(s12, Inches(6.9), Inches(1.8), Inches(5.6), Inches(5.1), "Chính Sách Mạng CORS", C_AMBER)
    add_bullets(s12, Inches(7.2), Inches(2.5), Inches(5.0), Inches(4.0), [
        "• Same-Origin Policy: Trình duyệt mặc định chặn request khác Origin.",
        "• Cấu hình linh hoạt: Cho phép domain Vercel và mạng LAN kết nối.",
        "• Hỗ trợ Preflight: Phản hồi mã 204 No Content cho các lệnh OPTIONS.",
        "• AllowCredentials: Cho phép truyền tải an toàn Token và Cookie.",
        "• Bảo mật chặt chẽ: Vẫn kiểm soát toàn diện bằng Middleware JWT."
    ])

    # ==========================================
    # SLIDE 13: HỆ THỐNG CHỐNG GIAN LẬN ĐA TẦNG (3 LỚP)
    # ==========================================
    s13 = prs.slides.add_slide(blank_layout)
    add_header(s13, "12. Chống Gian Lận", "Hệ Thống Chống Gian Lận Đa Tầng (3 Lớp)", "Giám sát toàn diện hành vi thi cử, đảm bảo tính công bằng và minh bạch")

    add_card(s13, Inches(0.8), Inches(1.8), Inches(3.6), Inches(5.1), "Lớp 1: Bắt Chuyển Tab", C_RED)
    add_bullets(s13, Inches(1.05), Inches(2.5), Inches(3.1), Inches(4.0), [
        "• Bắt visibilitychange & blur.",
        "• Thuật toán Debounce 2.5s.",
        "• Chống đếm trùng sự kiện.",
        "• Vi phạm 1 & 2: Cảnh báo đỏ.",
        "• Vi phạm 3: Tự động nộp bài."
    ])

    add_card(s13, Inches(4.85), Inches(1.8), Inches(3.6), Inches(5.1), "Lớp 2: Chặn Chụp Màn Hình", C_AMBER)
    add_bullets(s13, Inches(5.1), Inches(2.5), Inches(3.1), Inches(4.0), [
        "• Chặn phím PrintScreen.",
        "• Màn hình chớp đen khi chụp.",
        "• Chặn Ctrl+C, Ctrl+V, Ctrl+P.",
        "• Chặn F12 & DevTools soi đáp án.",
        "• Tắt chuột phải & chống bôi đen."
    ])

    add_card(s13, Inches(8.9), Inches(1.8), Inches(3.6), Inches(5.1), "Lớp 3: Watermark Chống Camera", C_CYAN)
    add_bullets(s13, Inches(9.15), Inches(2.5), Inches(3.1), Inches(4.0), [
        "• In chìm Họ tên & Tên đăng nhập.",
        "• Phủ chéo toàn bộ màn hình thi.",
        "• Chụp điện thoại sẽ lộ danh tính.",
        "• Ghi số lần vi phạm vào CSDL.",
        "• Giáo viên đối soát trên Excel."
    ])

    # ==========================================
    # SLIDE 14: LUỒNG DỮ LIỆU CỐT LÕI (DATA FLOW)
    # ==========================================
    s14 = prs.slides.add_slide(blank_layout)
    add_header(s14, "13. Luồng Dữ Liệu", "Luồng Dữ Liệu Cốt Lõi Của Hệ Thống (Data Flow)", "Các quy trình xử lý chính giữa Client, Server, Database và Gemini AI")

    add_card(s14, Inches(0.8), Inches(1.8), Inches(3.6), Inches(5.1), "Luồng 1: Xác Thực", C_PRIMARY)
    add_bullets(s14, Inches(1.05), Inches(2.5), Inches(3.1), Inches(4.0), [
        "1. Gửi POST /auth/login.",
        "2. So khớp BCrypt Hash.",
        "3. Ký số JWT Token.",
        "4. Lưu vào LocalStorage.",
        "5. Phân quyền Admin/User."
    ])

    add_card(s14, Inches(4.85), Inches(1.8), Inches(3.6), Inches(5.1), "Luồng 2: Thi & Chấm Điểm", C_GREEN)
    add_bullets(s14, Inches(5.1), Inches(2.5), Inches(3.1), Inches(4.0), [
        "1. Bắt đầu: Nhận đề thi.",
        "2. Client: Trộn đề & Auto-Save.",
        "3. Giám sát: Đếm chuyển tab.",
        "4. Nộp bài: Gửi danh sách chọn.",
        "5. Chấm điểm & hiện giải thích."
    ])

    add_card(s14, Inches(8.9), Inches(1.8), Inches(3.6), Inches(5.1), "Luồng 3: AI Sinh Đề Thi", C_CYAN)
    add_bullets(s14, Inches(9.15), Inches(2.5), Inches(3.1), Inches(4.0), [
        "1. Giáo viên nhập chủ đề/tài liệu.",
        "2. Backend gửi Prompt tới Gemini.",
        "3. Nhận phản hồi JSON câu hỏi.",
        "4. Giáo viên duyệt & chỉnh sửa.",
        "5. Lưu vào ngân hàng CSDL."
    ])

    # ==========================================
    # SLIDE 15: KẾT QUẢ ĐẠT ĐƯỢC & ĐO LƯỜNG HIỆU NĂNG
    # ==========================================
    s15 = prs.slides.add_slide(blank_layout)
    add_header(s15, "14. Thực Nghiệm", "Kết Quả Đạt Được & Đo Lường Hiệu Năng", "Các chỉ số thực nghiệm đo đạc trong quá trình kiểm thử tải và chạy thực tế")

    # 4 Metric Cards
    m1 = add_card(s15, Inches(0.8), Inches(1.8), Inches(2.7), Inches(2.1), "", bg_color=C_CARD)
    tb = s15.shapes.add_textbox(Inches(0.9), Inches(1.95), Inches(2.5), Inches(1.8))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "< 120 ms"
    p.font.name = FONT_TITLE
    p.font.size = Pt(28)
    p.font.bold = True
    p.font.color.rgb = C_CYAN
    p2 = tf.add_paragraph()
    p2.text = "Thời gian phản hồi API trung bình qua giao thức HTTP/HTTPS"
    p2.font.name = FONT_BODY
    p2.font.size = Pt(12)
    p2.font.color.rgb = C_MUTED

    m2 = add_card(s15, Inches(3.75), Inches(1.8), Inches(2.7), Inches(2.1), "", bg_color=C_CARD)
    tb = s15.shapes.add_textbox(Inches(3.85), Inches(1.95), Inches(2.5), Inches(1.8))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "3 - 5 giây"
    p.font.name = FONT_TITLE
    p.font.size = Pt(28)
    p.font.bold = True
    p.font.color.rgb = C_PRIMARY
    p2 = tf.add_paragraph()
    p2.text = "Gemini AI sinh hoàn chỉnh 10-20 câu hỏi kèm 4 đáp án & giải thích"
    p2.font.name = FONT_BODY
    p2.font.size = Pt(12)
    p2.font.color.rgb = C_MUTED

    m3 = add_card(s15, Inches(6.7), Inches(1.8), Inches(2.7), Inches(2.1), "", bg_color=C_CARD)
    tb = s15.shapes.add_textbox(Inches(6.8), Inches(1.95), Inches(2.5), Inches(1.8))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "100%"
    p.font.name = FONT_TITLE
    p.font.size = Pt(28)
    p.font.bold = True
    p.font.color.rgb = C_GREEN
    p2 = tf.add_paragraph()
    p2.text = "Bảo toàn dữ liệu bài làm khi rớt mạng Wi-Fi hoặc F5 tải lại trang"
    p2.font.name = FONT_BODY
    p2.font.size = Pt(12)
    p2.font.color.rgb = C_MUTED

    m4 = add_card(s15, Inches(9.65), Inches(1.8), Inches(2.7), Inches(2.1), "", bg_color=C_CARD)
    tb = s15.shapes.add_textbox(Inches(9.75), Inches(1.95), Inches(2.5), Inches(1.8))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "Chuẩn .XLSX"
    p.font.name = FONT_TITLE
    p.font.size = Pt(26)
    p.font.bold = True
    p.font.color.rgb = C_AMBER
    p2 = tf.add_paragraph()
    p2.text = "Xuất bảng điểm Excel tự căn chỉnh độ rộng cột, triệt tiêu lỗi ###"
    p2.font.name = FONT_BODY
    p2.font.size = Pt(12)
    p2.font.color.rgb = C_MUTED

    h_box = add_card(s15, Inches(0.8), Inches(4.15), Inches(11.55), Inches(2.75), "Điểm Nổi Bật Vận Hành Thực Tế", C_WHITE)
    add_bullets(s15, Inches(1.1), Inches(4.75), Inches(11.0), Inches(1.9), [
        "✓ Chạy thực tế trên đám mây Production: https://quiz-ai-system.vercel.app/.",
        "✓ Hỗ trợ thi đồng thời nhiều thiết bị qua mạng LAN và Cloudflare Tunnel an toàn.",
        "✓ Hệ thống chống gian lận 3 lớp tự động ghi nhận số lần vi phạm chính xác vào CSDL.",
        "✓ 100% mã nguồn lưu trữ và kiểm soát phiên bản liên tục trên GitHub."
    ])

    # ==========================================
    # SLIDE 16: KẾT LUẬN & HƯỚNG MỞ RỘNG TƯƠNG LAI
    # ==========================================
    s16 = prs.slides.add_slide(blank_layout)
    add_header(s16, "15. Kết Luận", "Kết Luận & Hướng Mở Rộng Tương Lai", "Đóng góp thực tiễn của đề tài và định hướng nâng cấp trong giai đoạn tiếp theo")

    add_card(s16, Inches(0.8), Inches(1.8), Inches(5.6), Inches(5.1), "Kết Luận Đạt Được", C_GREEN)
    add_bullets(s16, Inches(1.1), Inches(2.5), Inches(5.0), Inches(4.0), [
        "• Hoàn thành trọn vẹn kiến trúc mạng Client-Server 3 tầng chuẩn chỉ.",
        "• Vận dụng xuất sắc kiến thức: TCP/IP, HTTP/HTTPS, REST, CORS & JWT.",
        "• Giải quyết triệt để vấn đề gian lận thi cử và mất bài khi rớt mạng.",
        "• Tích hợp thành công GenAI Gemini tạo đề thi thông minh tự động.",
        "• Triển khai thành công lên môi trường đám mây Vercel Production."
    ])

    add_card(s16, Inches(6.9), Inches(1.8), Inches(5.6), Inches(5.1), "Hướng Phát Triển Tương Lai", C_CYAN)
    add_bullets(s16, Inches(7.2), Inches(2.5), Inches(5.0), Inches(4.0), [
        "• WebSocket / SignalR: Chế độ thi đấu đối kháng trực tiếp (Kahoot Mode).",
        "• AI Camera Proctoring: Nhận diện khuôn mặt & phát hiện quay cóp qua webcam.",
        "• Mobile Application: Đóng gói app đa nền tảng Flutter / React Native.",
        "• Microservices Architecture: Tách riêng dịch vụ AI Generator và Auth Service.",
        "• Database Clustering: Nhân bản CSDL tăng khả năng chịu tải hàng nghìn thí sinh."
    ])

    # ==========================================
    # SLIDE 17: Q&A / CẢM ƠN HỘI ĐỒNG & GIẢNG VIÊN
    # ==========================================
    s17 = prs.slides.add_slide(blank_layout)
    set_background(s17)
    box = s17.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.5), Inches(1.0), Inches(10.333), Inches(5.5))
    box.fill.solid()
    box.fill.fore_color.rgb = C_CARD
    box.line.color.rgb = C_BORDER
    box.line.width = Pt(1.5)

    tx = s17.shapes.add_textbox(Inches(1.8), Inches(1.4), Inches(9.733), Inches(4.7))
    tf = tx.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0

    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.CENTER
    p.text = "LỜI CẢM ƠN"
    p.font.name = FONT_TITLE
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = C_CYAN
    p.space_after = Pt(12)

    p = tf.add_paragraph()
    p.alignment = PP_ALIGN.CENTER
    p.text = "Cảm Ơn Quý Thầy Cô & Hội Đồng Đã Lắng Nghe!"
    p.font.name = FONT_TITLE
    p.font.size = Pt(26)
    p.font.bold = True
    p.font.color.rgb = C_WHITE
    p.space_after = Pt(18)

    p = tf.add_paragraph()
    p.alignment = PP_ALIGN.CENTER
    p.text = "Hệ Thống Trực Tuyến: https://quiz-ai-system.vercel.app/\nGitHub: https://github.com/hieuqt05/quiz-ai-system"
    p.font.name = FONT_BODY
    p.font.size = Pt(14)
    p.font.color.rgb = C_GREEN
    p.space_after = Pt(24)

    p = tf.add_paragraph()
    p.alignment = PP_ALIGN.CENTER
    p.text = "Nhóm xin sẵn sàng lắng nghe nhận xét và trả lời các câu hỏi từ Hội Đồng!"
    p.font.name = FONT_BODY
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = C_TEXT

    prs.save(output_path)
    print(f"Presentation saved successfully to {output_path}")

if __name__ == "__main__":
    out_file = os.path.join(os.path.dirname(__file__), "slide_thuyet_trinh_QuizAI_final.pptx")
    create_presentation(out_file)
