# 🎓 Adaptive Physics Tutor - Version 3

An intelligent teaching agent that simulates a human-like physics tutor using LangGraph and Google's Gemini AI. The agent adapts its teaching strategy in real-time based on student understanding, creating a personalized learning experience.

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

4. **Run the agent**
   ```bash
   python main.py
   ```

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

## 🔧 Tech Stack

- **[LangGraph](https://github.com/langchain-ai/langgraph)**: Graph-based agentic workflows
- **[LangChain](https://github.com/langchain-ai/langchain)**: LLM orchestration
- **[Google Gemini](https://ai.google.dev/)**: Language model
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
