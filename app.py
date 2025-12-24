"""
Streamlit Web Interface for Adaptive Physics Tutor
===================================================
Interactive web application for the Version 3 Teaching Agent.

Run with: streamlit run app.py
"""

import streamlit as st
import uuid
from typing import Dict, Any

from config import (
    validate_config, 
    PENDULUM_DESCRIPTION, 
    INITIAL_PARAMS,
    MAX_EXCHANGES
)
from state import create_initial_state
from graph import start_session, continue_session, get_session_state


# ═══════════════════════════════════════════════════════════════════════════
# PAGE CONFIGURATION
# ═══════════════════════════════════════════════════════════════════════════

st.set_page_config(
    page_title="Adaptive Physics Tutor",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ═══════════════════════════════════════════════════════════════════════════
# SESSION STATE INITIALIZATION
# ═══════════════════════════════════════════════════════════════════════════

def initialize_session():
    """Initialize Streamlit session state."""
    if "thread_id" not in st.session_state:
        st.session_state.thread_id = f"session_{uuid.uuid4().hex[:8]}"
    
    if "initialized" not in st.session_state:
        st.session_state.initialized = False
    
    if "teaching_state" not in st.session_state:
        st.session_state.teaching_state = None
    
    if "messages" not in st.session_state:
        st.session_state.messages = []


# ═══════════════════════════════════════════════════════════════════════════
# UI COMPONENTS
# ═══════════════════════════════════════════════════════════════════════════

def render_header():
    """Render the page header."""
    st.markdown("""
        <div style='text-align: center; padding: 1rem 0; background: linear-gradient(90deg, #667eea 0%, #764ba2 100%); border-radius: 10px; margin-bottom: 2rem;'>
            <h1 style='color: white; margin: 0;'>🎓 Adaptive Physics Tutor</h1>
            <p style='color: #f0f0f0; margin: 0.5rem 0 0 0;'>Interactive Teaching with Real-time Adaptation</p>
        </div>
    """, unsafe_allow_html=True)


def render_simulation_state(params: Dict[str, float]):
    """Display current simulation parameters."""
    st.markdown("### 🧪 Simulation State")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Length", f"{params.get('length', 1.0):.2f} m")
    with col2:
        st.metric("Mass", f"{params.get('mass', 1.0):.2f} kg")
    with col3:
        st.metric("Angle", f"{params.get('angle', 15):.1f}°")
    with col4:
        st.metric("Gravity", f"{params.get('gravity', 9.8):.1f} m/s²")


def render_progress(state: Dict[str, Any]):
    """Display learning progress."""
    st.markdown("### 📊 Learning Progress")
    
    concepts = state.get("concepts", [])
    current_idx = state.get("current_concept_index", 0)
    understanding = state.get("understanding_level", "none")
    trajectory = state.get("trajectory_status", "improving")
    exchange = state.get("exchange_count", 0)
    
    # Progress metrics
    col1, col2, col3 = st.columns(3)
    
    with col1:
        total = len(concepts)
        completed = current_idx
        progress = completed / total if total > 0 else 0
        st.metric("Concepts Completed", f"{completed}/{total}")
        st.progress(progress)
    
    with col2:
        # Understanding level with emoji
        level_display = {
            "none": "⬜ None",
            "partial": "🟨 Partial",
            "mostly": "🟧 Mostly",
            "complete": "🟩 Complete"
        }
        st.metric("Understanding", level_display.get(understanding, "⬜ None"))
    
    with col3:
        # Trajectory with emoji
        trajectory_emoji = {
            "improving": "📈 Improving",
            "stagnating": "📊 Stagnating",
            "regressing": "📉 Regressing"
        }
        st.metric("Trend", trajectory_emoji.get(trajectory, "📊 Stagnating"))
    
    # Exchange count
    st.progress(exchange / MAX_EXCHANGES, text=f"Exchange {exchange}/{MAX_EXCHANGES}")
    
    # Current concept
    if current_idx < len(concepts):
        concept = concepts[current_idx]
        st.info(f"**Current Concept:** {concept.get('title', 'Unknown')}")


def render_conversation(state: Dict[str, Any]):
    """Display conversation history."""
    st.markdown("### 💬 Conversation")
    
    conversation_history = state.get("conversation_history", [])
    
    if not conversation_history:
        st.info("Start the session to begin learning!")
        return
    
    # Display messages
    for msg in conversation_history:
        role = msg.get("role", "")
        content = msg.get("content", "")
        
        if role == "teacher":
            with st.chat_message("assistant", avatar="🎓"):
                st.markdown(f"**Teacher Alex:**\n\n{content}")
        elif role == "student":
            with st.chat_message("user", avatar="👩‍🎓"):
                st.markdown(content)


def render_sidebar():
    """Render sidebar with session info and controls."""
    with st.sidebar:
        st.markdown("## Session Info")
        st.text(f"ID: {st.session_state.thread_id}")
        
        st.markdown("---")
        
        st.markdown("## About")
        st.markdown("""
        This adaptive physics tutor uses AI to:
        - 🧠 Assess your understanding
        - 📈 Track your learning progress
        - 🔄 Adapt teaching strategy
        - 🎯 Personalize explanations
        """)
        
        st.markdown("---")
        
        st.markdown("## How to Use")
        st.markdown("""
        1. Click **Start Session** below
        2. Read the teacher's message
        3. Type your response in the chat
        4. Continue the conversation!
        """)
        
        st.markdown("---")
        
        # Control buttons
        if not st.session_state.initialized:
            if st.button("🚀 Start Session", use_container_width=True, type="primary"):
                start_teaching_session()
        else:
            if st.button("🔄 Reset Session", use_container_width=True):
                reset_session()
        
        st.markdown("---")
        
        # Tips
        with st.expander("💡 Tips for Learning"):
            st.markdown("""
            - Think out loud - explain your reasoning
            - Make predictions before changes
            - Ask "why" when you're curious
            - It's okay to say "I don't know"
            """)


# ═══════════════════════════════════════════════════════════════════════════
# SESSION MANAGEMENT
# ═══════════════════════════════════════════════════════════════════════════

def start_teaching_session():
    """Initialize and start a new teaching session."""
    with st.spinner("🎓 Initializing teaching session..."):
        try:
            # Validate config
            validate_config()
            
            # Create initial state
            initial_state = create_initial_state(
                topic_description=PENDULUM_DESCRIPTION,
                initial_params=INITIAL_PARAMS
            )
            
            # Start session
            state = start_session(initial_state, st.session_state.thread_id)
            
            # Update session state
            st.session_state.teaching_state = state
            st.session_state.initialized = True
            st.session_state.messages = []
            
            st.success("✅ Session started! The teacher is ready.")
            st.rerun()
            
        except Exception as e:
            st.error(f"❌ Error starting session: {e}")
            st.exception(e)


def reset_session():
    """Reset the session and start fresh."""
    st.session_state.thread_id = f"session_{uuid.uuid4().hex[:8]}"
    st.session_state.initialized = False
    st.session_state.teaching_state = None
    st.session_state.messages = []
    st.rerun()


def process_student_response(response: str):
    """Process student's response and get teacher's reply."""
    if not response.strip():
        st.warning("Please enter a response.")
        return
    
    with st.spinner("🤔 Teacher is thinking..."):
        try:
            # Continue session with response
            state = continue_session(response, st.session_state.thread_id)
            
            # Update state
            st.session_state.teaching_state = state
            
            # Force rerun to show new message
            st.rerun()
            
        except Exception as e:
            st.error(f"❌ Error processing response: {e}")
            st.exception(e)


# ═══════════════════════════════════════════════════════════════════════════
# MAIN APP
# ═══════════════════════════════════════════════════════════════════════════

def main():
    """Main application entry point."""
    initialize_session()
    render_header()
    render_sidebar()
    
    # Main content area
    if not st.session_state.initialized:
        # Welcome screen
        st.markdown("""
        ## 👋 Welcome to the Adaptive Physics Tutor!
        
        This intelligent tutoring system will guide you through understanding pendulum physics
        using interactive simulations and personalized teaching.
        
        ### What makes this tutor special?
        
        - **🧠 Adaptive Learning**: The tutor adjusts its teaching strategy based on your progress
        - **📊 Real-time Assessment**: Your understanding is continuously evaluated
        - **🔄 Interactive Simulation**: Parameters change to help you visualize concepts
        - **💬 Natural Conversation**: Learn through dialogue, just like with a human tutor
        
        ### Ready to start?
        
        Click the **"Start Session"** button in the sidebar to begin your learning journey!
        """)
        
        # Show example
        with st.expander("📖 Preview: What you'll learn"):
            st.markdown(PENDULUM_DESCRIPTION)
    
    else:
        # Active session
        state = st.session_state.teaching_state
        
        if state is None:
            st.error("Session state is missing. Please restart.")
            return
        
        # Check if session is complete
        if state.get("session_complete", False):
            st.balloons()
            st.success("🎉 Congratulations! You've completed all concepts!")
            
            # Show summary
            concepts = state.get("concepts", [])
            st.markdown("### 📚 Concepts Mastered")
            for i, concept in enumerate(concepts, 1):
                st.markdown(f"{i}. ✅ {concept.get('title', 'Unknown')}")
            
            param_history = state.get("parameter_history", [])
            effective_count = sum(1 for p in param_history if p.get("was_effective"))
            st.markdown(f"\n### 🧪 Exploration Summary")
            st.markdown(f"- Total parameter changes: {len(param_history)}")
            st.markdown(f"- Effective changes: {effective_count}")
            
            if st.button("🔄 Start New Session", type="primary"):
                reset_session()
            return
        
        # Display state
        col1, col2 = st.columns([2, 1])
        
        with col1:
            render_conversation(state)
        
        with col2:
            render_simulation_state(state.get("current_params", INITIAL_PARAMS))
            st.markdown("---")
            render_progress(state)
        
        # Input area
        st.markdown("---")
        st.markdown("### ✍️ Your Response")
        
        # Use a form for input
        with st.form("response_form", clear_on_submit=True):
            user_input = st.text_area(
                "Type your response here...",
                height=100,
                placeholder="Share your thoughts, predictions, or questions...",
                label_visibility="collapsed"
            )
            
            col1, col2, col3 = st.columns([1, 1, 4])
            with col1:
                submitted = st.form_submit_button("📤 Send", use_container_width=True, type="primary")
            with col2:
                if st.form_submit_button("💭 I don't know", use_container_width=True):
                    user_input = "I don't know"
                    submitted = True
            
            if submitted and user_input:
                process_student_response(user_input)


if __name__ == "__main__":
    main()
