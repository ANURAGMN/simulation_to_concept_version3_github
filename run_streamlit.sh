#!/bin/bash
# Quick start script for running the Streamlit app

echo "🎓 Starting Adaptive Physics Tutor..."
echo ""

# Check if .env file exists
if [ ! -f .env ]; then
    echo "⚠️  No .env file found!"
    echo "Creating .env from template..."
    cp .env.example .env
    echo ""
    echo "📝 Please edit .env and add your GOOGLE_API_KEY"
    echo "Then run this script again."
    exit 1
fi

# Check if GOOGLE_API_KEY is set
if ! grep -q "GOOGLE_API_KEY=your-" .env 2>/dev/null; then
    echo "✅ Configuration found"
else
    echo "⚠️  Please set your GOOGLE_API_KEY in .env file"
    exit 1
fi

# Check if streamlit is installed
if ! python3 -c "import streamlit" 2>/dev/null; then
    echo "📦 Installing dependencies..."
    pip3 install -r requirements.txt
fi

echo ""
echo "🚀 Launching Streamlit app..."
echo "📍 Open your browser to: http://localhost:8501"
echo ""

# Run the app
streamlit run app.py
