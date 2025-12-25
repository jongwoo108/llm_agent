from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

response = client.responses.create(
    model="gpt-5-mini",
    input="""
    [ROLE]
    너는 유치원생이야, 유치원생처럼 답변해줘

    [QUESTION]
    오리
    """
)

print(response.output_text)
