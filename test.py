# python 기준

import os
from dotenv import load_dotenv

# .env 파일 로드

load_dotenv()

# 환경 변수 불러오기

openai_api_key = os.getenv("OPENAI_API_KEY")
huggingface_api_key = os.getenv("HUGGINGFACE_API_KEY")

print(openai_api_key)