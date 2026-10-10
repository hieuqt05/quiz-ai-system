import { createContext, useContext, useState, useEffect } from 'react';
import { authApi } from '../services/api';

const AuthContext = createContext(null);

export function AuthProvider({ children }) {
  const [user, setUser] = useState(() => {
    try { return JSON.parse(localStorage.getItem('quiz_user') || 'null'); }
    catch { return null; }
  });
  const [loading, setLoading] = useState(false);

  const login = async (username, password) => {
    const res = await authApi.login({ username, password });
    const { token, user: userData } = res.data;
    localStorage.setItem('quiz_token', token);
    localStorage.setItem('quiz_user', JSON.stringify(userData));
    setUser(userData);
    return userData;
  };

  const register = async (data) => {
    const res = await authApi.register(data);
    return res.data;
  };

  const logout = () => {
    localStorage.removeItem('quiz_token');
    localStorage.removeItem('quiz_user');
    setUser(null);
  };

  const isAdmin = user?.role === 'ADMIN';
  const isTeacher = user?.role === 'TEACHER' || isAdmin;
  const isStudent = user?.role === 'STUDENT';

  return (
    <AuthContext.Provider value={{ user, loading, login, register, logout, isAdmin, isTeacher, isStudent }}>
      {children}
    </AuthContext.Provider>
  );
}

export const useAuth = () => useContext(AuthContext);
