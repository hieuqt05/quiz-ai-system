import axios from 'axios';

// Kết nối trực tiếp tới Backend ASP.NET Core qua Cloudflare Tunnel
const API_BASE = import.meta.env.VITE_API_BASE_URL || 'https://examples-counsel-stored-root.trycloudflare.com/api';

const api = axios.create({
  baseURL: API_BASE,
  timeout: 15000, // 15 giây timeout
  headers: {
    'Content-Type': 'application/json',
  },
});

// Attach JWT to every request
api.interceptors.request.use(config => {
  const token = localStorage.getItem('quiz_token');
  if (token) config.headers.Authorization = `Bearer ${token}`;
  return config;
});

// Auto-logout on 401 / handle network errors
api.interceptors.response.use(
  res => res,
  err => {
    if (err.response?.status === 401) {
      localStorage.removeItem('quiz_token');
      localStorage.removeItem('quiz_user');
      window.location.href = '/login';
    }

    // Lỗi mạng (không kết nối được server)
    if (!err.response) {
      err.message = 'Không thể kết nối server. Kiểm tra lại mạng hoặc server đã tắt.';
    }

    return Promise.reject(err);
  }
);

// ── Auth ──────────────────────────────────────────────
export const authApi = {
  login: (data) => api.post('/auth/login', data),
  register: (data) => api.post('/auth/register', data),
  me: () => api.get('/auth/me'),
};

// ── Exams ──────────────────────────────────────────────
export const examApi = {
  getPublished: () => api.get('/exams'),
  getAll: () => api.get('/exams/all'),
  getDetail: (id) => api.get(`/exams/${id}`),
  create: (data) => api.post('/exams', data),
  publish: (id) => api.patch(`/exams/${id}/publish`),
  archive: (id) => api.patch(`/exams/${id}/archive`),
  delete: (id) => api.delete(`/exams/${id}`),
  addQuestion: (examId, data) => api.post(`/exams/${examId}/questions`, data),
  getPendingQuestions: (examId) => api.get('/exams/questions/pending', { params: { examId } }),
  approveQuestion: (qId) => api.patch(`/exams/questions/${qId}/approve`),
  rejectQuestion: (qId) => api.patch(`/exams/questions/${qId}/reject`),
};

// ── AI ──────────────────────────────────────────────
export const aiApi = {
  generate: (data) => api.post('/ai/generate', data),
};

// ── Submissions ──────────────────────────────────────────────
export const submissionApi = {
  start: (examId) => api.post('/submissions/start', { examId }),
  submit: (data) => api.post('/submissions/submit', data),
  getResult: (id) => api.get(`/submissions/${id}/result`),
  getHistory: () => api.get('/submissions/history'),
};

// ── Admin ──────────────────────────────────────────────
export const adminApi = {
  getUsers: () => api.get('/admin/users'),
  toggleUser: (id) => api.patch(`/admin/users/${id}/toggle`),
  getExamStats: (id) => api.get(`/admin/stats/exam/${id}`),
  getExamSubmissions: (id) => api.get(`/admin/stats/exam/${id}/submissions`),
};

export default api;
