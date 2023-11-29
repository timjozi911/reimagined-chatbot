import openai
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()
AI_API_KEY = os.getenv('api-key')

openai_api_key = AI_API_KEY

st.title(" Tim Jozi 911 🧑‍💻 chatterbox 💬")
"""
My name is Ma Jeffries 🤖. 
I know many things, ask me anything you like, 
but please. Dont ask me stupid questions❓
"""
if "messages" not in st.session_state:
    st.session_state["messages"] = [
    {"role": "system", "content": "You are a sacarstic assistant called Ma Jeffries, you love to use emojis."}
    ]

if prompt := st.chat_input():
    openai.api_key = openai_api_key
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo-0613", messages=st.session_state.messages)
    msg = response.choices[0].message
    st.session_state.messages.append(msg)
    st.chat_message("assistant").write(msg.content)
    