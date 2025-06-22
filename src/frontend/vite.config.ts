import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import tailwindcss from '@tailwindcss/vite'

// https://vite.dev/config/
export default defineConfig({
  plugins: [
    react(),
    tailwindcss()],
  server: {
    proxy: {
      '/api': 'http://localhost:8000', // Adjust the port if your backend runs on a different port
      '/images': 'http://localhost:8000' // Proxy for serving images
    }
  }
})
