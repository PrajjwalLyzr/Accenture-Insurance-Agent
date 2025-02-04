# import streamlit as st
# import requests
# import json
# import os
# from dotenv import load_dotenv
# import time

# # Load environment variables
# load_dotenv()
# CUSTOMER_AGENT_ID = os.getenv("CUSTOMER_AGENT_ID")
# AGENT_AGENT_ID = os.getenv("AGENT_AGENT_ID")

# API_KEY = os.getenv("API_KEY")  # Store API key in .env for security


# def send_message(agent_id, user_id, session_id, message):
#     url = "https://agent-prod.studio.lyzr.ai/v3/inference/chat/"
#     headers = {
#         "accept": "application/json",
#         "x-api-key": API_KEY,
#     }
#     payload = json.dumps({
#         "user_id": user_id,
#         "agent_id": agent_id,
#         "session_id": session_id,
#         "message": message,
#     })
#     start_time = time.time()
#     response = requests.post(url, headers=headers, data=payload)
#     end_time = time.time()
    
#     response_time = end_time - start_time
#     if response.status_code == 200:
#         return response.json().get("response", "No response received"), response_time
#     else:
#         return f"Error: {response.status_code} - {response.text}", None

# # Streamlit App Layout
# st.title("SBI Support Agent")

# def clear_chat():
#     st.session_state.customer_chat = [
#         {"role": "assistant", "text": "Hello! How can I assist you with your SBI Life Insurance today? If you have any questions about your policy or need general insurance information, feel free to ask."}
#     ]
#     st.session_state.agent_chat = [
#         {"role": "assistant", "text": "Hello! How can I assist you today? Whether you have questions about commissions, policy recommendations, or sales strategies, I'm here to help. If your query is related to personal details like commission earned or sales progress, please include your Agent ID and Name for verification. Otherwise, feel free to ask any general questions about our products or services."}
#     ]

# st.sidebar.button("🗑️ Clear Chat", on_click=clear_chat)

# # Tabs for different chat interfaces
# tab1, tab2 = st.tabs(["Customer Support", "SBI Insurance Agent"])

# # Customer Support Chat Interface
# with tab1:
#     st.subheader("Chat with Customer Support Bot")
#     if "customer_chat" not in st.session_state:
#         st.session_state.customer_chat = [
#             {"role": "assistant", "text": "Hello! How can I assist you with your SBI Life Insurance today? If you have any questions about your policy or need general insurance information, feel free to ask."}
#         ]
    
#     for msg in st.session_state.customer_chat:
#         with st.chat_message(msg["role"]):
#             st.markdown(msg["text"])
    
#     customer_input = st.chat_input("Enter your message for Customer Support")
#     if customer_input:
#         st.session_state.customer_chat.append({"role": "user", "text": customer_input})
#         st.rerun()
        
#     if len(st.session_state.customer_chat) > 0 and st.session_state.customer_chat[-1]["role"] == "user":
#         # with st.spinner("Thinking..."):
#         with st.chat_message("assistant"):
#             customer_response, response_time = send_message(CUSTOMER_AGENT_ID, "prajjwal@lyzr.ai", "sessionfour", st.session_state.customer_chat[-1]["text"])
#             st.session_state.customer_chat.append({"role": "assistant", "text": customer_response})
#         st.rerun()

# # SBI Life Insurance Agent Chat Interface
# with tab2:
#     st.subheader("Chat with SBI Insurance AI Agent")
#     if "agent_chat" not in st.session_state:
#         st.session_state.agent_chat = [
#             {"role": "assistant", "text": "Hello! How can I assist you today? Whether you have questions about commissions, policy recommendations, or sales strategies, I'm here to help. If your query is related to personal details like commission earned or sales progress, please include your Agent ID and Name for verification. Otherwise, feel free to ask any general questions about our products or services."}
#         ]
    
#     for msg in st.session_state.agent_chat:
#         with st.chat_message(msg["role"]):
#             st.markdown(msg["text"])
    
#     agent_input = st.chat_input("Enter your message for SBI Insurance AI Agent")
#     if agent_input:
#         st.session_state.agent_chat.append({"role": "user", "text": agent_input})
#         st.rerun()
        
#     if len(st.session_state.agent_chat) > 0 and st.session_state.agent_chat[-1]["role"] == "user":
#         # with st.spinner("Thinking..."):
#         with st.chat_message("assistant"):
#             agent_response, response_time = send_message(AGENT_AGENT_ID, "prajjwal@lyzr.ai", "sessionfour", st.session_state.agent_chat[-1]["text"])
#             st.session_state.agent_chat.append({"role": "assistant", "text": agent_response})
#         st.rerun()


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
st.title("SBI Support Agent")

