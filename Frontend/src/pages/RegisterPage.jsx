import { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { useAuth } from '../contexts/AuthContext';
import { Brain, Loader2 } from 'lucide-react';
import toast from 'react-hot-toast';

export default function RegisterPage() {
  const [form, setForm] = useState({ username: '', email: '', password: '', fullName: '' });
  const [loading, setLoading] = useState(false);
  const { register } = useAuth();
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    try {
      await register(form);
      toast.success('Đăng ký thành công! Hãy đăng nhập.');
      navigate('/login');
    } catch (err) {
      toast.error(err.response?.data?.message || 'Đăng ký thất bại!');
    } finally {
      setLoading(false);
    }
  };

  const fields = [
    { id: 'reg-fullname', key: 'fullName', label: 'Họ và tên', placeholder: 'Nguyễn Văn A', type: 'text' },
    { id: 'reg-username', key: 'username', label: 'Tên đăng nhập', placeholder: 'nguyenvana', type: 'text' },
    { id: 'reg-email', key: 'email', label: 'Email', placeholder: 'example@email.com', type: 'email' },
    { id: 'reg-password', key: 'password', label: 'Mật khẩu (tối thiểu 6 ký tự)', placeholder: '••••••••', type: 'password' },
  ];

  return (
    <div className="min-h-screen flex items-center justify-center px-4 py-8">
      <div className="absolute inset-0 overflow-hidden pointer-events-none">
        <div className="absolute top-1/3 right-1/4 w-96 h-96 bg-primary-200/50 rounded-full blur-3xl" />
        <div className="absolute bottom-1/3 left-1/4 w-80 h-80 bg-purple-200/40 rounded-full blur-3xl" />
      </div>

      <div className="w-full max-w-md animate-slide-up relative z-10">
        <div className="text-center mb-8">
          <div className="inline-flex items-center justify-center w-20 h-20 rounded-2xl bg-gradient-to-br from-primary-500 to-cyan-500 mb-4 shadow-xl shadow-primary-500/20">
            <Brain className="w-10 h-10 text-white" />
          </div>
          <h1 className="text-3xl font-bold gradient-text">Tạo tài khoản</h1>
          <p className="text-slate-500 mt-2">Tham gia QuizAI ngay hôm nay</p>
        </div>

        <div className="card">
          <form onSubmit={handleSubmit} className="space-y-4">
            {fields.map(f => (
              <div key={f.key}>
                <label className="block text-sm font-medium text-slate-700 mb-2">{f.label}</label>
                <input
                  id={f.id}
                  type={f.type}
                  className="input-field"
                  placeholder={f.placeholder}
                  value={form[f.key]}
                  onChange={e => setForm(p => ({ ...p, [f.key]: e.target.value }))}
                  required
                />
              </div>
            ))}
            <button id="register-submit" type="submit" disabled={loading} className="btn-primary w-full flex items-center justify-center gap-2 mt-2">
              {loading ? <><Loader2 className="w-4 h-4 animate-spin" /> Đang đăng ký...</> : 'Đăng ký'}
            </button>
          </form>
          <div className="mt-6 text-center">
            <p className="text-slate-500 text-sm">
              Đã có tài khoản?{' '}
              <Link to="/login" className="text-primary-600 hover:text-primary-700 font-semibold">Đăng nhập</Link>
            </p>
          </div>
        </div>
      </div>
    </div>
  );
}
