import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
try:
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("NO API KEY IN ENV!")
        sys.exit(1)
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-1.5-flash")
    resp = model.generate_content("hello")
    print(resp.text.encode("utf-8"))
except Exception as e:
    print("API ERROR:", repr(e))
