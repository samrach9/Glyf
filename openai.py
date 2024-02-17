# This code is for v1 of the openai package: pypi.org/project/openai
import openai
import jsonify
import json
client = openai.OpenAI(api_key="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")
import readingFronty

def processAI(x):
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
        {
            "role": "user",
            "content": f"give me JUST a number: AVERAGE time spent in {x} without any extra words. don't say \"the average time spent in a {x} is\" and don't say “minute”. the unit will be minutes, but only give the number back"
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