def clear_chat():
    st.session_state.customer_chat = [
        {"role": "assistant", "text": "Hello! How can I assist you with your SBI Life Insurance today? If you have any questions about your policy or need general insurance information, feel free to ask."}
    ]
    st.session_state.agent_chat = [
        {"role": "assistant", "text": "Hello! How can I assist you today? Whether you have questions about commissions, policy recommendations, or sales strategies, I'm here to help. If your query is related to personal details like commission earned or sales progress, please include your Agent ID and Name for verification. Otherwise, feel free to ask any general questions about our products or services."}
    ]
    st.session_state.pop("customer_first_message", None)  # Clear stored first message
    st.session_state.pop("agent_first_message", None)  # Clear stored first message

st.sidebar.button("🗑️ Clear Chat", on_click=clear_chat)

# Tabs for different chat interfaces
tab1, tab2 = st.tabs(["Customer Support", "SBI Insurance Agent"])

# Customer Support Chat Interface
with tab1:
    st.subheader("Chat with Customer Support Bot")
    
    if "customer_chat" not in st.session_state:
        st.session_state.customer_chat = [
            {"role": "assistant", "text": "Hello! How can I assist you with your SBI Life Insurance today? If you have any questions about your policy or need general insurance information, feel free to ask."}
        ]
    
    for msg in st.session_state.customer_chat:
        with st.chat_message(msg["role"]):
            st.markdown(msg["text"])
    
    customer_input = st.chat_input("Enter your message for Customer Support")

    # If no first message is stored, define it
    if "customer_first_message" not in st.session_state:
        st.session_state.customer_first_message = None

    if customer_input:
        # Store the first message if not already stored
        if st.session_state.customer_first_message is None:
            st.session_state.customer_first_message = customer_input

        # Append the stored first message to all user queries
        full_message = f"{st.session_state.customer_first_message},{customer_input}"

        print(full_message)
        
        st.session_state.customer_chat.append({"role": "user", "text": customer_input})
        st.rerun()

    # Ensure `full_message` is always defined
    if st.session_state.customer_first_message:
        last_query = st.session_state.customer_chat[-1]["text"]
        full_message = f"{st.session_state.customer_first_message}\n{last_query}"
    else:
        full_message = st.session_state.customer_chat[-1]["text"]

    if len(st.session_state.customer_chat) > 0 and st.session_state.customer_chat[-1]["role"] == "user":
        with st.chat_message("assistant"):
            customer_response, response_time = send_message(
                CUSTOMER_AGENT_ID, "prajjwal@lyzr.ai", "sessionfour", full_message
            )
            st.session_state.customer_chat.append({"role": "assistant", "text": customer_response})
        st.rerun()

# SBI Life Insurance Agent Chat Interface
with tab2:
    st.subheader("Chat with SBI Insurance AI Agent")
    
    if "agent_chat" not in st.session_state:
        st.session_state.agent_chat = [
            {"role": "assistant", "text": "Hello! How can I assist you today? Whether you have questions about commissions, policy recommendations, or sales strategies, I'm here to help. If your query is related to personal details like commission earned or sales progress, please include your Agent ID and Name for verification. Otherwise, feel free to ask any general questions about our products or services."}
        ]
    
    for msg in st.session_state.agent_chat:
        with st.chat_message(msg["role"]):
            st.markdown(msg["text"])
    
    agent_input = st.chat_input("Enter your message for SBI Insurance AI Agent")

    # If no first message is stored, define it
    if "agent_first_message" not in st.session_state:
        st.session_state.agent_first_message = None

    if agent_input:
        # Store the first message if not already stored
        if st.session_state.agent_first_message is None:
            st.session_state.agent_first_message = agent_input

        # Append the stored first message to all user queries
        full_message = f"{st.session_state.agent_first_message}, {agent_input}"

        print(full_message)
        
        st.session_state.agent_chat.append({"role": "user", "text": agent_input})
        st.rerun()

    # Ensure `full_message` is always defined
    if st.session_state.agent_first_message:
        last_query = st.session_state.agent_chat[-1]["text"]
        full_message = f"{st.session_state.agent_first_message}\n{last_query}"
    else:
        full_message = st.session_state.agent_chat[-1]["text"]

    if len(st.session_state.agent_chat) > 0 and st.session_state.agent_chat[-1]["role"] == "user":
        with st.chat_message("assistant"):
            agent_response, response_time = send_message(
                AGENT_AGENT_ID, "prajjwal@lyzr.ai", "sessionfour", full_message
            )
            st.session_state.agent_chat.append({"role": "assistant", "text": agent_response})
        st.rerun()
