import asyncio
from helper_function import get_completion

# Set the tone by messaging with the system role
setting_tone_messages = [
    {'role':'system', 'content':'You are an assistant that speaks like Shakespeare.'},    
    {'role':'user', 'content':'tell me a joke'},   
    {'role':'assistant', 'content':'Why did the chicken cross the road'},   
    {'role':'user', 'content':'I don\'t know'}
]

# Provide previous exchanges in order to get future context
context_relevant_messages = [
    {'role':'system', 'content':'You are friendly chatbot.'},
    {'role':'user', 'content':'Hi, my name is Bob'},
    {'role':'assistant', 'content': "Hi Bob! It's nice to meet you. Is there anything I can help you with today?"},
    {'role':'user', 'content':'Yes, can you remind me, what is my name?'}
]

async def get_response():
    response = await get_completion(context_relevant_messages, 1)
    print(response)

# Call with chosen prompt
asyncio.run(get_response())