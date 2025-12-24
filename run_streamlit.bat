@echo off
REM Quick start script for running the Streamlit app on Windows

echo 🎓 Starting Adaptive Physics Tutor...
echo.

REM Check if .env file exists
if not exist .env (
    echo ⚠️  No .env file found!
    echo Creating .env from template...
    copy .env.example .env
    echo.
    echo 📝 Please edit .env and add your GOOGLE_API_KEY
    echo Then run this script again.
    exit /b 1
)

echo ✅ Configuration found
echo.
echo 🚀 Launching Streamlit app...
echo 📍 Open your browser to: http://localhost:8501
echo.

REM Run the app
streamlit run app.py
