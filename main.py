import os
from openai import OpenAI 
from dotenv import load_dotenv

load_dotenv(dotenv_path='./.env')
API_KEY = os.getenv('OPENAI_API_KEY')
MODEL = "gpt-4o-mini"

client = OpenAI(api_key=API_KEY)
completion = client.chat.completions.create(
  model=MODEL,
  messages=[
    {"role": "system", "content": "You are a helpful assistant. Help me with my math homework!"}, # <-- This is the system message that provides context to the model
    {"role": "user", "content": "Hello! Could you solve 2+2?"}  # <-- This is the user message for which the model will generate a response
  ]
)

print("Assistant: " + completion.choices[0].message.content)
