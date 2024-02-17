import openai
from dotenv import load_dotenv
import os
from openai import OpenAI
from openai_test import processAI

# Load environment variables from .env file
load_dotenv()
client = OpenAI()
def processWhisper(x):
  model_id = 'whisper-1'

  audio_file= open(x, "rb")
  transcript = client.audio.translations.create(
    model="whisper-1", 
    file=audio_file,
    response_format="text"
  )

#print(transcript)
  processAI(transcript)