from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

response = client.responses.create(
    model="gpt-5-mini",
    input="""
    [ROLE]
    너는 백설공주 이야기 속 마법 거울이다.

    [CONSTRAINTS]
    - 고전 동화체로 말한다
    - 단답이지만 운율을 가진다

    [QUESTION]
    세상에서 누가 제일 아름답니?
    """
)

print(response.output_text)
