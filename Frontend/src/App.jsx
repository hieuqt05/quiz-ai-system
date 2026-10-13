import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import { Toaster } from 'react-hot-toast';
import { AuthProvider, useAuth } from './contexts/AuthContext';
import Navbar from './components/Navbar';
import LoginPage from './pages/LoginPage';
import RegisterPage from './pages/RegisterPage';
import ExamListPage from './pages/ExamListPage';
import QuizPage from './pages/QuizPage';
import ResultPage from './pages/ResultPage';
import HistoryPage from './pages/HistoryPage';
import AdminPage from './pages/AdminPage';

function ProtectedRoute({ children, roles }) {
  const { user } = useAuth();
  if (!user) return <Navigate to="/login" replace />;
  if (roles && !roles.includes(user.role)) return <Navigate to="/exams" replace />;
  return children;
}

function AppRoutes() {
  const { user } = useAuth();

  return (
    <div className="min-h-screen">
      <Navbar />
      <main className="relative">
        <Routes>
          <Route path="/" element={<Navigate to={user ? '/exams' : '/login'} replace />} />
          <Route path="/login" element={user ? <Navigate to="/exams" /> : <LoginPage />} />
          <Route path="/register" element={user ? <Navigate to="/exams" /> : <RegisterPage />} />

          <Route path="/exams" element={
            <ProtectedRoute><ExamListPage /></ProtectedRoute>
          } />
          <Route path="/quiz/:examId" element={
            <ProtectedRoute><QuizPage /></ProtectedRoute>
          } />
          <Route path="/result/:submissionId" element={
            <ProtectedRoute><ResultPage /></ProtectedRoute>
          } />
          <Route path="/history" element={
            <ProtectedRoute><HistoryPage /></ProtectedRoute>
          } />
          <Route path="/admin" element={
            <ProtectedRoute roles={['TEACHER', 'ADMIN']}><AdminPage /></ProtectedRoute>
          } />

          <Route path="*" element={<Navigate to="/" replace />} />
        </Routes>
      </main>
    </div>
  );
}

export default function App() {
  return (
    <BrowserRouter>
      <AuthProvider>
        <AppRoutes />
        <Toaster
          position="top-right"
          toastOptions={{
            style: {
              background: '#ffffff',
              color: '#0f172a',
              border: '1px solid #e2e8f0',
              boxShadow: '0 10px 15px -3px rgba(0, 0, 0, 0.08), 0 4px 6px -4px rgba(0, 0, 0, 0.04)',
              borderRadius: '12px',
              fontWeight: 500,
            },
            success: { iconTheme: { primary: '#10b981', secondary: '#fff' } },
            error: { iconTheme: { primary: '#ef4444', secondary: '#fff' } },
          }}
        />
      </AuthProvider>
    </BrowserRouter>
  );
}
