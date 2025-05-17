import os
os.environ["GOOGLE_API_KEY"]=st.secrets["GOOGLE_API_KEYS"]
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

# Initialize the LLM (make sure GOOGLE_API_KEY is set in your environment)
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

# Initialize session state for chat history
if "chat_history" not in st.session_state: 
    st.session_state.chat_history = [SystemMessage(content="You are a helpful assistant.")]

# App UI
st.title("💬 Gemini Chatbot")
st.markdown("Type something to start chatting with Gemini-2.0-Flash!")

# Text input
user_input = st.chat_input("Say something...")

if user_input:
    # Display user message
    st.chat_message("user").markdown(user_input)

    # Add user message to chat history
    st.session_state.chat_history.append(HumanMessage(content=user_input))

    # Invoke the LLM
    response = llm.invoke(st.session_state.chat_history)

    # Display AI response
    st.chat_message("assistant").markdown(response.content)

    # Add AI response to chat history
    st.session_state.chat_history.append(AIMessage(content=response.content))
