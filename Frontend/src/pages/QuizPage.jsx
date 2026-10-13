import { useEffect, useState, useCallback } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { examApi, submissionApi } from '../services/api';
import { Clock, ChevronLeft, ChevronRight, Send, Loader2, AlertCircle } from 'lucide-react';
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
  const [exam, setExam] = useState(null);
  const [submissionId, setSubmissionId] = useState(null);
  const [timeLeft, setTimeLeft] = useState(null);
  const [answers, setAnswers] = useState({});
  const [currentQ, setCurrentQ] = useState(0);
  const [loading, setLoading] = useState(true);
  const [submitting, setSubmitting] = useState(false);

  useEffect(() => {
    const init = async () => {
      try {
        const [examRes, startRes] = await Promise.all([
          examApi.getDetail(examId),
          submissionApi.start(parseInt(examId)),
        ]);
        setExam(examRes.data);
        setSubmissionId(startRes.data.submissionId);
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
  }, [examId]);

  const handleSubmit = useCallback(async () => {
    if (submitting) return;
    setSubmitting(true);
    try {
      const answerList = exam?.questions?.map(q => ({
        questionId: q.questionId,
        selectedOptionId: answers[q.questionId] || null,
      })) || [];
      const res = await submissionApi.submit({ submissionId, answers: answerList });
      toast.success('Nộp bài thành công!');
      navigate(`/result/${res.data.submissionId}`);
    } catch {
      toast.error('Lỗi khi nộp bài!');
      setSubmitting(false);
    }
  }, [submissionId, answers, exam, submitting, navigate]);

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
    <div className="max-w-4xl mx-auto px-4 py-6">
      {/* Header */}
      <div className="card mb-6">
        <div className="flex items-center justify-between">
          <div>
            <h2 className="text-xl font-bold text-slate-800">{exam.title}</h2>
            <p className="text-slate-500 text-sm mt-1">{answered}/{questions.length} câu đã trả lời</p>
          </div>
          <div className={`flex items-center gap-2 text-2xl font-mono font-bold ${timerClass}`}>
            <Clock className="w-6 h-6" />
            {formatTime(timeLeft)}
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
            <p className="text-xs font-semibold text-slate-500 mb-3 uppercase tracking-wide">Câu hỏi</p>
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
          </div>
        </div>

        {/* Question Area */}
        <div className="lg:col-span-3">
          <div className="card">
            <div className="flex items-center gap-2 mb-4">
              <span className="text-xs font-semibold text-slate-500 uppercase tracking-wide">Câu {currentQ + 1}</span>
              <span className={`text-xs px-2 py-0.5 rounded-full font-medium ${
                q?.difficulty === 'HARD' ? 'bg-red-50 text-red-700 border border-red-200' :
                q?.difficulty === 'MEDIUM' ? 'bg-amber-50 text-amber-700 border border-amber-200' :
                'bg-emerald-50 text-emerald-700 border border-emerald-200'
              }`}>{q?.difficulty}</span>
            </div>

            <p className="text-slate-800 text-lg font-semibold leading-relaxed mb-6">
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
                      <span className="text-sm font-normal text-slate-800">{opt.optionText}</span>
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
                  onClick={handleSubmit}
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
