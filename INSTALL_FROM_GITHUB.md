# 🚀 Install and Run from GitHub

Complete guide to run the Adaptive Physics Tutor directly from the GitHub repository.

---

## 📥 Quick Install (All Platforms)

### Step 1: Clone the Repository

**Clone the specific branch:**
```bash
git clone -b cursor/simulation-to-concept-v3-80fc https://github.com/ANURAGMN/simulation_to_concept_version3_github.git
cd simulation_to_concept_version3_github
```

**Or clone main and switch to the branch:**
```bash
git clone https://github.com/ANURAGMN/simulation_to_concept_version3_github.git
cd simulation_to_concept_version3_github
git checkout cursor/simulation-to-concept-v3-80fc
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

**Using a virtual environment (recommended):**
```bash
# Create virtual environment
python -m venv venv

# Activate it
# On Linux/Mac:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Step 3: Configure Your API Key

```bash
# Copy the example file
cp .env.example .env
```

**Edit `.env` and add your Google API key:**
```bash
GOOGLE_API_KEY=your-actual-google-api-key-here
GEMINI_MODEL=gemini-2.0-flash
TEMPERATURE=0.7
MAX_EXCHANGES=6
SCAFFOLD_TRIGGER=3
```

### Step 4: Run the Application

**Streamlit Web Interface (Recommended):**
```bash
streamlit run app.py
```
Then open **http://localhost:8501** in your browser

**Terminal Interface:**
```bash
python main.py
```

---

## 🎯 One-Command Install (Copy & Paste)

### Linux/Mac

```bash
git clone -b cursor/simulation-to-concept-v3-80fc https://github.com/ANURAGMN/simulation_to_concept_version3_github.git && \
cd simulation_to_concept_version3_github && \
python3 -m venv venv && \
source venv/bin/activate && \
pip install -r requirements.txt && \
cp .env.example .env && \
echo "" && \
echo "✅ Installation complete!" && \
echo "" && \
echo "📝 Next steps:" && \
echo "1. Edit .env and add your GOOGLE_API_KEY" && \
echo "2. Run: streamlit run app.py"
```

### Windows (PowerShell)

```powershell
git clone -b cursor/simulation-to-concept-v3-80fc https://github.com/ANURAGMN/simulation_to_concept_version3_github.git; `
cd simulation_to_concept_version3_github; `
python -m venv venv; `
.\venv\Scripts\Activate.ps1; `
pip install -r requirements.txt; `
Copy-Item .env.example .env; `
Write-Host "`n✅ Installation complete!`n" -ForegroundColor Green; `
Write-Host "📝 Next steps:" -ForegroundColor Yellow; `
Write-Host "1. Edit .env and add your GOOGLE_API_KEY"; `
Write-Host "2. Run: streamlit run app.py"
```

### Windows (Command Prompt)

```cmd
git clone -b cursor/simulation-to-concept-v3-80fc https://github.com/ANURAGMN/simulation_to_concept_version3_github.git && ^
cd simulation_to_concept_version3_github && ^
python -m venv venv && ^
venv\Scripts\activate.bat && ^
pip install -r requirements.txt && ^
copy .env.example .env && ^
echo. && ^
echo Installation complete! && ^
echo Edit .env and add your GOOGLE_API_KEY, then run: streamlit run app.py
```

---

## 🔑 Getting Your Google API Key

1. **Go to Google AI Studio:**
   - Visit: https://makersuite.google.com/app/apikey
   - Or: https://aistudio.google.com/app/apikey

2. **Create API Key:**
   - Click "Create API Key"
   - Select a Google Cloud project (or create new)
   - Copy your API key

3. **Add to .env file:**
   ```bash
   GOOGLE_API_KEY=AIzaSy...your-key-here
   ```

**Free Tier Limits:**
- 60 requests per minute
- Perfect for personal use and demos

---

## 🐳 Using Docker (Alternative)

If you prefer Docker:

```bash
# Clone repository
git clone -b cursor/simulation-to-concept-v3-80fc https://github.com/ANURAGMN/simulation_to_concept_version3_github.git
cd simulation_to_concept_version3_github

# Build Docker image
docker build -t adaptive-physics-tutor .

