import streamlit as st
import ollama

# -----------------------------
# PAGE SETTINGS
# -----------------------------
st.set_page_config(
    page_title="AI Mission Control",
    page_icon="🚀",
    layout="wide"
)

# -----------------------------
# MISSION DATA
# -----------------------------
fuel = 85
battery = 78
oxygen = 92
human_status = "Safe"
mission_status = "Active"

# -----------------------------
# TITLE
# -----------------------------
st.title("🚀 AI Mission Control")

st.write(
    "Monitor the mission and ask the AI anything."
)

st.divider()

# -----------------------------
# MISSION STATUS
# -----------------------------
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric("⛽ Fuel", f"{fuel}%")

with col2:
    st.metric("🔋 Battery", f"{battery}%")

with col3:
    st.metric("🫁 Oxygen", f"{oxygen}%")

with col4:
    st.metric("👨‍🚀 Human", human_status)

with col5:
    st.metric("🚀 Mission", mission_status)

st.divider()

# -----------------------------
# AI RESPONSE
# -----------------------------
st.subheader("🤖 AI Response")

st.info(
    "Ask me anything. I can answer mission questions and general questions."
)

# -----------------------------
# CHAT HISTORY
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# -----------------------------
# AI FUNCTION
# -----------------------------
def ask_ai(question):

    mission_information = f"""
You are an AI Mission Control Assistant.

Current mission information:

Fuel: {fuel}%
Battery: {battery}%
Oxygen: {oxygen}%
Human Status: {human_status}
Mission Status: {mission_status}

Important:
- If the user asks about the mission, spacecraft, fuel, battery,
  oxygen, human status, or mission status, use the information above.
- If the user asks a general question unrelated to the mission,
  answer it normally.
- You are not limited to mission questions.
- Answer questions clearly and simply.
- Do not say that you can only answer mission questions.

User question:
{question}
"""

    try:

        response = ollama.chat(
            model="llama3.2:3b",
            messages=[
                {
                    "role": "system",
                    "content": mission_information
                },
                {
                    "role": "user",
                    "content": question
                }
            ]
        )

        return response["message"]["content"]

    except Exception as e:

        return f"""
❌ AI connection error.

Make sure Ollama is running and the model is installed.

Error:
{e}
"""


# -----------------------------
# QUICK QUESTION BUTTONS
# -----------------------------
st.subheader("🚀 Quick Questions")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("⛽ Fuel Status", use_container_width=True):

        question = "What is the current fuel status?"

        st.session_state.messages.append(
            {"role": "user", "content": question}
        )

        answer = ask_ai(question)

        st.session_state.messages.append(
            {"role": "assistant", "content": answer}
        )

        st.rerun()


with col2:
    if st.button("🔋 Battery Status", use_container_width=True):

        question = "What is the current battery status?"

        st.session_state.messages.append(
            {"role": "user", "content": question}
        )

        answer = ask_ai(question)

        st.session_state.messages.append(
            {"role": "assistant", "content": answer}
        )

        st.rerun()


with col3:
    if st.button("🫁 Oxygen Status", use_container_width=True):

        question = "What is the current oxygen status?"

        st.session_state.messages.append(
            {"role": "user", "content": question}
        )

        answer = ask_ai(question)

        st.session_state.messages.append(
            {"role": "assistant", "content": answer}
        )

        st.rerun()


col1, col2, col3 = st.columns(3)

with col1:
    if st.button("👨‍🚀 Human Status", use_container_width=True):

        question = "What is the current human status?"

        st.session_state.messages.append(
            {"role": "user", "content": question}
        )

        answer = ask_ai(question)

        st.session_state.messages.append(
            {"role": "assistant", "content": answer}
        )

        st.rerun()


with col2:
    if st.button("🚀 Mission Status", use_container_width=True):

        question = "What is the current mission status?"

        st.session_state.messages.append(
            {"role": "user", "content": question}
        )

        answer = ask_ai(question)

        st.session_state.messages.append(
            {"role": "assistant", "content": answer}
        )

        st.rerun()


with col3:
    if st.button("📊 Full Status", use_container_width=True):

        question = "Give me the complete current mission status."

        st.session_state.messages.append(
            {"role": "user", "content": question}
        )

        answer = ask_ai(question)

        st.session_state.messages.append(
            {"role": "assistant", "content": answer}
        )

        st.rerun()


# -----------------------------
# ASK ANYTHING
# -----------------------------
st.divider()

st.subheader("💬 Ask Anything")

question = st.chat_input(
    "Ask anything..."
)

if question:

    # Show user question
    st.session_state.messages.append(
        {"role": "user", "content": question}
    )

    # Generate AI answer
    answer = ask_ai(question)

    # Store answer
    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )

    st.rerun()