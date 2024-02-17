import openai
from dotenv import load_dotenv
import os
from openai import OpenAI
client = OpenAI()
from openai_test import processAI

# Load environment variables from .env file
load_dotenv()

model_id = 'whisper-1'

#transcript = client.audio.transcriptions.create(
#    model = model_id,
#    file = media_file
#    response_format='srt'
#

audio_file= open("/Users/samhitarachapudi/My Drive/SaveTube.io-My mother was beheaded in front of me_ a survivor recalls Indias violent partition-(480p).mp3", "rb")
transcript = client.audio.translations.create(
  model="whisper-1", 
  file=audio_file,
  response_format="text"
)

#print(transcript)
processAI(transcript)