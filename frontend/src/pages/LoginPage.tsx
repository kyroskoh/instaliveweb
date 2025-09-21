import { useState } from 'react'
import { useForm } from 'react-hook-form'
import { useMutation } from 'react-query'
import { Radio, Loader2, AlertCircle } from 'lucide-react'
import { useAuthStore } from '../stores/authStore'
import { api } from '../services/api'

interface LoginForm {
  username: string
  password: string
}

export default function LoginPage() {
  const [error, setError] = useState('')
  const { login } = useAuthStore()
  const { register, handleSubmit, formState: { errors } } = useForm<LoginForm>()

  const loginMutation = useMutation(
    (data: LoginForm) => api.login(data.username, data.password),
    {
      onSuccess: (response, variables) => {
        login(response.access_token, variables.username)
      },
      onError: (error: any) => {
        setError(error.response?.data?.detail || 'Login failed')
      }
    }
  )

  const onSubmit = (data: LoginForm) => {
    setError('')
    loginMutation.mutate(data)
  }

  return (
    <div className="min-h-screen flex items-center justify-center py-12 px-4 sm:px-6 lg:px-8">
      <div className="max-w-md w-full">
        <div className="card">
          <div className="text-center mb-8">
            <Radio className="h-12 w-12 text-instagram-500 mx-auto mb-4" />
            <h2 className="text-3xl font-bold text-gray-900">Sign in to InstaLiveWeb</h2>
            <p className="mt-2 text-gray-600">Enter your Instagram credentials to start streaming</p>
          </div>

          <form onSubmit={handleSubmit(onSubmit)} className="space-y-6">
            <div>
              <label htmlFor="username" className="block text-sm font-medium text-gray-700 mb-2">
                Instagram Username
              </label>
              <input
                {...register('username', { required: 'Username is required' })}
                type="text"
                className="input"
                placeholder="Enter your Instagram username"
              />
              {errors.username && (
                <p className="mt-1 text-sm text-red-600">{errors.username.message}</p>
              )}
            </div>

            <div>
              <label htmlFor="password" className="block text-sm font-medium text-gray-700 mb-2">
                Password
              </label>
              <input
                {...register('password', { required: 'Password is required' })}
                type="password"
                className="input"
                placeholder="Enter your Instagram password"
              />
              {errors.password && (
                <p className="mt-1 text-sm text-red-600">{errors.password.message}</p>
              )}
            </div>

            {error && (
              <div className="flex items-center space-x-2 p-3 bg-red-50 border border-red-200 rounded-lg">
                <AlertCircle className="h-5 w-5 text-red-500" />
                <span className="text-sm text-red-700">{error}</span>
              </div>
            )}

            <button
              type="submit"
              disabled={loginMutation.isLoading}
              className="w-full btn btn-primary flex items-center justify-center space-x-2"
            >
              {loginMutation.isLoading ? (
                <>
                  <Loader2 className="h-5 w-5 animate-spin" />
                  <span>Signing in...</span>
                </>
              ) : (
                <span>Sign in</span>
              )}
            </button>
          </form>

          <div className="mt-6 text-center">
            <p className="text-sm text-gray-600">
              Your credentials are used only to authenticate with Instagram's servers
            </p>
          </div>
        </div>
      </div>
    </div>
  )
}