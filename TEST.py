import os
from dotenv import load_dotenv
load_dotenv()  
api = os.getenv("GEMINI_API_KEY")

print(api)