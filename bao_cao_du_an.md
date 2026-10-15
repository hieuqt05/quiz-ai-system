# BÁO CÁO ĐỒ ÁN MÔN LẬP TRÌNH MẠNG
## Đề tài: Hệ Thống Trắc Nghiệm Online Tích Hợp Trí Tuệ Nhân Tạo (QuizAI)

---

> **GitHub Repository:** https://github.com/hieuqt05/quiz-ai-system

---

## MỤC LỤC

1. [Giới thiệu đề tài](#1-giới-thiệu-đề-tài)
2. [Công nghệ sử dụng](#2-công-nghệ-sử-dụng)
3. [Kiến trúc hệ thống](#3-kiến-trúc-hệ-thống)
4. [Cơ sở dữ liệu](#4-cơ-sở-dữ-liệu)
5. [Backend - ASP.NET Core Web API](#5-backend---aspnet-core-web-api)
6. [Frontend - React + Vite](#6-frontend---react--vite)
7. [Tích hợp AI (Google Gemini)](#7-tích-hợp-ai-google-gemini)
8. [Các chức năng chính](#8-các-chức-năng-chính)
9. [Hướng dẫn cài đặt và chạy](#9-hướng-dẫn-cài-đặt-và-chạy)
10. [Kết luận](#10-kết-luận)

---

## 1. Giới Thiệu Đề Tài

### 1.1. Tên đề tài
**QuizAI – Hệ Thống Trắc Nghiệm Online Tích Hợp Trí Tuệ Nhân Tạo**

### 1.2. Mô tả
QuizAI là một ứng dụng web fullstack cho phép:
- **Giáo viên / Admin** tạo đề thi trắc nghiệm, sử dụng AI (Google Gemini) để tự động sinh câu hỏi từ chủ đề hoặc đoạn văn bản, sau đó duyệt và quản lý câu hỏi.
- **Học sinh** đăng ký tài khoản, tra cứu danh sách đề thi, làm bài với đồng hồ đếm ngược, nộp bài, xem kết quả và lời giải thích chi tiết.
- **Quản trị viên** theo dõi thống kê điểm số, tỷ lệ đạt và quản lý người dùng.

### 1.3. Mục tiêu
- Áp dụng kiến thức lập trình mạng: REST API, HTTP Client, xác thực JWT.
- Ứng dụng AI thực tế vào bài toán giáo dục.
- Xây dựng hệ thống phân quyền (RBAC) cho 3 loại người dùng: STUDENT, TEACHER, ADMIN.

---

## 2. Công Nghệ Sử Dụng

### 2.1. Backend

| Công nghệ | Phiên bản | Mục đích |
|-----------|-----------|----------|
| ASP.NET Core Web API | .NET 9.0 | Framework REST API |
| Entity Framework Core | 9.0.0 | ORM – truy vấn cơ sở dữ liệu |
| SQL Server (LocalDB) | - | Hệ quản trị cơ sở dữ liệu |
| JWT Bearer Authentication | 9.0.0 | Xác thực & phân quyền |
| BCrypt.Net-Next | 4.2.0 | Mã hóa mật khẩu |
| Swashbuckle (Swagger) | 7.3.1 | Tài liệu API tự động |
| HttpClientFactory | Built-in | Gọi Google Gemini API |

### 2.2. Frontend

| Công nghệ | Phiên bản | Mục đích |
|-----------|-----------|----------|
| React | 19.2.8 | Thư viện giao diện người dùng |
| Vite | 8.3.0 | Build tool & dev server |
| React Router DOM | 7.18.4 | Định tuyến phía client (SPA) |
| TailwindCSS | 3.4.19 | Framework CSS utility-first |
| Axios | 1.20.0 | HTTP Client gọi API |
| Lucide React | 1.55.0 | Bộ icon hiện đại |
| React Hot Toast | 2.6.1 | Thông báo toast |

### 2.3. AI
- **Google Gemini API** – model `gemini-3.8-flash` – sinh câu hỏi trắc nghiệm tự động.

---

## 3. Kiến Trúc Hệ Thống

```
┌─────────────────────────────────────────────────────┐
│                  CLIENT (Browser)                    │
│         React SPA – http://localhost:5173            │
└───────────────────────┬─────────────────────────────┘
                        │ HTTP REST (JSON) + JWT Token
                        ▼
┌─────────────────────────────────────────────────────┐
│          BACKEND – ASP.NET Core Web API              │
│              http://localhost:5000                   │
│                                                      │
│  ┌──────────┐ ┌──────────┐ ┌───────┐ ┌───────────┐ │
│  │   Auth   │ │  Exams   │ │  AI   │ │  Admin/   │ │
│  │Controller│ │Controller│ │Control│ │Submissions│ │
│  └────┬─────┘ └────┬─────┘ └───┬───┘ └─────┬─────┘ │
│       │            │           │            │        │
│  ┌────▼──────────────────────────────────────▼────┐  │
│  │              Service Layer                     │  │
│  │  AuthService │ ExamService │ QuizService       │  │
│  │  AIService   │ StatsService                   │  │
│  └────────────────────┬───────────────────────────┘  │
│                       │ Entity Framework Core         │
│  ┌────────────────────▼───────────────────────────┐  │
│  │              AppDbContext                       │  │
│  └────────────────────────────────────────────────┘  │
└───────────────────────┬─────────────────────────────┘
                        │ ADO.NET / EF
                        ▼
┌─────────────────────────────────────────────────────┐
│           SQL Server (LocalDB)                       │
│    QuizSystemDB – 7 bảng dữ liệu                    │
└─────────────────────────────────────────────────────┘
                        │
                        │ HTTPS REST
                        ▼
┌─────────────────────────────────────────────────────┐
│          Google Gemini API (External)                │
│  generativelanguage.googleapis.com – gemini-3.8-flash│
└─────────────────────────────────────────────────────┘
```

### 3.1. Luồng xử lý chính

**Luồng làm bài thi:**
```
Học sinh → Chọn đề thi → POST /api/submissions/start
         → Nhận submissionId + thời gian còn lại
         → Làm bài với đồng hồ đếm ngược
         → POST /api/submissions/submit (gửi tất cả câu trả lời)
         → Nhận kết quả điểm + lời giải thích
         → Xem kết quả tại /result/:submissionId
```

**Luồng sinh câu hỏi AI:**
```
Teacher/Admin → Nhập chủ đề hoặc văn bản
              → POST /api/ai/generate
              → AIService → Gemini API (HTTP POST)
              → Parse JSON response
              → Lưu vào DB (status = PENDING)
              → Admin duyệt → APPROVED
              → Câu hỏi xuất hiện trong đề thi
```

---

## 4. Cơ Sở Dữ Liệu

### 4.1. Sơ đồ thực thể (ERD)

```
┌─────────────┐       ┌─────────────┐       ┌─────────────┐
│    Users     │       │    Exams    │       │  Questions  │
├─────────────┤       ├─────────────┤       ├─────────────┤
│ UserId (PK)  │──1───<│ ExamId (PK) │──1───<│QuestionId   │
│ Username     │       │ CreatedBy   │       │ ExamId (FK) │
│ Email        │       │ Title       │       │ GeneratedBy │
│ PasswordHash │       │ Description │       │QuestionText │
│ FullName     │       │DurationMins │       │ Explanation │
│ Role         │       │ PassScore   │       │ Difficulty  │
│ IsActive     │       │ Status      │       │ SourceType  │
│ CreatedAt    │       │ Category    │       │ Status      │
│ LastLoginAt  │       │ CreatedAt   │       │ OrderIndex  │
└─────────────┘       └─────────────┘       └──────┬──────┘
                                                    │
       ┌────────────────────────────────────────────┤
       │                                            │
┌──────▼──────┐       ┌─────────────┐    ┌─────────▼─────┐
│   Options   │       │ Submissions │    │SubmissionDetail│
├─────────────┤       ├─────────────┤    ├───────────────┤
│ OptionId    │       │SubmissionId │    │ DetailId      │
│ QuestionId  │       │ UserId (FK) │    │ SubmissionId  │
│ OptionLabel │       │ ExamId (FK) │    │ QuestionId    │
│ OptionText  │       │ StartedAt   │    │SelectedOption │
│ IsCorrect   │       │ SubmittedAt │    │ IsCorrect     │
└─────────────┘       │ TotalScore  │    └───────────────┘
                      │CorrectAns   │
                      │ TimeTaken   │    ┌─────────────────┐
                      │ Status      │    │ AIGenerationLogs│
                      └─────────────┘    ├─────────────────┤
                                         │ LogId           │
                                         │ RequestedBy     │
                                         │ ExamId          │
                                         │ InputType       │
                                         │ InputContent    │
                                         │ QuestionsReq    │
                                         │ QuestionsGen    │
                                         │ RawAIResponse   │
                                         │ Status          │
                                         │ ErrorMessage    │
                                         └─────────────────┘
```

### 4.2. Mô tả các bảng

| Bảng | Mô tả |
|------|-------|
| **Users** | Lưu thông tin người dùng, vai trò (STUDENT/TEACHER/ADMIN), mật khẩu được mã hóa BCrypt |
| **Exams** | Đề thi với trạng thái DRAFT → PUBLISHED → ARCHIVED, thời gian làm bài, điểm đạt |
| **Questions** | Câu hỏi trắc nghiệm, hỗ trợ nguồn AI hoặc MANUAL, trạng thái PENDING/APPROVED/REJECTED |
| **Options** | 4 lựa chọn A/B/C/D cho mỗi câu hỏi, đánh dấu đáp án đúng |
| **Submissions** | Bài làm của học sinh, lưu điểm, thời gian, trạng thái IN_PROGRESS/COMPLETED/TIMEOUT |
| **SubmissionDetails** | Chi tiết từng câu trả lời, ghi nhận đúng/sai |
| **AIGenerationLogs** | Nhật ký mỗi lần gọi AI: prompt, kết quả, lỗi nếu có |

---

## 5. Backend – ASP.NET Core Web API

### 5.1. Cấu trúc thư mục

```
Backend/
├── Controllers/
│   ├── AuthController.cs         # Đăng ký, đăng nhập, lấy thông tin user
│   ├── ExamsController.cs        # CRUD đề thi, quản lý câu hỏi
│   ├── AIController.cs           # Sinh câu hỏi bằng AI
│   ├── SubmissionsController.cs  # Bắt đầu làm bài, nộp bài, xem kết quả
│   └── AdminController.cs        # Thống kê, quản lý người dùng
├── Models/
│   ├── Entities/                 # Entity classes (7 bảng)
│   └── DTOs/                     # Data Transfer Objects
├── Services/
│   ├── AuthService.cs            # Xác thực, tạo JWT
│   ├── ExamService.cs            # Logic quản lý đề thi & câu hỏi
│   ├── QuizService.cs            # Logic làm bài thi, chấm điểm
│   ├── AIService.cs              # Gọi Gemini API, parse kết quả
│   └── StatsService.cs           # Thống kê điểm, quản lý users
├── Data/
│   └── AppDbContext.cs           # EF Core DbContext
└── Program.cs                    # Cấu hình DI, JWT, CORS, Swagger
```

### 5.2. API Endpoints

#### Auth (`/api/auth`)
| Method | Endpoint | Mô tả | Auth |
|--------|----------|-------|------|
| POST | `/register` | Đăng ký tài khoản mới (vai trò STUDENT) | Public |
| POST | `/login` | Đăng nhập, nhận JWT token | Public |
| GET | `/me` | Lấy thông tin người dùng hiện tại | JWT |

#### Exams (`/api/exams`)
| Method | Endpoint | Mô tả | Auth |
|--------|----------|-------|------|
| GET | `/` | Lấy danh sách đề thi đã công bố | Public |
| GET | `/all` | Lấy tất cả đề thi | TEACHER/ADMIN |
| GET | `/{id}` | Chi tiết đề thi + câu hỏi | JWT |
| POST | `/` | Tạo đề thi mới | TEACHER/ADMIN |
| PATCH | `/{id}/publish` | Công bố đề thi | TEACHER/ADMIN |
| PATCH | `/{id}/archive` | Lưu trữ đề thi | ADMIN |
| POST | `/{examId}/questions` | Thêm câu hỏi thủ công | TEACHER/ADMIN |
| GET | `/questions/pending` | Câu hỏi chờ duyệt | TEACHER/ADMIN |
| PATCH | `/questions/{id}/approve` | Duyệt câu hỏi | TEACHER/ADMIN |
| PATCH | `/questions/{id}/reject` | Từ chối câu hỏi | TEACHER/ADMIN |

#### AI (`/api/ai`)
| Method | Endpoint | Mô tả | Auth |
|--------|----------|-------|------|
| POST | `/generate` | Sinh câu hỏi tự động bằng Gemini AI | TEACHER/ADMIN |

#### Submissions (`/api/submissions`)
| Method | Endpoint | Mô tả | Auth |
|--------|----------|-------|------|
| POST | `/start` | Bắt đầu bài thi, nhận submissionId | JWT |
| POST | `/submit` | Nộp bài, tính điểm tự động | JWT |
| GET | `/{id}/result` | Xem kết quả bài thi | JWT |
| GET | `/history` | Lịch sử làm bài | JWT |

#### Admin (`/api/admin`)
| Method | Endpoint | Mô tả | Auth |
|--------|----------|-------|------|
| GET | `/users` | Danh sách người dùng | ADMIN |
| PATCH | `/users/{id}/toggle` | Kích hoạt/khóa tài khoản | ADMIN |
| GET | `/stats/exam/{id}` | Thống kê đề thi | TEACHER/ADMIN |
| GET | `/stats/exam/{id}/submissions` | Danh sách bài nộp | TEACHER/ADMIN |

### 5.3. Xác thực và phân quyền

```
Đăng nhập → JWT Token (hạn 24 giờ) → Lưu localStorage
                │
                ▼
     Header: Authorization: Bearer <token>
                │
                ▼
     ┌──────────────────────────────┐
     │  Kiểm tra Claims:            │
     │  - NameIdentifier (UserId)   │
     │  - Name (Username)           │
     │  - Email                     │
     │  - Role (STUDENT/TEACHER/    │
     │          ADMIN)              │
     │  - FullName                  │
     └──────────────────────────────┘
```

Mật khẩu được mã hóa bằng **BCrypt** với salt ngẫu nhiên trước khi lưu vào database.

### 5.4. Cơ chế chấm điểm

```csharp
TotalScore = Math.Round((decimal)correct / totalQuestions * 100, 2)
TimeTaken  = Math.Clamp(elapsedSeconds, 1, maxAllowedSeconds)
```
- Điểm tính theo phần trăm số câu đúng.
- Bài thi cũ đang dở dang (IN_PROGRESS) nhưng đã hết giờ sẽ **tự động đóng** khi học sinh bắt đầu bài thi mới.

---

## 6. Frontend – React + Vite

### 6.1. Cấu trúc thư mục

```
Frontend/src/
├── pages/
│   ├── LoginPage.jsx         # Đăng nhập
│   ├── RegisterPage.jsx      # Đăng ký
│   ├── ExamListPage.jsx      # Danh sách đề thi
│   ├── QuizPage.jsx          # Giao diện làm bài + đồng hồ đếm ngược
│   ├── ResultPage.jsx        # Kết quả và lời giải thích
│   ├── HistoryPage.jsx       # Lịch sử làm bài
│   └── AdminPage.jsx         # Trang quản trị (tạo đề, sinh AI, duyệt câu hỏi, thống kê)
├── components/
│   └── Navbar.jsx            # Thanh điều hướng với phân quyền
├── contexts/
│   └── AuthContext.jsx       # Context quản lý trạng thái đăng nhập toàn cục
├── services/
│   └── api.js                # Axios instance + tất cả hàm gọi API
└── App.jsx                   # Routing + Protected Routes
```

### 6.2. Định tuyến và bảo vệ route

```jsx
// Route bảo vệ: chỉ cho phép người đã đăng nhập
<ProtectedRoute> → Redirect /login nếu chưa đăng nhập

// Route bảo vệ theo vai trò
<ProtectedRoute roles={['TEACHER', 'ADMIN']}> → /admin
```

| Route | Component | Yêu cầu |
|-------|-----------|---------|
| `/login` | LoginPage | Public |
| `/register` | RegisterPage | Public |
| `/exams` | ExamListPage | Đã đăng nhập |
| `/quiz/:examId` | QuizPage | Đã đăng nhập |
| `/result/:submissionId` | ResultPage | Đã đăng nhập |
| `/history` | HistoryPage | Đã đăng nhập |
| `/admin` | AdminPage | TEACHER / ADMIN |

### 6.3. Quản lý trạng thái xác thực

`AuthContext` lưu thông tin user vào `localStorage`, cung cấp hook `useAuth()` cho tất cả component con. Axios interceptor tự động đính kèm JWT token vào mọi request.

---

## 7. Tích Hợp AI (Google Gemini)

### 7.1. Luồng sinh câu hỏi

```
1. Teacher nhập: chủ đề/văn bản + số câu + độ khó
2. Frontend → POST /api/ai/generate
3. AIController → AIService.GenerateQuestionsAsync()
4. AIService.BuildPrompt() → tạo prompt tiếng Việt có cấu trúc JSON
5. AIService.CallGeminiAsync() → HTTP POST đến Gemini API
   - Retry logic: tối đa 3 lần nếu lỗi 503/429
   - Exponential backoff: delay 2s, 4s giữa các lần retry
6. Parse JSON response (loại bỏ markdown code block nếu có)
7. Validate: đủ 4 lựa chọn, đúng 1 đáp án đúng
8. Lưu câu hỏi vào DB với status = PENDING
9. Ghi log vào AIGenerationLogs
10. Admin duyệt → APPROVED → xuất hiện trong đề thi
```

### 7.2. Prompt Engineering

Hệ thống sử dụng prompt có cấu trúc chặt chẽ, yêu cầu AI:
- Trả về **JSON thuần** (không có markdown wrapper).
- Đúng số lượng câu hỏi theo yêu cầu.
- Mỗi câu có 4 đáp án A/B/C/D, chỉ 1 đáp án đúng.
- Có trường `explanation` giải thích đáp án.
- Hỗ trợ 2 kiểu đầu vào: **TOPIC** (chủ đề) và **TEXT** (văn bản).

### 7.3. Cấu hình Gemini API

```json
{
  "temperature": 0.7,
  "maxOutputTokens": 8192,
  "responseMimeType": "application/json"
}
```

- Giới hạn nội dung đầu vào: **15.000 ký tự** để tránh lạm dụng.
- API Key lưu trong `appsettings.json` (cấu hình bảo mật).

---

## 8. Các Chức Năng Chính

### 8.1. Quản lý người dùng

| Chức năng | Mô tả |
|-----------|-------|
| Đăng ký | Tạo tài khoản mới với vai trò STUDENT, kiểm tra trùng username/email |
| Đăng nhập | Xác thực BCrypt, trả về JWT token 24 giờ |
| Phân quyền | 3 vai trò: STUDENT (làm bài), TEACHER (tạo đề + AI), ADMIN (toàn quyền) |
| Quản lý users | Admin kích hoạt / khóa tài khoản người dùng |

### 8.2. Quản lý đề thi

| Chức năng | Mô tả |
|-----------|-------|
| Tạo đề thi | Đặt tiêu đề, mô tả, danh mục, thời gian, điểm đạt |
| Vòng đời đề thi | DRAFT → PUBLISHED → ARCHIVED |
| Thêm câu hỏi thủ công | Nhập câu hỏi + 4 đáp án trực tiếp |
| Sinh câu hỏi AI | Nhập chủ đề/văn bản, Gemini tự sinh câu hỏi |
| Duyệt câu hỏi | Approve/Reject câu hỏi do AI tạo trước khi đưa vào thi |

### 8.3. Làm bài thi

| Chức năng | Mô tả |
|-----------|-------|
| Bắt đầu làm bài | Tạo submission, nhận thời gian còn lại |
| Đồng hồ đếm ngược | Hiển thị countdown, tự động nộp khi hết giờ |
| Bài dở dang | Tiếp tục bài thi cũ nếu còn trong thời gian cho phép |
| Nộp bài | Gửi tất cả câu trả lời, tính điểm tức thì |
| Xem kết quả | Điểm, số câu đúng, lời giải thích từng câu |

### 8.4. Thống kê và lịch sử

| Chức năng | Mô tả |
|-----------|-------|
| Lịch sử làm bài | Học sinh xem các bài đã làm, điểm, ngày giờ |
| Thống kê đề thi | Tổng lượt làm, điểm trung bình, tỷ lệ đạt, điểm cao/thấp nhất |
| Danh sách bài nộp | Admin xem bài làm của tất cả học sinh theo từng đề thi |

---

## 9. Hướng Dẫn Cài Đặt Và Chạy

### 9.1. Yêu cầu hệ thống

- **Node.js** ≥ 18.x
- **.NET SDK** 9.0
- **SQL Server** hoặc **SQL Server LocalDB**
- **Google Gemini API Key** (miễn phí tại [aistudio.google.com](https://aistudio.google.com))

### 9.2. Cài đặt Backend

```bash
# 1. Clone repository
git clone https://github.com/hieuqt05/quiz-ai-system.git
cd quiz-ai-system/Backend

# 2. Thêm Gemini API Key vào appsettings.json
# "GeminiApiKey": "YOUR_API_KEY_HERE"

# 3. Chạy Backend (tự động migrate DB)
dotnet run --urls="http://localhost:5000"
```

> Database và tài khoản Admin mặc định (`admin` / `Admin@123`) sẽ được tự động tạo khi khởi động lần đầu.

### 9.3. Cài đặt Frontend

```bash
# Mở terminal mới
cd quiz-ai-system/Frontend

# Cài dependencies
npm install

# Chạy dev server
npm run dev
# → http://localhost:5173
```

### 9.4. Tài khoản mặc định

| Vai trò | Username | Mật khẩu |
|---------|----------|----------|
| Admin | `admin` | `Admin@123` |
| Học sinh | Tự đăng ký | - |

---

## 10. Kết Luận

### 10.1. Kết quả đạt được

Dự án **QuizAI** đã xây dựng thành công một hệ thống trắc nghiệm online đầy đủ tính năng với những kết quả sau:

✅ **Kiến trúc Fullstack hoàn chỉnh**: Backend ASP.NET Core RESTful API + Frontend React SPA giao tiếp qua HTTP/JSON.

✅ **Bảo mật**: Xác thực JWT, mã hóa mật khẩu BCrypt, phân quyền RBAC 3 cấp.

✅ **Tích hợp AI thực tế**: Kết nối thành công Google Gemini API, sinh câu hỏi trắc nghiệm tự động với cơ chế retry và validate đầu ra.

✅ **Quy trình kiểm duyệt**: AI sinh câu hỏi → Lưu PENDING → Admin duyệt → APPROVED vào đề thi.

✅ **Trải nghiệm người dùng**: Đồng hồ đếm ngược, tự động lưu bài dở dang, xem lời giải chi tiết sau khi nộp bài.

✅ **Thống kê**: Theo dõi điểm trung bình, tỷ lệ đạt, lịch sử làm bài.

### 10.2. Hướng phát triển

- Thêm tính năng **xuất đề thi ra PDF**.
- Hỗ trợ câu hỏi **nhiều đáp án đúng** (Multiple Choice).
- **Xếp hạng** học sinh theo từng đề thi (leaderboard).
- **Thông báo real-time** khi câu hỏi AI được duyệt (SignalR/WebSocket).
- Tích hợp **OAuth2** (đăng nhập bằng Google).
- Triển khai lên **cloud** (Azure / AWS).

---

*Báo cáo được tổng hợp từ source code tại: https://github.com/hieuqt05/quiz-ai-system*
