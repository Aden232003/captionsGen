#!/bin/bash

# Get the directory where the script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

echo "🚀 Caption Generator Vercel Deployment Script"
echo "=============================================="

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='[0m' # No Color

# Check if vercel CLI is installed
if ! command -v vercel &> /dev/null; then
    echo -e "${YELLOW}📦 Installing Vercel CLI...${NC}"
    npm install -g vercel
fi

echo -e "${BLUE}🔑 Please make sure you're logged into Vercel${NC}"
echo "Run: vercel login (if not already logged in)"
echo ""
read -p "Press Enter when you're logged in to continue..."

# --- Deploy Full-Stack Application ---
cd "$SCRIPT_DIR/frontend"

# Deploy the full-stack application (API key should be set in Vercel dashboard)
echo -e "${YELLOW}🚀 Deploying Full-Stack Application...${NC}"
echo -e "${BLUE}ℹ️  Using ANTHROPIC_API_KEY from Vercel environment variables${NC}"
echo -e "${BLUE}ℹ️  Frontend will be served from root, API from /api routes${NC}"

# The last line of the output from 'vercel --prod' is the URL
DEPLOY_OUTPUT=$(vercel --prod --yes)
APP_URL=$(echo "$DEPLOY_OUTPUT" | tail -n 1)

if [[ $? -ne 0 || -z "$APP_URL" || ! "$APP_URL" == *https* ]]; then
    echo -e "${RED}❌ Application deployment failed. Aborting.${NC}"
    echo -e "${RED}Vercel output:\n$DEPLOY_OUTPUT${NC}"
    exit 1
fi

echo -e "${GREEN}🎉 Deployment Complete!${NC}"
echo "=============================================="
echo -e "${GREEN}✅ Your Caption Generator is now live!${NC}"
echo -e "${BLUE}🌐 Application URL:${NC} $APP_URL"
echo -e "${BLUE}🔧 API Endpoint:${NC} $APP_URL/api"
echo ""
echo -e "${YELLOW}📝 Next Steps:${NC}"
echo "1. Open your frontend URL in a browser"
echo "2. Test the caption generator"
echo "3. Share with the world! 🌍"
