import streamlit as st

from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

from services.llm_service import LLMService
from utils.validators import validate_code_input
from examples.example_codes import EXAMPLES

# Configure Streamlit page
st.set_page_config(
    page_title="CodeLens AI",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Initialize LLM Service ---
def get_llm_service():
    try:
        return LLMService()
    except Exception as e:
        return None

llm_service = get_llm_service()

# --- Advanced Premium CSS ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }
    
    @keyframes fadeUp {
        0% { opacity: 0; transform: translateY(20px); }
        100% { opacity: 1; transform: translateY(0); }
    }
    
    @keyframes gradientShift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    .main-header {
        font-size: 4rem;
        font-weight: 800;
        margin-bottom: 0rem;
        background: linear-gradient(-45deg, #FF3366, #FF9933, #33CCFF, #9933FF);
        background-size: 300% 300%;
        animation: gradientShift 10s ease infinite;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        letter-spacing: -1.5px;
        line-height: 1.2;
    }
    
    .sub-header {
        font-size: 1.2rem;
        color: #A0AEC0;
        font-weight: 400;
        margin-bottom: 2rem;
        margin-top: 0.2rem;
        letter-spacing: 0.5px;
    }

    div[data-testid="stMetric"] {
        background: rgba(30, 30, 35, 0.6);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.08);
        padding: 20px;
        border-radius: 16px;
        box-shadow: 0 10px 30px -10px rgba(0, 0, 0, 0.3);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    
    div[data-testid="stMetric"]:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 35px -10px rgba(0, 0, 0, 0.5);
        border: 1px solid rgba(255, 255, 255, 0.15);
    }

    div[data-testid="stMetricValue"] {
        font-size: 2.2rem;
        font-weight: 700;
        background: -webkit-linear-gradient(45deg, #00f2fe, #4facfe);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    div[data-testid="stMetricLabel"] {
        font-weight: 600;
        color: #E2E8F0;
        font-size: 1rem;
    }

    /* --- MAC WINDOW UNIFIED FRAME --- */
    
    /* 1. Target the Streamlit Bordered Container to act as the single Mac Window */
    div[data-testid="stVerticalBlockBorderWrapper"] {
        background-color: #1d1f21 !important;
        border: 1px solid rgba(255, 255, 255, 0.15) !important;
        border-radius: 12px !important;
        box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.7) !important;
        padding: 0 !important; /* Remove internal padding to let elements touch edges */
        overflow: hidden !important; /* Ensure perfectly rounded corners */
    }

    /* 2. Remove the internal gap between the top bar and editor */
    div[data-testid="stVerticalBlockBorderWrapper"] [data-testid="stVerticalBlock"] {
        gap: 0 !important;
    }

    /* 3. The Top Bar (Inside the window, no borders needed) */
    .mac-top-bar {
        background-color: #1d1f21 !important;
        width: 100% !important;
        height: 38px !important;
        display: flex !important;
        align-items: center !important;
        padding: 0 15px !important;
        position: relative !important;
        margin: 0 !important;
    }
    
    /* 4. Ultra Premium Text Area Styling */
    div[data-baseweb="textarea"] {
        background-color: #1d1f21 !important;
        border: none !important;
        border-radius: 0 0 12px 12px !important;
    }
    div[data-baseweb="textarea"] textarea {
        background-color: #1d1f21 !important;
        color: #c5c8c6 !important;
        font-family: 'Consolas', 'Fira Code', 'JetBrains Mono', monospace !important;
        font-size: 15px !important;
        line-height: 1.6 !important;
        padding: 16px 20px !important;
        border: none !important;
        box-shadow: none !important; /* Remove Streamlit focus ring */
        caret-color: #81a2be !important;
        resize: none !important;
    }
    div[data-testid="stTextArea"] {
        margin: 0 !important;
        padding: 0 !important;
    }

    .mac-buttons {
        width: 12px;
        height: 12px;
        border-radius: 50%;
        background-color: #ff5f56;
        box-shadow: 20px 0 0 #ffbd2e, 40px 0 0 #27c93f;
    }
    
    .mac-title {
        position: absolute;
        width: 100%;
        text-align: center;
        color: #888;
        font-size: 13px;
        font-weight: 500;
        font-family: 'Inter', sans-serif;
        left: 0;
        pointer-events: none;
    }

    .result-container {
        animation: fadeUp 0.6s cubic-bezier(0.16, 1, 0.3, 1) forwards;
    }

    .custom-divider {
        height: 1px;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.2), transparent);
        margin: 2.5rem 0;
    }
    
    .stButton>button {
        font-weight: 600;
        border-radius: 8px;
        transition: all 0.2s ease;
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
    }
