from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

response = client.responses.create(
    model="gpt-5-mini",
    input="2025년 APEC은 어디서 개최되었어?",
)

print(response.output_text)
