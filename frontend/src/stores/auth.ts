import { defineStore } from 'pinia'
import api from '../api/axios'

interface User {
  username: string
}

export const useAuthStore = defineStore('auth', {
  state: () => ({
    user: null as User | null,
    isAuthenticated: false,
  }),
  actions: {
    async login(username: string, password: string) {
      const res = await api.post('token/', { username, password })
      localStorage.setItem('access_token', res.data.access)
      localStorage.setItem('refresh_token', res.data.refresh)
      this.isAuthenticated = true
      this.user = { username }
    },

    async register(username: string, password: string) {
      await api.post('register/', { username, password })
      // Optionally log in automatically after register
      await this.login(username, password)
    },

    logout() {
      localStorage.removeItem('access_token')
      localStorage.removeItem('refresh_token')
      this.user = null
      this.isAuthenticated = false
    },

    checkAuth() {
      const token = localStorage.getItem('access_token')
      this.isAuthenticated = !!token
      if (this.isAuthenticated) {
      }
    },
  },
})
