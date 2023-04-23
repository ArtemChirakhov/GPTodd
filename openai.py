
import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv('CHATGPT_APIKEY')

def chatgpt_response(prompt):
    response = openai.Completion.create(
        model="gpt-3.5-turbo",
        prompt=prompt,
        temperature=1,
        max_tokens=100,
        messages=[
            {"role": "system", "content": "You are a helpful friend."},
            {"role": "user", "content": "Can you help me solve my math problem?"},
            {"role": "assistant", "content": "Ofcourse bro, what do you need"},
            {"role": "user", "content": "Can you solve this? x^2 - 5x + 6 = 0"},
            {"role": "assistant", "content": "Thats easy my guy. The answer is x = 3 and x = 2!"}
        ])
    prompt_response = response['choices'][0]['message']['content']
    return prompt_response