</style>
""", unsafe_allow_html=True)

if not llm_service:
    st.error("⚠️ **API Key Missing or Invalid**")
    st.info("Please create a `.env` file with your `GEMINI_API_KEY`.")
    st.stop()

# --- State Initialization ---
if "code_input" not in st.session_state:
    st.session_state.code_input = ""
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "report_markdown" not in st.session_state:
    st.session_state.report_markdown = ""
if "analysis_result" not in st.session_state:
    st.session_state.analysis_result = None
if "analysis_type" not in st.session_state:
    st.session_state.analysis_type = None

def load_example():
    lang = st.session_state.language
    st.session_state.code_input = EXAMPLES[lang]['code']
    st.session_state.chat_history = []
    st.session_state.report_markdown = ""
    st.session_state.analysis_result = None

# --- Sidebar Configuration ---
with st.sidebar:
    st.title("⚙️ Workspace")
    st.markdown("Customize your analysis environment.")
    
    st.selectbox(
        "Programming Language",
        options=["Python", "C++", "Java", "JavaScript"],
        key="language"
    )
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("### Templates")
    st.markdown("Test the engine with a pre-written snippet.")
    
    st.button(
        f"Load {EXAMPLES[st.session_state.language]['name']}", 
        on_click=load_example,
        use_container_width=True
    )
    
    st.markdown("---")
    # Caption removed as requested

# --- Main Application Area ---
st.markdown('<div class="main-header">CodeLens AI</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Understand logic. Improve readability. Optimize performance.</div>', unsafe_allow_html=True)

st.markdown("#### 💻 Source Editor")
st.caption("Press `CTRL + ENTER` or click outside the editor to apply your code changes.")

ace_lang_map = {"Python": "python", "C++": "c_cpp", "Java": "java", "JavaScript": "javascript"}
ace_lang = ace_lang_map.get(st.session_state.language, "python")

file_name_map = {"Python": "main.py", "C++": "main.cpp", "Java": "Main.java", "JavaScript": "index.js"}
dynamic_filename = file_name_map.get(st.session_state.language, "main.py")

# Wrap everything in a Streamlit Bordered Container for a guaranteed single unified border
with st.container(border=True):
    # Inject the standalone Mac Top Bar
    st.markdown(f"""
    <div class="mac-top-bar">
        <div class="mac-buttons"></div>
        <div class="mac-title">{dynamic_filename}</div>
    </div>
    """, unsafe_allow_html=True)

    # Ultra-premium native text area (Works perfectly with Streamlit state!)
    code = st.text_area(
        "Source Code",
        value=st.session_state.code_input,
        height=350,
        label_visibility="collapsed"
    )

st.session_state.code_input = code # Keep state in sync

# Action Bar
st.markdown("<br>", unsafe_allow_html=True)
col_action1, col_action2, col_action3 = st.columns([3, 1, 1])

with col_action1:
    action = st.radio(
        "Analysis Mode:",
        options=["🔍 Explain Code", "✨ Improve Code", "⚡ Optimize Code"],
        horizontal=True,
        label_visibility="collapsed"
    )

with col_action2:
    run_btn = st.button("Run Analysis", type="primary", use_container_width=True)

with col_action3:
    if st.session_state.report_markdown:
        st.download_button(
            label="📥 Download Report",
            data=st.session_state.report_markdown,
            file_name="codelens_analysis.md",
            mime="text/markdown",
            use_container_width=True
        )

st.markdown('<div class="custom-divider"></div>', unsafe_allow_html=True)

# --- Execution Logic (Fetch Data) ---
if run_btn:
    is_valid, error_msg = validate_code_input(code)
    
    if not is_valid:
        st.error(error_msg)
    else:
        st.session_state.chat_history = [] # Reset chat for new analysis
        
        if action == "🔍 Explain Code":
            with st.spinner("Analyzing code architecture and logic..."):
                try:
                    response = llm_service.explain_code(code, st.session_state.language)
                    st.session_state.analysis_result = response
                    st.session_state.analysis_type = "explain"
                    st.session_state.report_markdown = f"# Code Explanation\n\n## Summary\n{response.summary}\n\n## Complexity\n- Time: {response.time_complexity.complexity}\n- Space: {response.space_complexity.complexity}\n"
                except Exception as e:
                    st.error(f"Failed to explain code: {str(e)}")
                    
        elif action == "✨ Improve Code":
            with st.spinner("Refactoring code for readability and maintainability..."):
                try:
                    response = llm_service.improve_code(code, st.session_state.language)
                    st.session_state.analysis_result = response
                    st.session_state.analysis_type = "improve"
                    st.session_state.report_markdown = f"# Code Improvement\n\n## Changes\n{response.explanation}\n\n## New Code\n```\n{response.improved_code}\n```"
                except Exception as e:
                    st.error(f"Failed to improve code: {str(e)}")

        elif action == "⚡ Optimize Code":
            with st.spinner("Identifying performance bottlenecks..."):
                try:
                    response = llm_service.optimize_code(code, st.session_state.language)
                    st.session_state.analysis_result = response
                    st.session_state.analysis_type = "optimize"
                    st.session_state.report_markdown = f"# Code Optimization\n\n## Analysis\n{response.analysis}\n\n## Optimized Code\n```\n{response.optimized_code}\n```"
                except Exception as e:
                    st.error(f"Failed to optimize code: {str(e)}")

# --- Render Results (Outside button logic so it persists during chat) ---
if st.session_state.analysis_result:
    response = st.session_state.analysis_result
    st.markdown('<div class="result-container">', unsafe_allow_html=True)
    
    if st.session_state.analysis_type == "explain":
        with st.container(border=True):
            st.markdown("### 📊 Executive Summary")
            st.info(response.summary)
            st.markdown("<br>", unsafe_allow_html=True)
            
            col_tc, col_sc = st.columns(2)
            with col_tc:
                st.metric("Time Complexity", response.time_complexity.complexity, help=response.time_complexity.explanation)
            with col_sc:
                st.metric("Space Complexity", response.space_complexity.complexity, help=response.space_complexity.explanation)
            
            st.markdown("---")
            tab1, tab2, tab3 = st.tabs(["🔄 Execution Flow", "🛠️ Key Functions", "📦 Key Variables"])
            
            with tab1:
                for i, step in enumerate(response.how_it_works):
                    st.markdown(f"**{i+1}.** {step}")
            with tab2:
                if response.important_functions:
                    for func in response.important_functions:
                        st.markdown(f"- **`{func.name}`**: {func.description}")
                else:
                    st.write("No major functions identified.")
            with tab3:
                if response.important_variables:
                    for var in response.important_variables:
                        st.markdown(f"- **`{var.name}`**: {var.description}")
                else:
                    st.write("No major variables identified.")
                    
    elif st.session_state.analysis_type == "improve":
        with st.container(border=True):
            st.markdown("### 💡 Refactoring Insights")
            st.success(response.explanation)
            with st.expander("View Specific Changes", expanded=True):
                for change in response.changes:
                    st.markdown(f"- {change}")
            st.markdown("### ✨ Improved Implementation")
            st.code(response.improved_code, language=st.session_state.language.lower())
            
    elif st.session_state.analysis_type == "optimize":
        with st.container(border=True):
            st.markdown("### 📈 Performance Analysis")
            st.info(response.analysis)
            st.markdown("<br>", unsafe_allow_html=True)
            col_o1, col_o2 = st.columns(2)
            with col_o1:
                st.metric("Original Time Complexity", response.original_time_complexity)
                st.metric("Original Space Complexity", response.original_space_complexity)
            with col_o2:
                st.metric("Optimized Time Complexity", response.optimized_time_complexity)
                st.metric("Optimized Space Complexity", response.optimized_space_complexity)
            st.markdown("---")
            if response.no_optimization_possible or not response.optimized_code:
                st.success("The provided code is already highly optimal.")
            else:
                with st.expander("View Optimization Strategy", expanded=True):
                    for change in response.changes:
                        st.markdown(f"- {change}")
                st.markdown("### ⚡ Optimized Implementation")
                st.code(response.optimized_code, language=st.session_state.language.lower())
                
    st.markdown('</div>', unsafe_allow_html=True)
