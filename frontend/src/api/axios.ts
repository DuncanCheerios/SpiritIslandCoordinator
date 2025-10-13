// src/api/axios.ts
import axios from 'axios'

const api = axios.create({
  baseURL: 'http://localhost:8000/api/',
})

// Attach JWT access token to every request
api.interceptors.request.use((config) => {
  const token = localStorage.getItem('access_token')
  if (token) config.headers.Authorization = `Bearer ${token}`
  return config
})

// Refresh access token if expired
api.interceptors.response.use(
  (response) => response,
  async (error) => {
    const originalRequest = error.config
    if (
      error.response?.status === 401 &&
      !originalRequest._retry
    ) {
      originalRequest._retry = true
      try {
        const refresh = localStorage.getItem('refresh_token')
        if (!refresh) throw error

        const res = await axios.post(
          'http://localhost:8000/api/token/refresh/',
          { refresh }
        )
        localStorage.setItem('access_token', res.data.access)
        originalRequest.headers.Authorization = `Bearer ${res.data.access}`
        return axios(originalRequest)
      } catch (e) {
        localStorage.removeItem('access_token')
        localStorage.removeItem('refresh_token')
        window.location.href = '/login'
        return Promise.reject(e)
      }
    }
    return Promise.reject(error)
  }
)

export default api
