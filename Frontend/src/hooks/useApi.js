import { useState, useEffect, useCallback } from 'react';

/**
 * useApi - hook tiện lợi để gọi API với loading / error / data state tự động.
 *
 * @param {Function} apiFn   - Hàm trả về Promise (vd: () => examApi.getPublished())
 * @param {Array}    deps    - Dependencies (như useEffect)
 * @param {boolean}  eager   - Gọi ngay khi mount (default: true)
 *
 * @returns {{ data, loading, error, refetch }}
 *
 * Ví dụ dùng:
 *   const { data: exams, loading, error, refetch } = useApi(() => examApi.getPublished());
 */
export function useApi(apiFn, deps = [], eager = true) {
  const [data, setData]       = useState(null);
  const [loading, setLoading] = useState(eager);
  const [error, setError]     = useState(null);

  const fetch = useCallback(async () => {
    setLoading(true);
    setError(null);
    try {
      const res = await apiFn();
      setData(res.data);
    } catch (err) {
      setError(err?.response?.data?.message || err?.message || 'Lỗi kết nối server');
    } finally {
      setLoading(false);
    }
  // eslint-disable-next-line react-hooks/exhaustive-deps
  }, deps);

  useEffect(() => {
    if (eager) fetch();
  // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [fetch]);

  return { data, loading, error, refetch: fetch };
}
