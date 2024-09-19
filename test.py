# python 기준

import os
import requests
import json
from dotenv import load_dotenv

# .env 파일 로드
load_dotenv()

# 환경 변수 불러오기
openai_api_key = os.getenv("OPENAI_API_KEY")

# api endpoint
url = "https://api.openai.com/v1/chat/completions"

# request headers
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {openai_api_key}"
}

# request body
data = {
    "model": "gpt-3.5-turbo",
    "messages": [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is the purpose of life?"}
    ]
}

# make request
response = requests.post(url=url, headers=headers, data=json.dumps(data))
if response.status_code == 200:
    answer = response.json()
    print("AI Response:", answer['choices'][0]['message']['content'].strip())
else:
    print(f"Error: {response.status_code}")
    print(response.text)