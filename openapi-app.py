import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
# Load API key
client = OpenAI(api_key= os.getenv("open_api_key"))
prompt = "What is the capital of Ireland?"

response = client.chat.completions.create(
    model = "gpt-4o-mini",
    messages = [{
        "role":"user",
        "content": prompt
    }],
    max_tokens=200
)
#try below to know the whole reponse sent by open ai
#print(response)
print(response.choices[0].message.content.strip())