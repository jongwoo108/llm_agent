import os
import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

with st.sidebar:
    openai_api_key = os.getenv("OPENAI_API_KEY")

    st.markdown("[Get an OpenAI API key](https://platform.openai.com/account/api-keys)")
    st.markdown("[View the source code](https://github.com/streamlit/llm-examples/blob/main/Chatbot.py)")
    st.markdown(
        "[![Open in GintHub Codaspaces](https://github.com/codespaces/badge.svg)]"
        "(https://codespaces.new/streamlit/llm-examples?quickstart=1)"
    )

st.title("Chatbot")

# 세션 초기화
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# 기존 대화 렌더링
for msg in st.session_state["messages"]:
    st.chat_message(msg["role"]).write(msg["content"])

# 입력 받기
prompt = st.chat_input("Type your message...")
if prompt:
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue")
        st.stop()

    client = OpenAI(api_key=openai_api_key)

    # 유저 메시지 저장 
    st.session_state["messages"].append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    # GPT-5-mini 호출 (chat.completions)
    response = client.chat.completions.create(
        model="gpt-5-mini",
        messages=st.session_state["messages"],
    )

    msg = response.choices[0].message.content

    # 어시스턴트 메시지 저장
    st.session_state["messages"].append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)



