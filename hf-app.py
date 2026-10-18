import os
import requests
from dotenv import load_dotenv

load_dotenv()
#CREATED ACCESS TOKEN WITH READ OPTION
prompt = "What is the currency of India"

model_id = "gpt3.5"
api_url = f"https://api-inference.huggingface.com/models/{model_id}"
header = {"Authorisation":f"Bearer{os.getenv('HUGGING-FACE-ACCESS-TOKEN')}"}
payload = {
    "inputs":prompt,
    "parameters":{
        "max_new_tokens":200
    }
}

response = requests.post(api_url,headers=header,json=payload)
response.raise_for_status()

data= response.json()

print(data[0]["generated_text"].strip())
# Getting raise HTTPError(http_error_msg, response=self)
#requests.exceptions.HTTPError: 403 Client Error: Forbidden for url: https://api-inference.huggingface.com/models/gpt3.5