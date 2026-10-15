import { Link, useNavigate } from 'react-router-dom';
import { useAuth } from '../contexts/AuthContext';
import { BookOpen, LogOut, User, BarChart2, Brain, Shield } from 'lucide-react';
import ServerStatus from './ServerStatus';

export default function Navbar() {
  const { user, logout, isTeacher, isAdmin } = useAuth();
  const navigate = useNavigate();

  const handleLogout = () => { logout(); navigate('/login'); };

  return (
    <nav className="sticky top-0 z-50 bg-white/90 backdrop-blur-md border-b border-slate-200 px-6 py-4 shadow-sm">
      <div className="max-w-7xl mx-auto flex items-center justify-between">
        {/* Logo */}
        <Link to="/" className="flex items-center gap-3 group">
          <div className="w-10 h-10 rounded-xl bg-gradient-to-br from-primary-500 to-cyan-500 flex items-center justify-center shadow-md shadow-primary-500/20 group-hover:scale-110 transition-transform">
            <Brain className="w-5 h-5 text-white" />
          </div>
          <span className="text-xl font-bold gradient-text">QuizAI</span>
        </Link>

        {/* Nav Links */}
        {user && (
          <div className="flex items-center gap-2">
            <Link to="/exams" className="flex items-center gap-2 px-4 py-2 rounded-lg hover:bg-slate-100 text-slate-600 hover:text-slate-900 transition-all text-sm font-medium">
              <BookOpen className="w-4 h-4" /> Đề thi
            </Link>
            <Link to="/history" className="flex items-center gap-2 px-4 py-2 rounded-lg hover:bg-slate-100 text-slate-600 hover:text-slate-900 transition-all text-sm font-medium">
              <BarChart2 className="w-4 h-4" /> Lịch sử
            </Link>
            {isTeacher && (
              <Link to="/admin" className="flex items-center gap-2 px-4 py-2 rounded-lg hover:bg-slate-100 text-slate-600 hover:text-slate-900 transition-all text-sm font-medium">
                <Shield className="w-4 h-4" /> Quản lý
              </Link>
            )}
          </div>
        )}

        {/* User / Auth */}
        <div className="flex items-center gap-3">
          {/* Server status badge */}
          <ServerStatus />

          {user ? (
            <>
              <div className="flex items-center gap-2 px-3 py-1.5 bg-slate-50 border border-slate-200 rounded-lg">
                <div className="w-7 h-7 rounded-full bg-gradient-to-br from-primary-500 to-cyan-500 flex items-center justify-center text-xs font-bold text-white">
                  {user.fullName?.[0] || user.username?.[0]}
                </div>
                <span className="text-sm font-medium text-slate-700">{user.fullName || user.username}</span>
                <span className={`text-xs px-2 py-0.5 rounded font-medium ${
                  user.role === 'ADMIN' ? 'bg-red-50 text-red-700 border border-red-200' :
                  user.role === 'TEACHER' ? 'bg-amber-50 text-amber-700 border border-amber-200' :
                  'bg-primary-50 text-primary-700 border border-primary-200'
                }`}>{user.role}</span>
              </div>
              <button onClick={handleLogout} className="p-2 rounded-lg hover:bg-red-50 text-slate-400 hover:text-red-500 transition-all" title="Đăng xuất">
                <LogOut className="w-4 h-4" />
              </button>
            </>
          ) : (
            <div className="flex gap-2">
              <Link to="/login" className="btn-secondary py-2 px-4 text-sm">Đăng nhập</Link>
              <Link to="/register" className="btn-primary py-2 px-4 text-sm">Đăng ký</Link>
            </div>
          )}
        </div>
      </div>
    </nav>
  );
}
