from builtins import print
import google.generativeai as genai
from dotenv import load_dotenv

import httpx
import os
import base64

# Load environment variables
load_dotenv()
genai.configure(api_key=os.environ["API_KEY"])
model = genai.GenerativeModel("gemini-1.5-flash")


image_path = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTGIvLLgZKrg_BXtaJxXSUOo1rcOg4mle9Onw&s"

image = httpx.get(image_path)

prompt = "transcribe and translate the image to english"
response = model.generate_content([{'mime_type':'image/jpeg', 'data': base64.b64encode(image.content).decode('utf-8')}, prompt])

print(response.text)


