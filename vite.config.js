import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import proxy from 'http-proxy'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    vue(),
  ],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  },
  server: {
    proxy: {
      '/items': {
        target:'http://127.0.0.1:8000/',
        changeOrigin: true, 
        rewrite: (path) => path.replace(/^\/items/, '/items')
      },
      '/smaa2results': {
        target: 'http://127.0.0.1:8000/',
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/smaa2results/, '/smaa2results')
      } ,
      '/smaatriresults': {
        target: 'http://127.0.0.1:8000/',
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/smaatriresults/, '/smaatriresults')
      } 
    }
  }
})
