import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

prompt = "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."
chat = client.models.generate_content(
    model='gemini-2.0-flash-001',
    contents=prompt)

print(chat.text)
print(f"Prompt tokens: {chat.usage_metadata.prompt_token_count}")
print(f"Response tokens: {chat.usage_metadata.candidates_token_count}")
