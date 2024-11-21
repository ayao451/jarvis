import os
from openai import OpenAI 
from dotenv import load_dotenv
from pop_up.pop_up_generator import PopUpGenerator
from input_processing.input_processor import Whisper
from input_processing.record_audio.new_audio_recording import Recording

load_dotenv(dotenv_path='./.env')
API_KEY = os.getenv('OPENAI_API_KEY')
MODEL = "gpt-4o-mini"

client = OpenAI(api_key=API_KEY)
file = "output.wav"
Recording(file).start()
prompt = Whisper().transcribe(file)
pop_up_generator = PopUpGenerator()

completion = client.chat.completions.create(
  model=MODEL,
  messages=[
    {"role": "system", "content": "Answer all questions in as few characters as possible."},
    {"role": "user", "content": prompt}
  ]
)

pop_up_generator.generate_regular_box(prompt, completion.choices[0].message.content)