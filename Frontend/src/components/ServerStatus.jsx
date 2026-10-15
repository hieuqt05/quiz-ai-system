import { useState, useEffect } from 'react';
import { Wifi, WifiOff, Loader2 } from 'lucide-react';
import api from '../services/api';

/**
 * ServerStatus - badge nhỏ hiển thị trạng thái kết nối với backend API.
 * Ping `/api/exams` mỗi 30 giây.
 */
export default function ServerStatus() {
  const [status, setStatus] = useState('checking'); // 'checking' | 'online' | 'offline'

  const check = async () => {
    try {
      await api.get('/exams', { timeout: 5000 });
      setStatus('online');
    } catch {
      setStatus('offline');
    }
  };

  useEffect(() => {
    check();
    const interval = setInterval(check, 30_000);
    return () => clearInterval(interval);
  }, []);

  if (status === 'checking') {
    return (
      <span className="inline-flex items-center gap-1.5 text-xs text-slate-400 font-medium">
        <Loader2 className="w-3 h-3 animate-spin" />
        Đang kết nối...
      </span>
    );
  }

  if (status === 'offline') {
    return (
      <span className="inline-flex items-center gap-1.5 text-xs text-red-600 font-medium bg-red-50 border border-red-200 px-2 py-1 rounded-full">
        <WifiOff className="w-3 h-3" />
        Mất kết nối server
      </span>
    );
  }

  return (
    <span className="inline-flex items-center gap-1.5 text-xs text-emerald-600 font-medium bg-emerald-50 border border-emerald-200 px-2 py-1 rounded-full">
      <Wifi className="w-3 h-3" />
      Đã kết nối
    </span>
  );
}
