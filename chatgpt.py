import openai
import os
import json


openai.api_key = input('Enter ChatGPT API Key')

def add_json(data):
    with open("log.json", mode="r") as file:
        messeges = json.load(file)
    messeges.append(data)
    with open("log.json", mode="w") as file:
        json.dump(messeges, file)

def chatgpt_response(prompt):
    add_json({"role": "user", "content": prompt})
    with open("log.json", mode="r") as file:
        json_messeges = json.load(file)
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=json_messeges,
        temperature=0.5,
        max_tokens=100
        )
    print(response)
    prompt_response = response['choices'][0]['message']['content']
    print(prompt_response)
    add_json(response['choices'][0]['message'])
    return prompt_response
