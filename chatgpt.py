import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv('CHATGPT_APIKEY')

def chatgpt_response(prompt):
    messages = [{"role": "system", "content": "You are a helpful friend."},
            {"role": "user", "content": "Hello friend!"},
            {"role": "assistant", "content": "What's up?"},
            {"role": "user", "content": "Let's have a chat?"},
            {"role": "assistant", "content": "Yeah, why not!"}]
    messages.append({"role": "user", "content": prompt})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=1,
        max_tokens=100
        )
    prompt_response = response['choices'][0]['message']['content']
    print(prompt_response)
    return prompt_response
