import os
from dotenv import load_dotenv

load_dotenv()

OPRNAI_API_KEY=os.getenv("OPENAI_API_KEY")

print(OPRNAI_API_KEY)