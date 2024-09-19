import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY1")
#print(OPENAI_API_KEY)

# API endpoint
url = "https://api.openai.com/v1/chat/completions"

# Request headers
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {OPENAI_API_KEY}"  # 철자 수정
}

# Request body
data = {
    "model": "gpt-3.5-turbo",
    "messages": [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "How to be a billionaire?"}
    ]
}

# Make request
response = requests.post(url=url, headers=headers, data=json.dumps(data))

if response.status_code == 200:
    answer = response.json()
    print("AI Response:", answer['choices'][0]['message']['content'].strip())
else:
    print("Error: {response.status_code}")
    print(response.text)