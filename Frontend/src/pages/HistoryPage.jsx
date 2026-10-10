import { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { submissionApi } from '../services/api';
import { BarChart2, Trophy, Clock, CheckCircle, Loader2, BookOpen } from 'lucide-react';

export default function HistoryPage() {
  const [history, setHistory] = useState([]);
  const [loading, setLoading] = useState(true);
  const navigate = useNavigate();

  useEffect(() => {
    submissionApi.getHistory()
      .then(r => setHistory(r.data))
      .finally(() => setLoading(false));
  }, []);

  if (loading) return (
    <div className="flex justify-center min-h-[60vh] items-center">
      <Loader2 className="w-12 h-12 text-primary-400 animate-spin" />
    </div>
  );

  return (
    <div className="max-w-4xl mx-auto px-4 py-8">
      <div className="flex items-center gap-3 mb-8">
        <BarChart2 className="w-8 h-8 text-primary-400" />
        <h1 className="text-3xl font-bold gradient-text">Lịch Sử Làm Bài</h1>
      </div>

      {history.length === 0 ? (
        <div className="text-center py-20">
          <BookOpen className="w-16 h-16 text-gray-600 mx-auto mb-4" />
          <p className="text-gray-400 text-lg">Bạn chưa làm bài thi nào</p>
          <button onClick={() => navigate('/exams')} className="btn-primary mt-4">Bắt đầu làm bài</button>
        </div>
      ) : (
        <div className="space-y-4">
          {history.map((item, i) => {
            const passed = item.totalScore >= 50;
            return (
              <div
                key={item.submissionId}
                id={`history-${item.submissionId}`}
                className="card hover:bg-white/10 transition-all cursor-pointer group"
                onClick={() => navigate(`/result/${item.submissionId}`)}
              >
                <div className="flex items-center gap-4">
                  <div className={`w-14 h-14 rounded-xl flex items-center justify-center text-xl font-black flex-shrink-0 ${
                    passed ? 'bg-emerald-500/20 text-emerald-400' : 'bg-red-500/20 text-red-400'
                  }`}>
                    {item.totalScore.toFixed(0)}%
                  </div>
                  <div className="flex-1">
                    <h3 className="font-semibold text-gray-100 group-hover:text-primary-300 transition-colors">
                      {item.examTitle}
                    </h3>
                    <div className="flex items-center gap-4 mt-1 text-sm text-gray-400">
                      <span className="flex items-center gap-1">
                        <CheckCircle className="w-3.5 h-3.5 text-emerald-400" />
                        {item.correctAnswers}/{item.totalQuestions} câu đúng
                      </span>
                      <span className="flex items-center gap-1">
                        <Clock className="w-3.5 h-3.5 text-cyan-400" />
                        {Math.floor(item.timeTaken / 60)}:{String(item.timeTaken % 60).padStart(2, '0')}
                      </span>
                      <span className="text-xs">
                        {new Date(item.submittedAt).toLocaleDateString('vi-VN', {
                          day: '2-digit', month: '2-digit', year: 'numeric',
                          hour: '2-digit', minute: '2-digit'
                        })}
                      </span>
                    </div>
                  </div>
                  <span className={`text-xs font-semibold px-3 py-1 rounded-full ${
                    passed ? 'bg-emerald-500/20 text-emerald-300' : 'bg-red-500/20 text-red-300'
                  }`}>
                    {passed ? 'ĐẠT' : 'CHƯA ĐẠT'}
                  </span>
                </div>
              </div>
            );
          })}
        </div>
      )}
    </div>
  );
}
