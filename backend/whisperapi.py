import openai
from dotenv import load_dotenv
import os
from openai import OpenAI
<<<<<<< HEAD
from openai_test import processAI
from openai_test import tags
=======
import jsonify
import os
import json
from openai import OpenAI
import os
import config
from dotenv import load_dotenv
load_dotenv()
>>>>>>> 8e15a4c27ef4ea6fc751de35271f4b6bac9676e8

# Load environment variables from .env file
load_dotenv()
ret = []

client = OpenAI()
story = []

def processWhisper(x):
  model_id = 'whisper-1'
  audio_file= open(x, "rb")
  transcript = client.audio.translations.create(
    model="whisper-1", 
    file=audio_file,
    response_format="text"
  )
  #print(summarize(transcript))
  return(summarize(transcript))

<<<<<<< HEAD
#print(transcript)
  ret = processAI(transcript)

processWhisper("output.wav")

=======

def summarize(x):
  #uses the openAPI to summarize story from transcript
  response = client.chat.completions.create(
    model="gpt-4",      
    messages=[
    {
        "role": "user",
        "content": f"Please summarize this story: {x}"
    }
    ],
    temperature=1,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
  )
  jsonified_response=json.loads(response.model_dump_json())
  story.append(x)
  story.append(jsonified_response["choices"][0]["message"]["content"])
  #uses the openAPI to get tags from the summarized story
  response1 = client.chat.completions.create(
        model="gpt-4",    
        messages=[
        {
            "role": "user",
            "content": f"please tag this story with these four tags: location, historical event/ cultural event, decade of historical even, and personal story theme, seperated by commas: {x}"
        }
        ],
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
  jsonified_response1=json.loads(response1.model_dump_json())
  story.append(jsonified_response1["choices"][0]["message"]["content"])
  return(story)


print(processWhisper("output.wav"))
>>>>>>> 8e15a4c27ef4ea6fc751de35271f4b6bac9676e8
