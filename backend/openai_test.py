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
# from data_modification import NewStory # Import Function to Add a New Story Onto Database

#print(os.environ.get("OPENAI_API_KEY"))
client = OpenAI()

# Output Lists 
story = []
attributes = []


def processAI(x):
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
    global story
    story.append(jsonified_response["choices"][0]["message"]["content"])
    
    # calling tags function to generate tags
    tags(x)
    # return tags(x)
    return story



    
    

def tags(x):
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

    global attributes
    attributes.append(jsonified_response1["choices"][0]["message"]["content"])

    # print(attributes)
    return attributes

#processAI("my name is arran, and i lived through the partition as i moved from pakistan to india")