# Run with environment variable
docker run -p 8501:8501 -e GOOGLE_API_KEY=your-key-here adaptive-physics-tutor
```

---

## 📋 System Requirements

### Minimum Requirements
- **Python:** 3.12 or higher
- **RAM:** 512MB available
- **Disk:** 100MB free space
- **Internet:** For API calls to Google Gemini

### Recommended
- **Python:** 3.12.3
- **RAM:** 1GB available
- **Internet:** Stable connection

### Operating Systems
- ✅ Linux (Ubuntu, Debian, Fedora, etc.)
- ✅ macOS (10.14+)
- ✅ Windows (10/11)
- ✅ WSL2 (Windows Subsystem for Linux)

---

## 🔍 Verify Installation

After installation, verify everything works:

```bash
# Check Python version
python --version  # or python3 --version

# Check if packages installed
pip list | grep -E "streamlit|langgraph|langchain"

# Test import (should show no errors)
python -c "import streamlit; print('✓ Streamlit OK')"
python -c "import langgraph; print('✓ LangGraph OK')"

# Check files
ls -la app.py main.py config.py
```

---

## ⚡ Quick Start Scripts

After cloning, you can use the built-in quick start scripts:

**Linux/Mac:**
```bash
chmod +x run_streamlit.sh
./run_streamlit.sh
```

**Windows:**
```bash
run_streamlit.bat
```

These scripts will:
- Check your environment
- Verify dependencies
- Help you set up .env
- Launch the app

---

## 🌐 Deploy to Cloud (Optional)

### Streamlit Cloud (Free & Easy)

1. **Fork the repository** on GitHub
2. **Go to** https://share.streamlit.io
3. **Sign in** with GitHub
4. **Click "New app"**
5. **Select:**
   - Repository: Your fork
   - Branch: `cursor/simulation-to-concept-v3-80fc`
   - Main file: `app.py`
6. **Add secrets** in Advanced settings:
   ```toml
   GOOGLE_API_KEY = "your-key-here"
   GEMINI_MODEL = "gemini-2.0-flash"
   ```
7. **Deploy!**

Your app will be live at: `https://[your-app-name].streamlit.app`

---

## ❓ Troubleshooting

### "git: command not found"
Install Git:
- **Linux:** `sudo apt install git` or `sudo yum install git`
- **Mac:** `brew install git` or download from git-scm.com
- **Windows:** Download from git-scm.com

### "python: command not found"
- Try `python3` instead of `python`
- Or install Python from python.org

### "Permission denied" on scripts
Make scripts executable:
```bash
chmod +x run_streamlit.sh
```

### "No module named 'streamlit'"
Install dependencies:
```bash
pip install -r requirements.txt
```

### "GOOGLE_API_KEY not found"
Make sure:
1. `.env` file exists in project root
2. File contains: `GOOGLE_API_KEY=your-actual-key`
3. No quotes around the key
4. No spaces around the `=` sign

### Port 8501 already in use
Use a different port:
```bash
streamlit run app.py --server.port 8502
```

### Dependencies failing to install
Upgrade pip first:
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

---

## 📂 What You'll Get

After cloning, your directory will contain:

```
simulation_to_concept_version3_github/
├── app.py                      # Streamlit web interface
├── main.py                     # Terminal interface
├── config.py                   # Configuration
├── state.py                    # State management
├── graph.py                    # LangGraph workflow
├── requirements.txt            # Python dependencies
├── .env.example               # Environment template
├── nodes/                     # Teaching agent nodes
│   ├── content_loader.py
│   ├── teacher.py
│   ├── evaluator.py
│   ├── trajectory.py
│   └── strategy.py
├── .streamlit/                # Streamlit config
│   └── config.toml
├── run_streamlit.sh           # Quick start (Linux/Mac)
├── run_streamlit.bat          # Quick start (Windows)
└── Documentation files (.md)
```

---

## 🎓 After Installation

Once everything is running:

1. **Choose your interface:**
   - Streamlit: Beautiful web UI at http://localhost:8501
   - Terminal: Interactive CLI

2. **Start learning:**
   - Answer the teacher's questions
   - Make predictions
   - Explore physics concepts

3. **Check out the docs:**
   - `README.md` - Overview
   - `QUICKSTART.md` - Getting started
   - `DOCUMENTATION.md` - Technical details

---

## 🚀 You're All Set!

The app should now be running. Enjoy learning physics with your AI tutor! 🎓

**Need help?** 
- Check other .md files in the repository
- Open an issue on GitHub
- Review the troubleshooting section above

---

## 📞 Support

If you encounter issues:
1. Check this guide's troubleshooting section
2. Review QUICKSTART.md
3. Open a GitHub issue with:
   - Your OS and Python version
   - Error messages
   - Steps you followed
