import os
import requests
import json

from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY3")

url = "https://api.openai.com/v1/chat/completions"

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {OPENAI_API_KEY}"
}

data = {
    "model": "gpt-3.5-turbo",
    "messages": [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is the purpose of life?"}
    ]
}

response = requests.post(url=url, headers=headers, data=json.dumps(data))
if response.status_code == 200:
    answer = response.json()
    print("AI Response:", answer['choices'][0]['message']['content'].strip())
else:
    print(f"Error: {response.status_code}")
    print(response.text)