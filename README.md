# Caption Generator Backend API

AI-powered caption and title generator using Anthropic Claude.

## 🚀 Quick Deploy

### Railway (Recommended)
[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new/template/railway-template)

1. Click Railway button above
2. Connect your GitHub account and select this repo
3. Set environment variable: `ANTHROPIC_API_KEY`
4. Deploy!

### Render
1. Go to [render.com](https://render.com)
2. Create new Web Service from GitHub
3. Select this repository and branch: `backend`
4. Settings:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`
   - Environment Variable: `ANTHROPIC_API_KEY`

### Heroku
```bash
heroku create your-app-name
heroku config:set ANTHROPIC_API_KEY=your_key
git push heroku backend:main
```

## 📋 API Endpoints

- `GET /health` - Health check
- `POST /generate` - Generate Instagram caption and YouTube title
- `POST /analyze-crux` - Analyze script crux element

## 🔧 Environment Variables

- `ANTHROPIC_API_KEY` - Your Anthropic API key (required)
- `PORT` - Port number (auto-set by hosting platforms)

## 🏃 Local Development

```bash
export ANTHROPIC_API_KEY=your_key
pip install -r requirements.txt
python app.py
```