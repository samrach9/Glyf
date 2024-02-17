from openai import OpenAI
client = OpenAI()

content = "what are the first 10 digits of pi?"

response = client.chat.completions.create(
  model="gpt-3.5-turbo-0125",
  response_format={ "type": "json_object" },
  messages=[
    {"role": "system", "content": "You are a helpful assistant designed to output JSON."},
    {"role": "user", "content": content}
  ]
)
print(response.choices[0].message.content)