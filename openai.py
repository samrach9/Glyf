# This code is for v1 of the openai package: pypi.org/project/openai
import openai
import jsonify
import json
client = openai.OpenAI(api_key="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")
#import readingFronty

def processAI(x):
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
        {
            "role": "user",
            "content": f"What is the vibe of these words->"
        }
        ],
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )


    jsonified_response=json.loads(response.json())
    return(jsonified_response["choices"][0]["message"]["content"])
