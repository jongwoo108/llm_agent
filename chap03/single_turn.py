from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

while True:
    user_input = input("사용자: ").strip()

    if user_input.lower() == "exit":
        break

    response = client.responses.create(
        model="gpt-5-mini",
        input=f"""
[ROLE]
너는 유치원생이야. 유치원생처럼 짧고 귀엽게 대답해줘.

[QUESTION]
{user_input}
"""
    )

    print("AI:", response.output_text)
