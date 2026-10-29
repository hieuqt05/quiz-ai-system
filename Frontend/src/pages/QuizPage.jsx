import { useEffect, useState, useCallback, useRef } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { examApi, submissionApi } from '../services/api';
import {
  Clock, ChevronLeft, ChevronRight, Send, Loader2,
  AlertTriangle, ShieldAlert, CheckCircle2, Save, Maximize2
} from 'lucide-react';
import toast from 'react-hot-toast';

function formatTime(sec) {
  if (sec === null || sec === undefined) return '--:--';
  const m = Math.floor(sec / 60).toString().padStart(2, '0');
  const s = (sec % 60).toString().padStart(2, '0');
  return `${m}:${s}`;
}

export default function QuizPage() {
  const { examId } = useParams();
  const navigate = useNavigate();

  // State chính
  const [exam, setExam] = useState(null);
  const [submissionId, setSubmissionId] = useState(null);
  const [timeLeft, setTimeLeft] = useState(null);
  const [answers, setAnswers] = useState({});
  const [currentQ, setCurrentQ] = useState(0);
  const [loading, setLoading] = useState(true);
  const [submitting, setSubmitting] = useState(false);
  const [lastSavedTime, setLastSavedTime] = useState(null);

  // Chống gian lận: Vi phạm chuyển tab
  const [violationCount, setViolationCount] = useState(0);
  const [violationModal, setViolationModal] = useState(null);
  const [isScreenBlanks, setIsScreenBlanks] = useState(false);
  const submittingRef = useRef(false);

  // Thông tin thí sinh hiển thị Watermark
  const currentUser = (() => {
    try {
      return JSON.parse(localStorage.getItem('quiz_user')) || { fullName: 'Thí sinh', username: 'student' };
    } catch {
      return { fullName: 'Thí sinh', username: 'student' };
    }
  })();

  // 1. KHỞI TẠO BÀI THI & TRỘN ĐỀ NGẪU NHIÊN
  useEffect(() => {
    const init = async () => {
      try {
        const [examRes, startRes] = await Promise.all([
          examApi.getDetail(examId),
          submissionApi.start(parseInt(examId)),
        ]);

        const subId = startRes.data.submissionId;
        setSubmissionId(subId);

        // Khôi phục số lần vi phạm đã ghi nhận trước đó (nếu F5 trang)
        const savedViolations = parseInt(sessionStorage.getItem(`quiz_violations_${subId}`) || '0', 10);
        setViolationCount(savedViolations);

        // Trộn đề ngẫu nhiên (Câu hỏi & Đáp án) cho từng lượt thi
        const shuffleKey = `quiz_shuffled_exam_${subId}`;
        let finalQuestions = [];
        const cachedShuffle = sessionStorage.getItem(shuffleKey);

        if (cachedShuffle) {
          finalQuestions = JSON.parse(cachedShuffle);
        } else {
          // Trộn thứ tự câu hỏi (Fisher-Yates shuffle)
          const shuffledQuestions = [...(examRes.data.questions || [])].sort(() => Math.random() - 0.5);

          // Trộn thứ tự đáp án A, B, C, D của từng câu
          const labels = ['A', 'B', 'C', 'D', 'E', 'F'];
          finalQuestions = shuffledQuestions.map(q => {
            const shuffledOptions = [...(q.options || [])].sort(() => Math.random() - 0.5);
            const relabeledOptions = shuffledOptions.map((opt, idx) => ({
              ...opt,
              optionLabel: labels[idx] || opt.optionLabel
            }));
            return {
              ...q,
              options: relabeledOptions
            };
          });
          sessionStorage.setItem(shuffleKey, JSON.stringify(finalQuestions));
        }

        setExam({ ...examRes.data, questions: finalQuestions });

        // Khôi phục câu trả lời đã lưu từ LocalStorage (Auto-Save)
        const cachedAnswers = localStorage.getItem(`quiz_answers_${subId}`);
        if (cachedAnswers) {
          try {
            const parsed = JSON.parse(cachedAnswers);
            if (parsed && typeof parsed === 'object') {
              setAnswers(parsed);
              setLastSavedTime(new Date().toLocaleTimeString('vi-VN'));
            }
          } catch (e) {
            console.error('Lỗi đọc auto-save:', e);
          }
        }

        const remaining = startRes.data.remainingSeconds ?? (examRes.data.durationMinutes * 60);
        setTimeLeft(remaining);
      } catch (err) {
        toast.error('Không thể bắt đầu bài thi!');
        navigate('/exams');
      } finally {
        setLoading(false);
      }
    };
    init();
  }, [examId, navigate]);

  // 2. TỰ ĐỘNG LƯU ĐÁP ÁN (AUTO-SAVE) VÀO LOCALSTORAGE
  useEffect(() => {
    if (!submissionId || Object.keys(answers).length === 0) return;
    try {
      localStorage.setItem(`quiz_answers_${submissionId}`, JSON.stringify(answers));
      setLastSavedTime(new Date().toLocaleTimeString('vi-VN'));
    } catch (e) {
      console.error('Lỗi ghi auto-save:', e);
    }
  }, [answers, submissionId]);

  // 3. HÀM NỘP BÀI (HỖ TRỢ TRUYỀN SỐ LẦN VI PHẠM)
  const handleSubmit = useCallback(async (forcedViolationCount) => {
    if (submittingRef.current) return;
    submittingRef.current = true;
    setSubmitting(true);

    try {
      const currentViolations = typeof forcedViolationCount === 'number'
        ? forcedViolationCount
        : parseInt(sessionStorage.getItem(`quiz_violations_${submissionId}`) || '0', 10);

      const answerList = exam?.questions?.map(q => ({
        questionId: q.questionId,
        selectedOptionId: answers[q.questionId] || null,
      })) || [];

      const res = await submissionApi.submit({
        submissionId,
        answers: answerList,
        violationCount: currentViolations
      });

      // Dọn dẹp dữ liệu tạm sau khi nộp thành công
      localStorage.removeItem(`quiz_answers_${submissionId}`);
      sessionStorage.removeItem(`quiz_shuffled_exam_${submissionId}`);
      sessionStorage.removeItem(`quiz_violations_${submissionId}`);

      toast.success('Nộp bài thành công!');
      navigate(`/result/${res.data.submissionId}`);
    } catch {
      toast.error('Lỗi khi nộp bài!');
      setSubmitting(false);
      submittingRef.current = false;
    }
  }, [submissionId, answers, exam, navigate]);

  // 4. CHỐNG GIAN LẬN: PHÁT HIỆN CHUYỂN TAB / THU NHỎ / ALT+TAB
  useEffect(() => {
    if (!submissionId || loading || submitting) return;

    const recordViolation = (reason) => {
      if (submittingRef.current) return;

      setViolationCount(prev => {
        const next = prev + 1;
        sessionStorage.setItem(`quiz_violations_${submissionId}`, next.toString());

        if (next >= 3) {
          // Vi phạm 3 lần -> Tự động nộp bài lập tức
          toast.error('BẠN ĐÃ VI PHẠM QUY CHẾ 3 LẦN! HỆ THỐNG TỰ ĐỘNG THU HỒI BÀI THI!', {
            duration: 8000,
            icon: '🚨'
          });
          handleSubmit(next);
        } else {
          setViolationModal({
            count: next,
            max: 3,
            reason: reason || 'Rời khỏi màn hình làm bài thi (Chuyển tab / Mở ứng dụng khác)'
          });
        }
        return next;
      });
    };

    const handleVisibilityChange = () => {
      if (document.hidden) {
        recordViolation('Chuyển tab trình duyệt hoặc thu nhỏ cửa sổ');
      }
    };

    const handleWindowBlur = () => {
      recordViolation('Mất tiêu điểm màn hình thi (Alt + Tab hoặc nhấp ra ngoài ứng dụng)');
    };

    document.addEventListener('visibilitychange', handleVisibilityChange);
    window.addEventListener('blur', handleWindowBlur);

    return () => {
      document.removeEventListener('visibilitychange', handleVisibilityChange);
      window.removeEventListener('blur', handleWindowBlur);
    };
  }, [submissionId, loading, submitting, handleSubmit]);

  // 5. CHỐNG CHỤP MÀN HÌNH, COPY, IN ẤN VÀ PHÍM TẮT GIAN LẬN
  useEffect(() => {
    const handleKeyDown = (e) => {
      // 1. Phím PrintScreen hoặc Alt+PrintScreen
      if (e.key === 'PrintScreen' || e.code === 'PrintScreen') {
        e.preventDefault();
        try {
          navigator.clipboard?.writeText('QuizAI: Thao tác chụp màn hình đã bị vô hiệu hóa!');
        } catch {}
        setIsScreenBlanks(true);
        setTimeout(() => setIsScreenBlanks(false), 800);
        toast.error('CẢNH BÁO: Thao tác chụp màn hình (PrintScreen) bị nghiêm cấm!', { icon: '📸' });
        return false;
      }

      // 2. Chặn Ctrl + P (In trang web)
      if ((e.ctrlKey || e.metaKey) && (e.key === 'p' || e.key === 'P')) {
        e.preventDefault();
        toast.error('Chức năng in bài thi đã bị vô hiệu hóa!', { icon: '🖨️' });
        return false;
      }

      // 3. Chặn Ctrl + C, Ctrl + X, Ctrl + A (Sao chép văn bản câu hỏi)
      if ((e.ctrlKey || e.metaKey) && ['c', 'C', 'x', 'X', 'a', 'A', 'u', 'U'].includes(e.key)) {
        e.preventDefault();
        toast.error('Sao chép nội dung bài thi bị nghiêm cấm!', { icon: '🚫' });
        return false;
      }

      // 4. Chặn F12, Ctrl + Shift + I/J/C (Mở Developer Tools soi đáp án)
      if (
        e.key === 'F12' ||
        ((e.ctrlKey || e.metaKey) && e.shiftKey && ['I', 'i', 'J', 'j', 'C', 'c'].includes(e.key))
      ) {
        e.preventDefault();
        toast.error('Công cụ phát triển (DevTools) đã bị khóa!', { icon: '🔒' });
        return false;
      }
    };

    const handleCopy = (e) => {
      e.preventDefault();
      toast.error('Không được phép sao chép nội dung đề thi!', { icon: '🛡️' });
    };

    window.addEventListener('keydown', handleKeyDown);
    document.addEventListener('copy', handleCopy);

    return () => {
      window.removeEventListener('keydown', handleKeyDown);
      document.removeEventListener('copy', handleCopy);
    };
  }, []);

  // 6. ĐỒNG HỒ ĐẾM NGƯỢC
  useEffect(() => {
    if (timeLeft === null || timeLeft <= 0) return;

    const timer = setInterval(() => {
      setTimeLeft(prev => {
        if (prev === null) return null;
        if (prev <= 1) {
          clearInterval(timer);
          handleSubmit();
          return 0;
        }
        return prev - 1;
      });
    }, 1000);

    return () => clearInterval(timer);
  }, [timeLeft === null, handleSubmit]);

  // Bật chế độ Fullscreen
  const requestFullScreen = () => {
    if (!document.fullscreenElement) {
      document.documentElement.requestFullscreen().catch(() => {});
    }
  };

  if (loading) return (
    <div className="flex items-center justify-center min-h-[60vh]">
      <Loader2 className="w-12 h-12 text-primary-400 animate-spin" />
    </div>
  );

  if (!exam) return null;
  const questions = exam.questions || [];
  const q = questions[currentQ];
  const answered = Object.keys(answers).length;
  const progress = questions.length > 0 ? (answered / questions.length) * 100 : 0;
  const timerClass = (timeLeft !== null && timeLeft < 60) ? 'timer-danger' : (timeLeft !== null && timeLeft < 300) ? 'timer-warning' : 'timer-normal';

  return (
    <div
      onContextMenu={(e) => {
        e.preventDefault();
        toast('Chuột phải đã bị khóa để bảo mật đề thi!', { icon: '🛡️' });
      }}
      className="max-w-4xl mx-auto px-4 py-6 relative select-none"
      style={{ WebkitUserSelect: 'none', userSelect: 'none' }}
    >
      {/* Màn hình chớp đen khi phát hiện PrintScreen */}
      {isScreenBlanks && (
        <div className="fixed inset-0 bg-black z-50 flex items-center justify-center text-white text-2xl font-bold">
          [ẢNH CHỤP ĐÃ BỊ CHE ĐỂ BẢO VỆ ĐỀ THI]
        </div>
      )}

      {/* WATERMARK CHỐNG CHỤP MÀN HÌNH BẰNG ĐIỆN THOẠI */}
      <div
        className="fixed inset-0 pointer-events-none z-10 opacity-[0.035] flex flex-wrap content-around justify-around overflow-hidden select-none"
        aria-hidden="true"
      >
        {Array.from({ length: 24 }).map((_, idx) => (
          <div key={idx} className="transform -rotate-45 text-sm font-bold text-slate-900 tracking-wider p-6">
            {currentUser.fullName} • {currentUser.username} • QuizAI Secure
          </div>
        ))}
      </div>

      {/* POPUP CẢNH BÁO VI PHẠM QUY CHẾ (CHUYỂN TAB) */}
      {violationModal && (
        <div className="fixed inset-0 z-50 bg-slate-900/80 backdrop-blur-sm flex items-center justify-center p-4">
          <div className="card max-w-md w-full border-2 border-red-500 shadow-2xl animate-bounce-short text-center">
            <div className="w-16 h-16 rounded-full bg-red-100 flex items-center justify-center mx-auto mb-4">
              <ShieldAlert className="w-10 h-10 text-red-600 animate-pulse" />
            </div>
            <h3 className="text-xl font-bold text-red-600 mb-2">CẢNH BÁO VI PHẠM QUY CHẾ!</h3>
            <p className="text-slate-600 text-sm mb-4 leading-relaxed">
              Hệ thống phát hiện hành vi: <br />
              <strong className="text-slate-900 font-semibold">{violationModal.reason}</strong>
            </p>

            <div className="p-3 bg-red-50 rounded-xl border border-red-200 mb-6">
              <div className="text-sm font-medium text-red-800">
                Số lần vi phạm: <span className="text-lg font-black text-red-600">{violationModal.count}</span> / {violationModal.max}
              </div>
              <p className="text-xs text-red-500 mt-1">
                {violationModal.count >= 2
                  ? '⚠️ CHÚ Ý: Vi phạm thêm 1 lần nữa bài thi sẽ bị TỰ ĐỘNG THU HỒI VÀ CHẤM ĐIỂM!'
                  : 'Nghiêm cấm chuyển tab, mở tài liệu hoặc chia sẻ màn hình trong lúc làm bài.'}
              </p>
            </div>

            <button
              onClick={() => setViolationModal(null)}
              className="btn-primary w-full py-2.5 font-bold bg-red-600 hover:bg-red-700"
            >
              Tôi cam kết không tái phạm & Tiếp tục làm bài
            </button>
          </div>
        </div>
      )}

      {/* Header bài thi */}
      <div className="card mb-6">
        <div className="flex flex-col md:flex-row md:items-center justify-between gap-4">
          <div>
            <div className="flex items-center gap-2">
              <h2 className="text-xl font-bold text-slate-800">{exam.title}</h2>
              <span className="text-xs px-2 py-0.5 rounded-full font-medium bg-emerald-50 text-emerald-700 border border-emerald-200">
                Đã xáo trộn câu & đáp án
              </span>
            </div>
            <div className="flex items-center gap-3 text-slate-500 text-xs mt-1">
              <span>{answered}/{questions.length} câu đã trả lời</span>
              <span>•</span>
              {lastSavedTime ? (
                <span className="text-emerald-600 flex items-center gap-1 font-medium">
                  <Save className="w-3.5 h-3.5" /> Đã tự động lưu ({lastSavedTime})
                </span>
              ) : (
                <span>Tự động lưu đang bật</span>
              )}
            </div>
          </div>

          <div className="flex items-center gap-4">
            {/* Hiển thị số lần vi phạm nếu có */}
            {violationCount > 0 && (
              <div className="flex items-center gap-1 text-xs px-2.5 py-1 rounded-lg bg-red-50 text-red-700 border border-red-200 font-semibold animate-pulse">
                <AlertTriangle className="w-3.5 h-3.5" /> Vi phạm: {violationCount}/3
              </div>
            )}

            {/* Nút bật toàn màn hình */}
            <button
              onClick={requestFullScreen}
              title="Bật chế độ thi Toàn màn hình"
              className="p-2 rounded-lg bg-slate-100 hover:bg-slate-200 text-slate-600 text-xs flex items-center gap-1"
            >
              <Maximize2 className="w-4 h-4" />
            </button>

            {/* Đồng hồ đếm ngược */}
            <div className={`flex items-center gap-2 text-2xl font-mono font-bold ${timerClass}`}>
              <Clock className="w-6 h-6" />
              {formatTime(timeLeft)}
            </div>
          </div>
        </div>

        {/* Progress bar */}
        <div className="mt-4 h-2 bg-slate-200 rounded-full overflow-hidden">
          <div
            className="h-full bg-gradient-to-r from-primary-500 to-cyan-500 rounded-full transition-all duration-500"
            style={{ width: `${progress}%` }}
          />
        </div>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-4 gap-6">
        {/* Question Navigator */}
        <div className="lg:col-span-1">
          <div className="card">
            <p className="text-xs font-semibold text-slate-500 mb-3 uppercase tracking-wide">Danh sách câu hỏi</p>
            <div className="grid grid-cols-5 lg:grid-cols-4 gap-1.5">
              {questions.map((_, i) => (
                <button
                  key={i}
                  id={`nav-q-${i + 1}`}
                  onClick={() => setCurrentQ(i)}
                  className={`w-9 h-9 rounded-lg text-xs font-semibold transition-all ${
                    i === currentQ ? 'bg-primary-600 text-white scale-110 shadow-sm' :
                    answers[questions[i]?.questionId] ? 'bg-emerald-100 text-emerald-800 border border-emerald-300 font-bold' :
                    'bg-slate-100 text-slate-600 hover:bg-slate-200 border border-slate-200'
                  }`}
                >
                  {i + 1}
                </button>
              ))}
            </div>

            <div className="mt-6 pt-4 border-t border-slate-100 text-xs text-slate-500 space-y-2">
              <div className="flex items-center gap-2">
                <span className="w-3 h-3 rounded bg-emerald-100 border border-emerald-300"></span>
                <span>Đã trả lời</span>
              </div>
              <div className="flex items-center gap-2">
                <span className="w-3 h-3 rounded bg-slate-100 border border-slate-200"></span>
                <span>Chưa trả lời</span>
              </div>
            </div>
          </div>
        </div>

        {/* Question Area */}
        <div className="lg:col-span-3">
          <div className="card relative">
            <div className="flex items-center justify-between mb-4">
              <div className="flex items-center gap-2">
                <span className="text-xs font-semibold text-slate-500 uppercase tracking-wide">Câu {currentQ + 1}</span>
                <span className={`text-xs px-2 py-0.5 rounded-full font-medium ${
                  q?.difficulty === 'HARD' ? 'bg-red-50 text-red-700 border border-red-200' :
                  q?.difficulty === 'MEDIUM' ? 'bg-amber-50 text-amber-700 border border-amber-200' :
                  'bg-emerald-50 text-emerald-700 border border-emerald-200'
                }`}>{q?.difficulty}</span>
              </div>

              {answers[q?.questionId] && (
                <span className="text-xs text-emerald-600 font-medium flex items-center gap-1">
                  <CheckCircle2 className="w-3.5 h-3.5" /> Đã chọn
                </span>
              )}
            </div>

            <p className="text-slate-800 text-lg font-semibold leading-relaxed mb-6 select-none">
              {q?.questionText}
            </p>

            <div className="space-y-3">
              {q?.options?.map(opt => {
                const selected = answers[q.questionId] === opt.optionId;
                return (
                  <button
                    key={opt.optionId}
                    id={`option-${opt.optionLabel}`}
                    onClick={() => setAnswers(prev => ({ ...prev, [q.questionId]: opt.optionId }))}
                    className={`option-btn ${selected ? 'option-selected' : 'option-default'}`}
                  >
                    <div className="flex items-center gap-3">
                      <span className={`w-8 h-8 rounded-lg flex items-center justify-center text-sm font-bold flex-shrink-0 ${
                        selected ? 'bg-primary-600 text-white' : 'bg-slate-100 text-slate-700 border border-slate-200'
                      }`}>{opt.optionLabel}</span>
                      <span className="text-sm font-normal text-slate-800 text-left">{opt.optionText}</span>
                    </div>
                  </button>
                );
              })}
            </div>

            {/* Navigation */}
            <div className="flex items-center justify-between mt-6 pt-4 border-t border-slate-200">
              <button
                id="prev-question"
                onClick={() => setCurrentQ(p => Math.max(0, p - 1))}
                disabled={currentQ === 0}
                className="btn-secondary flex items-center gap-2 py-2 px-4 text-sm"
              >
                <ChevronLeft className="w-4 h-4" /> Trước
              </button>

              {currentQ === questions.length - 1 ? (
                <button
                  id="submit-exam"
                  onClick={() => handleSubmit()}
                  disabled={submitting}
                  className="btn-primary flex items-center gap-2"
                >
                  {submitting ? <Loader2 className="w-4 h-4 animate-spin" /> : <Send className="w-4 h-4" />}
                  Nộp bài
                </button>
              ) : (
                <button
                  id="next-question"
                  onClick={() => setCurrentQ(p => Math.min(questions.length - 1, p + 1))}
                  className="btn-primary flex items-center gap-2"
                >
                  Tiếp <ChevronRight className="w-4 h-4" />
                </button>
              )}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
