import sys
import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

def create_concise_presentation(output_path):
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # Theme Colors (Modern Dark Tech)
    C_BG = RGBColor(11, 15, 25)          # Deep dark
    C_CARD = RGBColor(19, 27, 46)        # Card background
    C_BORDER = RGBColor(40, 53, 84)      # Card border
    C_PRIMARY = RGBColor(99, 102, 241)   # Indigo
    C_CYAN = RGBColor(6, 182, 212)       # Cyan
    C_GREEN = RGBColor(16, 185, 129)     # Emerald
    C_AMBER = RGBColor(245, 158, 11)     # Amber
    C_RED = RGBColor(239, 68, 68)        # Red
    C_WHITE = RGBColor(255, 255, 255)
    C_TEXT_SUB = RGBColor(203, 213, 225) # Slate 300
    C_MUTED = RGBColor(148, 163, 184)    # Slate 400

    FONT_TITLE = "Segoe UI"
    FONT_BODY = "Segoe UI"

    def set_slide_background(slide):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
        bg.fill.solid()
        bg.fill.fore_color.rgb = C_BG
        bg.line.fill.background()

        # Accent top bar
        top_bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, Inches(0.08))
        top_bar.fill.solid()
        top_bar.fill.fore_color.rgb = C_PRIMARY
        top_bar.line.fill.background()

    def add_header(slide, tag_text, title_text, subtitle_text=""):
        set_slide_background(slide)
        txBox = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.733), Inches(1.2))
        tf = txBox.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0

        p_tag = tf.paragraphs[0]
        p_tag.text = tag_text.upper()
        p_tag.font.name = FONT_TITLE
        p_tag.font.size = Pt(11)
        p_tag.font.bold = True
        p_tag.font.color.rgb = C_CYAN
        p_tag.space_after = Pt(2)

        p_title = tf.add_paragraph()
        p_title.text = title_text
        p_title.font.name = FONT_TITLE
        p_title.font.size = Pt(23)
        p_title.font.bold = True
        p_title.font.color.rgb = C_WHITE
        p_title.space_after = Pt(2)

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
            p.font.color.rgb = C_TEXT_SUB
            p.space_after = Pt(8)

    # ==========================================
    # SLIDE 1: TRANG BÌA
    # ==========================================
    s1 = prs.slides.add_slide(blank_layout)
    set_slide_background(s1)

    box = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.5), Inches(1.2), Inches(10.333), Inches(5.1))
    box.fill.solid()
    box.fill.fore_color.rgb = C_CARD
    box.line.color.rgb = C_BORDER
    box.line.width = Pt(1.5)

    txBox = s1.shapes.add_textbox(Inches(1.8), Inches(1.6), Inches(9.733), Inches(4.3))
    tf = txBox.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0

    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.CENTER
    p.text = "ĐỒ ÁN MÔN HỌC • LẬP TRÌNH MẠNG"
    p.font.name = FONT_TITLE
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = C_CYAN
    p.space_after = Pt(14)

    p = tf.add_paragraph()
    p.alignment = PP_ALIGN.CENTER
    p.text = "QuizAI – Hệ Thống Trắc Nghiệm Online\nTích Hợp Trí Tuệ Nhân Tạo & Giám Sát Thi"
    p.font.name = FONT_TITLE
    p.font.size = Pt(30)
    p.font.bold = True
    p.font.color.rgb = C_WHITE
    p.space_after = Pt(16)

    p = tf.add_paragraph()
    p.alignment = PP_ALIGN.CENTER
    p.text = "Client-Server • RESTful API • TCP/IP • Bảo Mật JWT • Chống Gian Lận Đa Tầng"
    p.font.name = FONT_BODY
    p.font.size = Pt(14)
    p.font.color.rgb = C_TEXT_SUB
    p.space_after = Pt(30)

    p = tf.add_paragraph()
    p.alignment = PP_ALIGN.CENTER
    p.text = "Giảng viên: Bộ môn Lập Trình Mạng    |    Sinh viên: Nhóm thực hiện QuizAI"
    p.font.name = FONT_BODY
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = C_MUTED

    # ==========================================
    # SLIDE 2: ĐẶT VẤN ĐỀ & MỤC TIÊU
    # ==========================================
    s2 = prs.slides.add_slide(blank_layout)
    add_header(s2, "01. Đặt Vấn Đề", "Thực Trạng Thi Online & Mục Tiêu Dự Án", "Giải quyết bài toán tạo đề thi và an toàn dữ liệu trên môi trường mạng")

    add_card(s2, Inches(0.8), Inches(1.8), Inches(5.6), Inches(5.1), "Thực Trạng & Thách Thức", C_AMBER)
    add_bullets(s2, Inches(1.1), Inches(2.5), Inches(5.0), Inches(4.0), [
        "• Biên soạn đề thủ công: Tốn nhiều công sức, khó đa dạng hóa ngân hàng câu hỏi.",
        "• Gian lận thi cử: Học sinh dễ dàng chuyển tab, tra Google hoặc nhờ ChatGPT giải hộ.",
        "• Nhìn bài lẫn nhau: Thí sinh ngồi cạnh trong phòng lab có cùng thứ tự câu hỏi và đáp án.",
        "• Rủi ro đường truyền: Rớt mạng Wi-Fi đột ngột làm mất toàn bộ bài thi đang làm dở."
    ])

    add_card(s2, Inches(6.9), Inches(1.8), Inches(5.6), Inches(5.1), "Mục Tiêu QuizAI", C_GREEN)
    add_bullets(s2, Inches(7.2), Inches(2.5), Inches(5.0), Inches(4.0), [
        "• AI Tự động sinh đề: Gemini AI sinh 10-30 câu hỏi chuẩn xác chỉ trong vài giây.",
        "• Chống gian lận 3 lớp: Bắt chuyển tab (3 lần hủy bài), khóa PrintScreen/DevTools, Watermark camera.",
        "• Trộn đề ngẫu nhiên: Đảo vị trí câu hỏi & 4 đáp án A, B, C, D cho từng thí sinh.",
        "• Chống mất dữ liệu: Tự động lưu (Auto-Save) real-time, bảo toàn trạng thái khi gặp sự cố mạng."
    ])

    # ==========================================
    # SLIDE 3: KIẾN TRÚC HỆ THỐNG (3-TIER)
    # ==========================================
    s3 = prs.slides.add_slide(blank_layout)
    add_header(s3, "02. Kiến Trúc Mạng", "Mô Hình 3 Tầng (Client - Server - Database)", "Kiến trúc Client-Server chuẩn mực đảm bảo hiệu năng và tính sẵn sàng cao")

    add_card(s3, Inches(0.8), Inches(1.8), Inches(3.6), Inches(5.1), "Tầng Client (Giao Diện)", C_CYAN)
    add_bullets(s3, Inches(1.05), Inches(2.5), Inches(3.1), Inches(4.0), [
        "• React 19 + Vite: SPA mượt mà, tải trang cực nhanh.",
        "• TailwindCSS: Giao diện Dark Mode trực quan, responsive.",
        "• Axios Interceptors: Tự gắn Bearer Token vào header.",
        "• Auto-Save: Ghi nhận đáp án real-time vào LocalStorage."
    ])

    add_card(s3, Inches(4.85), Inches(1.8), Inches(3.6), Inches(5.1), "Tầng Server (Xử Lý)", C_PRIMARY)
    add_bullets(s3, Inches(5.1), Inches(2.5), Inches(3.1), Inches(4.0), [
        "• ASP.NET Core 9: Web API đa luồng, độ trễ thấp (<150ms).",
        "• JWT Authentication: Xác thực phi trạng thái (Stateless).",
        "• CORS Controller: Cho phép mọi IP mạng LAN kết nối.",
        "• Gemini Client: Gọi Google AI Studio API qua HTTPS."
    ])

    add_card(s3, Inches(8.9), Inches(1.8), Inches(3.6), Inches(5.1), "Tầng Data (Dữ Liệu)", C_GREEN)
    add_bullets(s3, Inches(9.15), Inches(2.5), Inches(3.1), Inches(4.0), [
        "• SQL Server LocalDB: Cơ sở dữ liệu quan hệ ACID.",
        "• EF Core 9: Quản lý Migration và ánh xạ ORM.",
        "• BCrypt: Băm mật khẩu một chiều chống lộ dữ liệu.",
        "• Lưu trữ toàn diện: Đề thi, bài nộp và số lần vi phạm."
    ])

    # ==========================================
    # SLIDE 4: MÔ HÌNH CHẠY ĐA MÁY (LAN / INTERNET)
    # ==========================================
    s4 = prs.slides.add_slide(blank_layout)
    add_header(s4, "03. Truyền Thông Mạng", "Cơ Chế Chạy Đa Máy: LAN & Public Internet", "Khả năng kết nối đa nền tảng từ máy tính, laptop đến điện thoại di động")

    add_card(s4, Inches(0.8), Inches(1.8), Inches(5.6), Inches(5.1), "1. Chế Độ Mạng LAN (Phòng Lab / Wi-Fi)", C_CYAN)
    add_bullets(s4, Inches(1.1), Inches(2.5), Inches(5.0), Inches(4.0), [
        "• Lắng nghe đa card mạng: Backend & Frontend bind vào 0.0.0.0 (Port 5000 & 5173).",
        "• Vite Reverse Proxy: Forward /api/* cục bộ về Backend Kestrel Server.",
        "• Truy cập tức thì: Các máy con chỉ cần gõ http://192.168.x.x:5173.",
        "• 1-Click Startup: Script chay_he_thong.bat tự tìm IP và khởi chạy song song."
    ])

    add_card(s4, Inches(6.9), Inches(1.8), Inches(5.6), Inches(5.1), "2. Chế Độ Public Internet (Cloud / 4G)", C_PRIMARY)
    add_bullets(s4, Inches(7.2), Inches(2.5), Inches(5.0), Inches(4.0), [
        "• SSH Reverse Tunnel (Pinggy): Chia sẻ link web ra toàn cầu không cần mở port modem.",
        "• Bỏ qua Firewall & AP Isolation: Vượt qua bộ lọc chặn mạng nội bộ của trường.",
        "• Tự động tạo QR Code: Điện thoại chỉ cần bật camera quét mã để vào thi.",
        "• Bảo mật TLS End-to-End: Toàn bộ gói tin truyền qua Internet đều được mã hóa HTTPS."
    ])

    # ==========================================
    # SLIDE 5: TÍCH HỢP GENAI (GEMINI AI)
    # ==========================================
    s5 = prs.slides.add_slide(blank_layout)
    add_header(s5, "04. Trí Tuệ Nhân Tạo", "Quy Trình Tạo Ngân Hàng Câu Hỏi Bằng AI", "Tự động hóa 100% khâu biên soạn đề thi dựa trên Google Gemini GenAI")

    add_card(s5, Inches(0.8), Inches(1.8), Inches(3.6), Inches(5.1), "Bước 1: Nhập Liệu", C_AMBER)
    add_bullets(s5, Inches(1.05), Inches(2.5), Inches(3.1), Inches(4.0), [
        "• Giáo viên chọn chủ đề hoặc dán văn bản bài giảng.",
        "• Tùy chọn: Số lượng câu (5-30) và độ khó (Dễ / Vừa / Khó).",
        "• Đóng gói vào System Prompt với JSON Schema nghiêm ngặt."
    ])

    add_card(s5, Inches(4.85), Inches(1.8), Inches(3.6), Inches(5.1), "Bước 2: Xử Lý AI", C_PRIMARY)
    add_bullets(s5, Inches(5.1), Inches(2.5), Inches(3.1), Inches(4.0), [
        "• Gọi Gemini API qua HTTPS POST an toàn.",
        "• Mô hình Gemini 1.5 / 2.0 phân tích ngữ nghĩa và tạo nội dung.",
        "• Ép phản hồi chuẩn JSON: Câu hỏi, 4 đáp án và lời giải chi tiết."
    ])

    add_card(s5, Inches(8.9), Inches(1.8), Inches(3.6), Inches(5.1), "Bước 3: Kiểm Duyệt", C_GREEN)
    add_bullets(s5, Inches(9.15), Inches(2.5), Inches(3.1), Inches(4.0), [
        "• Backend kiểm tra cấu trúc dữ liệu trước khi lưu vào DB (Pending).",
        "• Giáo viên xem trước, chỉnh sửa hoặc xóa câu không đạt.",
        "• Bấm 'Duyệt' để xuất bản vào đề thi chính thức."
    ])

    # ==========================================
    # SLIDE 6: HỆ THỐNG CHỐNG GIAN LẬN ĐA TẦNG
    # ==========================================
    s6 = prs.slides.add_slide(blank_layout)
    add_header(s6, "05. An Toàn Kỳ Thi", "Hệ Thống Chống Gian Lận Đa Tầng (3 Lớp)", "Giám sát toàn diện hành vi thí sinh, đảm bảo kết quả thi trung thực và minh bạch")

    add_card(s6, Inches(0.8), Inches(1.8), Inches(3.6), Inches(5.1), "Lớp 1: Chống Chuyển Tab", C_RED)
    add_bullets(s6, Inches(1.05), Inches(2.5), Inches(3.1), Inches(4.0), [
        "• Bắt sự kiện: visibilitychange và window.blur khi thí sinh Alt+Tab hoặc mở tab khác.",
        "• Cooldown 2.5s: Chống kích hoạt đúp, đếm chuẩn xác từng lần vi phạm.",
        "• Chính sách 3 Lần: Cảnh báo lần 1 & 2 -> Vi phạm lần 3 tự động hủy bài & nộp điểm."
    ])

    add_card(s6, Inches(4.85), Inches(1.8), Inches(3.6), Inches(5.1), "Lớp 2: Chống Sao Chép", C_AMBER)
    add_bullets(s6, Inches(5.1), Inches(2.5), Inches(3.1), Inches(4.0), [
        "• Chặn phím tắt: PrintScreen, Ctrl+P (in), Ctrl+C/X/A (copy câu hỏi dán ChatGPT).",
        "• Chặn DevTools: Khóa F12, Ctrl+Shift+I để ngăn xem đáp án trong mã nguồn.",
        "• Khóa chuột phải & CSS select-none: Chống bôi đen sao chép văn bản."
    ])

    add_card(s6, Inches(8.9), Inches(1.8), Inches(3.6), Inches(5.1), "Lớp 3: Watermark Camera", C_CYAN)
    add_bullets(s6, Inches(9.15), Inches(2.5), Inches(3.1), Inches(4.0), [
        "• Dynamic Watermark: In mờ chéo Họ tên và Username của thí sinh khắp màn hình.",
        "• Chống chụp bằng điện thoại: Nếu thí sinh dùng điện thoại chụp màn hình, danh tính sẽ in rõ trên ảnh.",
        "• Màn hình chớp đen: Tự động che đề thi nếu phát hiện lệnh chụp màn hình."
    ])

    # ==========================================
    # SLIDE 7: ĐỘ TIN CẬY & TỰ PHỤC HỒI MẠNG
    # ==========================================
    s7 = prs.slides.add_slide(blank_layout)
    add_header(s7, "06. Độ Tin Cậy Mạng", "Cơ Chế Chống Mất Dữ Liệu & Đảo Đề Thi", "Khả năng chịu lỗi (Fault Tolerance) và chống gian lận vị trí ngồi")

    add_card(s7, Inches(0.8), Inches(1.8), Inches(5.6), Inches(5.1), "Cơ Chế Chống Mất Mạng (Auto-Save)", C_GREEN)
    add_bullets(s7, Inches(1.1), Inches(2.5), Inches(5.0), Inches(4.0), [
        "• Real-time Auto-Save: Mỗi khi tick chọn đáp án, dữ liệu lập tức ghi vào LocalStorage.",
        "• Hiển thị trạng thái: Huy hiệu '🟢 Đã tự động lưu (HH:mm:ss)' trên thanh tiêu đề.",
        "• Chịu lỗi cao: Sập nguồn máy tính, vô tình bấm F5 hoặc rớt Wi-Fi -> Bật lại còn nguyên vẹn đáp án.",
        "• Đồng hồ Server Timestamp: Thời gian tính theo UTC Server, triệt tiêu gian lận tua giờ máy Client."
    ])

    add_card(s7, Inches(6.9), Inches(1.8), Inches(5.6), Inches(5.1), "Trộn Đề Ngẫu Nhiên (Shuffling)", C_PRIMARY)
    add_bullets(s7, Inches(7.2), Inches(2.5), Inches(5.0), Inches(4.0), [
        "• Đảo thứ tự câu hỏi: Thuật toán Fisher-Yates xáo trộn câu hỏi cho từng thí sinh.",
        "• Đảo thứ tự 4 đáp án: Vị trí các lựa chọn A, B, C, D được hoán đổi ngẫu nhiên.",
        "• Chống nhìn bài: 2 học sinh ngồi cạnh nhau có đề thi và vị trí đáp án hoàn toàn khác nhau.",
        "• Cố định theo phiên thi: Lưu trạng thái vào SessionStorage để không bị nhảy đề khi tải lại trang."
    ])

    # ==========================================
    # SLIDE 8: BẢNG QUẢN TRỊ & XUẤT BÁO CÁO EXCEL
    # ==========================================
    s8 = prs.slides.add_slide(blank_layout)
    add_header(s8, "07. Quản Trị Hệ Thống", "Bảng Giám Sát Thời Gian Thực & Xuất Báo Cáo", "Công cụ hỗ trợ giáo viên theo dõi kỳ thi và tổng kết điểm số chuyên nghiệp")

    add_card(s8, Inches(0.8), Inches(1.8), Inches(5.6), Inches(5.1), "Theo Dõi & Giám Sát Kỳ Thi", C_CYAN)
    add_bullets(s8, Inches(1.1), Inches(2.5), Inches(5.0), Inches(4.0), [
        "• Bảng điểm trực tiếp: Cập nhật danh sách thí sinh đã nộp, điểm số và thời gian làm bài.",
        "• Thống kê phổ điểm: Tổng lượt thi, điểm trung bình, tỉ lệ đạt và điểm cao nhất.",
        "• Cột Giám Sát Vi Phạm: Bôi đỏ cảnh báo các thí sinh có hành vi rời màn hình (⚠️ X lần).",
        "• Quản lý tài khoản: Kích hoạt / Khóa tài khoản học sinh chỉ với 1 cú click."
    ])

    add_card(s8, Inches(6.9), Inches(1.8), Inches(5.6), Inches(5.1), "Xuất Báo Cáo Điểm Excel (.CSV)", C_GREEN)
    add_bullets(s8, Inches(7.2), Inches(2.5), Inches(5.0), Inches(4.0), [
        "• 1-Click Export: Nút 'Xuất Bảng Điểm (Excel / CSV)' tải file ngay về máy tính.",
        "• Chuẩn mã hóa UTF-8 BOM: Mở trực tiếp trên Microsoft Excel không bị lỗi font tiếng Việt.",
        "• Đầy đủ trường thông tin: STT, Mã bài, Họ tên, Tài khoản, Điểm số, Số câu đúng, Số lần vi phạm.",
        "• Sẵn sàng nộp phòng đào tạo: Giảm 100% thời gian tổng hợp điểm thủ công của giáo viên."
    ])

    # ==========================================
    # SLIDE 9: KẾT QUẢ ĐẠT ĐƯỢC & HIỆU NĂNG
    # ==========================================
    s9 = prs.slides.add_slide(blank_layout)
    add_header(s9, "08. Thực Nghiệm", "Kết Quả Đạt Được & Hiệu Năng Hệ Thống", "Các chỉ số kỹ thuật thực nghiệm đo đạc trong môi trường kiểm thử")

    # 4 Metric Cards
    m1 = add_card(s9, Inches(0.8), Inches(1.8), Inches(2.7), Inches(2.2), "", bg_color=C_CARD)
    tb = s9.shapes.add_textbox(Inches(0.9), Inches(2.0), Inches(2.5), Inches(1.8))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "< 120 ms"
    p.font.name = FONT_TITLE
    p.font.size = Pt(28)
    p.font.bold = True
    p.font.color.rgb = C_CYAN
    p2 = tf.add_paragraph()
    p2.text = "Thời gian phản hồi API trung bình qua giao thức HTTP/REST"
    p2.font.name = FONT_BODY
    p2.font.size = Pt(12)
    p2.font.color.rgb = C_MUTED

    m2 = add_card(s9, Inches(3.75), Inches(1.8), Inches(2.7), Inches(2.2), "", bg_color=C_CARD)
    tb = s9.shapes.add_textbox(Inches(3.85), Inches(2.0), Inches(2.5), Inches(1.8))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "3 - 5 giây"
    p.font.name = FONT_TITLE
    p.font.size = Pt(28)
    p.font.bold = True
    p.font.color.rgb = C_PRIMARY
    p2 = tf.add_paragraph()
    p2.text = "Thời gian Gemini AI phân tích và sinh bộ đề 10 câu hỏi hoàn chỉnh"
    p2.font.name = FONT_BODY
    p2.font.size = Pt(12)
    p2.font.color.rgb = C_MUTED

    m3 = add_card(s9, Inches(6.7), Inches(1.8), Inches(2.7), Inches(2.2), "", bg_color=C_CARD)
    tb = s9.shapes.add_textbox(Inches(6.8), Inches(2.0), Inches(2.5), Inches(1.8))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "100%"
    p.font.name = FONT_TITLE
    p.font.size = Pt(28)
    p.font.bold = True
    p.font.color.rgb = C_GREEN
    p2 = tf.add_paragraph()
    p2.text = "Bảo toàn dữ liệu làm bài khi gặp sự cố ngắt kết nối mạng hoặc F5"
    p2.font.name = FONT_BODY
    p2.font.size = Pt(12)
    p2.font.color.rgb = C_MUTED

    m4 = add_card(s9, Inches(9.65), Inches(1.8), Inches(2.7), Inches(2.2), "", bg_color=C_CARD)
    tb = s9.shapes.add_textbox(Inches(9.75), Inches(2.0), Inches(2.5), Inches(1.8))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "0 Lỗi"
    p.font.name = FONT_TITLE
    p.font.size = Pt(28)
    p.font.bold = True
    p.font.color.rgb = C_AMBER
    p2 = tf.add_paragraph()
    p2.text = "Xung đột gói tin mạng; bảo mật toàn diện với Token JWT & BCrypt"
    p2.font.name = FONT_BODY
    p2.font.size = Pt(12)
    p2.font.color.rgb = C_MUTED

    # Highlights box below
    h_box = add_card(s9, Inches(0.8), Inches(4.3), Inches(11.55), Inches(2.6), "Điểm Nổi Bật Đạt Được", C_WHITE)
    add_bullets(s9, Inches(1.1), Inches(4.9), Inches(11.0), Inches(1.8), [
        "✓ Hoàn thiện 100% các yêu cầu kiến trúc mạng Client-Server và giao thức TCP/IP.",
        "✓ Hệ thống chạy ổn định đồng thời trên nhiều máy tính trong mạng LAN và Internet.",
        "✓ Tính năng chống gian lận hoạt động mượt mà, phân loại chính xác thí sinh trung thực và vi phạm.",
        "✓ Giao diện Dark Mode chuẩn thẩm mỹ công nghệ, trải nghiệm người dùng trực quan trên cả mobile."
    ])

    # ==========================================
    # SLIDE 10: KẾT LUẬN & ĐỊNH HƯỚNG
    # ==========================================
    s10 = prs.slides.add_slide(blank_layout)
    add_header(s10, "09. Kết Luận", "Tổng Kết & Hướng Phát Triển Tương Lai", "Đóng góp của dự án và các bước nâng cấp tiếp theo cho giai đoạn cuối kỳ")

    add_card(s10, Inches(0.8), Inches(1.8), Inches(5.6), Inches(5.1), "Giá Trị Đạt Được", C_GREEN)
    add_bullets(s10, Inches(1.1), Inches(2.5), Inches(5.0), Inches(4.0), [
        "• Ứng dụng thực tiễn cao: Kết hợp xuất sắc giữa lý thuyết Lập trình mạng và công nghệ AI hiện đại.",
        "• Giải quyết triệt để vấn đề: Tự động hóa đề thi, chống gian lận và tối ưu hóa quản lý điểm.",
        "• Độ sẵn sàng cao: Có thể áp dụng ngay cho các buổi kiểm tra trên lớp hoặc kỳ thi nội bộ trường học.",
        "• Mã nguồn mở hoàn chỉnh: Lưu trữ chuẩn mực và triển khai dễ dàng qua GitHub."
    ])

    add_card(s10, Inches(6.9), Inches(1.8), Inches(5.6), Inches(5.1), "Định Hướng Cuối Kỳ", C_CYAN)
    add_bullets(s10, Inches(7.2), Inches(2.5), Inches(5.0), Inches(4.0), [
        "• WebSocket / SignalR: Xây dựng chế độ thi đối kháng trực tiếp thời gian thực (Quiz Battle phong cách Kahoot).",
        "• Giám sát Camera AI: Tích hợp webcam nhận diện khuôn mặt và cảnh báo người lạ trong phòng thi.",
        "• Dockerization: Đóng gói toàn bộ Backend và Database vào Docker Container.",
        "• Cloud Deployment: Triển khai lên máy chủ đám mây (Render / VPS) với tên miền và chứng chỉ SSL riêng."
    ])

    # Save presentation
    prs.save(output_path)
    print(f"Presentation saved successfully to {output_path}")

if __name__ == "__main__":
    out_file = os.path.join(os.path.dirname(__file__), "slide_QuizAI_ngan_gon.pptx")
    create_concise_presentation(out_file)

