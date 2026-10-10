import { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { useAuth } from '../contexts/AuthContext';
import { Brain, Eye, EyeOff, Loader2 } from 'lucide-react';
import toast from 'react-hot-toast';

export default function LoginPage() {
  const [form, setForm] = useState({ username: '', password: '' });
  const [showPw, setShowPw] = useState(false);
  const [loading, setLoading] = useState(false);
  const { login } = useAuth();
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    try {
      const user = await login(form.username, form.password);
      toast.success(`Chào mừng, ${user.fullName}!`);
      if (user.role === 'STUDENT') navigate('/exams');
      else navigate('/admin');
    } catch (err) {
      toast.error(err.response?.data?.message || 'Đăng nhập thất bại!');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center px-4">
      {/* Background glow */}
      <div className="absolute inset-0 overflow-hidden pointer-events-none">
        <div className="absolute top-1/4 left-1/4 w-96 h-96 bg-primary-600/20 rounded-full blur-3xl" />
        <div className="absolute bottom-1/4 right-1/4 w-80 h-80 bg-cyan-600/15 rounded-full blur-3xl" />
      </div>

      <div className="w-full max-w-md animate-slide-up relative z-10">
        {/* Header */}
        <div className="text-center mb-8">
          <div className="inline-flex items-center justify-center w-20 h-20 rounded-2xl bg-gradient-to-br from-primary-500 to-cyan-500 mb-4 shadow-2xl shadow-primary-500/40">
            <Brain className="w-10 h-10 text-white" />
          </div>
          <h1 className="text-3xl font-bold gradient-text">QuizAI</h1>
          <p className="text-gray-400 mt-2">Đăng nhập để tiếp tục học</p>
        </div>

        <div className="card">
          <form onSubmit={handleSubmit} className="space-y-5">
            <div>
              <label className="block text-sm font-medium text-gray-300 mb-2">Tên đăng nhập</label>
              <input
                id="login-username"
                className="input-field"
                placeholder="Nhập tên đăng nhập..."
                value={form.username}
                onChange={e => setForm(p => ({ ...p, username: e.target.value }))}
                required
              />
            </div>
            <div>
              <label className="block text-sm font-medium text-gray-300 mb-2">Mật khẩu</label>
              <div className="relative">
                <input
                  id="login-password"
                  type={showPw ? 'text' : 'password'}
                  className="input-field pr-12"
                  placeholder="Nhập mật khẩu..."
                  value={form.password}
                  onChange={e => setForm(p => ({ ...p, password: e.target.value }))}
                  required
                />
                <button type="button" onClick={() => setShowPw(!showPw)}
                  className="absolute right-3 top-1/2 -translate-y-1/2 text-gray-400 hover:text-gray-200">
                  {showPw ? <EyeOff className="w-5 h-5" /> : <Eye className="w-5 h-5" />}
                </button>
              </div>
            </div>

            <button id="login-submit" type="submit" disabled={loading} className="btn-primary w-full flex items-center justify-center gap-2">
              {loading ? <><Loader2 className="w-4 h-4 animate-spin" /> Đang đăng nhập...</> : 'Đăng nhập'}
            </button>
          </form>

          <div className="mt-6 text-center">
            <p className="text-gray-400 text-sm">
              Chưa có tài khoản?{' '}
              <Link to="/register" className="text-primary-400 hover:text-primary-300 font-medium">
                Đăng ký ngay
              </Link>
            </p>
          </div>

          {/* Demo accounts */}
          <div className="mt-4 p-3 bg-white/5 rounded-xl border border-white/5">
            <p className="text-xs text-gray-500 text-center mb-2">Tài khoản demo</p>
            <div className="grid grid-cols-2 gap-2 text-xs text-gray-400">
              <div><span className="text-yellow-400">Admin:</span> admin / Admin@123</div>
              <div><span className="text-emerald-400">Student:</span> Tự đăng ký</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
