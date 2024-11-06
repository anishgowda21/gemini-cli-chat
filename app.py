import google.generativeai as genai
import sys
import os
from dotenv import load_dotenv
import PIL.Image as image

load_dotenv()

API_KEY = os.getenv("API_KEY",None)

if API_KEY is None:
    print("Gemini API KEY NOT FOUND....")
    sys.exit(1)

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash")
img = image.open("img.png")
response = model.generate_content("Tell me about space",stream=True)
for chunk in response:
    print(chunk.text)
    print("_" * 80)
