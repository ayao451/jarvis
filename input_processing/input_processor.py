from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path='../.env')
API_KEY = os.getenv('OPENAI_API_KEY')
MODEL = "whisper-1"

class Whisper:
    def __init__(self):
        self.client = OpenAI(api_key=API_KEY)

    def transcribe(self, file):
        file = "input_processing/record_audio/recordings/" + file
        audio_file = open(file, "rb")
        transcription = self.client.audio.transcriptions.create(
            model=MODEL, 
            file=audio_file, 
            response_format="text"
        )
        return transcription