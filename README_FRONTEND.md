# Caption Generator Frontend

A modern React frontend with Flask backend for the AI-powered Instagram caption and YouTube title generator.

## 🎨 Features

- **Modern UI Design**: Glass morphism effects, gradient backgrounds, smooth animations
- **Real-time Processing**: Live feedback and loading states
- **Copy Functionality**: One-click copy for Instagram captions and YouTube titles
- **Responsive Design**: Works perfectly on desktop and mobile
- **Validation**: Character limits, hashtag counts, and format validation
- **Error Handling**: Graceful error messages and network error handling

## 🚀 Quick Start

### 1. Setup Backend

```bash
# Navigate to backend directory
cd backend

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Start the Flask API
python app.py
```

The backend will run on `http://localhost:5000`

### 2. Setup Frontend

```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Start the React app
npm start
```

The frontend will run on `http://localhost:3000`

## 📁 Project Structure

```
scriptsCode/
├── backend/
│   ├── app.py                 # Flask API server
│   ├── requirements.txt       # Python dependencies
│   └── ...
├── frontend/
│   ├── public/               # Static files
│   ├── src/
│   │   ├── App.js           # Main React component
│   │   ├── index.js         # React entry point
│   │   └── index.css        # Tailwind CSS styles
│   ├── package.json         # Node.js dependencies
│   ├── tailwind.config.js   # Tailwind configuration
│   └── ...
├── caption_generator.py      # Core AI logic
└── ...
```

## 🎯 Usage

1. **Start Backend**: Run the Flask API server
2. **Start Frontend**: Run the React development server
3. **Open Browser**: Navigate to `http://localhost:3000`
4. **Enter Script**: Paste your video script in the text area
5. **Generate**: Click "Generate Content" to create captions and titles
6. **Copy**: Use the copy buttons to copy generated content

## 🔧 API Endpoints

### `POST /generate`
Generate Instagram caption and YouTube title from script.

**Request:**
```json
{
  "script": "Your video script here..."
}
```

**Response:**
```json
{
  "success": true,
  "data": {
    "instagram_caption": "Generated caption...",
    "youtube_title": "Generated title #Tag #Tag",
    "youtube_title_length": 45,
    "hashtag_count": 2,
    "word_count": 150,
    "script_length": 500
  }
}
```

### `POST /analyze-crux`
Analyze and return just the crux element from script.

### `GET /health`
Health check endpoint.

## 🎨 Design Features

- **Glass Morphism**: Frosted glass effects with backdrop blur
- **Gradient Backgrounds**: Beautiful color gradients throughout
- **Smooth Animations**: Fade-in, slide-up, and hover effects
- **Modern Typography**: Inter font with proper weight hierarchy
- **Responsive Layout**: Grid-based layout that adapts to all screen sizes
- **Interactive Elements**: Hover states, loading spinners, success indicators

## 📱 Mobile Responsive

The app is fully responsive and works great on:
- Desktop (1024px+)
- Tablet (768px - 1023px)
- Mobile (320px - 767px)

## 🔒 Environment Variables

The API key is currently hardcoded in the backend. For production, use:

```bash
export ANTHROPIC_API_KEY="your-api-key-here"
```

## 🛠️ Development

### Backend Development
```bash
cd backend
source venv/bin/activate
python app.py
```

### Frontend Development
```bash
cd frontend
npm start
```

### Building for Production
```bash
cd frontend
npm run build
```

## 📦 Dependencies

### Backend
- Flask 3.0.0
- Flask-CORS 4.0.0
- anthropic >=0.34.0

### Frontend
- React 18.2.0
- Tailwind CSS 3.3.0
- Axios 1.4.0
- Lucide React 0.263.1
- React Hot Toast 2.4.1

## 🚀 Features Included

✅ **Modern UI Components**
- Glass morphism cards
- Gradient buttons
- Animated loading states
- Toast notifications

✅ **Functionality**
- Real-time script processing
- Copy to clipboard
- Character count validation
- Error handling

✅ **Responsive Design**
- Mobile-first approach
- Flexible grid layouts
- Touch-friendly interactions

✅ **Performance**
- Optimized API calls
- Efficient state management
- Fast load times

## 🎯 Next Steps

1. **Production Deployment**: Deploy to Vercel (frontend) and Railway/Heroku (backend)
2. **Environment Variables**: Secure API key management
3. **Advanced Features**: 
   - Save/load scripts
   - Content history
   - Batch processing
   - Analytics dashboard

Your modern, production-ready Caption Generator is now complete! 🎉