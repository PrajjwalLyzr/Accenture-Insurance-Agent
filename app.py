import streamlit as st
import requests
import json
import os
from dotenv import load_dotenv
import time

# Load environment variables
load_dotenv()
CUSTOMER_AGENT_ID = os.getenv("CUSTOMER_AGENT_ID")
AGENT_AGENT_ID = os.getenv("AGENT_AGENT_ID")

API_KEY = os.getenv("API_KEY")  # Store API key in .env for security


def send_message(agent_id, user_id, session_id, message):
    url = "https://agent-prod.studio.lyzr.ai/v3/inference/chat/"
    headers = {
        "accept": "application/json",
        "x-api-key": API_KEY,
    }
    payload = json.dumps({
        "user_id": user_id,
        "agent_id": agent_id,
        "session_id": session_id,
        "message": message,
    })
    start_time = time.time()
    response = requests.post(url, headers=headers, data=payload)
    end_time = time.time()
    
    response_time = end_time - start_time
    if response.status_code == 200:
        return response.json().get("response", "No response received"), response_time
    else:
        return f"Error: {response.status_code} - {response.text}", None

# Streamlit App Layout
st.title("SBI Chat Interface")

# Tabs for different chat interfaces
tab1, tab2 = st.tabs(["Customer Support", "SBI Life Insurance Agent"])

# Customer Support Chat Interface
with tab1:
    st.subheader("Chat with Customer Support Bot")
    if "customer_chat" not in st.session_state:
        st.session_state.customer_chat = []
    
    for msg in st.session_state.customer_chat:
        with st.chat_message(msg["role"]):
            st.markdown(msg["text"])
    
    customer_input = st.chat_input("Enter your message for Customer Support")
    if customer_input:
        st.session_state.customer_chat.append({"role": "user", "text": customer_input})
        st.rerun()
        
    if len(st.session_state.customer_chat) > 0 and st.session_state.customer_chat[-1]["role"] == "user":
        with st.chat_message("assistant"):
            # with st.spinner("Thinking..."):
                customer_response, response_time = send_message(CUSTOMER_AGENT_ID, "prajjwal@lyzr.ai", "prajjwal@lyzr.ai", st.session_state.customer_chat[-1]["text"])
        st.session_state.customer_chat.append({"role": "assistant", "text": customer_response})
        st.rerun()

# SBI Life Insurance Agent Chat Interface
with tab2:
    st.subheader("Chat with SBI Life Insurance Agent Bot")
    if "agent_chat" not in st.session_state:
        st.session_state.agent_chat = []
    
    for msg in st.session_state.agent_chat:
        with st.chat_message(msg["role"]):
            st.markdown(msg["text"])
    
    agent_input = st.chat_input("Enter your message for SBI Life Insurance Agent")
    if agent_input:
        st.session_state.agent_chat.append({"role": "user", "text": agent_input})
        st.rerun()
        
    if len(st.session_state.agent_chat) > 0 and st.session_state.agent_chat[-1]["role"] == "user":
        with st.chat_message("assistant"):
            # with st.spinner("Thinking..."):
                agent_response, response_time = send_message(AGENT_AGENT_ID, "prajjwal@lyzr.ai", "prajjwal@lyzr.ai", st.session_state.agent_chat[-1]["text"])
        st.session_state.agent_chat.append({"role": "assistant", "text": agent_response})
        st.rerun()
