import { ReactNode } from 'react'
import { useAuthStore } from '../stores/authStore'
import { LogOut, Radio } from 'lucide-react'

interface LayoutProps {
  children: ReactNode
}

export default function Layout({ children }: LayoutProps) {
  const { isAuthenticated, username, logout } = useAuthStore()

  return (
    <div className="min-h-screen bg-gradient-to-br from-instagram-500 via-instagram-600 to-instagram-700">
      {isAuthenticated && (
        <nav className="bg-white/10 backdrop-blur-sm border-b border-white/20">
          <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div className="flex justify-between items-center h-16">
              <div className="flex items-center">
                <Radio className="h-8 w-8 text-white mr-3" />
                <h1 className="text-xl font-bold text-white">InstaLiveWeb</h1>
              </div>
              <div className="flex items-center space-x-4">
                <span className="text-white/90">@{username}</span>
                <button
                  onClick={logout}
                  className="flex items-center space-x-2 text-white/90 hover:text-white transition-colors"
                >
                  <LogOut className="h-5 w-5" />
                  <span>Logout</span>
                </button>
              </div>
            </div>
          </div>
        </nav>
      )}
      <main className="flex-1">
        {children}
      </main>
    </div>
  )
}