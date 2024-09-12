# pip install python-dotenv
# pip show python-dotenv

from dotenv import load_dotenv
import os

load_dotenv()

OPENAI_KEY = os.getenv('OPENAI_KEY')
print(OPENAI_KEY)