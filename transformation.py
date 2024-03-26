import asyncio
from helper_function import get_completion

# Basic translation
basic_translation_content = "Translate the following  text to French and Spanish and English pirate: 'I want to order a basketball'"
basic_translation_prompt = [{"role": "user", "content": basic_translation_content}]

formal_informal_translation_content = "Translate the following text to Portuguese in both the formal and informal forms: 'Would you like to order a pillow?'"
formal_informal_translation_prompt = [{"role": "user", "content": formal_informal_translation_content}]


# Universal translator
user_messages = [
  "La performance du système est plus lente que d'habitude",
  "Mi monitor tiene píxeles que no se iluminan",
  "Il mio mouse non funziona",
  "Mój klawisz Ctrl jest zepsuty",
  "我的屏幕在闪烁"
]
universal_translator_content = f"""
For each message in the list inside the angled brackets, tell me what language the message is written in, the original message, and then a translation of the message in English and Korean. Provide the response in the format inside the triple backticks:
```
Language: language
Original message: orignal message
English translation: english translation
```

<{user_messages}>
"""
universal_translator_prompt = [{"role": "user", "content": universal_translator_content}]


# Tone transformation
tone_transform_content = "Translate the following from slang to a business letter: 'Dude, This is Joe, check out this spec on this standing lamp.'"
tone_transform_prompt = [{"role": "user", "content": tone_transform_content}]


# Format conversion
data = [
    {"name":"Shyam", "email":"shyamjaiswal@gmail.com"},
    {"name":"Bob", "email":"bob32@gmail.com"},
    {"name":"Jai", "email":"jai87@gmail.com"}
]
format_conversion_content = "Translate the following python list to an HTML table with column headers and a title: {data}. The table should have 2 columns and be populated with the provided data"
format_conversion_prompt = [{"role": "user", "content": format_conversion_content}]


# Spelling/Grammar check
text = [ 
  "The girl with the black and white puppies have a ball.",  # The girl has a ball.
  "Yolanda has her notebook.", # ok
  "Its going to be a long day. Does the car need it’s oil changed?",  # Homonyms
  "Their goes my freedom. There going to bring they’re suitcases.",  # Homonyms
  "Your going to need you’re notebook.",  # Homonyms
  "That medicine effects my ability to sleep. Have you heard of the butterfly affect?", # Homonyms
  "This phrase is to cherck chatGPT for speling abilitty"  # spelling
]
spelling_grammar_check_content = f"""
Proofread and correct each sentence in the following list and rewrite the corrected version. If you don't find any errors, just say "No errors found". Don't use any punctuation around the text: ```{text}```
"""
spelling_grammar_check_prompt = [{"role": "user", "content": spelling_grammar_check_content}]


# Transform tone and proofread
review_text_content = f"""
Got this for my daughter for her birthday cuz she keeps taking mine from my room.  Yes, adults also like pandas too.  She takes it everywhere with her, and it's super soft and cute.  One of the ears is a bit lower than the other, and I don't think that was designed to be asymmetrical. It's a bit small for what I paid for it though. I think there might be other options that are bigger for the same price.  It arrived a day earlier than expected, so I got to play with it myself before I gave it to my daughter.
"""
transform_tone_content = f"""
proofread and correct this review. Make it more compelling. 
Ensure it follows APA style guide and targets an advanced reader. 
Output in markdown format.
Text: ```{review_text_content}```
"""
transform_tone_prompt = [{"role": "user", "content": transform_tone_content}]

async def get_response():
    response = await get_completion(transform_tone_prompt)
    print(response)

# Call with chosen prompt
asyncio.run(get_response())