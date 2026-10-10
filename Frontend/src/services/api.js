import axios from 'axios';

const API_BASE = 'http://localhost:5000/api';

const api = axios.create({ baseURL: API_BASE });

// Attach JWT to every request
api.interceptors.request.use(config => {
  const token = localStorage.getItem('quiz_token');
  if (token) config.headers.Authorization = `Bearer ${token}`;
  return config;
});

// Auto-logout on 401
api.interceptors.response.use(
  res => res,
  err => {
    if (err.response?.status === 401) {
      localStorage.removeItem('quiz_token');
      localStorage.removeItem('quiz_user');
      window.location.href = '/login';
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
