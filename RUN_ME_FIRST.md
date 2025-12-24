# 🎓 Quick Start - Run the Adaptive Physics Tutor

## Step 1: Install Dependencies

```bash
pip install -r requirements.txt
```

## Step 2: Set up Your API Key

### Option A: Create .env file
```bash
# Copy the example file
cp .env.example .env

# Edit .env and add your Google API key
# GOOGLE_API_KEY=your-actual-key-here
```

### Option B: Use the quick setup script
**Linux/Mac:**
```bash
./run_streamlit.sh
```

**Windows:**
```bash
run_streamlit.bat
```

## Step 3: Run the App

### Option 1: Streamlit Web Interface (Recommended)
```bash
streamlit run app.py
```
Then open your browser to: **http://localhost:8501**

### Option 2: Terminal Interface
```bash
python main.py
```
or
```bash
python3 main.py
```

## 🔑 Don't Have a Google API Key?

Get one for free:
1. Go to https://makersuite.google.com/app/apikey
2. Click "Create API Key"
3. Copy your key
4. Add it to your .env file

## ❓ Troubleshooting

**"No module named 'streamlit'"**
```bash
pip install -r requirements.txt
```

**"GOOGLE_API_KEY not found"**
- Make sure you created the .env file
- Check that your key is in the format: GOOGLE_API_KEY=your-key-here

**"Port 8501 already in use"**
```bash
streamlit run app.py --server.port 8502
```

## 🎉 That's It!

You're ready to start learning physics! 🚀
