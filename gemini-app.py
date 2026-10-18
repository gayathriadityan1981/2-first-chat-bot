import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-3.8-flash")

response = model.generate_content("Explain python list in short and simple")
print(response.text)
# couldnt execute this program as there is no free plan for gemini_api_key at the moment