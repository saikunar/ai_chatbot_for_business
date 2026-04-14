import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.title("AI Business Chatbot")

# Train section
st.header("Train Chatbot")
data = st.text_area("Enter business info")

if st.button("Train"):
    requests.post(f"{API_URL}/train", json={"data": data})
    st.success("Chatbot trained!")

# Chat section
st.header("Chat")
user_input = st.text_input("Ask something")

if st.button("Send"):
    res = requests.post(f"{API_URL}/chat", json={"message": user_input})
    st.write(res.json()["response"])