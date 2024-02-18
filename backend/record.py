import pyaudio
import wave
import openai
from dotenv import load_dotenv
import os
from openai import OpenAI
import jsonify
import json
import config
load_dotenv()
from data_modification import NewStory
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
client = OpenAI()


def record_audio():
  chunk = 1024  # Record in chunks of 1024 samples
  sample_format = pyaudio.paInt16  # 16 bits per sample
  channels = 1
  fs = 44100  # Record at 44100 samples per second
  seconds = 10
  filename = "output.wav"
  p = pyaudio.PyAudio()  # Create an interface to PortAudio
  stream = p.open(format=sample_format,
                  channels=channels,
                  rate=fs,
                  frames_per_buffer=chunk,
                  input=True)
  frames = []  # Initialize array to store frames
  # Store data in chunks for 3 seconds
  for i in range(0, int(fs / chunk * seconds)):
    data = stream.read(chunk)
    frames.append(data)
  # Stop and close the stream 
  stream.stop_stream()
  stream.close()
  # Terminate the PortAudio interface
  p.terminate()
  # Save the recorded data as a WAV file
  wf = wave.open(filename, 'wb')
  wf.setnchannels(channels)
  wf.setsampwidth(p.get_sample_size(sample_format))
  wf.setframerate(fs)
  wf.writeframes(b''.join(frames))
  wf.close()
  return 'wav file'

@app.route('/processWhisper')
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

def summarize(x):
  #uses the openAPI to summarize story from transcript
  story = []
  summary = []
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
  
  #this adds the real story
  story.append(x)
  #this adds the summary
  summary.append(jsonified_response["choices"][0]["message"]["content"])
  story.append(jsonified_response["choices"][0]["message"]["content"])
  #uses the openAPI to get tags from the summarized story
  response1 = client.chat.completions.create(
        model="gpt-4",    
        messages=[
        {
            "role": "user",
            "content": f"Assign this story 4 tags: decade, historical event/ cultural event name or title, personal story theme, location. Return a list seperated by commas, do not include the promts in this list (if there is no clear prompt answer, return 'N/A' in the list instead of the potential answer): {x}"
        }
        ],
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
  jsonified_response1=json.loads(response1.model_dump_json())
  #this adds the tags!!! 
  cat = jsonified_response1["choices"][0]["message"]["content"]
  eagle = cat.split(',')
  for y in eagle:
     story.append(y)
  NewStory(story)
  return jsonify(summary)


@app.route('/summarizer')
def executing():
  record_audio()
  return(processWhisper("output.wav"))