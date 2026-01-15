from dotenv import load_dotenv
import os

load_dotenv()
key = os.getenv("API_KEY")

if key is None:
    print("No Key")
else:
    print("Key Loaded")

