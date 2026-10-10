import { useEffect, useState, useCallback } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { examApi, submissionApi } from '../services/api';
import { Clock, ChevronLeft, ChevronRight, Send, Loader2, AlertCircle } from 'lucide-react';
import toast from 'react-hot-toast';

function useTimer(durationSeconds, onExpire) {
  const [timeLeft, setTimeLeft] = useState(durationSeconds);
  useEffect(() => {
    if (timeLeft <= 0) { onExpire(); return; }
    const t = setTimeout(() => setTimeLeft(t => t - 1), 1000);
    return () => clearTimeout(t);
  }, [timeLeft]);
  return timeLeft;
}

function formatTime(sec) {
  const m = Math.floor(sec / 60).toString().padStart(2, '0');
  const s = (sec % 60).toString().padStart(2, '0');
  return `${m}:${s}`;
}

export default function QuizPage() {
  const { examId } = useParams();
  const navigate = useNavigate();
  const [exam, setExam] = useState(null);
  const [submissionId, setSubmissionId] = useState(null);
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
      const answerList = exam.questions.map(q => ({
        questionId: q.questionId,
        selectedOptionId: answers[q.questionId] || null,
      }));
      const res = await submissionApi.submit({ submissionId, answers: answerList });
      toast.success('Nộp bài thành công!');
      navigate(`/result/${res.data.submissionId}`);
    } catch {
      toast.error('Lỗi khi nộp bài!');
      setSubmitting(false);
    }
  }, [submissionId, answers, exam, submitting]);

  const timeLeft = useTimer(
    exam ? exam.durationMinutes * 60 : 3600,
    handleSubmit
  );

  if (loading) return (
    <div className="flex items-center justify-center min-h-[60vh]">
      <Loader2 className="w-12 h-12 text-primary-400 animate-spin" />
    </div>
  );

  if (!exam) return null;
  const questions = exam.questions || [];
  const q = questions[currentQ];
  const answered = Object.keys(answers).length;
  const progress = (answered / questions.length) * 100;
  const timerClass = timeLeft < 60 ? 'timer-danger' : timeLeft < 300 ? 'timer-warning' : 'timer-normal';

  return (
    <div className="max-w-4xl mx-auto px-4 py-6">
      {/* Header */}
      <div className="card mb-6">
        <div className="flex items-center justify-between">
          <div>
            <h2 className="text-xl font-bold text-gray-100">{exam.title}</h2>
            <p className="text-gray-400 text-sm mt-1">{answered}/{questions.length} câu đã trả lời</p>
          </div>
          <div className={`flex items-center gap-2 text-2xl font-mono font-bold ${timerClass}`}>
            <Clock className="w-6 h-6" />
            {formatTime(timeLeft)}
          </div>
        </div>
        {/* Progress bar */}
        <div className="mt-4 h-2 bg-white/10 rounded-full overflow-hidden">
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
            <p className="text-xs font-medium text-gray-400 mb-3 uppercase tracking-wide">Câu hỏi</p>
            <div className="grid grid-cols-5 lg:grid-cols-4 gap-1.5">
              {questions.map((_, i) => (
                <button
                  key={i}
                  id={`nav-q-${i + 1}`}
                  onClick={() => setCurrentQ(i)}
                  className={`w-9 h-9 rounded-lg text-xs font-semibold transition-all ${
                    i === currentQ ? 'bg-primary-500 text-white scale-110' :
                    answers[questions[i]?.questionId] ? 'bg-emerald-500/30 text-emerald-300 border border-emerald-500/30' :
                    'bg-white/5 text-gray-400 hover:bg-white/10'
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
              <span className="text-xs font-medium text-gray-500 uppercase tracking-wide">Câu {currentQ + 1}</span>
              <span className={`text-xs px-2 py-0.5 rounded-full ${
                q?.difficulty === 'HARD' ? 'bg-red-500/20 text-red-300' :
                q?.difficulty === 'MEDIUM' ? 'bg-yellow-500/20 text-yellow-300' :
                'bg-emerald-500/20 text-emerald-300'
              }`}>{q?.difficulty}</span>
            </div>

            <p className="text-gray-100 text-lg font-medium leading-relaxed mb-6">
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
                        selected ? 'bg-primary-500 text-white' : 'bg-white/10 text-gray-400'
                      }`}>{opt.optionLabel}</span>
                      <span className="text-sm">{opt.optionText}</span>
                    </div>
                  </button>
                );
              })}
            </div>

            {/* Navigation */}
            <div className="flex items-center justify-between mt-6 pt-4 border-t border-white/10">
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
