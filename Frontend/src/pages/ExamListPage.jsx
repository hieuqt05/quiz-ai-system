import { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { examApi } from '../services/api';
import { BookOpen, Clock, Target, ChevronRight, Search, Filter, Loader2 } from 'lucide-react';
import toast from 'react-hot-toast';

export default function ExamListPage() {
  const [exams, setExams] = useState([]);
  const [loading, setLoading] = useState(true);
  const [search, setSearch] = useState('');
  const navigate = useNavigate();

  useEffect(() => {
    examApi.getPublished()
      .then(r => setExams(r.data))
      .catch(() => toast.error('Không tải được danh sách đề thi'))
      .finally(() => setLoading(false));
  }, []);

  const filtered = exams.filter(e =>
    e.title.toLowerCase().includes(search.toLowerCase()) ||
    e.category.toLowerCase().includes(search.toLowerCase())
  );

  return (
    <div className="max-w-5xl mx-auto px-4 py-8">
      {/* Hero */}
      <div className="text-center mb-10 animate-fade-in">
        <h1 className="text-4xl font-bold mb-3">
          <span className="gradient-text">Kho Đề Thi</span>
        </h1>
        <p className="text-gray-400 text-lg">Chọn đề thi phù hợp và bắt đầu luyện tập ngay</p>
      </div>

      {/* Search */}
      <div className="relative mb-8">
        <Search className="absolute left-4 top-1/2 -translate-y-1/2 w-5 h-5 text-gray-500" />
        <input
          id="exam-search"
          className="input-field pl-12 text-base"
          placeholder="Tìm kiếm theo tên đề thi hoặc chủ đề..."
          value={search}
          onChange={e => setSearch(e.target.value)}
        />
      </div>

      {loading ? (
        <div className="flex justify-center py-20">
          <Loader2 className="w-10 h-10 text-primary-400 animate-spin" />
        </div>
      ) : filtered.length === 0 ? (
        <div className="text-center py-20">
          <BookOpen className="w-16 h-16 text-gray-600 mx-auto mb-4" />
          <p className="text-gray-400 text-lg">Không tìm thấy đề thi nào</p>
        </div>
      ) : (
        <div className="grid gap-4 md:grid-cols-2">
          {filtered.map((exam, i) => (
            <div
              key={exam.examId}
              id={`exam-card-${exam.examId}`}
              onClick={() => navigate(`/quiz/${exam.examId}`)}
              className="card-hover group animate-slide-up"
              style={{ animationDelay: `${i * 60}ms` }}
            >
              <div className="flex items-start justify-between mb-4">
                <div className="flex-1">
                  <div className="flex items-center gap-2 mb-1">
                    {exam.category && (
                      <span className="text-xs bg-primary-500/20 text-primary-300 border border-primary-500/30 px-2 py-0.5 rounded-full font-medium">
                        {exam.category}
                      </span>
                    )}
                  </div>
                  <h3 className="text-lg font-semibold text-gray-100 group-hover:text-primary-300 transition-colors">
                    {exam.title}
                  </h3>
                </div>
                <ChevronRight className="w-5 h-5 text-gray-500 group-hover:text-primary-400 group-hover:translate-x-1 transition-all mt-1 flex-shrink-0" />
              </div>
              {exam.description && (
                <p className="text-gray-400 text-sm mb-4 line-clamp-2">{exam.description}</p>
              )}
              <div className="flex items-center gap-4 text-sm text-gray-400">
                <div className="flex items-center gap-1.5">
                  <Clock className="w-4 h-4 text-cyan-400" />
                  <span>{exam.durationMinutes} phút</span>
                </div>
                <div className="flex items-center gap-1.5">
                  <BookOpen className="w-4 h-4 text-purple-400" />
                  <span>{exam.questionCount} câu hỏi</span>
                </div>
                <div className="flex items-center gap-1.5">
                  <Target className="w-4 h-4 text-emerald-400" />
                  <span>Đạt: {exam.passScore}%</span>
                </div>
              </div>
              <div className="mt-4 pt-4 border-t border-white/5 text-xs text-gray-500">
                Tạo bởi: {exam.creatorName}
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}
