# This code is for v1 of the openai package: pypi.org/project/openai
#import backend.openai as openai
import jsonify
import os
import json
from openai import OpenAI
import os
import config
from dotenv import load_dotenv
load_dotenv()

#print(os.environ.get("OPENAI_API_KEY"))
client = OpenAI()

def processAI():
    response = client.chat.completions.create(
        model="gpt-4",
        
        
        messages=[
        {
            "role": "user",
            "content": f"Please summarize this story: i am a young boy named arran and im from india punjab"
        }
        ],
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    jsonified_response=json.loads(response.model_dump_json())
    print(jsonified_response["choices"][0]["message"]["content"])
    return(jsonified_response["choices"][0]["message"]["content"])

