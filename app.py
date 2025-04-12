import streamlit as st
import google.generativeai as genai

# === Configuration ===
API_KEY = "AIzaSyCDbIQrUKBpo-jbB24CbKkMG9nnYJ807b0"  # Replace this with your actual Gemini API key
genai.configure(api_key=API_KEY)

# Initialize the Gemini model
model = genai.GenerativeModel('models/gemini-2.0-flash-lite-preview-02-05')

# === Chatbot Logic ===
def chat_with_bot(user_input, conversation_history):
    try:
        conversation_history.append(user_input)
        with st.spinner("Thinking..."):
            response = model.generate_content(conversation_history)
        conversation_history.append(response.text)
        return response.text, conversation_history
    except Exception as e:
        return f"An error occurred: {e}", conversation_history

# === Streamlit App ===
def main():
    st.set_page_config(page_title="PulseBot", page_icon="🤖", layout="wide")
    st.title("🤖 PulseBot")
    st.markdown("Welcome to **PulseBot**. Ask anything and I'll try my best to help!")

    # === Sidebar Settings ===
    st.sidebar.header("⚙️ Settings")  # Gear icon for settings
    theme = st.sidebar.selectbox("🎨 Theme", ["Light", "Dark"])  # Palette icon for theme

    # === About Section ===
    st.sidebar.header("ℹ️ About PulseBot")  # Info icon for about section
    st.sidebar.markdown("""
    **PulseBot** is a powerful AI-powered chatbot built using Google's Gemini API. 
    It is designed to assist users by providing intelligent responses to their queries.
    
    **Features**:
    - Real-time conversational AI.
    - Light/Dark theme support.
    - Clear conversation history with one click.
    
    **Developed By**:  
    - Uppala Aravind  
    - uppalaaravind28@gmail.com
    """)

    # === Custom CSS ===
    chat_styles = """
        <style>
        .chat-container {
            max-height: 65vh;
            overflow-y: auto;
            border: 1px solid #ccc;
            border-radius: 10px;
            background-color: %s;
        }
        .msg-user, .msg-bot {
            width: fit-content;
            padding: 1rem;
            border-radius: 12px;
            margin-bottom: 1rem;
            max-width: 75%%;
            line-height: 1.5;
        }
        .msg-user {
            background-color: #DCF8C6;
            margin-left: auto;
            color: black;
        }
        .msg-bot {
            background-color: #F1F1F1;
            margin-right: auto;
            color: black;
        }
        .footer {
            bottom: 0;
            width: 100%%;
            text-align: center;
            padding: 10px;
            background-color: %s;  /* Footer background color */
            color: %s;             /* Footer text color */
            font-size: 16px;
        }
        .footer-content {
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 10px;
            max-width: 900px;
            margin: 0 auto;
        }
        .footer p {
            margin: 0;
            line-height: 1.7;
            font-weight: 400;
            color: #34495e;
        }
        .footer a {
            color: #2980b9;
            font-weight: 500;
            text-decoration: none;
            transition: color 0.25s ease-in-out, text-decoration 0.25s ease-in-out;
        }
        .footer a:hover {
            color: #1abc9c;
            text-decoration: underline;
        }
        .footer strong {
            color: #2c3e50;
            font-weight: 600;
            letter-spacing: 0.3px;
        }
        </style>
    """ % (
        "#1e1e1e" if theme == "Dark" else "#ffffff",  # Argument 1: Chat container background
        "#1e1e1e" if theme == "Dark" else "#ffffff",  # Argument 2: Footer background color
        "#ffffff" if theme == "Dark" else "#000000"   # Argument 3: Footer text color
    )

    st.markdown(chat_styles, unsafe_allow_html=True)

    # === Session State ===
    if "conversation_history" not in st.session_state:
        st.session_state.conversation_history = []
    if "clear_input" not in st.session_state:
        st.session_state.clear_input = False

    # === Clear Input if Flagged ===
    if st.session_state.clear_input:
        st.session_state.clear_input = False  # Reset the flag immediately
        st.rerun()

    # === Chat Display ===
    with st.container():
        st.markdown('<div class="chat-container">', unsafe_allow_html=True)
        for i, message in enumerate(st.session_state.conversation_history):
            role_class = "msg-user" if i % 2 == 0 else "msg-bot"
            st.markdown(f'<div class="{role_class}">{message}</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # === User Input ===
    user_input = st.text_input(
        "Ask me something:", 
        key="user_input", 
        value="" if st.session_state.clear_input else ""
    )

    if user_input.strip():
        response, st.session_state.conversation_history = chat_with_bot(
            user_input.strip(), st.session_state.conversation_history
        )
        st.session_state.clear_input = True
        st.rerun()

    # === Clear Chat Button ===
    if st.button("🧹 Clear Conversation"):  # Broom icon for clearing chat
        st.session_state.conversation_history = []
        st.session_state.clear_input = True
        st.rerun()

    # === Footer ===
    st.markdown("""
        <footer class="footer">
            <div class="footer-content">
                <p>
                    Developed by <strong>Uppala Aravind</strong> | 
                    <a href="https://github.com/UppalaAravind28" target="_blank" style="color: #2980b9; text-decoration: none;">GitHub</a> | 
                    <a href="https://www.linkedin.com/in/uppala-aravind-28-lin/" target="_blank" style="color: #2980b9; text-decoration: none;">LinkedIn</a>
                </p>
                <p>&copy; 2025 All Rights Reserved.</p>
            </div>
        </footer>
    """, unsafe_allow_html=True)


# Run the app
if __name__ == "__main__":
    main()