import sys
import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

def create_quiz_ai_presentation(output_path):
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # Colors
    C_BG = RGBColor(11, 15, 25)          # Deep dark
    C_CARD = RGBColor(19, 27, 46)        # Card background
    C_CARD_HOVER = RGBColor(28, 39, 66)
    C_BORDER = RGBColor(40, 53, 84)      # Card border
    C_PRIMARY = RGBColor(99, 102, 241)   # Indigo
    C_PRIMARY_LIGHT = RGBColor(129, 140, 248)
    C_CYAN = RGBColor(6, 182, 212)       # Cyan
    C_CYAN_LIGHT = RGBColor(56, 189, 248)
    C_GREEN = RGBColor(16, 185, 129)     # Emerald
    C_AMBER = RGBColor(245, 158, 11)     # Amber
    C_PINK = RGBColor(236, 72, 153)      # Pink
    C_WHITE = RGBColor(255, 255, 255)
    C_TEXT_SUB = RGBColor(203, 213, 225) # Slate 300
    C_MUTED = RGBColor(148, 163, 184)    # Slate 400

    FONT_TITLE = "Segoe UI"
    FONT_BODY = "Segoe UI"
    FONT_MONO = "Consolas"

    def set_slide_background(slide):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
        bg.fill.solid()
        bg.fill.fore_color.rgb = C_BG
        bg.line.fill.background()
        
        # Subtle top accent bar
        top_bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, Inches(0.08))
        top_bar.fill.solid()
        top_bar.fill.fore_color.rgb = C_PRIMARY
        top_bar.line.fill.background()

    def add_header(slide, tag_text, title_text, subtitle_text=""):
        set_slide_background(slide)
        
        # Header container
        txBox = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.733), Inches(1.3))
        tf = txBox.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0

        # Tag
        p_tag = tf.paragraphs[0]
        p_tag.text = tag_text.upper()
        p_tag.font.name = FONT_TITLE
        p_tag.font.size = Pt(11)
        p_tag.font.bold = True
        p_tag.font.color.rgb = C_CYAN_LIGHT
        p_tag.space_after = Pt(4)

        # Title
        p_title = tf.add_paragraph()
        p_title.text = title_text
        p_title.font.name = FONT_TITLE
        p_title.font.size = Pt(24)
        p_title.font.bold = True
        p_title.font.color.rgb = C_WHITE
        p_title.space_after = Pt(4)

        # Subtitle
        if subtitle_text:
            p_sub = tf.add_paragraph()
            p_sub.text = subtitle_text
            p_sub.font.name = FONT_BODY
            p_sub.font.size = Pt(13)
            p_sub.font.color.rgb = C_MUTED

    def add_card(slide, left, top, width, height, title="", title_color=C_WHITE, bg_color=C_CARD, border_color=C_BORDER):
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        card.fill.solid()
        card.fill.fore_color.rgb = bg_color
        card.line.color.rgb = border_color
        card.line.width = Pt(1)

        if title:
            # Title inside card
            txBox = slide.shapes.add_textbox(left + Inches(0.25), top + Inches(0.2), width - Inches(0.5), Inches(0.45))
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

    # ==========================================
    # SLIDE 1: COVER
    # ==========================================
    s1 = prs.slides.add_slide(blank_layout)
    set_slide_background(s1)

    # Big Banner Box
    b_box = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.2), Inches(1.1), Inches(10.933), Inches(5.3))
    b_box.fill.solid()
    b_box.fill.fore_color.rgb = C_CARD
    b_box.line.color.rgb = C_BORDER
    b_box.line.width = Pt(1.5)

    txBox = s1.shapes.add_textbox(Inches(1.6), Inches(1.4), Inches(10.133), Inches(4.7))
    tf = txBox.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0

    p0 = tf.paragraphs[0]
    p0.alignment = PP_ALIGN.CENTER
    p0.text = "BÁO CÁO GIỮA KỲ • MÔN LẬP TRÌNH MẠNG"
    p0.font.name = FONT_TITLE
    p0.font.size = Pt(13)
    p0.font.bold = True
    p0.font.color.rgb = C_CYAN_LIGHT
    p0.space_after = Pt(12)

    p1 = tf.add_paragraph()
    p1.alignment = PP_ALIGN.CENTER
    p1.text = "QuizAI – Hệ Thống Trắc Nghiệm Online\nTích Hợp Trí Tuệ Nhân Tạo"
    p1.font.name = FONT_TITLE
    p1.font.size = Pt(32)
    p1.font.bold = True
    p1.font.color.rgb = C_WHITE
    p1.space_after = Pt(16)

    p2 = tf.add_paragraph()
    p2.alignment = PP_ALIGN.CENTER
    p2.text = "Ứng dụng mô hình Client-Server • Giao thức TCP/IP • Chuẩn RESTful API • Cơ chế bảo mật HTTPS/TLS & Xác thực JWT"
    p2.font.name = FONT_BODY
    p2.font.size = Pt(14)
    p2.font.color.rgb = C_TEXT_SUB
    p2.space_after = Pt(28)

    # Info sub cards inside Cover
    c1 = add_card(s1, Inches(2.2), Inches(4.3), Inches(4.2), Inches(1.5), "Giảng Viên Hướng Dẫn", C_CYAN_LIGHT)
    tb1 = s1.shapes.add_textbox(Inches(2.45), Inches(4.85), Inches(3.7), Inches(0.8))
    tb1.text_frame.word_wrap = True
    tb1.text_frame.margin_left = tb1.text_frame.margin_top = tb1.text_frame.margin_right = tb1.text_frame.margin_bottom = 0
    p = tb1.text_frame.paragraphs[0]
    p.text = "Giảng viên bộ môn Lập Trình Mạng\nKhoa Công Nghệ Thông Tin"
    p.font.name = FONT_BODY
    p.font.size = Pt(13)
    p.font.color.rgb = C_TEXT_SUB

    c2 = add_card(s1, Inches(6.9), Inches(4.3), Inches(4.2), Inches(1.5), "Sinh Viên Thực Hiện", C_PRIMARY_LIGHT)
    tb2 = s1.shapes.add_textbox(Inches(7.15), Inches(4.85), Inches(3.7), Inches(0.8))
    tb2.text_frame.word_wrap = True
    tb2.text_frame.margin_left = tb2.text_frame.margin_top = tb2.text_frame.margin_right = tb2.text_frame.margin_bottom = 0
    p = tb2.text_frame.paragraphs[0]
    p.text = "Nguyễn Văn Tèo & Nhóm\nGitHub: github.com/hieuqt05/quiz-ai-system"
    p.font.name = FONT_BODY
    p.font.size = Pt(13)
    p.font.color.rgb = C_TEXT_SUB

    # ==========================================
    # SLIDE 2: LÝ DO CHỌN ĐỀ TÀI & MỤC TIÊU
    # ==========================================
    s2 = prs.slides.add_slide(blank_layout)
    add_header(s2, "01. Tổng Quan & Bối Cảnh", "Lý Do Chọn Đề Tài & Mục Tiêu Dự Án", "Nhu cầu kiểm tra trắc nghiệm online kết hợp AI và công nghệ mạng tin cậy.")

    add_card(s2, Inches(0.8), Inches(1.8), Inches(5.7), Inches(3.6), "⚠️ Thực Trạng & Khó Khăn", C_AMBER)
    tb = s2.shapes.add_textbox(Inches(1.05), Inches(2.4), Inches(5.2), Inches(2.8))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
    points_left = [
        "Biên soạn đề thi thủ công: Tốn nhiều thời gian, công sức và khó đa dạng hóa ngân hàng câu hỏi.",
        "Thiếu giải thích chi tiết: Thí sinh làm bài sai nhưng không biết lý do tại sao sai để ôn luyện.",
        "Yêu cầu mạng khắt khe: Hệ thống thi online đòi hỏi truyền tin tin cậy, tuyệt đối không được thất lạc gói tin khi nộp bài."
    ]
    for pt in points_left:
        p = tf.add_paragraph() if tf.paragraphs[0].text else tf.paragraphs[0]
        p.text = "• " + pt
        p.font.name = FONT_BODY
        p.font.size = Pt(13.5)
        p.font.color.rgb = C_TEXT_SUB
        p.space_after = Pt(10)

    add_card(s2, Inches(6.8), Inches(1.8), Inches(5.7), Inches(3.6), "💡 Giải Pháp Của QuizAI", C_CYAN_LIGHT)
    tb = s2.shapes.add_textbox(Inches(7.05), Inches(2.4), Inches(5.2), Inches(2.8))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
    points_right = [
        "Tích hợp Google Gemini AI: Tự động sinh câu hỏi trắc nghiệm theo chủ đề hoặc văn bản kèm lời giải thích chi tiết.",
        "Kiến trúc RESTful API đa luồng: Tốc độ xử lý cao, độc lập giữa giao diện client và server.",
        "Bảo mật mạng toàn diện: Chuẩn hóa HTTPS/TLS, mã hóa mật khẩu BCrypt và xác thực người dùng bằng JWT Token."
    ]
    for pt in points_right:
        p = tf.add_paragraph() if tf.paragraphs[0].text else tf.paragraphs[0]
        p.text = "• " + pt
        p.font.name = FONT_BODY
        p.font.size = Pt(13.5)
        p.font.color.rgb = C_TEXT_SUB
        p.space_after = Pt(10)

    # Goal banner at bottom
    add_card(s2, Inches(0.8), Inches(5.6), Inches(11.7), Inches(1.3), "🎯 Mục Tiêu Đạt Được Trong Môn Lập Trình Mạng", C_GREEN)
    tb = s2.shapes.add_textbox(Inches(1.05), Inches(6.05), Inches(11.2), Inches(0.7))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
    p = tf.paragraphs[0]
    p.text = "Triển khai thực tế mô hình Client-Server, giao thức truyền tin TCP, cơ chế bắt tay 3 bước, định dạng gói tin HTTP RESTful, kỹ thuật bảo mật HTTPS/TLS và xác thực không trạng thái (Stateless Authentication) qua JWT Token."
    p.font.name = FONT_BODY
    p.font.size = Pt(13)
    p.font.color.rgb = C_WHITE

    # ==========================================
    # SLIDE 3: THÀNH VIÊN & PHÂN CÔNG VIỆC
    # ==========================================
    s3 = prs.slides.add_slide(blank_layout)
    add_header(s3, "02. Tổ Chức Dự Án", "Thành Viên & Phân Công Công Việc", "Phân chia rõ ràng trách nhiệm chuyên môn giữa các thành viên trong nhóm.")

    # Table of members
    rows, cols = 5, 5
    left, top, width, height = Inches(0.8), Inches(1.8), Inches(11.733), Inches(4.3)
    table_shape = s3.shapes.add_table(rows, cols, left, top, width, height)
    tbl = table_shape.table

    tbl.columns[0].width = Inches(2.2)
    tbl.columns[1].width = Inches(2.0)
    tbl.columns[2].width = Inches(3.6)
    tbl.columns[3].width = Inches(2.7)
    tbl.columns[4].width = Inches(1.233)

    headers = ["Thành Viên", "Vai Trò", "Nhiệm Vụ Chính", "Giao Thức & Kỹ Thuật", "Tiến Độ"]
    for i, h in enumerate(headers):
        cell = tbl.cell(0, i)
        cell.fill.solid()
        cell.fill.fore_color.rgb = RGBColor(30, 41, 69)
        p = cell.text_frame.paragraphs[0]
        p.text = h
        p.font.name = FONT_TITLE
        p.font.size = Pt(13)
        p.font.bold = True
        p.font.color.rgb = C_CYAN_LIGHT

    data = [
        ["Nguyễn Văn Tèo\n(Trưởng nhóm)", "Fullstack & Network Architecture", "Thiết kế kiến trúc hệ thống, Backend REST API, Database EF Core, quản lý mạng & triển khai", "HTTP REST, TCP Connection, JWT Security, Reverse Proxy", "100%"],
        ["Thành viên 02", "Frontend & UI/UX Specialist", "Xây dựng giao diện React SPA, màn hình thi trắc nghiệm đếm ngược, responsive Tailwind CSS", "HTTP Axios, State Management, LocalStorage Token", "100%"],
        ["Thành viên 03", "AI Integration & Backend", "Tích hợp Google Gemini API, Prompt Engineering, cơ chế Retry & Exponential Backoff", "External HTTPS Calls, JSON Schema Validation", "100%"],
        ["Thành viên 04", "Testing & Documentation", "Kiểm thử API (Postman/Swagger), bắt gói tin phân tích HTTP/HTTPS, viết báo cáo & slide", "Wireshark, DevTools Network, Swagger OpenAPI", "100%"]
    ]

    for row_idx, row_data in enumerate(data):
        for col_idx, cell_value in enumerate(row_data):
            cell = tbl.cell(row_idx + 1, col_idx)
            cell.fill.solid()
            cell.fill.fore_color.rgb = C_CARD if row_idx % 2 == 0 else RGBColor(15, 21, 36)
            p = cell.text_frame.paragraphs[0]
            p.text = cell_value
            p.font.name = FONT_BODY
            p.font.size = Pt(12)
            p.font.color.rgb = C_WHITE if col_idx == 0 or col_idx == 4 else C_TEXT_SUB

    add_card(s3, Inches(0.8), Inches(6.3), Inches(11.733), Inches(0.7), "", bg_color=RGBColor(15, 21, 36))
    tb = s3.shapes.add_textbox(Inches(1.0), Inches(6.4), Inches(11.3), Inches(0.5))
    tb.text_frame.word_wrap = True
    tb.text_frame.margin_left = tb.text_frame.margin_top = tb.text_frame.margin_right = tb.text_frame.margin_bottom = 0
    p = tb.text_frame.paragraphs[0]
    p.text = "Quản lý mã nguồn tập trung trên GitHub: https://github.com/hieuqt05/quiz-ai-system (Phân chia nhánh tính năng rõ ràng)"
    p.font.name = FONT_BODY
    p.font.size = Pt(12)
    p.font.color.rgb = C_CYAN_LIGHT

    # ==========================================
    # SLIDE 4: TIMELINE TIẾN ĐỘ
    # ==========================================
    s4 = prs.slides.add_slide(blank_layout)
    add_header(s4, "03. Kế Hoạch & Tiến Độ", "Timeline – Lộ Trình Phát Triển Dự Án", "Quy trình thực hiện qua 5 giai đoạn tuần tự từ nghiên cứu đến hoàn thiện đồ án.")

    stages = [
        ("G1", "Tuần 1 - 2: Khảo Sát & Thiết Kế Kiến Trúc Mạng", "Phân tích yêu cầu bài toán thi trắc nghiệm, thiết kế mô hình thực thể ERD (7 bảng), phác thảo RESTful API Endpoints và định tuyến mạng.", C_PRIMARY_LIGHT, "ĐÃ XONG"),
        ("G2", "Tuần 3 - 4: Lập Trình Backend API & Cơ Sở Dữ Liệu", "Xây dựng ASP.NET Core 9 Web API, kết nối SQL Server qua EF Core, cấu hình xác thực JWT Bearer, phân quyền Role (Student, Teacher, Admin), mã hóa BCrypt.", C_CYAN_LIGHT, "ĐÃ XONG"),
        ("G3", "Tuần 5 - 6: Tích Hợp AI & Xây Dựng Frontend SPA", "Kết nối Google Gemini API với cơ chế retry; xây dựng Frontend React + Vite: màn hình làm bài thi có đếm ngược, nộp bài, xem giải thích chi tiết, dashboard.", C_PINK, "ĐÃ XONG"),
        ("G4", "Tuần 7: Kiểm Thử Mạng, Bảo Mật & Bắt Gói Tin", "Kiểm thử API qua Swagger/Postman, bắt gói tin HTTP/HTTPS, kiểm tra token header, cơ chế chống gian lận thời gian và tự động nộp bài khi hết giờ.", C_AMBER, "ĐÃ XONG"),
        ("G5", "Tuần 8 (Hiện Tại): Báo Cáo Giữa Kỳ & Kế Hoạch Cuối Kỳ", "Hoàn thiện slide thuyết trình, đóng gói tài liệu kỹ thuật, chuẩn bị kịch bản demo trực tiếp hệ thống cho hội đồng đánh giá.", C_GREEN, "BÁO CÁO")
    ]

    top_y = 1.8
    for code, title, desc, col, status in stages:
        add_card(s4, Inches(0.8), Inches(top_y), Inches(11.733), Inches(0.95), "", bg_color=C_CARD)
        
        # Badge
        badge = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.0), Inches(top_y + 0.15), Inches(0.7), Inches(0.65))
        badge.fill.solid()
        badge.fill.fore_color.rgb = col
        badge.line.fill.background()
        p = badge.text_frame.paragraphs[0]
        p.text = code
        p.font.name = FONT_TITLE
        p.font.size = Pt(14)
        p.font.bold = True
        p.font.color.rgb = C_WHITE
        p.alignment = PP_ALIGN.CENTER

        # Content
        tb = s4.shapes.add_textbox(Inches(1.9), Inches(top_y + 0.1), Inches(9.0), Inches(0.75))
        tf = tb.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
        p_t = tf.paragraphs[0]
        p_t.text = title
        p_t.font.name = FONT_TITLE
        p_t.font.size = Pt(13.5)
        p_t.font.bold = True
        p_t.font.color.rgb = C_WHITE
        
        p_d = tf.add_paragraph()
        p_d.text = desc
        p_d.font.name = FONT_BODY
        p_d.font.size = Pt(11.5)
        p_d.font.color.rgb = C_TEXT_SUB

        # Status
        stat_box = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(11.1), Inches(top_y + 0.25), Inches(1.2), Inches(0.45))
        stat_box.fill.solid()
        stat_box.fill.fore_color.rgb = RGBColor(20, 30, 48)
        stat_box.line.color.rgb = col
        stat_box.line.width = Pt(1)
        p = stat_box.text_frame.paragraphs[0]
        p.text = status
        p.font.name = FONT_TITLE
        p.font.size = Pt(10)
        p.font.bold = True
        p.font.color.rgb = col
        p.alignment = PP_ALIGN.CENTER

        top_y += 1.05

    # ==========================================
    # SLIDE 5: PHÁC THẢO AI
    # ==========================================
    s5 = prs.slides.add_slide(blank_layout)
    add_header(s5, "04. Trí Tuệ Nhân Tạo", "Phác Thảo Thiết Kế AI & Prompt Engineering", "Quy trình sinh câu hỏi trắc nghiệm tự động có kiểm soát bởi con người (Human-in-the-Loop).")

    add_card(s5, Inches(0.8), Inches(1.8), Inches(5.7), Inches(4.0), "🤖 Cấu Hình & Prompt Engineering", C_CYAN_LIGHT)
    tb = s5.shapes.add_textbox(Inches(1.05), Inches(2.4), Inches(5.2), Inches(3.2))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
    ai_points = [
        "Mô hình sử dụng: Google Gemini 3.8 Flash (Tối ưu hóa độ trễ và chi phí gọi API).",
        "System Instruction JSON: Bắt buộc mô hình chỉ trả về định dạng JSON thuần túy, tuyệt đối không bọc trong markdown (```json).",
        "Cấu trúc mỗi câu hỏi: QuestionText, 4 Options (A, B, C, D), IsCorrect (duy nhất 1 đáp án đúng), Explanation (lời giải chi tiết) và Difficulty.",
        "Hỗ trợ 2 kiểu đầu vào: Sinh theo Chủ đề (Topic) hoặc trích xuất từ Đoạn văn bản bài học (Raw Text dài tối đa 15.000 ký tự)."
    ]
    for pt in ai_points:
        p = tf.add_paragraph() if tf.paragraphs[0].text else tf.paragraphs[0]
        p.text = "• " + pt
        p.font.name = FONT_BODY
        p.font.size = Pt(12.5)
        p.font.color.rgb = C_TEXT_SUB
        p.space_after = Pt(8)

    add_card(s5, Inches(6.8), Inches(1.8), Inches(5.7), Inches(4.0), "🛡️ Quy Trình Phê Duyệt (Human-in-the-Loop)", C_GREEN)
    tb = s5.shapes.add_textbox(Inches(7.05), Inches(2.4), Inches(5.2), Inches(3.2))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
    flow_steps = [
        "Bước 1: Giáo viên gửi yêu cầu sinh câu hỏi (POST /api/ai/generate).",
        "Bước 2: Backend gọi Gemini API qua HTTPS POST; nhận chuỗi JSON.",
        "Bước 3: Parse và Validate: Kiểm tra đúng 4 đáp án và duy nhất 1 đáp án đúng.",
        "Bước 4: Lưu vào CSDL với trạng thái PENDING (Chưa xuất hiện trong đề thi).",
        "Bước 5: Giáo viên xem xét, sửa nội dung nếu cần và duyệt (APPROVED) để chính thức mở cho học sinh thi."
    ]
    for pt in flow_steps:
        p = tf.add_paragraph() if tf.paragraphs[0].text else tf.paragraphs[0]
        p.text = pt
        p.font.name = FONT_BODY
        p.font.size = Pt(12.5)
        p.font.color.rgb = C_TEXT_SUB
        p.space_after = Pt(8)

    add_card(s5, Inches(0.8), Inches(6.0), Inches(11.733), Inches(0.95), "⚡ Cơ Chế Xử Lý Lỗi Mạng & Rate Limit (Exponential Backoff)", C_AMBER)
    tb = s5.shapes.add_textbox(Inches(1.05), Inches(6.4), Inches(11.2), Inches(0.5))
    tb.text_frame.word_wrap = True
    tb.text_frame.margin_left = tb.text_frame.margin_top = tb.text_frame.margin_right = tb.text_frame.margin_bottom = 0
    p = tb.text_frame.paragraphs[0]
    p.text = "Khi gặp sự cố mạng hoặc mã lỗi HTTP 429 (Too Many Requests) / 503 (Service Unavailable) từ Google API, hệ thống tự động Retry tối đa 3 lần với thời gian chờ tăng lũy tiến (2s → 4s) trước khi thông báo lỗi, bảo vệ hệ thống không bị crash."
    p.font.name = FONT_BODY
    p.font.size = Pt(12)
    p.font.color.rgb = C_WHITE

    # ==========================================
    # SLIDE 6: CHỨC NĂNG HỆ THỐNG
    # ==========================================
    s6 = prs.slides.add_slide(blank_layout)
    add_header(s6, "05. Tính Năng Sản Phẩm", "Các Chức Năng Chính Của Hệ Thống", "Xây dựng trọn vẹn theo 3 nhóm vai trò người dùng (Role-Based Access Control).")

    add_card(s6, Inches(0.8), Inches(1.8), Inches(3.7), Inches(5.1), "🎓 Dành Cho Học Sinh", C_CYAN_LIGHT)
    tb = s6.shapes.add_textbox(Inches(1.05), Inches(2.4), Inches(3.2), Inches(4.3))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
    pts = [
        "Đăng ký tài khoản & Đăng nhập bảo mật.",
        "Tra cứu danh sách đề thi theo môn học.",
        "Làm bài thi trực tuyến với đồng hồ đếm ngược.",
        "Tự động nộp bài khi hết giờ quy định.",
        "Xem kết quả tức thời, phổ điểm & lời giải thích chi tiết cho từng câu.",
        "Tra cứu lịch sử các bài thi đã hoàn thành."
    ]
    for pt in pts:
        p = tf.add_paragraph() if tf.paragraphs[0].text else tf.paragraphs[0]
        p.text = "• " + pt
        p.font.name = FONT_BODY
        p.font.size = Pt(12.5)
        p.font.color.rgb = C_TEXT_SUB
        p.space_after = Pt(8)

    add_card(s6, Inches(4.8), Inches(1.8), Inches(3.7), Inches(5.1), "👨‍🏫 Dành Cho Giáo Viên", C_PRIMARY_LIGHT)
    tb = s6.shapes.add_textbox(Inches(5.05), Inches(2.4), Inches(3.2), Inches(4.3))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
    pts = [
        "Quản lý đề thi: Tạo mới, chỉnh sửa, xóa đề thi.",
        "Quản lý vòng đời đề thi: DRAFT → PUBLISHED → ARCHIVED.",
        "Sinh câu hỏi tự động bằng AI (Google Gemini).",
        "Kiểm duyệt / Chỉnh sửa / Phê duyệt câu hỏi AI.",
        "Thêm câu hỏi thủ công truyền thống.",
        "Xem thống kê điểm trung bình, tỷ lệ đạt của từng đề thi."
    ]
    for pt in pts:
        p = tf.add_paragraph() if tf.paragraphs[0].text else tf.paragraphs[0]
        p.text = "• " + pt
        p.font.name = FONT_BODY
        p.font.size = Pt(12.5)
        p.font.color.rgb = C_TEXT_SUB
        p.space_after = Pt(8)

    add_card(s6, Inches(8.8), Inches(1.8), Inches(3.7), Inches(5.1), "⚙️ Quản Trị Viên (Admin)", C_PINK)
    tb = s6.shapes.add_textbox(Inches(9.05), Inches(2.4), Inches(3.2), Inches(4.3))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
    pts = [
        "Toàn quyền quản lý ngân hàng đề thi toàn trường.",
        "Quản lý danh sách người dùng (Khóa / Mở khóa tài khoản).",
        "Phân quyền hệ thống: STUDENT, TEACHER, ADMIN.",
        "Giám sát nhật ký gọi AI (AIGenerationLogs).",
        "Theo dõi toàn bộ danh sách bài thi đã nộp của các lớp.",
        "Báo cáo thống kê hiệu suất hệ thống."
    ]
    for pt in pts:
        p = tf.add_paragraph() if tf.paragraphs[0].text else tf.paragraphs[0]
        p.text = "• " + pt
        p.font.name = FONT_BODY
        p.font.size = Pt(12.5)
        p.font.color.rgb = C_TEXT_SUB
        p.space_after = Pt(8)

    # ==========================================
    # SLIDE 7: CÔNG NGHỆ SỬ DỤNG
    # ==========================================
    s7 = prs.slides.add_slide(blank_layout)
    add_header(s7, "06. Công Nghệ & Kỹ Thuật", "Ngăn Xếp Công Nghệ Sử Dụng (Technology Stack)", "Sự kết hợp giữa nền tảng Microsoft .NET mạnh mẽ và hệ sinh thái React hiện đại.")

    add_card(s7, Inches(0.8), Inches(1.8), Inches(5.7), Inches(3.9), "🖥️ Backend: ASP.NET Core 9.0 Web API", C_PRIMARY_LIGHT)
    tb = s7.shapes.add_textbox(Inches(1.05), Inches(2.4), Inches(5.2), Inches(3.1))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
    pts = [
        "Framework: ASP.NET Core Web API (.NET 9.0) – Xử lý I/O mạng hiệu năng cao.",
        "ORM & Database: Entity Framework Core 9.0 + SQL Server LocalDB (7 bảng dữ liệu quan hệ chặt chẽ).",
        "Bảo mật: JWT Bearer Token xác thực & BCrypt.Net mã hóa mật khẩu kèm Salt.",
        "HTTP Client: IHttpClientFactory cấu hình tối ưu kết nối gọi Google Gemini API.",
        "Tài liệu API: Swagger / OpenAPI UI tự động sinh tài liệu chuẩn hóa."
    ]
    for pt in pts:
        p = tf.add_paragraph() if tf.paragraphs[0].text else tf.paragraphs[0]
        p.text = "• " + pt
        p.font.name = FONT_BODY
        p.font.size = Pt(12.5)
        p.font.color.rgb = C_TEXT_SUB
        p.space_after = Pt(7)

    add_card(s7, Inches(6.8), Inches(1.8), Inches(5.7), Inches(3.9), "🌐 Frontend: React 19 + Vite 8", C_CYAN_LIGHT)
    tb = s7.shapes.add_textbox(Inches(7.05), Inches(2.4), Inches(5.2), Inches(3.1))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
    pts = [
        "Thư viện UI & Build Tool: React 19 kết hợp Vite 8 (Hot Module Replacement siêu tốc).",
        "Styling: Tailwind CSS 3.4 thiết kế giao diện Dark Mode cao cấp, hiện đại.",
        "Định tuyến SPA: React Router DOM v7 với cơ chế bảo vệ Route (Protected Routes theo vai trò).",
        "HTTP Client: Axios kèm Interceptor tự động đính kèm Token JWT vào Header.",
        "UI Feedback: Lucide React icon hiện đại và React Hot Toast thông báo trạng thái."
    ]
    for pt in pts:
        p = tf.add_paragraph() if tf.paragraphs[0].text else tf.paragraphs[0]
        p.text = "• " + pt
        p.font.name = FONT_BODY
        p.font.size = Pt(12.5)
        p.font.color.rgb = C_TEXT_SUB
        p.space_after = Pt(7)

    # 3 highlight cards below
    cards_data = [
        ("Google Gemini AI", "Model: gemini-3.8-flash\nSinh đề tự động thông minh", C_CYAN_LIGHT),
        ("Bảo Mật Kép Mạng", "JWT Claims + BCrypt\nChống giả mạo & rò rỉ", C_PRIMARY_LIGHT),
        ("Kiến Trúc Tách Rời", "Decoupled SPA & API\nDễ mở rộng sang Mobile App", C_GREEN)
    ]
    left_x = 0.8
    for title, desc, col in cards_data:
        add_card(s7, Inches(left_x), Inches(5.9), Inches(3.7), Inches(1.1), title, col)
        tb = s7.shapes.add_textbox(Inches(left_x + 0.25), Inches(6.35), Inches(3.2), Inches(0.6))
        tb.text_frame.word_wrap = True
        tb.text_frame.margin_left = tb.text_frame.margin_top = tb.text_frame.margin_right = tb.text_frame.margin_bottom = 0
        p = tb.text_frame.paragraphs[0]
        p.text = desc
        p.font.name = FONT_BODY
        p.font.size = Pt(11)
        p.font.color.rgb = C_TEXT_SUB
        left_x += 4.0

    # ==========================================
    # SLIDE 8: KIẾN TRÚC HỆ THỐNG
    # ==========================================
    s8 = prs.slides.add_slide(blank_layout)
    add_header(s8, "07. Kiến Trúc Mạng", "Kiến Trúc Hệ Thống Tổng Thể (3-Tier Architecture)", "Mô hình phân tầng Client - Server phân tán bảo đảm tính độc lập và mở rộng cao.")

    # Tier 1
    add_card(s8, Inches(1.2), Inches(1.8), Inches(10.933), Inches(1.2), "TẦNG 1: CLIENT TIER (React SPA – Port 5173)", C_CYAN_LIGHT)
    tb = s8.shapes.add_textbox(Inches(1.45), Inches(2.3), Inches(10.4), Inches(0.6))
    tb.text_frame.word_wrap = True
    tb.text_frame.margin_left = tb.text_frame.margin_top = tb.text_frame.margin_right = tb.text_frame.margin_bottom = 0
    p = tb.text_frame.paragraphs[0]
    p.text = "Trình duyệt người dùng: Học sinh làm bài thi đếm ngược • Giáo viên quản lý đề & duyệt câu hỏi • Admin xem thống kê\nThực hiện gọi API qua giao thức HTTP REST (JSON) + Header: Authorization: Bearer <Token>"
    p.font.name = FONT_BODY
    p.font.size = Pt(12)
    p.font.color.rgb = C_TEXT_SUB

    # Tier 2
    add_card(s8, Inches(1.2), Inches(3.3), Inches(10.933), Inches(1.6), "TẦNG 2: SERVER TIER (ASP.NET Core Web API – Port 5000)", C_PRIMARY_LIGHT)
    tb = s8.shapes.add_textbox(Inches(1.45), Inches(3.8), Inches(10.4), Inches(1.0))
    tb.text_frame.word_wrap = True
    tb.text_frame.margin_left = tb.text_frame.margin_top = tb.text_frame.margin_right = tb.text_frame.margin_bottom = 0
    pts = [
        "Controllers: AuthController, ExamsController, AIController, SubmissionsController, AdminController.",
        "Service Layer: AuthService (xác thực JWT), ExamService (CRUD đề thi), QuizService (chấm điểm), AIService (gọi Gemini).",
        "Data Access Layer: Entity Framework Core 9.0 DbContext, cấu hình quan hệ khóa ngoại và chỉ mục tìm kiếm."
    ]
    for pt in pts:
        p = tb.text_frame.add_paragraph() if tb.text_frame.paragraphs[0].text else tb.text_frame.paragraphs[0]
        p.text = "• " + pt
        p.font.name = FONT_BODY
        p.font.size = Pt(12)
        p.font.color.rgb = C_TEXT_SUB

    # Tier 3
    add_card(s8, Inches(1.2), Inches(5.2), Inches(5.3), Inches(1.7), "TẦNG 3A: DATABASE TIER", C_GREEN)
    tb = s8.shapes.add_textbox(Inches(1.45), Inches(5.7), Inches(4.8), Inches(1.1))
    tb.text_frame.word_wrap = True
    tb.text_frame.margin_left = tb.text_frame.margin_top = tb.text_frame.margin_right = tb.text_frame.margin_bottom = 0
    p = tb.text_frame.paragraphs[0]
    p.text = "SQL Server LocalDB (QuizSystemDB):\n7 bảng quan hệ: Users, Exams, Questions, Options, Submissions, SubmissionDetails, AIGenerationLogs."
    p.font.name = FONT_BODY
    p.font.size = Pt(12)
    p.font.color.rgb = C_TEXT_SUB

    add_card(s8, Inches(6.8), Inches(5.2), Inches(5.3), Inches(1.7), "TẦNG 3B: EXTERNAL AI CLOUD", C_PINK)
    tb = s8.shapes.add_textbox(Inches(7.05), Inches(5.7), Inches(4.8), Inches(1.1))
    tb.text_frame.word_wrap = True
    tb.text_frame.margin_left = tb.text_frame.margin_top = tb.text_frame.margin_right = tb.text_frame.margin_bottom = 0
    p = tb.text_frame.paragraphs[0]
    p.text = "Google Gemini AI API:\nKết nối qua HTTPS REST Endpoint (generativelanguage.googleapis.com) sử dụng model gemini-3.8-flash."
    p.font.name = FONT_BODY
    p.font.size = Pt(12)
    p.font.color.rgb = C_TEXT_SUB

    # ==========================================
    # SLIDE 9: GIAO THỨC MẠNG TRONG HỆ THỐNG
    # ==========================================
    s9 = prs.slides.add_slide(blank_layout)
    add_header(s9, "08. Giao Thức Mạng", "Các Giao Thức Mạng Áp Dụng (Mô Hình TCP/IP)", "Phân tầng mạng và cơ chế vận chuyển gói tin từ người dùng đến hạ tầng máy chủ.")

    add_card(s9, Inches(0.8), Inches(1.8), Inches(5.7), Inches(5.1), "📦 Phân Tầng Giao Thức TCP/IP", C_CYAN_LIGHT)
    tb = s9.shapes.add_textbox(Inches(1.05), Inches(2.4), Inches(5.2), Inches(4.3))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
    pts = [
        "Tầng Ứng Dụng (Application Layer):\n• Giao thức HTTP / HTTPS: Truyền tải các payload JSON RESTful API giữa React và ASP.NET Core.\n• DNS (Domain Name System): Phân giải tên miền khi gọi Google Gemini API.",
        "Tầng Truyền Vận (Transport Layer):\n• Giao thức TCP (Transmission Control Protocol): Đảm bảo truyền tin tin cậy, không mất gói khi nộp bài thi.",
        "Tầng Mạng (Network / Internet Layer):\n• Giao thức IP (IPv4 / IPv6): Đóng gói và định tuyến các gói tin qua các router trên môi trường mạng.",
        "Tầng Truy Cập Mạng (Network Access Layer):\n• Ethernet / Wi-Fi (802.11): Truyền tín hiệu vật lý."
    ]
    for pt in pts:
        p = tf.add_paragraph() if tf.paragraphs[0].text else tf.paragraphs[0]
        p.text = pt
        p.font.name = FONT_BODY
        p.font.size = Pt(12)
        p.font.color.rgb = C_TEXT_SUB
        p.space_after = Pt(10)

    add_card(s9, Inches(6.8), Inches(1.8), Inches(5.7), Inches(5.1), "🤝 Tại Sao Bắt Buộc Dùng TCP Thay Vì UDP?", C_GREEN)
    tb = s9.shapes.add_textbox(Inches(7.05), Inches(2.4), Inches(5.2), Inches(4.3))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
    pts = [
        "Tính toàn vẹn tuyệt đối: Trong bài thi trắc nghiệm, mất dù chỉ 1 câu trả lời sẽ làm sai lệch kết quả điểm số. UDP không bảo đảm mất gói, do đó không thể sử dụng.",
        "Bảo đảm thứ tự (In-Order Delivery): TCP đánh số thứ tự (Sequence Number) cho từng gói tin, bảo đảm dữ liệu nộp bài được ghép nối chính xác.",
        "Cơ chế báo nhận (ACK) & Phát lại (Retransmission): Nếu gói tin bị rớt trên đường truyền, TCP tự động gửi lại.",
        "Bắt tay 3 bước (TCP 3-Way Handshake):\n• Bước 1: Client gửi SYN (seq = x)\n• Bước 2: Server trả lời SYN-ACK (seq = y, ack = x+1)\n• Bước 3: Client gửi ACK (ack = y+1) → Kết nối ESTABLISHED sẵn sàng truyền dữ liệu."
    ]
    for pt in pts:
        p = tf.add_paragraph() if tf.paragraphs[0].text else tf.paragraphs[0]
        p.text = "• " + pt
        p.font.name = FONT_BODY
        p.font.size = Pt(12)
        p.font.color.rgb = C_TEXT_SUB
        p.space_after = Pt(8)

    # ==========================================
    # SLIDE 10: WEB PROTOCOL & RESTFUL API
    # ==========================================
    s10 = prs.slides.add_slide(blank_layout)
    add_header(s10, "09. Web Protocol", "Giao Thức Web & Cơ Chế Hoạt Động RESTful API", "Cấu trúc thông điệp HTTP Request / Response và nguyên lý truyền thông không trạng thái.")

    add_card(s10, Inches(0.8), Inches(1.8), Inches(5.7), Inches(5.1), "📬 Cấu Trúc Thông Điệp HTTP", C_PRIMARY_LIGHT)
    tb = s10.shapes.add_textbox(Inches(1.05), Inches(2.4), Inches(5.2), Inches(4.3))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
    pts = [
        "1. HTTP Request Line:\nPOST /api/submissions/submit HTTP/1.1",
        "2. HTTP Headers:\nHost: localhost:5000\nAuthorization: Bearer <JWT_TOKEN>\nContent-Type: application/json",
        "3. HTTP Message Body:\n{\n  \"submissionId\": 15,\n  \"answers\": [{ \"questionId\": 42, \"selectedOptionId\": 168 }]\n}",
        "4. HTTP Response:\nHTTP/1.1 200 OK\nContent-Type: application/json\n{ \"totalScore\": 90.0, \"status\": \"COMPLETED\" }"
    ]
    for pt in pts:
        p = tf.add_paragraph() if tf.paragraphs[0].text else tf.paragraphs[0]
        p.text = pt
        p.font.name = FONT_MONO
        p.font.size = Pt(11.5)
        p.font.color.rgb = C_CYAN_LIGHT if "HTTP" in pt else C_TEXT_SUB
        p.space_after = Pt(10)

    add_card(s10, Inches(6.8), Inches(1.8), Inches(5.7), Inches(5.1), "📑 Phương Thức & Mã Trạng Thái Chuẩn", C_CYAN_LIGHT)
    tb = s10.shapes.add_textbox(Inches(7.05), Inches(2.4), Inches(5.2), Inches(4.3))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
    pts = [
        "Các phương thức HTTP (HTTP Verbs):\n• GET: Lấy danh sách đề thi, kết quả thi (an toàn, chỉ đọc).\n• POST: Tạo tài khoản, đăng nhập, nộp bài, sinh đề AI.\n• PATCH: Cập nhật từng phần (duyệt câu hỏi, publish đề thi).\n• DELETE: Xóa đề thi rác khỏi hệ thống.",
        "Mã trạng thái chuẩn (HTTP Status Codes):\n• 200 OK: Xử lý thành công yêu cầu.\n• 201 Created: Tạo mới đề thi/tài khoản thành công.\n• 401 Unauthorized: Chưa đăng nhập hoặc Token hết hạn.\n• 403 Forbidden: Không đủ quyền hạn (vd: Student cố gọi API Admin).\n• 500 Internal Error: Lỗi ngoại lệ phía máy chủ.",
        "Nguyên lý Stateless:\nMỗi HTTP request độc lập hoàn toàn, máy chủ không lưu session trong RAM mà trích xuất danh tính từ JWT Token."
    ]
    for pt in pts:
        p = tf.add_paragraph() if tf.paragraphs[0].text else tf.paragraphs[0]
        p.text = pt
        p.font.name = FONT_BODY
        p.font.size = Pt(12)
        p.font.color.rgb = C_TEXT_SUB
        p.space_after = Pt(8)

    # ==========================================
    # SLIDE 11: HTTPS & CƠ CHẾ HOẠT ĐỘNG
    # ==========================================
    s11 = prs.slides.add_slide(blank_layout)
    add_header(s11, "10. An Ninh Mạng", "HTTPS: Cơ Chế Hoạt Động & Bảo Mật TLS/SSL", "Bảo vệ dữ liệu đề thi và thông tin đăng nhập trước các nguy cơ tấn công mạng.")

    add_card(s11, Inches(0.8), Inches(1.8), Inches(5.7), Inches(5.1), "🔐 Bản Chất Của HTTPS (HTTP over TLS)", C_GREEN)
    tb = s11.shapes.add_textbox(Inches(1.05), Inches(2.4), Inches(5.2), Inches(4.3))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
    pts = [
        "Định nghĩa: HTTPS là giao thức HTTP chạy trên nền tầng bảo mật TLS (Transport Layer Security) tại cổng mặc định 443.",
        "3 Mục tiêu an ninh cốt lõi (CIA Triad):\n1. Confidentiality (Tính bí mật): Mã hóa dữ liệu truyền tải, chống nghe lén (Sniffing) qua Wireshark trong mạng LAN/Wi-Fi.\n2. Integrity (Tính toàn vẹn): Dùng mã băm MAC (Message Authentication Code) phát hiện nếu dữ liệu bài thi bị sửa đổi trên đường truyền.\n3. Authentication (Xác thực danh tính): Chứng chỉ số SSL/TLS do cơ quan CA chứng thực, chống tấn công giả mạo máy chủ (Man-in-the-Middle - MitM)."
    ]
    for pt in pts:
        p = tf.add_paragraph() if tf.paragraphs[0].text else tf.paragraphs[0]
        p.text = pt
        p.font.name = FONT_BODY
        p.font.size = Pt(12.5)
        p.font.color.rgb = C_TEXT_SUB
        p.space_after = Pt(12)

    add_card(s11, Inches(6.8), Inches(1.8), Inches(5.7), Inches(5.1), "⚡ Quy Trình Bắt Tay TLS Handshake", C_PINK)
    tb = s11.shapes.add_textbox(Inches(7.05), Inches(2.4), Inches(5.2), Inches(4.3))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
    pts = [
        "1. Client Hello:\nClient gửi phiên bản TLS hỗ trợ, chuỗi ngẫu nhiên (Client Random) và danh sách bộ thuật toán mã hóa (Cipher Suites).",
        "2. Server Hello & Certificate:\nServer chọn bộ mã hóa phù hợp, gửi Server Random và gửi Chứng chỉ số SSL (chứa Khóa công khai - Public Key).",
        "3. Key Exchange (Trao đổi khóa bí mật):\nClient xác thực chứng chỉ với CA; tạo Pre-Master Secret và mã hóa bằng Public Key của Server gửi đi.",
        "4. Thiết lập Khóa Phiên (Session Key):\nCả 2 bên dùng thuật toán băm tạo Session Key chung (AES-256).",
        "5. Mã hóa đối xứng dữ liệu:\nSau khi bắt tay hoàn tất, mọi gói tin HTTP đều được mã hóa đối xứng AES tốc độ cao."
    ]
    for pt in pts:
        p = tf.add_paragraph() if tf.paragraphs[0].text else tf.paragraphs[0]
        p.text = pt
        p.font.name = FONT_BODY
        p.font.size = Pt(12)
        p.font.color.rgb = C_TEXT_SUB
        p.space_after = Pt(8)

    # ==========================================
    # SLIDE 12: BẢO MẬT XÁC THỰC JWT & CORS
    # ==========================================
    s12 = prs.slides.add_slide(blank_layout)
    add_header(s12, "11. Xác Thực & Kiểm Soát Truy Cập", "Cơ Chế Xác Thực JWT & Chính Sách Mạng CORS", "Bảo vệ tài nguyên API thông qua cơ chế chữ ký số không trạng thái (Stateless Token).")

    add_card(s12, Inches(0.8), Inches(1.8), Inches(5.7), Inches(5.1), "🎫 Cấu Trúc & Cơ Chế Xác Thực JWT", C_CYAN_LIGHT)
    tb = s12.shapes.add_textbox(Inches(1.05), Inches(2.4), Inches(5.2), Inches(4.3))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
    pts = [
        "Cấu trúc 3 phần ngăn cách bởi dấu chấm:\n• Header: { \"alg\": \"HS256\", \"typ\": \"JWT\" }\n• Payload: { \"nameid\": \"1\", \"role\": \"TEACHER\", \"exp\": 1730000 }\n• Signature: HMAC-SHA256(Header + Payload, SecretKey)",
        "Ưu điểm mạng vượt trội:\n• Không trạng thái (Stateless): Server giải mã vai trò và ID của user trực tiếp từ Token mà không cần query Database.\n• Giảm tải băng thông và tải truy vấn CSDL đáng kể.\n• Token có hạn sử dụng 24h, bảo vệ tài nguyên an toàn.",
        "Mã hóa mật khẩu BCrypt:\nMật khẩu được băm một chiều với chuỗi muối (Salt) ngẫu nhiên, chống lại tấn công Rainbow Table."
    ]
    for pt in pts:
        p = tf.add_paragraph() if tf.paragraphs[0].text else tf.paragraphs[0]
        p.text = pt
        p.font.name = FONT_BODY
        p.font.size = Pt(12)
        p.font.color.rgb = C_TEXT_SUB
        p.space_after = Pt(10)

    add_card(s12, Inches(6.8), Inches(1.8), Inches(5.7), Inches(5.1), "🛡️ Giải Quyết CORS & Reverse Proxy", C_AMBER)
    tb = s12.shapes.add_textbox(Inches(7.05), Inches(2.4), Inches(5.2), Inches(4.3))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
    pts = [
        "Vấn đề mạng (Cross-Origin Resource Sharing):\nTrình duyệt thực thi chính sách bảo mật Same-Origin Policy, chặn các yêu cầu JavaScript giữa 2 nguồn khác port: React (5173) và ASP.NET Core (5000).",
        "Giải pháp 1: CORS Middleware (ASP.NET Core):\nCấu hình builder.Services.AddCors() cấp phép rõ ràng cho Origin http://localhost:5173, cho phép các HTTP Header và Method cần thiết.",
        "Giải pháp 2: Vite Reverse Proxy (Triển khai chính):\nCấu hình proxy trong vite.config.js: Mọi request /api/* gửi từ React được proxy tự động chuyển tiếp nội bộ sang http://localhost:5000, triệt tiêu hoàn toàn lỗi CORS và che giấu địa chỉ máy chủ backend."
    ]
    for pt in pts:
        p = tf.add_paragraph() if tf.paragraphs[0].text else tf.paragraphs[0]
        p.text = pt
        p.font.name = FONT_BODY
        p.font.size = Pt(12)
        p.font.color.rgb = C_TEXT_SUB
        p.space_after = Pt(10)

    # ==========================================
    # SLIDE 13: LUỒNG DỮ LIỆU - XÁC THỰC ĐĂNG NHẬP
    # ==========================================
    s13 = prs.slides.add_slide(blank_layout)
    add_header(s13, "12. Luồng Dữ Liệu (Data Flow)", "Luồng Dữ Liệu 1: Đăng Nhập & Xác Thực Tài Khoản", "Sơ đồ tuần tự các bước truyền tin từ khi người dùng nhập tài khoản đến khi cấp phát Token.")

    steps_auth = [
        ("Bước 1", "Client gửi yêu cầu đăng nhập", "React gửi HTTP POST /api/auth/login mang body JSON { username, password } qua kết nối TCP tới Backend API.", C_CYAN_LIGHT),
        ("Bước 2", "Server truy vấn & Đối soát mật khẩu", "AuthController chuyển tiếp tới AuthService; truy vấn SQL Server tìm User; dùng BCrypt.Verify() so khớp mật khẩu người dùng nhập với hash trong CSDL.", C_PRIMARY_LIGHT),
        ("Bước 3", "Ký số JWT Token & Phản hồi", "AuthService sinh chuỗi JWT chứa các Claims (UserId, Role, Username) có hạn dùng 24 giờ; trả về HTTP 200 OK kèm Token cho Client.", C_GREEN),
        ("Bước 4", "Lưu trữ Token & Đính kèm Header", "React lưu Token vào localStorage; Axios Interceptor tự động gán Header Authorization: Bearer <Token> vào mọi HTTP request sau đó.", C_AMBER)
    ]

    top_y = 1.8
    for st_num, st_title, st_desc, col in steps_auth:
        add_card(s13, Inches(0.8), Inches(top_y), Inches(11.733), Inches(1.15), "", bg_color=C_CARD)
        
        # Num Badge
        badge = s13.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.1), Inches(top_y + 0.2), Inches(1.1), Inches(0.75))
        badge.fill.solid()
        badge.fill.fore_color.rgb = col
        badge.line.fill.background()
        p = badge.text_frame.paragraphs[0]
        p.text = st_num
        p.font.name = FONT_TITLE
        p.font.size = Pt(14)
        p.font.bold = True
        p.font.color.rgb = C_WHITE
        p.alignment = PP_ALIGN.CENTER

        # Content
        tb = s13.shapes.add_textbox(Inches(2.4), Inches(top_y + 0.15), Inches(9.8), Inches(0.85))
        tf = tb.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
        p_t = tf.paragraphs[0]
        p_t.text = st_title
        p_t.font.name = FONT_TITLE
        p_t.font.size = Pt(14)
        p_t.font.bold = True
        p_t.font.color.rgb = C_WHITE

        p_d = tf.add_paragraph()
        p_d.text = st_desc
        p_d.font.name = FONT_BODY
        p_d.font.size = Pt(12)
        p_d.font.color.rgb = C_TEXT_SUB

        top_y += 1.3

    # ==========================================
    # SLIDE 14: LUỒNG DỮ LIỆU - SINH CÂU HỎI AI
    # ==========================================
    s14 = prs.slides.add_slide(blank_layout)
    add_header(s14, "13. Luồng Dữ Liệu (Data Flow)", "Luồng Dữ Liệu 2: Tự Động Sinh Câu Hỏi Bằng AI", "Quy trình gọi API bên thứ ba (External REST Service) tích hợp kiểm duyệt chất lượng.")

    steps_ai = [
        ("Bước 1", "Giáo viên gửi yêu cầu sinh câu hỏi", "Client gửi POST /api/ai/generate kèm Token JWT; mang payload gồm chủ đề hoặc văn bản bài giảng, số lượng câu và độ khó.", C_CYAN_LIGHT),
        ("Bước 2", "Backend gọi Google Gemini API qua HTTPS", "AIService đóng gói Prompt có System Instructions JSON; dùng HttpClientFactory thực hiện HTTPS POST đến generativelanguage.googleapis.com (có cơ chế Retry).", C_PRIMARY_LIGHT),
        ("Bước 3", "Parse JSON, Validate & Lưu CSDL PENDING", "Backend bóc tách chuỗi JSON trả về; kiểm tra đủ 4 phương án A/B/C/D; lưu câu hỏi vào DB với trạng thái PENDING và ghi log vào AIGenerationLogs.", C_PINK),
        ("Bước 4", "Kiểm duyệt & Công bố đề thi (Approval)", "Giáo viên tra cứu danh sách câu hỏi chờ duyệt; gửi PATCH /api/exams/questions/{id}/approve để chính thức đưa câu hỏi vào đề thi cho học sinh làm bài.", C_GREEN)
    ]

    top_y = 1.8
    for st_num, st_title, st_desc, col in steps_ai:
        add_card(s14, Inches(0.8), Inches(top_y), Inches(11.733), Inches(1.15), "", bg_color=C_CARD)
        
        # Num Badge
        badge = s14.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.1), Inches(top_y + 0.2), Inches(1.1), Inches(0.75))
        badge.fill.solid()
        badge.fill.fore_color.rgb = col
        badge.line.fill.background()
        p = badge.text_frame.paragraphs[0]
        p.text = st_num
        p.font.name = FONT_TITLE
        p.font.size = Pt(14)
        p.font.bold = True
        p.font.color.rgb = C_WHITE
        p.alignment = PP_ALIGN.CENTER

        # Content
        tb = s14.shapes.add_textbox(Inches(2.4), Inches(top_y + 0.15), Inches(9.8), Inches(0.85))
        tf = tb.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
        p_t = tf.paragraphs[0]
        p_t.text = st_title
        p_t.font.name = FONT_TITLE
        p_t.font.size = Pt(14)
        p_t.font.bold = True
        p_t.font.color.rgb = C_WHITE

        p_d = tf.add_paragraph()
        p_d.text = st_desc
        p_d.font.name = FONT_BODY
        p_d.font.size = Pt(12)
        p_d.font.color.rgb = C_TEXT_SUB

        top_y += 1.3

    # ==========================================
    # SLIDE 15: LUỒNG DỮ LIỆU - LÀM BÀI & CHẤM ĐIỂM
    # ==========================================
    s15 = prs.slides.add_slide(blank_layout)
    add_header(s15, "14. Luồng Dữ Liệu (Data Flow)", "Luồng Dữ Liệu 3: Làm Bài Thi & Chấm Điểm Thời Gian Thực", "Cơ chế đồng bộ thời gian máy chủ và xử lý bài nộp tin cậy chống gian lận.")

    add_card(s15, Inches(0.8), Inches(1.8), Inches(5.7), Inches(3.9), "⏱️ Giai Đoạn 1: Bắt Đầu & Đồng Bộ Thời Gian", C_CYAN_LIGHT)
    tb = s15.shapes.add_textbox(Inches(1.05), Inches(2.4), Inches(5.2), Inches(3.1))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
    pts = [
        "Khởi tạo bài thi: Client gửi POST /api/submissions/start kèm ExamId.",
        "Ghi nhận mốc giờ Server (Server Time): Server tạo record Submissions với StartedAt = DateTime.UtcNow và trạng thái IN_PROGRESS.",
        "Chống gian lận giờ: Server tính toán RemainingSeconds gửi về Client. Thời gian làm bài hoàn toàn không phụ thuộc vào đồng hồ trên máy tính cá nhân của học sinh.",
        "Tiếp tục bài dở dang: Nếu học sinh bị rớt mạng, vào lại bài thi sẽ tự động nhận diện bài nộp cũ và trừ đi thời gian đã trôi qua."
    ]
    for pt in pts:
        p = tf.add_paragraph() if tf.paragraphs[0].text else tf.paragraphs[0]
        p.text = "• " + pt
        p.font.name = FONT_BODY
        p.font.size = Pt(12)
        p.font.color.rgb = C_TEXT_SUB
        p.space_after = Pt(6)

    add_card(s15, Inches(6.8), Inches(1.8), Inches(5.7), Inches(3.9), "📊 Giai Đoạn 2: Nộp Bài & Chấm Điểm Tức Thì", C_GREEN)
    tb = s15.shapes.add_textbox(Inches(7.05), Inches(2.4), Inches(5.2), Inches(3.1))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
    pts = [
        "Kích hoạt nộp bài: Khi học sinh nhấn Nộp bài hoặc đồng hồ đếm ngược chạm mốc 00:00 (Tự động trigger).",
        "Gửi gói tin: POST /api/submissions/submit chứa danh sách câu trả lời.",
        "Chấm điểm tự động: Server duyệt từng câu hỏi, đối chiếu IsCorrect trong bảng Options.",
        "Công thức: TotalScore = (Số câu đúng / Tổng số câu) * 100.",
        "Lưu kết quả & Trả về: Cập nhật trạng thái COMPLETED, ghi nhận từng câu đúng/sai vào SubmissionDetails và trả kết quả kèm lời giải thích chi tiết."
    ]
    for pt in pts:
        p = tf.add_paragraph() if tf.paragraphs[0].text else tf.paragraphs[0]
        p.text = "• " + pt
        p.font.name = FONT_BODY
        p.font.size = Pt(12)
        p.font.color.rgb = C_TEXT_SUB
        p.space_after = Pt(6)

    add_card(s15, Inches(0.8), Inches(5.9), Inches(11.733), Inches(1.1), "🛡️ Cơ Chế Xử Lý Lỗi Rớt Mạng (Fault Tolerance)", C_AMBER)
    tb = s15.shapes.add_textbox(Inches(1.05), Inches(6.3), Inches(11.2), Inches(0.6))
    tb.text_frame.word_wrap = True
    tb.text_frame.margin_left = tb.text_frame.margin_top = tb.text_frame.margin_right = tb.text_frame.margin_bottom = 0
    p = tb.text_frame.paragraphs[0]
    p.text = "Mọi bài thi đang dở dang (IN_PROGRESS) quá hạn làm bài sẽ tự động được hệ thống đóng và tính điểm khi học sinh thao tác lại, bảo đảm tính công bằng tuyệt đối cho kỳ thi."
    p.font.name = FONT_BODY
    p.font.size = Pt(12)
    p.font.color.rgb = C_WHITE

    # ==========================================
    # SLIDE 16: KẾT QUẢ ĐẠT ĐƯỢC & DEMO GIAO DIỆN
    # ==========================================
    s16 = prs.slides.add_slide(blank_layout)
    add_header(s16, "15. Thực Nghiệm & Kết Quả", "Kết Quả Đạt Được & Giao Diện Thực Tế", "Hệ thống đã triển khai hoàn chỉnh và vận hành ổn định trên môi trường thực tế.")

    # 4 metrics
    metrics = [
        ("100%", "API RESTful Ổn Định", C_CYAN_LIGHT),
        ("< 150ms", "Thời Gian Đáp Ứng API", C_PRIMARY_LIGHT),
        ("~ 3 giây", "Sinh Câu Hỏi Bằng AI", C_PINK),
        ("3 Cấp", "Phân Quyền RBAC Chặt Chẽ", C_GREEN)
    ]
    left_x = 0.8
    for val, lbl, col in metrics:
        add_card(s16, Inches(left_x), Inches(1.8), Inches(2.7), Inches(1.3), "", bg_color=C_CARD)
        tb = s16.shapes.add_textbox(Inches(left_x + 0.1), Inches(1.95), Inches(2.5), Inches(0.95))
        tf = tb.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
        p1 = tf.paragraphs[0]
        p1.text = val
        p1.font.name = FONT_TITLE
        p1.font.size = Pt(26)
        p1.font.bold = True
        p1.font.color.rgb = col
        p1.alignment = PP_ALIGN.CENTER

        p2 = tf.add_paragraph()
        p2.text = lbl
        p2.font.name = FONT_BODY
        p2.font.size = Pt(11)
        p2.font.color.rgb = C_MUTED
        p2.alignment = PP_ALIGN.CENTER
        left_x += 3.0

    # 3 screen cards
    add_card(s16, Inches(0.8), Inches(3.3), Inches(3.7), Inches(3.6), "🖥️ Màn Hình Làm Bài Thi", C_CYAN_LIGHT)
    tb = s16.shapes.add_textbox(Inches(1.05), Inches(3.9), Inches(3.2), Inches(2.8))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
    p = tf.paragraphs[0]
    p.text = "• Đồng hồ đếm ngược thời gian thực.\n• Bảng điều hướng câu hỏi trực quan.\n• Trạng thái câu đã làm/chưa làm.\n• Cảnh báo xác nhận khi nộp bài.\n• Tự động nộp khi hết thời gian quy định."
    p.font.name = FONT_BODY
    p.font.size = Pt(12)
    p.font.color.rgb = C_TEXT_SUB

    add_card(s16, Inches(4.8), Inches(3.3), Inches(3.7), Inches(3.6), "🤖 Quản Trị AI & Duyệt Đề", C_PRIMARY_LIGHT)
    tb = s16.shapes.add_textbox(Inches(5.05), Inches(3.9), Inches(3.2), Inches(2.8))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
    p = tf.paragraphs[0]
    p.text = "• Form nhập chủ đề/tài liệu sinh câu hỏi.\n• Tùy chọn số lượng câu và cấp độ khó.\n• Bảng danh sách câu hỏi chờ duyệt (Pending).\n• Phê duyệt (Approve) hoặc Từ chối (Reject).\n• Chỉnh sửa nội dung câu hỏi trước khi publish."
    p.font.name = FONT_BODY
    p.font.size = Pt(12)
    p.font.color.rgb = C_TEXT_SUB

    add_card(s16, Inches(8.8), Inches(3.3), Inches(3.7), Inches(3.6), "📈 Thống Kê & Phân Tích Điểm", C_PINK)
    tb = s16.shapes.add_textbox(Inches(9.05), Inches(3.9), Inches(3.2), Inches(2.8))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
    p = tf.paragraphs[0]
    p.text = "• Biểu đồ phổ điểm trực quan của từng đề.\n• Thống kê điểm trung bình, điểm cao/thấp nhất.\n• Tỷ lệ đạt/trượt của học sinh tham gia.\n• Danh sách chi tiết từng bài nộp của thí sinh.\n• Lịch sử làm bài thi cá nhân của từng học sinh."
    p.font.name = FONT_BODY
    p.font.size = Pt(12)
    p.font.color.rgb = C_TEXT_SUB

    # ==========================================
    # SLIDE 17: KẾT LUẬN & ĐỊNH HƯỚNG CUỐI KỲ
    # ==========================================
    s17 = prs.slides.add_slide(blank_layout)
    add_header(s17, "16. Tổng Kết & Tương Lai", "Kết Luận & Định Hướng Phát Triển Cuối Kỳ", "Đánh giá kết quả đạt được giữa kỳ và kế hoạch mở rộng tính năng nâng cao cho cuối kỳ.")

    add_card(s17, Inches(0.8), Inches(1.8), Inches(5.7), Inches(4.3), "✅ Kết Quả Đạt Được (Giữa Kỳ)", C_GREEN)
    tb = s17.shapes.add_textbox(Inches(1.05), Inches(2.4), Inches(5.2), Inches(3.5))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
    pts = [
        "Hoàn thành xuất sắc kiến trúc mạng Client - Server độc lập giữa ASP.NET Core 9 và React 19.",
        "Ứng dụng đầy đủ các kiến thức cốt lõi của môn Lập trình mạng: Giao thức truyền tin TCP tin cậy, mô hình RESTful API, bảo mật HTTPS/TLS, cơ chế xác thực JWT và giải quyết bài toán CORS.",
        "Tích hợp thành công mô hình AI Google Gemini giải quyết bài toán tự động sinh đề thi thực tiễn.",
        "Hệ thống vận hành mượt mà, phân quyền chặt chẽ và xử lý ngoại lệ mạng ổn định."
    ]
    for pt in pts:
        p = tf.add_paragraph() if tf.paragraphs[0].text else tf.paragraphs[0]
        p.text = "• " + pt
        p.font.name = FONT_BODY
        p.font.size = Pt(12.5)
        p.font.color.rgb = C_TEXT_SUB
        p.space_after = Pt(10)

    add_card(s17, Inches(6.8), Inches(1.8), Inches(5.7), Inches(4.3), "🚀 Kế Hoạch Nâng Cấp (Cuối Kỳ)", C_CYAN_LIGHT)
    tb = s17.shapes.add_textbox(Inches(7.05), Inches(2.4), Inches(5.2), Inches(3.5))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
    pts = [
        "Mạng Real-time với WebSocket / SignalR: Giám sát thí sinh trực tiếp theo thời gian thực (real-time proctoring), cảnh báo khi học sinh chuyển tab hoặc rời màn hình thi.",
        "Thi đấu đối kháng trực tiếp (Quiz Battle): Hai hoặc nhiều thí sinh thi đấu trực tiếp qua Socket mạng thời gian thực.",
        "Xuất đề thi ra PDF/Word: Cho phép in ấn đề thi giấy truyền thống khi cần.",
        "Triển khai Cloud & Docker: Đóng gói Docker Container và triển khai lên hạ tầng đám mây (Azure/AWS) với chứng chỉ SSL chính thức."
    ]
    for pt in pts:
        p = tf.add_paragraph() if tf.paragraphs[0].text else tf.paragraphs[0]
        p.text = "• " + pt
        p.font.name = FONT_BODY
        p.font.size = Pt(12.5)
        p.font.color.rgb = C_TEXT_SUB
        p.space_after = Pt(10)

    # Thank you footer
    add_card(s17, Inches(0.8), Inches(6.3), Inches(11.733), Inches(0.75), "", bg_color=C_CARD)
    tb = s17.shapes.add_textbox(Inches(1.0), Inches(6.4), Inches(11.3), Inches(0.55))
    tb.text_frame.word_wrap = True
    tb.text_frame.margin_left = tb.text_frame.margin_top = tb.text_frame.margin_right = tb.text_frame.margin_bottom = 0
    p = tb.text_frame.paragraphs[0]
    p.text = "CẢM ƠN THẦY CÔ VÀ CÁC BẠN ĐÃ LẮNG NGHE! NHÓM SẴN SÀNG TRẢ LỜI CÂU HỎI PHẢN BIỆN."
    p.font.name = FONT_TITLE
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = C_CYAN_LIGHT
    p.alignment = PP_ALIGN.CENTER

    prs.save(output_path)
    print(f"Presentation saved successfully to: {output_path}")

if __name__ == "__main__":
    out_file = sys.argv[1] if len(sys.argv) > 1 else "slide_thuyet_trinh_QuizAI.pptx"
    create_quiz_ai_presentation(out_file)
