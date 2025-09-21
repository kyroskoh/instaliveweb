import { useState, useEffect } from 'react'
import { useQuery, useMutation, useQueryClient } from 'react-query'
import { Play, Square, RefreshCw, Users, Copy, CheckCircle, AlertTriangle } from 'lucide-react'
import { api } from '../services/api'

export default function DashboardPage() {
  const [copied, setCopied] = useState('')
  const queryClient = useQueryClient()

  const { data: streamInfo, refetch: refetchStreamInfo } = useQuery(
    'streamInfo',
    api.getStreamInfo,
    { refetchInterval: 5000 }
  )

  const { data: viewers } = useQuery(
    'viewers',
    api.getViewers,
    {
      refetchInterval: streamInfo?.status === 'running' ? 10000 : false,
      enabled: streamInfo?.status === 'running'
    }
  )

  const startStreamMutation = useMutation(api.startStream, {
    onSuccess: () => {
      queryClient.invalidateQueries('streamInfo')
    }
  })

  const stopStreamMutation = useMutation(api.stopStream, {
    onSuccess: () => {
      queryClient.invalidateQueries('streamInfo')
    }
  })

  const refreshKeyMutation = useMutation(api.refreshStreamKey, {
    onSuccess: () => {
      queryClient.invalidateQueries('streamInfo')
    }
  })

  const copyToClipboard = async (text: string, type: string) => {
    try {
      await navigator.clipboard.writeText(text)
      setCopied(type)
      setTimeout(() => setCopied(''), 2000)
    } catch (err) {
      console.error('Failed to copy:', err)
    }
  }

  const getStatusColor = (status: string) => {
    switch (status) {
      case 'running':
        return 'text-green-600 bg-green-100'
      case 'stopped':
        return 'text-red-600 bg-red-100'
      case 'ready':
        return 'text-blue-600 bg-blue-100'
      default:
        return 'text-gray-600 bg-gray-100'
    }
  }

  return (
    <div className="max-w-4xl mx-auto py-8 px-4 sm:px-6 lg:px-8">
      <div className="space-y-6">

        {/* Status Card */}
        <div className="card">
          <div className="flex items-center justify-between mb-6">
            <h2 className="text-2xl font-bold text-gray-900">Live Stream Status</h2>
            <div className={`px-3 py-1 rounded-full text-sm font-medium ${getStatusColor(streamInfo?.status || 'unknown')}`}>
              {streamInfo?.status?.toUpperCase() || 'LOADING...'}
            </div>
          </div>

          <div className="flex space-x-4">
            <button
              onClick={() => startStreamMutation.mutate()}
              disabled={streamInfo?.status === 'running' || startStreamMutation.isLoading}
              className="btn btn-primary flex items-center space-x-2 disabled:opacity-50 disabled:cursor-not-allowed"
            >
              <Play className="h-5 w-5" />
              <span>{startStreamMutation.isLoading ? 'Starting...' : 'Start Stream'}</span>
            </button>

            <button
              onClick={() => stopStreamMutation.mutate()}
              disabled={streamInfo?.status !== 'running' || stopStreamMutation.isLoading}
              className="btn btn-danger flex items-center space-x-2 disabled:opacity-50 disabled:cursor-not-allowed"
            >
              <Square className="h-5 w-5" />
              <span>{stopStreamMutation.isLoading ? 'Stopping...' : 'Stop Stream'}</span>
            </button>

            <button
              onClick={() => refreshKeyMutation.mutate()}
              disabled={refreshKeyMutation.isLoading}
              className="btn btn-secondary flex items-center space-x-2"
            >
              <RefreshCw className={`h-5 w-5 ${refreshKeyMutation.isLoading ? 'animate-spin' : ''}`} />
              <span>Refresh Key</span>
            </button>
          </div>
        </div>

        {/* Stream Details Card */}
        <div className="card">
          <h3 className="text-xl font-semibold text-gray-900 mb-4">Stream Configuration</h3>

          <div className="space-y-4">
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-2">
                RTMP Server URL
              </label>
              <div className="flex items-center space-x-2">
                <input
                  type="text"
                  value={streamInfo?.stream_url || 'Loading...'}
                  readOnly
                  className="input font-mono text-sm bg-gray-50"
                />
                <button
                  onClick={() => copyToClipboard(streamInfo?.stream_url || '', 'url')}
                  className="btn btn-secondary"
                  disabled={!streamInfo?.stream_url}
                >
                  {copied === 'url' ? <CheckCircle className="h-5 w-5" /> : <Copy className="h-5 w-5" />}
                </button>
              </div>
            </div>

            <div>
              <label className="block text-sm font-medium text-gray-700 mb-2">
                Stream Key
              </label>
              <div className="flex items-center space-x-2">
                <input
                  type="password"
                  value={streamInfo?.stream_key || 'Loading...'}
                  readOnly
                  className="input font-mono text-sm bg-gray-50"
                />
                <button
                  onClick={() => copyToClipboard(streamInfo?.stream_key || '', 'key')}
                  className="btn btn-secondary"
                  disabled={!streamInfo?.stream_key}
                >
                  {copied === 'key' ? <CheckCircle className="h-5 w-5" /> : <Copy className="h-5 w-5" />}
                </button>
              </div>
            </div>
          </div>

          <div className="mt-6 p-4 bg-yellow-50 border border-yellow-200 rounded-lg">
            <div className="flex items-start space-x-3">
              <AlertTriangle className="h-5 w-5 text-yellow-600 mt-0.5" />
              <div className="text-sm text-yellow-800">
                <p className="font-medium">Instructions for OBS Studio:</p>
                <ol className="mt-2 list-decimal list-inside space-y-1">
                  <li>Go to Settings → Stream</li>
                  <li>Set Service to "Custom..."</li>
                  <li>Copy the RTMP Server URL to the "Server" field</li>
                  <li>Copy the Stream Key to the "Stream Key" field</li>
                  <li>Click "Start Streaming" in OBS, then click "Start Stream" above</li>
                </ol>
              </div>
            </div>
          </div>
        </div>

        {/* Viewers Card */}
        {streamInfo?.status === 'running' && (
          <div className="card">
            <div className="flex items-center space-x-3 mb-4">
              <Users className="h-6 w-6 text-gray-600" />
              <h3 className="text-xl font-semibold text-gray-900">Live Viewers</h3>
              <span className="px-2 py-1 bg-green-100 text-green-800 text-sm font-medium rounded-full">
                {viewers?.count || 0}
              </span>
            </div>

            {viewers?.viewers && viewers.viewers.length > 0 ? (
              <div className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-3">
                {viewers.viewers.map((viewer, index) => (
                  <div key={index} className="p-2 bg-gray-50 rounded-lg text-sm text-gray-700">
                    @{viewer}
                  </div>
                ))}
              </div>
            ) : (
              <p className="text-gray-500 text-center py-4">No viewers yet. Share your stream to get started!</p>
            )}
          </div>
        )}
      </div>
    </div>
  )
}