import axios from 'axios'
import { useAuthStore } from '../stores/authStore'

const API_BASE = '/api/v1'

const apiClient = axios.create({
  baseURL: API_BASE,
})

// Add auth token to requests
apiClient.interceptors.request.use((config) => {
  const token = useAuthStore.getState().token
  if (token) {
    config.headers.Authorization = `Bearer ${token}`
  }
  return config
})

// Handle auth errors
apiClient.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      useAuthStore.getState().logout()
    }
    return Promise.reject(error)
  }
)

export const api = {
  // Auth endpoints
  login: async (username: string, password: string) => {
    const response = await apiClient.post('/auth/login', { username, password })
    return response.data
  },

  logout: async () => {
    await apiClient.post('/auth/logout')
  },

  getCurrentUser: async () => {
    const response = await apiClient.get('/auth/me')
    return response.data
  },

  // Streaming endpoints
  getStreamInfo: async () => {
    const response = await apiClient.get('/streaming/info')
    return response.data
  },

  startStream: async () => {
    const response = await apiClient.post('/streaming/start')
    return response.data
  },

  stopStream: async () => {
    const response = await apiClient.post('/streaming/stop')
    return response.data
  },

  refreshStreamKey: async () => {
    const response = await apiClient.post('/streaming/refresh-key')
    return response.data
  },

  getViewers: async () => {
    const response = await apiClient.get('/streaming/viewers')
    return response.data
  },
}