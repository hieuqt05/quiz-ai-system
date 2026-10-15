import { useEffect, useState } from 'react';
import { examApi, aiApi, adminApi } from '../services/api';
import {
  Shield, Users, BookOpen, Brain, CheckCircle, XCircle, Plus,
  Loader2, Send, Eye, BarChart2, Clock, Target, ChevronDown, ChevronUp, Trash2
} from 'lucide-react';
import toast from 'react-hot-toast';

const TABS = ['Đề Thi', 'Duyệt Câu Hỏi AI', 'Tạo Câu Hỏi AI', 'Người Dùng', 'Thống Kê'];

export default function AdminPage() {
  const [tab, setTab] = useState(0);
  const [exams, setExams] = useState([]);
  const [pending, setPending] = useState([]);
  const [users, setUsers] = useState([]);
  const [stats, setStats] = useState(null);
  const [loading, setLoading] = useState(false);

  // AI Generator state
  const [aiForm, setAiForm] = useState({ examId: '', inputType: 'DOCUMENT_TEXT', content: '', numQuestions: 5, difficulty: 'MEDIUM' });
  const [aiLoading, setAiLoading] = useState(false);
  const [aiResult, setAiResult] = useState(null);

  // Create Exam
  const [examForm, setExamForm] = useState({ title: '', description: '', durationMinutes: 30, passScore: 50, category: '' });
  const [showCreateExam, setShowCreateExam] = useState(false);

  useEffect(() => { loadExams(); }, []);
  useEffect(() => { if (tab === 1) loadPending(); }, [tab]);
  useEffect(() => { if (tab === 3) loadUsers(); }, [tab]);

  const loadExams = () => examApi.getAll().then(r => setExams(r.data));
  const loadPending = () => examApi.getPendingQuestions().then(r => setPending(r.data));
  const loadUsers = () => adminApi.getUsers().then(r => setUsers(r.data));

  const handleCreateExam = async (e) => {
    e.preventDefault();
    try {
      await examApi.create(examForm);
      toast.success('Tạo đề thi thành công!');
      setShowCreateExam(false);
      loadExams();
    } catch { toast.error('Lỗi khi tạo đề thi!'); }
  };

  const [deletingId, setDeletingId] = useState(null);

  const handlePublish = async (id) => {
    await examApi.publish(id);
    toast.success('Đề thi đã được công bố!');
    loadExams();
  };

  const handleDeleteExam = async (exam) => {
    if (!window.confirm(`Bạn có chắc chắn muốn xóa vĩnh viễn đề thi "${exam.title}" không?\n\nLưu ý: Tất cả câu hỏi và lượt thi liên quan cũng sẽ bị xóa!`)) {
      return;
    }
    setDeletingId(exam.examId);
    try {
      await examApi.delete(exam.examId);
      toast.success(`Đã xóa đề thi "${exam.title}" thành công!`);
      if (stats?.examId === exam.examId) setStats(null);
      loadExams();
    } catch (err) {
      toast.error(err.response?.data?.message || 'Lỗi khi xóa đề thi!');
    } finally {
      setDeletingId(null);
    }
  };

  const handleApprove = async (qId) => {
    await examApi.approveQuestion(qId);
    toast.success('Câu hỏi đã được duyệt!');
    setPending(p => p.filter(q => q.questionId !== qId));
  };

  const handleReject = async (qId) => {
    await examApi.rejectQuestion(qId);
    toast.success('Câu hỏi đã bị từ chối.');
    setPending(p => p.filter(q => q.questionId !== qId));
  };

  const handleApproveAll = async () => {
    setLoading(true);
    for (const q of pending) await examApi.approveQuestion(q.questionId);
    toast.success(`Đã duyệt ${pending.length} câu hỏi!`);
    setPending([]);
    setLoading(false);
  };

  const handleToggleUser = async (id) => {
    await adminApi.toggleUser(id);
    loadUsers();
    toast.success('Đã cập nhật trạng thái!');
  };

  const handleAIGenerate = async (e) => {
    e.preventDefault();
    if (!aiForm.examId) { toast.error('Vui lòng chọn đề thi!'); return; }
    setAiLoading(true); setAiResult(null);
    try {
      const res = await aiApi.generate({ ...aiForm, examId: parseInt(aiForm.examId), numQuestions: parseInt(aiForm.numQuestions) });
      setAiResult(res.data);
      toast.success(`AI đã tạo ${res.data.generatedCount} câu hỏi!`);
      if (tab !== 1) toast('Chuyển sang tab "Duyệt Câu Hỏi AI" để xem.', { icon: '👉' });
    } catch (err) {
      toast.error(err.response?.data?.message || 'AI gặp lỗi!');
    } finally { setAiLoading(false); }
  };

  const handleLoadStats = async (examId) => {
    const res = await adminApi.getExamStats(examId);
    setStats(res.data);
  };

  return (
    <div className="max-w-6xl mx-auto px-4 py-8">
      <div className="flex items-center gap-3 mb-8">
        <Shield className="w-8 h-8 text-primary-400" />
        <h1 className="text-3xl font-bold gradient-text">Bảng Quản Trị</h1>
      </div>

      {/* Tabs */}
      <div className="flex gap-1 mb-6 bg-slate-100 p-1 rounded-xl border border-slate-200 overflow-x-auto">
        {TABS.map((t, i) => (
          <button
            key={i}
            id={`admin-tab-${i}`}
            onClick={() => setTab(i)}
            className={`flex-shrink-0 px-4 py-2.5 rounded-lg text-sm font-medium transition-all ${
              tab === i ? 'bg-primary-600 text-white shadow-sm' : 'text-slate-600 hover:text-slate-900 hover:bg-white'
            }`}
          >{t}</button>
        ))}
      </div>

      {/* ── TAB 0: Exams ── */}
      {tab === 0 && (
        <div className="space-y-4 animate-fade-in">
          <div className="flex justify-between items-center">
            <h2 className="text-xl font-bold text-slate-800">Danh sách đề thi</h2>
            <button id="create-exam-btn" onClick={() => setShowCreateExam(!showCreateExam)} className="btn-primary flex items-center gap-2">
              <Plus className="w-4 h-4" /> Tạo đề thi
            </button>
          </div>

          {showCreateExam && (
            <div className="card animate-slide-up">
              <h3 className="font-semibold mb-4 text-primary-700">📝 Tạo đề thi mới</h3>
              <form onSubmit={handleCreateExam} className="grid grid-cols-2 gap-4">
                <div className="col-span-2">
                  <label className="block text-sm text-slate-600 mb-1 font-medium">Tên đề thi *</label>
                  <input id="exam-title" className="input-field" value={examForm.title}
                    onChange={e => setExamForm(p => ({ ...p, title: e.target.value }))} required />
                </div>
                <div className="col-span-2">
                  <label className="block text-sm text-slate-600 mb-1 font-medium">Mô tả</label>
                  <textarea className="input-field h-20 resize-none" value={examForm.description}
                    onChange={e => setExamForm(p => ({ ...p, description: e.target.value }))} />
                </div>
                <div>
                  <label className="block text-sm text-slate-600 mb-1 font-medium">Chủ đề / Môn học</label>
                  <input className="input-field" value={examForm.category}
                    onChange={e => setExamForm(p => ({ ...p, category: e.target.value }))} />
                </div>
                <div>
                  <label className="block text-sm text-slate-600 mb-1 font-medium">Thời gian (phút)</label>
                  <input type="number" className="input-field" value={examForm.durationMinutes}
                    onChange={e => setExamForm(p => ({ ...p, durationMinutes: e.target.value }))} min={5} max={180} />
                </div>
                <div>
                  <label className="block text-sm text-slate-600 mb-1 font-medium">Điểm đạt (%)</label>
                  <input type="number" className="input-field" value={examForm.passScore}
                    onChange={e => setExamForm(p => ({ ...p, passScore: e.target.value }))} min={0} max={100} />
                </div>
                <div className="flex items-end gap-2">
                  <button type="submit" className="btn-primary">Tạo ngay</button>
                  <button type="button" onClick={() => setShowCreateExam(false)} className="btn-secondary">Hủy</button>
                </div>
              </form>
            </div>
          )}

          <div className="space-y-3">
            {exams.map(exam => (
              <div key={exam.examId} className="card">
                <div className="flex items-center gap-4">
                  <div className="flex-1">
                    <div className="flex items-center gap-2 mb-1">
                      <h3 className="font-semibold text-slate-800">{exam.title}</h3>
                      <span className={`text-xs px-2 py-0.5 rounded-full font-medium ${
                        exam.status === 'PUBLISHED' ? 'bg-emerald-50 text-emerald-700 border border-emerald-200' :
                        exam.status === 'DRAFT' ? 'bg-amber-50 text-amber-700 border border-amber-200' :
                        'bg-slate-100 text-slate-600 border border-slate-200'
                      }`}>{exam.status}</span>
                    </div>
                    <div className="flex gap-4 text-sm text-slate-500">
                      <span>📚 {exam.questionCount} câu</span>
                      <span>⏱️ {exam.durationMinutes} phút</span>
                      {exam.category && <span>🏷️ {exam.category}</span>}
                    </div>
                  </div>
                  <div className="flex gap-2">
                    {exam.status === 'DRAFT' && (
                      <button id={`publish-exam-${exam.examId}`} onClick={() => handlePublish(exam.examId)} className="btn-success py-1.5 px-3 text-sm">
                        Công bố
                      </button>
                    )}
                    <button onClick={() => { setAiForm(p => ({ ...p, examId: exam.examId.toString() })); setTab(2); }}
                      className="btn-secondary py-1.5 px-3 text-sm flex items-center gap-1">
                      <Brain className="w-3.5 h-3.5" /> AI
                    </button>
                    <button onClick={() => handleLoadStats(exam.examId)} className="btn-secondary py-1.5 px-3 text-sm flex items-center gap-1">
                      <BarChart2 className="w-3.5 h-3.5" /> Stats
                    </button>
                    <button
                      id={`delete-exam-${exam.examId}`}
                      onClick={() => handleDeleteExam(exam)}
                      disabled={deletingId === exam.examId}
                      className="btn-secondary py-1.5 px-3 text-sm flex items-center gap-1 text-red-600 hover:bg-red-50 hover:border-red-300 transition-colors"
                      title="Xóa đề thi"
                    >
                      {deletingId === exam.examId ? (
                        <Loader2 className="w-3.5 h-3.5 animate-spin" />
                      ) : (
                        <Trash2 className="w-3.5 h-3.5" />
                      )}
                      Xóa
                    </button>
                  </div>
                </div>
                {stats?.examId === exam.examId && (
                  <div className="mt-4 pt-4 border-t border-slate-100 grid grid-cols-4 gap-3 animate-fade-in">
                    {[
                      { label: 'Lượt thi', value: stats.totalAttempts, color: 'text-primary-600' },
                      { label: 'Điểm TB', value: `${stats.averageScore}%`, color: 'text-amber-600' },
                      { label: 'Tỉ lệ đạt', value: `${stats.passRate}%`, color: 'text-emerald-600' },
                      { label: 'Cao nhất', value: `${stats.highestScore}%`, color: 'text-cyan-600' },
                    ].map(({ label, value, color }) => (
                      <div key={label} className="bg-slate-50 border border-slate-200/80 rounded-xl p-3 text-center">
                        <div className={`text-xl font-bold ${color}`}>{value}</div>
                        <div className="text-xs text-slate-500">{label}</div>
                      </div>
                    ))}
                  </div>
                )}
              </div>
            ))}
          </div>
        </div>
      )}

      {/* ── TAB 1: Review Pending ── */}
      {tab === 1 && (
        <div className="animate-fade-in">
          <div className="flex justify-between items-center mb-4">
            <h2 className="text-xl font-bold text-slate-800">Câu hỏi chờ duyệt ({pending.length})</h2>
            {pending.length > 0 && (
              <button id="approve-all-btn" onClick={handleApproveAll} disabled={loading} className="btn-success flex items-center gap-2">
                {loading ? <Loader2 className="w-4 h-4 animate-spin" /> : <CheckCircle className="w-4 h-4" />}
                Duyệt tất cả
              </button>
            )}
          </div>
          {pending.length === 0 ? (
            <div className="text-center py-20">
              <CheckCircle className="w-16 h-16 text-emerald-300 mx-auto mb-4" />
              <p className="text-slate-500">Không có câu hỏi nào chờ duyệt</p>
            </div>
          ) : (
            <div className="space-y-4">
              {pending.map((q, i) => (
                <div key={q.questionId} className="card border-l-4 border-l-amber-500">
                  <div className="flex items-start justify-between gap-4">
                    <div className="flex-1">
                      <div className="flex items-center gap-2 mb-2">
                        <span className="badge-pending">AI Generated</span>
                        <span className={`text-xs px-2 py-0.5 rounded-full font-medium ${
                          q.difficulty === 'HARD' ? 'bg-red-50 text-red-700 border border-red-200' :
                          q.difficulty === 'MEDIUM' ? 'bg-amber-50 text-amber-700 border border-amber-200' :
                          'bg-emerald-50 text-emerald-700 border border-emerald-200'
                        }`}>
                          {q.difficulty}
                        </span>
                      </div>
                      <p className="font-semibold text-slate-800 mb-3">{q.questionText}</p>
                      <div className="grid grid-cols-2 gap-2">
                        {q.options?.map(opt => (
                          <div key={opt.optionId} className={`text-sm p-2 rounded-lg ${
                            opt.isCorrect ? 'bg-emerald-50 text-emerald-800 border border-emerald-200 font-medium' :
                            'bg-slate-50 border border-slate-200/60 text-slate-700'
                          }`}>
                            <span className="font-bold mr-1">{opt.optionLabel}.</span>{opt.optionText}
                            {opt.isCorrect && ' ✓'}
                          </div>
                        ))}
                      </div>
                      {q.explanation && (
                        <div className="mt-3 p-3 bg-primary-50 border border-primary-200 rounded-xl">
                          <p className="text-xs text-primary-700 font-bold mb-1">💡 Giải thích</p>
                          <p className="text-sm text-slate-700">{q.explanation}</p>
                        </div>
                      )}
                    </div>
                    <div className="flex flex-col gap-2">
                      <button id={`approve-q-${q.questionId}`} onClick={() => handleApprove(q.questionId)} className="btn-success py-1.5 px-3 text-sm flex items-center gap-1">
                        <CheckCircle className="w-4 h-4" /> Duyệt
                      </button>
                      <button id={`reject-q-${q.questionId}`} onClick={() => handleReject(q.questionId)} className="btn-danger py-1.5 px-3 text-sm flex items-center gap-1">
                        <XCircle className="w-4 h-4" /> Từ chối
                      </button>
                    </div>
                  </div>
                </div>
              ))}
            </div>
          )}
        </div>
      )}

      {/* ── TAB 2: AI Generator ── */}
      {tab === 2 && (
        <div className="animate-fade-in">
          <h2 className="text-xl font-bold text-slate-800 mb-4">🤖 Tạo Câu Hỏi Bằng AI</h2>
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
            <div className="card">
              <form onSubmit={handleAIGenerate} className="space-y-4">
                <div>
                  <label className="block text-sm text-slate-600 mb-1 font-medium">Đề thi *</label>
                  <select id="ai-exam-select" className="input-field" value={aiForm.examId}
                    onChange={e => setAiForm(p => ({ ...p, examId: e.target.value }))}>
                    <option value="">-- Chọn đề thi --</option>
                    {exams.map(e => <option key={e.examId} value={e.examId}>{e.title}</option>)}
                  </select>
                </div>
                <div>
                  <label className="block text-sm text-slate-600 mb-1 font-medium">Loại input</label>
                  <div className="flex gap-2">
                    {['DOCUMENT_TEXT', 'TOPIC'].map(t => (
                      <button key={t} type="button"
                        onClick={() => setAiForm(p => ({ ...p, inputType: t }))}
                        className={`flex-1 py-2 rounded-lg text-sm font-medium transition-all ${
                          aiForm.inputType === t ? 'bg-primary-600 text-white shadow-sm' : 'bg-slate-100 text-slate-600 hover:bg-slate-200 border border-slate-200'
                        }`}>
                        {t === 'DOCUMENT_TEXT' ? '📄 Văn bản' : '💡 Chủ đề'}
                      </button>
                    ))}
                  </div>
                </div>
                <div>
                  <label className="block text-sm text-slate-600 mb-1 font-medium">
                    {aiForm.inputType === 'TOPIC' ? 'Chủ đề *' : 'Nội dung văn bản *'}
                  </label>
                  <textarea
                    id="ai-content-input"
                    className="input-field h-48 resize-none"
                    placeholder={aiForm.inputType === 'TOPIC'
                      ? 'Ví dụ: Lịch sử Việt Nam thời kỳ Bắc thuộc'
                      : 'Dán văn bản, bài báo, tài liệu cần tạo câu hỏi...'}
                    value={aiForm.content}
                    onChange={e => setAiForm(p => ({ ...p, content: e.target.value }))}
                    required
                  />
                </div>
                <div className="grid grid-cols-2 gap-3">
                  <div>
                    <label className="block text-sm text-slate-600 mb-1 font-medium">Số câu hỏi</label>
                    <select className="input-field" value={aiForm.numQuestions}
                      onChange={e => setAiForm(p => ({ ...p, numQuestions: e.target.value }))}>
                      {[3, 5, 10, 15, 20].map(n => <option key={n} value={n}>{n} câu</option>)}
                    </select>
                  </div>
                  <div>
                    <label className="block text-sm text-slate-600 mb-1 font-medium">Độ khó</label>
                    <select className="input-field" value={aiForm.difficulty}
                      onChange={e => setAiForm(p => ({ ...p, difficulty: e.target.value }))}>
                      <option value="EASY">Dễ</option>
                      <option value="MEDIUM">Trung bình</option>
                      <option value="HARD">Khó</option>
                    </select>
                  </div>
                </div>
                <button id="ai-generate-btn" type="submit" disabled={aiLoading} className="btn-primary w-full flex items-center justify-center gap-2">
                  {aiLoading ? <><Loader2 className="w-4 h-4 animate-spin" /> AI đang tạo...</> : <><Brain className="w-4 h-4" /> Tạo câu hỏi</>}
                </button>
              </form>
            </div>

            <div className="card">
              <h3 className="font-semibold text-slate-800 mb-3">📋 Kết quả AI</h3>
              {!aiResult && !aiLoading && (
                <div className="text-center py-12 text-slate-400">
                  <Brain className="w-12 h-12 mx-auto mb-3 opacity-30" />
                  <p className="text-sm">Điền form bên trái và nhấn "Tạo câu hỏi"</p>
                </div>
              )}
              {aiLoading && (
                <div className="text-center py-12">
                  <div className="relative w-20 h-20 mx-auto mb-4">
                    <div className="absolute inset-0 rounded-full border-4 border-primary-200" />
                    <div className="absolute inset-0 rounded-full border-4 border-transparent border-t-primary-600 animate-spin" />
                    <Brain className="absolute inset-0 m-auto w-8 h-8 text-primary-600" />
                  </div>
                  <p className="text-primary-600 font-semibold">AI đang phân tích nội dung...</p>
                  <p className="text-slate-400 text-sm mt-1">Quá trình có thể mất 10-30 giây</p>
                </div>
              )}
              {aiResult && (
                <div className="animate-fade-in">
                  <div className={`p-4 rounded-xl mb-4 ${aiResult.success ? 'bg-emerald-50 border border-emerald-200' : 'bg-red-50 border border-red-200'}`}>
                    {aiResult.success ? (
                      <p className="text-emerald-800 font-semibold">✅ Đã tạo {aiResult.generatedCount} câu hỏi. Đang chờ duyệt.</p>
                    ) : (
                      <p className="text-red-700 font-semibold">❌ {aiResult.errorMessage}</p>
                    )}
                  </div>
                  {aiResult.questions?.slice(0, 3).map((q, i) => (
                    <div key={i} className="mb-3 p-3 bg-slate-50 rounded-xl border border-slate-200/60">
                      <p className="text-sm font-semibold text-slate-800 mb-2">{i + 1}. {q.questionText}</p>
                      <p className="text-xs text-emerald-700 font-medium">✓ {q.options?.find(o => o.isCorrect)?.optionText}</p>
                    </div>
                  ))}
                  {aiResult.generatedCount > 3 && (
                    <p className="text-xs text-slate-500 text-center">...và {aiResult.generatedCount - 3} câu hỏi khác</p>
                  )}
                  {aiResult.success && (
                    <button onClick={() => setTab(1)} className="btn-primary w-full mt-3 text-sm">
                      Đi duyệt câu hỏi →
                    </button>
                  )}
                </div>
              )}
            </div>
          </div>
        </div>
      )}

      {/* ── TAB 3: Users ── */}
      {tab === 3 && (
        <div className="animate-fade-in">
          <h2 className="text-xl font-bold text-slate-800 mb-4">Quản Lý Người Dùng ({users.length})</h2>
          <div className="space-y-2">
            {users.map(u => (
              <div key={u.userId} className="card flex items-center gap-4">
                <div className="w-10 h-10 rounded-xl bg-gradient-to-br from-primary-500 to-cyan-500 flex items-center justify-center text-sm font-bold text-white flex-shrink-0">
                  {u.fullName?.[0] || u.username?.[0]}
                </div>
                <div className="flex-1">
                  <p className="font-semibold text-slate-800">{u.fullName}</p>
                  <p className="text-xs text-slate-500">{u.username} · {u.email}</p>
                </div>
                <span className={`text-xs px-2.5 py-1 rounded-full font-medium ${
                  u.role === 'ADMIN' ? 'bg-red-50 text-red-700 border border-red-200' :
                  u.role === 'TEACHER' ? 'bg-amber-50 text-amber-700 border border-amber-200' :
                  'bg-primary-50 text-primary-700 border border-primary-200'
                }`}>{u.role}</span>
                <button
                  id={`toggle-user-${u.userId}`}
                  onClick={() => handleToggleUser(u.userId)}
                  className={`text-xs px-3 py-1.5 rounded-lg font-medium transition-all ${
                    u.isActive ? 'bg-red-50 text-red-700 hover:bg-red-100 border border-red-200' : 'bg-emerald-50 text-emerald-700 hover:bg-emerald-100 border border-emerald-200'
                  }`}
                >
                  {u.isActive ? 'Khóa' : 'Mở khóa'}
                </button>
              </div>
            ))}
          </div>
        </div>
      )}

      {/* ── TAB 4: Stats ── */}
      {tab === 4 && (
        <div className="animate-fade-in">
          <h2 className="text-xl font-bold text-slate-800 mb-4">Thống Kê Đề Thi</h2>
          <div className="grid gap-4 md:grid-cols-2">
            {exams.map(exam => (
              <div key={exam.examId} className="card">
                <h3 className="font-semibold mb-2 text-slate-800">{exam.title}</h3>
                <p className="text-xs text-slate-500 mb-3">
                  {exam.questionCount} câu · {exam.durationMinutes} phút · {exam.status}
                </p>
                <button onClick={() => handleLoadStats(exam.examId)} className="btn-secondary py-1.5 px-4 text-sm w-full">
                  Xem thống kê
                </button>
                {stats?.examId === exam.examId && (
                  <div className="mt-4 pt-4 border-t border-slate-100 grid grid-cols-2 gap-3 animate-fade-in">
                    <div className="bg-primary-50 border border-primary-100 rounded-xl p-3 text-center">
                      <div className="text-2xl font-bold text-primary-600">{stats.totalAttempts}</div>
                      <div className="text-xs text-slate-500">Lượt thi</div>
                    </div>
                    <div className="bg-amber-50 border border-amber-100 rounded-xl p-3 text-center">
                      <div className="text-2xl font-bold text-amber-600">{stats.averageScore}%</div>
                      <div className="text-xs text-slate-500">Điểm TB</div>
                    </div>
                    <div className="bg-emerald-50 border border-emerald-100 rounded-xl p-3 text-center">
                      <div className="text-2xl font-bold text-emerald-600">{stats.passRate}%</div>
                      <div className="text-xs text-slate-500">Tỉ lệ đạt</div>
                    </div>
                    <div className="bg-cyan-50 border border-cyan-100 rounded-xl p-3 text-center">
                      <div className="text-2xl font-bold text-cyan-600">{stats.highestScore}%</div>
                      <div className="text-xs text-slate-500">Cao nhất</div>
                    </div>
                  </div>
                )}
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  );
}
