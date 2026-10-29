import react from '@vitejs/plugin-react'
import { defineConfig } from 'vite'

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    host: '0.0.0.0', // Cho phép các máy khác trong mạng LAN/Wi-Fi truy cập
    allowedHosts: true, // Cho phép mọi domain tunnel (Pinggy, Ngrok, Cloudflare) truy cập
    port: 5173,
    proxy: {
      // Forward /api/* → http://localhost:5000/api/*
      '/api': {
        target: 'http://localhost:5000',
        changeOrigin: true,
        secure: false,
      },
    },
  },
})
