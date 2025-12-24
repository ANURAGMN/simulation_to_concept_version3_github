# 🎓 Adaptive Physics Tutor - Version 3

[![Python 3.12+](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/streamlit-1.30+-red.svg)](https://streamlit.io)
[![LangGraph](https://img.shields.io/badge/langgraph-0.2+-green.svg)](https://github.com/langchain-ai/langgraph)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

An intelligent teaching agent that simulates a human-like physics tutor using LangGraph and Google's Gemini AI. The agent adapts its teaching strategy in real-time based on student understanding, creating a personalized learning experience.

**🌟 [Live Demo](https://your-app.streamlit.app)** | **📖 [Quick Start](QUICKSTART.md)** | **🚀 [Deployment Guide](DEPLOYMENT.md)**

## ✨ Features

- **🧠 Adaptive Teaching**: Dynamically adjusts strategy based on student progress
- **📊 Understanding Tracking**: Monitors learning trajectory with 4-level assessment (none → partial → mostly → complete)
- **🔄 Interactive Simulation**: Changes simulation parameters to help students visualize concepts
- **💬 Natural Conversation**: Engages students with varied, context-aware responses
- **🎯 Smart Routing**: Detects when students are improving, stagnating, or regressing
- **🛡️ Guardrails**: Prevents infinite loops while maintaining flexibility

## 🏗️ Architecture

The agent uses a graph-based workflow with checkpointing:

```
┌─────────────────┐
│ content_loader  │ Extract teachable concepts
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│    teacher      │◄──────────────────┐
└────────┬────────┘                   │
         │                            │
         ▼                            │
  [INTERRUPT]      Wait for input     │
         │                            │
         ▼                            │
┌─────────────────┐                   │
│   evaluator     │ Assess response   │
└────────┬────────┘                   │
         │                            │
         ▼                            │
┌─────────────────┐                   │
│   trajectory    │ Detect patterns   │
└────────┬────────┘                   │
         │                            │
         ▼                            │
┌─────────────────┐                   │
│    strategy     │───────────────────┘
└─────────────────┘   (loop or end)
```

## 🚀 Quick Start

### Prerequisites

- Python 3.12+
- Google API key with Gemini access

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/ANURAGMN/simulation_to_concept_version3_github.git
   cd simulation_to_concept_version3_github
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   
   Create a `.env` file in the project root:
   ```bash
   GOOGLE_API_KEY=your-api-key-here
   GEMINI_MODEL=gemini-2.0-flash
   TEMPERATURE=0.7
   MAX_EXCHANGES=6
   SCAFFOLD_TRIGGER=3
   ```

### Running the Application

#### Option 1: Streamlit Web Interface (Recommended)

Run the interactive web application:

```bash
streamlit run app.py
```

Then open your browser to `http://localhost:8501`

**Features:**
- 🎨 Beautiful, intuitive UI
- 📊 Real-time progress visualization
- 💬 Chat-based interface
- 📱 Mobile-friendly
- ☁️ Easy to deploy

#### Option 2: Terminal Interface

Run the command-line version:

```bash
python main.py
```

**Features:**
- ⚡ Lightweight and fast
- 🖥️ Terminal-based interaction
- 📝 Text-only interface

## 🖥️ Interface Comparison

| Feature | Streamlit (Web) | Terminal (CLI) |
|---------|----------------|----------------|
| **UI** | 🎨 Modern, colorful | 📝 Text-based |
| **Visualization** | ✅ Real-time graphs | ❌ Text only |
| **Accessibility** | ✅ Click & type | ⌨️ Keyboard only |
| **Mobile Support** | ✅ Responsive | ❌ Desktop only |
| **Deployment** | ☁️ Web hosting | 🖥️ Local/SSH |
| **Resources** | 🔋 Medium | 💨 Lightweight |
| **Best For** | Students, demos | Power users, servers |

**Recommendation**: Use Streamlit for the best learning experience!

## 📖 Example Session

```
╔════════════════════════════════════════════════════════════════════╗
║                                                                    ║
║      🎓 ADAPTIVE PHYSICS TUTOR - Version 3                        ║
║      Interactive Teaching with Parameter History                   ║
║                                                                    ║
╚════════════════════════════════════════════════════════════════════╝

📝 Session ID: session_abc12345

┌──────────────────────────────────────────────────┐
│ 🧪 SIMULATION STATE                              │
├──────────────────────────────────────────────────┤
│  Length:  1.00 m                                 │
│  Mass:    1.00 kg                                │
│  Angle:   15.0°                                  │
│  Gravity: 9.8 m/s²                               │
└──────────────────────────────────────────────────┘

────────────────────────────────────────────────────────────
🎓 Teacher Alex:
────────────────────────────────────────────────────────────
  Hey there, friend! 👋 Today we're going to explore something 
  really fascinating about pendulums. Have you ever watched a 
  grandfather clock? PREDICT: If we make the pendulum longer, 
  will it swing faster or slower?
────────────────────────────────────────────────────────────

👩‍🎓 Your response (or 'quit' to exit):
>>> I think it will swing slower

⏳ Processing your response...

┌──────────────────────────────────────────────────┐
│ 📊 LEARNING PROGRESS                             │
├──────────────────────────────────────────────────┤
│  Understanding: 🟨🟨🟨⬜ (mostly)                │
│  Trend: 📈 improving                             │
│  Exchange: 1/6                                   │
└──────────────────────────────────────────────────┘

────────────────────────────────────────────────────────────
🎓 Teacher Alex:
────────────────────────────────────────────────────────────
  Exactly right! Great observation! Now, can you think of WHY 
  a longer pendulum takes more time to swing?
────────────────────────────────────────────────────────────
```

## 🧩 Key Components

### State Management
- **Rich State Structure**: Tracks conversation history, understanding levels, parameter changes, and teaching strategy
- **Parameter History**: Records what simulation changes helped learning
- **Conversation Metadata**: Each message includes timestamp, understanding level, and exchange number

### Teaching Strategies
The agent adapts its strategy based on student progress:

| Strategy | When Used | Teacher Behavior |
|----------|-----------|------------------|
| **continue** | Student improving | Keep current approach |
| **try_different** | Progress slowing | Change explanation style |
| **scaffold** | Student stuck | Break concept into smaller parts |
| **give_hint** | Still struggling | Provide more direct guidance |
| **summarize_advance** | Concept mastered or max exchanges | Move to next concept |

### Understanding Levels
- **none**: Student doesn't understand or says "I don't know"
- **partial**: Some understanding but with gaps or misconceptions
- **mostly**: Correct observation but missing reasoning
- **complete**: Clear understanding with explanation

## 📚 Documentation

- **[DOCUMENTATION.md](DOCUMENTATION.md)**: Complete technical documentation with architecture details, state structure, and node descriptions
- **[FIXES_REPORT.md](FIXES_REPORT.md)**: Detailed changelog of all improvements made to create natural, effective teaching interactions

## 🛠️ Configuration

Customize the agent's behavior in `config.py` or via environment variables:

```python
# Teaching guardrails
MAX_EXCHANGES = 6        # Maximum back-and-forth per concept
SCAFFOLD_TRIGGER = 3     # When to start breaking down concepts

# LLM settings
GEMINI_MODEL = "gemini-2.0-flash"
TEMPERATURE = 0.7
```

## ☁️ Deploying to Streamlit Cloud

Deploy your own instance for free on Streamlit Cloud:

### Step 1: Fork the Repository

Click the "Fork" button on GitHub to create your own copy.

### Step 2: Sign up for Streamlit Cloud

1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Sign in with GitHub

### Step 3: Deploy

1. Click "New app"
2. Select your forked repository
3. Set main file path to `app.py`
4. Click "Advanced settings"
5. Add your secrets in the "Secrets" section:

```toml
GOOGLE_API_KEY = "your-api-key-here"
GEMINI_MODEL = "gemini-2.0-flash"
TEMPERATURE = "0.7"
MAX_EXCHANGES = "6"
SCAFFOLD_TRIGGER = "3"
```

6. Click "Deploy"!

Your app will be live at `https://your-app-name.streamlit.app` 🎉

### Alternative Deployment Options

- **Heroku**: Use the included `Procfile`
- **Docker**: Build a containerized version
- **AWS/GCP/Azure**: Deploy on cloud platforms
- **Self-hosted**: Run on your own server with `streamlit run app.py`

## 🔧 Tech Stack

- **[LangGraph](https://github.com/langchain-ai/langgraph)**: Graph-based agentic workflows
- **[LangChain](https://github.com/langchain-ai/langchain)**: LLM orchestration
- **[Google Gemini](https://ai.google.dev/)**: Language model
- **[Streamlit](https://streamlit.io/)**: Web interface
- **Python 3.12+**: Core runtime

## 🎯 Use Cases

- **Educational Technology**: Adaptive tutoring systems
- **E-Learning Platforms**: Personalized learning paths
- **Physics Education**: Interactive simulation-based learning
- **AI Research**: Studying adaptive dialogue systems

## 📝 Key Innovations

1. **Trajectory Analysis**: Detects improving/stagnating/regressing patterns
2. **Parameter History**: Learns from what teaching approaches worked
3. **Teacher Modes**: Switches between encouraging/challenging/simplifying
4. **Safety Valves**: Prevents getting stuck while maintaining quality
5. **Action Labels**: Clear PREDICT/OBSERVE/EXPLAIN instructions

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Anurag MN**
- GitHub: [@ANURAGMN](https://github.com/ANURAGMN)

## 🙏 Acknowledgments

- Built with LangGraph and LangChain
- Powered by Google's Gemini AI

---

**Note**: This agent requires a Google API key with access to Gemini models. Make sure to keep your API key secure and never commit it to the repository.
