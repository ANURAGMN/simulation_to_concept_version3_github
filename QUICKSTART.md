# 🚀 Quick Start Guide

Get up and running with the Adaptive Physics Tutor in 5 minutes!

## ⚡ Fastest Way (Streamlit Cloud)

**No installation required! Deploy in 3 steps:**

1. **Fork** this repo on GitHub
2. **Go to** [share.streamlit.io](https://share.streamlit.io)
3. **Deploy** and add your `GOOGLE_API_KEY` in secrets

Done! Your app is live. 🎉

---

## 💻 Local Development

### Step 1: Clone and Install

```bash
# Clone the repository
git clone https://github.com/ANURAGMN/simulation_to_concept_version3_github.git
cd simulation_to_concept_version3_github

# Install dependencies
pip install -r requirements.txt
```

### Step 2: Configure

```bash
# Copy environment template
cp .env.example .env

# Edit .env and add your Google API key
# GOOGLE_API_KEY=your-key-here
```

### Step 3: Run

**Streamlit (Recommended):**
```bash
streamlit run app.py
```
Then open `http://localhost:8501`

**Or use the quick start script:**
- Linux/Mac: `./run_streamlit.sh`
- Windows: `run_streamlit.bat`

**Terminal Version:**
```bash
python main.py
```

---

## 🔑 Getting a Google API Key

1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Click "Create API Key"
3. Copy your key
4. Add to `.env` file or Streamlit secrets

**Free tier includes:**
- 60 requests per minute
- Perfect for learning and demos

---

## 🐛 Troubleshooting

### "No module named 'streamlit'"
```bash
pip install -r requirements.txt
```

### "GOOGLE_API_KEY not found"
Make sure your `.env` file contains:
```
GOOGLE_API_KEY=your-actual-key-here
```

### "Port 8501 already in use"
```bash
streamlit run app.py --server.port 8502
```

### Still having issues?
Check the [full documentation](DOCUMENTATION.md) or [open an issue](https://github.com/ANURAGMN/simulation_to_concept_version3_github/issues)

---

## 📚 Next Steps

Once running:

1. **Start a session** - Click "Start Session" or just run the app
2. **Engage with the tutor** - Answer questions and make predictions
3. **Learn concepts** - Work through all physics concepts
4. **Share your instance** - Deploy to Streamlit Cloud and share with others

For deployment options, see [DEPLOYMENT.md](DEPLOYMENT.md)

---

## 💡 Tips

- **Be specific** in your responses - explain your reasoning
- **Make predictions** before parameter changes
- **Don't be afraid to say "I don't know"** - the tutor adapts!
- **Take your time** - learning is a process

---

## 🎓 Learning Path

The tutor will guide you through these concepts:

1. **Length affects period** - Longer pendulums swing slower
2. **Mass independence** - Weight doesn't change swing speed
3. **Small angle approximation** - Angle doesn't matter much for small swings
4. **Gravity's role** - Stronger gravity = faster swings

Each concept includes:
- Interactive predictions
- Real-time parameter changes
- Adaptive explanations
- Progress tracking

---

Happy learning! 🚀
