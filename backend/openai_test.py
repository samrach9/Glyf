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

    tags(x)

    # return story
    
    # attributesReal.append(jsonified_response["choices"][0]["message"]["content"])
    #print(jsonified_response["choices"][0]["message"]["content"])
    #print(story)
    
    

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
    # keys_list = list(jsonified_response1.keys())
    # values_list = list(jsonified_response1.values())
    #print("this is the keys list")
    #print(keys_list)
    #print("\n\nthis is the values list")
    #print(values_list)
    #print("\n\n")

    global attributes
    attributes.append(jsonified_response1["choices"][0]["message"]["content"])
    # print(attributes)
    #attributes.append(jsonified_response1["choices"][0]["message"])
    #attributes.append(jsonified_response1["content"])
    # return(attributes)
    #print(jsonified_response1["choices"][0]["message"]["content"])


    

#processAI("my name is arran, and i lived through the partition as i moved from pakistan to india")
print(story)
print("end global")
print(attributes)
