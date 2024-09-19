import os
from dotenv import load_dotenv
import requests
import json

load_dotenv()

OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")

print(OPENAI_API_KEY)


#api endpoint 
#отправляет на сайт который все остальные будут отправлят сайт
url = "https://api.openai.com/v1/chat/completions"

# request headers
# 
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {OPENAI_API_KEY}" #???? а  жто что означант не понятно 
}

#request body
# здесь задают роль и вопросф для каждого ассистента?
data = {
    "model":"gpt-3.5-turbo",
    "messages": [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "한국어로 시를 써줘"}
    ]
}

#main request
response = requests.post(url=url, headers=headers, data=json.dumps(data))

print(response)

if response.status_code == 200:
    answer = response.json()
    print("AI Response:", answer ['choices'] [0]['message'] ['content'].strip())
else:
    print(f"Error: {response.status_code}")