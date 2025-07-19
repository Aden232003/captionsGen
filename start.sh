#!/bin/bash

echo "🚀 Starting Caption Generator Application..."
echo "======================================="

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Check if we're in the right directory
if [ ! -f "caption_generator.py" ]; then
    echo -e "${RED}❌ Error: Please run this script from the project root directory${NC}"
    exit 1
fi

# Function to check if a command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Check dependencies
echo -e "${YELLOW}📋 Checking dependencies...${NC}"

if ! command_exists python3; then
    echo -e "${RED}❌ Python3 not found. Please install Python3${NC}"
    exit 1
fi

if ! command_exists npm; then
    echo -e "${RED}❌ npm not found. Please install Node.js${NC}"
    exit 1
fi

echo -e "${GREEN}✅ All dependencies found${NC}"

# Setup and start backend
echo -e "${YELLOW}🔧 Setting up backend...${NC}"
cd backend

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install Python dependencies
echo "Installing Python dependencies..."
pip install -r requirements.txt

# Start backend in background
echo -e "${GREEN}🚀 Starting Flask backend...${NC}"
python app.py &
BACKEND_PID=$!

# Wait for backend to start
echo "Waiting for backend to start..."
sleep 5

# Check if backend is running
if kill -0 $BACKEND_PID 2>/dev/null; then
    echo -e "${GREEN}✅ Backend started successfully on http://localhost:5001${NC}"
else
    echo -e "${RED}❌ Backend failed to start${NC}"
    exit 1
fi

# Setup and start frontend
echo -e "${YELLOW}🔧 Setting up frontend...${NC}"
cd ../frontend

# Install Node.js dependencies
echo "Installing Node.js dependencies..."
npm install

# Start frontend
echo -e "${GREEN}🚀 Starting React frontend...${NC}"
npm start &
FRONTEND_PID=$!

# Wait for frontend to start
echo "Waiting for frontend to start..."
sleep 10

echo -e "${GREEN}✅ Application started successfully!${NC}"
echo "======================================="
echo -e "${GREEN}🌐 Frontend: http://localhost:3000${NC}"
echo -e "${GREEN}🔧 Backend:  http://localhost:5001${NC}"
echo "======================================="
echo -e "${YELLOW}📝 Instructions:${NC}"
echo "1. Open http://localhost:3000 in your browser"
echo "2. Enter your video script in the text area"
echo "3. Click 'Generate Content' to create captions and titles"
echo "4. Use the copy buttons to copy the generated content"
echo ""
echo -e "${YELLOW}🛑 To stop the application:${NC}"
echo "Press Ctrl+C to stop this script"
echo "Or run: pkill -f 'python app.py' && pkill -f 'npm start'"

# Function to cleanup on exit
cleanup() {
    echo -e "\n${YELLOW}🛑 Stopping application...${NC}"
    kill $BACKEND_PID 2>/dev/null
    kill $FRONTEND_PID 2>/dev/null
    echo -e "${GREEN}✅ Application stopped${NC}"
    exit 0
}

# Set trap to cleanup on script exit
trap cleanup INT TERM

# Keep script running
echo -e "${GREEN}🔄 Application is running. Press Ctrl+C to stop.${NC}"
wait