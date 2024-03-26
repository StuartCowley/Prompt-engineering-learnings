import os
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
client = OpenAI(api_key=os.environ.get("OPEN_AI_KEY"))

# Messages are an array of objects in this format. Role can be user or system
# [
#   {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
#   {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
# ]
async def get_completion(messages, model="gpt-3.5-turbo"):
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0 # this is the degree of randomness of the model's output
    )
    return response.choices[0].message.content
