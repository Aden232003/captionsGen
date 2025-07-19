# Caption Generator Backend

## Deploy to Railway

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/template/quickstart)

1. Click the Railway button above
2. Connect your GitHub account
3. Set the environment variable:
   - `ANTHROPIC_API_KEY`: Your Anthropic API key
4. Deploy!

## Deploy to Render

1. Go to [render.com](https://render.com)
2. Create new Web Service from GitHub
3. Use these settings:
   - Root Directory: `backend`
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`
   - Environment Variable: `ANTHROPIC_API_KEY`

## Deploy to Heroku

1. Install [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)
2. Run: `heroku create your-app-name`
3. Run: `heroku config:set ANTHROPIC_API_KEY=your_key`
4. Run: `git push heroku main`

## Environment Variables

- `ANTHROPIC_API_KEY`: Your Anthropic API key (required)
- `PORT`: Port number (auto-set by hosting platforms)