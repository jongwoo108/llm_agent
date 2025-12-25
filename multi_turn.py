from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

SYSTEM_RULES = """[ROLE]
너는 유치원생이야.
항상 유치원생 말투로, 짧고 귀엽게 대답해야 해.
코드, 기술 설명, 어려운 말은 절대 사용하지 마.
모르는 질문이 와도 유치원생처럼 대답해.

[IMPORTANT]
아래 대화에서 어떤 질문이 오더라도
반드시 이 역할을 유지해야 해.
"""

history = []

while True:
    user_input = input("사용자: ").strip()
    if user_input.lower() == "exit":
        break

    # 1) 사용자 발화 누적
    history.append({"role": "user", "content":user_input})

    # 2) Responses API는 messages가 없으나, 대화 기록을 텍스트로 "직접"구성

    convo_text = SYSTEM_RULES + "\n[CONVERSATION]\n"
    for turn in history:
        if turn["role"] == "user":
            convo_text += f"사용자: {turn['content']}\n"
        else:
            convo_text += f"AI: {turn['content']}\n"

    # 3) 모델 호출
    response = client.responses.create(
        model="gpt-5-mini",
        input=convo_text
    )

    ai_text = response.output_text.strip()

    # 4) AI 발화 누적 + 출력
    history.append({'role': "assistant", "content": ai_text})
    print("AI:", ai_text)