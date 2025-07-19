import React, { useState } from 'react';
import { Toaster, toast } from 'react-hot-toast';
import { 
  Sparkles, 
  Copy, 
  Send, 
  Instagram, 
  Youtube, 
  Loader2,
  CheckCircle,
  AlertCircle,
  Zap,
  Target,
  TrendingUp
} from 'lucide-react';
import axios from 'axios';

const API_BASE_URL = process.env.NODE_ENV === 'production' 
  ? '' // Use relative URLs in production (same domain)
  : (process.env.REACT_APP_API_URL || 'http://localhost:5001');

function App() {
  const [script, setScript] = useState('');
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);
  const [error, setError] = useState('');

  const generateContent = async () => {
    if (!script.trim()) {
      toast.error('Please enter a script first!');
      return;
    }

    setLoading(true);
    setError('');
    setResult(null);

    try {
      const response = await axios.post(`${API_BASE_URL}/api/generate`, {
        script: script.trim()
      });

      if (response.data.success) {
        setResult(response.data.data);
        toast.success('Content generated successfully! 🎉');
      } else {
        setError(response.data.error || 'Failed to generate content');
        toast.error('Failed to generate content');
      }
    } catch (err) {
      const errorMessage = err.response?.data?.error || 'Network error. Make sure the backend is running.';
      setError(errorMessage);
      toast.error(errorMessage);
    } finally {
      setLoading(false);
    }
  };

  const copyToClipboard = (text, type) => {
    navigator.clipboard.writeText(text);
    toast.success(`${type} copied to clipboard! 📋`);
  };

  const formatInstagramCaption = (caption) => {
    return caption.split('\n').map((line, index) => (
      <span key={index}>
        {line}
        <br />
      </span>
    ));
  };

  return (
    <div className="min-h-screen p-4 lg:p-8">
      <Toaster 
        position="top-right"
        toastOptions={{
          duration: 3000,
          style: {
            background: 'rgba(255, 255, 255, 0.1)',
            backdropFilter: 'blur(10px)',
            border: '1px solid rgba(255, 255, 255, 0.2)',
            color: 'white',
          },
        }}
      />

      <div className="max-w-6xl mx-auto">
        {/* Header */}
        <div className="text-center mb-12">
          <div className="flex justify-center items-center gap-3 mb-4">
            <Sparkles className="w-8 h-8 text-white" />
            <h1 className="text-4xl lg:text-5xl font-bold text-white">
              Caption Generator
            </h1>
            <Sparkles className="w-8 h-8 text-white" />
          </div>
          <p className="text-white text-opacity-80 text-lg max-w-2xl mx-auto">
            Transform your video scripts into engaging Instagram captions and YouTube titles using AI-powered analysis
          </p>
        </div>

        {/* Main Content */}
        <div className="grid lg:grid-cols-2 gap-8">
          {/* Input Section */}
          <div className="card">
            <div className="flex items-center gap-3 mb-6">
              <Target className="w-6 h-6 text-white" />
              <h2 className="text-2xl font-semibold text-white">Script Input</h2>
            </div>
            
            <div className="space-y-4">
              <div>
                <label className="block text-white text-sm font-medium mb-2">
                  Video Script
                </label>
                <textarea
                  className="input-field h-64 resize-none"
                  placeholder="Paste your video script here... The AI will identify the 'crux' element and generate compelling content around it."
                  value={script}
                  onChange={(e) => setScript(e.target.value)}
                />
                <div className="text-white text-opacity-60 text-sm mt-2">
                  {script.length} characters
                </div>
              </div>

              <button
                onClick={generateContent}
                disabled={loading || !script.trim()}
                className={`btn-primary w-full flex items-center justify-center gap-2 ${
                  loading ? 'opacity-50 cursor-not-allowed' : ''
                }`}
              >
                {loading ? (
                  <Loader2 className="w-5 h-5 animate-spin" />
                ) : (
                  <Send className="w-5 h-5" />
                )}
                {loading ? 'Generating...' : 'Generate Content'}
              </button>
            </div>
          </div>

          {/* Results Section */}
          <div className="card">
            <div className="flex items-center gap-3 mb-6">
              <TrendingUp className="w-6 h-6 text-white" />
              <h2 className="text-2xl font-semibold text-white">Generated Content</h2>
            </div>

            {error && (
              <div className="result-card border-red-500 border-opacity-50 mb-6">
                <div className="flex items-center gap-3">
                  <AlertCircle className="w-5 h-5 text-red-400" />
                  <span className="text-red-200">{error}</span>
                </div>
              </div>
            )}

            {result ? (
              <div className="space-y-6">
                {/* Instagram Caption */}
                <div className="result-card">
                  <div className="flex items-center justify-between mb-4">
                    <div className="flex items-center gap-3">
                      <Instagram className="w-6 h-6 text-pink-400" />
                      <h3 className="text-xl font-semibold text-white">Instagram Caption</h3>
                    </div>
                    <button
                      onClick={() => copyToClipboard(result.instagram_caption, 'Instagram caption')}
                      className="btn-secondary !p-2"
                    >
                      <Copy className="w-4 h-4" />
                    </button>
                  </div>
                  
                  <div className="bg-black bg-opacity-20 rounded-lg p-4 mb-4">
                    <div className="text-white text-sm leading-relaxed whitespace-pre-wrap">
                      {formatInstagramCaption(result.instagram_caption)}
                    </div>
                  </div>
                  
                  <div className="flex items-center gap-4 text-sm text-white text-opacity-70">
                    <span>📝 {result.word_count} words</span>
                    <span>📊 Optimized format</span>
                  </div>
                </div>

                {/* YouTube Title */}
                <div className="result-card">
                  <div className="flex items-center justify-between mb-4">
                    <div className="flex items-center gap-3">
                      <Youtube className="w-6 h-6 text-red-400" />
                      <h3 className="text-xl font-semibold text-white">YouTube Title</h3>
                    </div>
                    <button
                      onClick={() => copyToClipboard(result.youtube_title, 'YouTube title')}
                      className="btn-secondary !p-2"
                    >
                      <Copy className="w-4 h-4" />
                    </button>
                  </div>
                  
                  <div className="bg-black bg-opacity-20 rounded-lg p-4 mb-4">
                    <div className="text-white text-lg font-medium">
                      {result.youtube_title}
                    </div>
                  </div>
                  
                  <div className="flex items-center gap-4 text-sm text-white text-opacity-70">
                    <span className={result.youtube_title_length <= 55 ? 'text-green-400' : 'text-red-400'}>
                      📏 {result.youtube_title_length}/55 characters
                    </span>
                    <span className={result.hashtag_count === 2 ? 'text-green-400' : 'text-yellow-400'}>
                      🏷️ {result.hashtag_count} hashtags
                    </span>
                    {result.youtube_title_length <= 55 && result.hashtag_count === 2 && (
                      <span className="text-green-400 flex items-center gap-1">
                        <CheckCircle className="w-4 h-4" />
                        Optimized
                      </span>
                    )}
                  </div>
                </div>
              </div>
            ) : (
              <div className="text-center py-12">
                <Zap className="w-16 h-16 text-white text-opacity-30 mx-auto mb-4" />
                <p className="text-white text-opacity-60">
                  Enter your script and click generate to see the magic happen!
                </p>
              </div>
            )}
          </div>
        </div>

        {/* Features */}
        <div className="mt-16 grid md:grid-cols-3 gap-6">
          <div className="card text-center">
            <Target className="w-12 h-12 text-white mx-auto mb-4" />
            <h3 className="text-xl font-semibold text-white mb-2">Crux Identification</h3>
            <p className="text-white text-opacity-70">
              AI identifies specific tools, concepts, and unique angles from your script
            </p>
          </div>
          
          <div className="card text-center">
            <Sparkles className="w-12 h-12 text-white mx-auto mb-4" />
            <h3 className="text-xl font-semibold text-white mb-2">Dynamic Processing</h3>
            <p className="text-white text-opacity-70">
              Adapts to any niche - no fixed templates, pure AI-driven content
            </p>
          </div>
          
          <div className="card text-center">
            <TrendingUp className="w-12 h-12 text-white mx-auto mb-4" />
            <h3 className="text-xl font-semibold text-white mb-2">Optimized Format</h3>
            <p className="text-white text-opacity-70">
              Follows exact specifications for maximum engagement and reach
            </p>
          </div>
        </div>

        {/* Footer */}
        <div className="text-center mt-16 text-white text-opacity-50">
          <p>Powered by Claude AI • Built for modern content creators</p>
        </div>
      </div>
    </div>
  );
}

export default App;