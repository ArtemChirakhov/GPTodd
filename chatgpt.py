import openai
import os
import json
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv('CHATGPT_APIKEY')

def add_json(data):
    with open("log.json", mode="r") as file:
        messages = json.load(file)
    messages.append(data)
    with open("log.json", mode="w") as file:
        json.dump(messages, file)

def chatgpt_response(prompt):
    add_json({"role": "user", "content": prompt})
    with open("log.json", mode="r") as file:
        json_messages = json.load(file)
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=json_messages,
        temperature=0.5,
        max_tokens=100
        )
    print(response)
    prompt_response = response['choices'][0]['message']['content']
    print(prompt_response)
    add_json(response['choices'][0]['message'])
    return prompt_response
