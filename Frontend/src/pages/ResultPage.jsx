import { useEffect, useState } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { submissionApi } from '../services/api';
import { CheckCircle, XCircle, Trophy, Clock, Target, ChevronDown, ChevronUp, RotateCcw, Loader2 } from 'lucide-react';

export default function ResultPage() {
  const { submissionId } = useParams();
  const navigate = useNavigate();
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(true);
  const [expandedQ, setExpandedQ] = useState(null);

  useEffect(() => {
    submissionApi.getResult(submissionId)
      .then(r => setResult(r.data))
      .catch(() => navigate('/exams'))
      .finally(() => setLoading(false));
  }, [submissionId]);

  if (loading) return (
    <div className="flex items-center justify-center min-h-[60vh]">
      <Loader2 className="w-12 h-12 text-primary-400 animate-spin" />
    </div>
  );
  if (!result) return null;

  const passed = result.totalScore >= 50;
  const scoreColor = result.totalScore >= 80 ? 'text-emerald-400' : result.totalScore >= 50 ? 'text-yellow-400' : 'text-red-400';

  return (
    <div className="max-w-3xl mx-auto px-4 py-8">
      {/* Score Card */}
      <div className="card text-center mb-6 animate-slide-up relative overflow-hidden">
        <div className={`absolute inset-0 opacity-10 ${passed ? 'bg-emerald-500' : 'bg-red-500'}`} />
        <div className="relative z-10">
          <Trophy className={`w-16 h-16 mx-auto mb-4 ${passed ? 'text-amber-500' : 'text-slate-400'}`} />
          <h1 className="text-2xl font-bold text-slate-800 mb-1">{result.examTitle}</h1>
          <div className={`text-7xl font-black my-4 ${scoreColor}`}>
            {result.totalScore.toFixed(0)}
            <span className="text-3xl">%</span>
          </div>
          <div className={`text-xl font-bold mb-4 ${passed ? 'text-emerald-600' : 'text-red-600'}`}>
            {passed ? '🎉 Chúc mừng! Bạn đã đạt yêu cầu!' : '💪 Cố lên! Hãy thử lại lần nữa!'}
          </div>
          <div className="grid grid-cols-3 gap-4 mt-4">
            {[
              { icon: CheckCircle, label: 'Đúng', value: result.correctAnswers, color: 'text-emerald-600' },
              { icon: Target, label: 'Tổng câu', value: result.totalQuestions, color: 'text-primary-600' },
              { icon: Clock, label: 'Thời gian', value: `${Math.floor(result.timeTaken / 60)}:${String(result.timeTaken % 60).padStart(2, '0')}`, color: 'text-cyan-600' },
            ].map(({ icon: Icon, label, value, color }) => (
              <div key={label} className="bg-slate-50 border border-slate-200/80 rounded-xl p-3">
                <Icon className={`w-6 h-6 ${color} mx-auto mb-1`} />
                <div className="text-xl font-bold text-slate-800">{value}</div>
                <div className="text-xs text-slate-500">{label}</div>
              </div>
            ))}
          </div>

          {/* Giám sát quy chế thi */}
          <div className="mt-4 pt-3 border-t border-slate-100 flex items-center justify-center">
            {result.violationCount > 0 ? (
              <div className="inline-flex items-center gap-2 px-3 py-1.5 rounded-lg bg-red-50 border border-red-200 text-red-700 text-xs font-semibold">
                ⚠️ Ghi nhận vi phạm quy chế: Rời màn hình {result.violationCount} lần
              </div>
            ) : (
              <div className="inline-flex items-center gap-2 px-3 py-1.5 rounded-lg bg-emerald-50 border border-emerald-200 text-emerald-700 text-xs font-semibold">
                🛡️ Giám sát thi: Trung thực, không phát hiện vi phạm
              </div>
            )}
          </div>
        </div>
      </div>

      {/* Detailed Results */}
      <div className="mb-6">
        <h2 className="text-xl font-bold mb-4 gradient-text">Chi tiết từng câu hỏi</h2>
        <div className="space-y-3">
          {result.details?.map((detail, i) => (
            <div key={detail.questionId} className={`card border-l-4 ${detail.isCorrect ? 'border-l-emerald-500' : 'border-l-red-500'}`}>
              <button
                id={`result-q-${i + 1}`}
                onClick={() => setExpandedQ(expandedQ === i ? null : i)}
                className="w-full text-left"
              >
                <div className="flex items-start gap-3">
                  {detail.isCorrect
                    ? <CheckCircle className="w-5 h-5 text-emerald-600 flex-shrink-0 mt-0.5" />
                    : <XCircle className="w-5 h-5 text-red-500 flex-shrink-0 mt-0.5" />
                  }
                  <div className="flex-1">
                    <div className="flex items-center gap-2 mb-1">
                      <span className="text-xs text-slate-400">Câu {i + 1}</span>
                      {detail.selectedLabel && (
                        <span className="text-xs text-slate-500">Bạn chọn: <span className="font-bold text-slate-800">{detail.selectedLabel}</span></span>
                      )}
                      {!detail.isCorrect && (
                        <span className="text-xs text-slate-500">Đáp án đúng: <span className="font-bold text-emerald-600">{detail.correctLabel}</span></span>
                      )}
                    </div>
                    <p className="text-sm text-slate-800 font-medium">{detail.questionText}</p>
                  </div>
                  {expandedQ === i ? <ChevronUp className="w-4 h-4 text-slate-400" /> : <ChevronDown className="w-4 h-4 text-slate-400" />}
                </div>
              </button>

              {expandedQ === i && (
                <div className="mt-4 pt-4 border-t border-slate-100 animate-fade-in">
                  <div className="space-y-2 mb-4">
                    {detail.options?.map(opt => (
                      <div key={opt.optionId} className={`flex items-center gap-3 p-3 rounded-xl text-sm ${
                        opt.isCorrect ? 'bg-emerald-50 border border-emerald-200 text-emerald-800' :
                        opt.optionLabel === detail.selectedLabel && !opt.isCorrect ? 'bg-red-50 border border-red-200 text-red-800' :
                        'bg-slate-50 border border-slate-200/60 text-slate-700'
                      }`}>
                        <span className="font-bold w-5">{opt.optionLabel}.</span>
                        <span>{opt.optionText}</span>
                        {opt.isCorrect && <CheckCircle className="w-4 h-4 ml-auto text-emerald-600" />}
                      </div>
                    ))}
                  </div>
                  {detail.explanation && (
                    <div className="bg-primary-50 border border-primary-200 rounded-xl p-4">
                      <p className="text-xs font-semibold text-primary-700 mb-1 uppercase tracking-wide">💡 Giải thích</p>
                      <p className="text-sm text-slate-700">{detail.explanation}</p>
                    </div>
                  )}
                </div>
              )}
            </div>
          ))}
        </div>
      </div>

      <div className="flex gap-3">
        <button id="back-to-exams" onClick={() => navigate('/exams')} className="btn-secondary flex items-center gap-2 flex-1 justify-center">
          <RotateCcw className="w-4 h-4" /> Làm bài khác
        </button>
        <button id="view-history" onClick={() => navigate('/history')} className="btn-primary flex items-center gap-2 flex-1 justify-center">
          Xem lịch sử
        </button>
      </div>
    </div>
  );
}
