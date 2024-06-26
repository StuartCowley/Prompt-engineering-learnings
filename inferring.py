import asyncio
import json
from helper_function import get_completion

# Inferring sentiment from text
lamp_review = "Needed a nice lamp for my bedroom, and this one had additional storage and not too high of a price point. Got it fast.  The string to our lamp broke during the transit and the company happily sent over a new one. Came within a few days as well. It was easy to put together.  I had a missing part, so I contacted their support and they very quickly got me the missing piece! Lumina seems to me to be a great company that cares about their customers and products!!"

pos_neg_content = f"""
What is the sentiment of the following product review, which is delimited with triple backticks?

Give your answer as a single word, either "positive" or "negative".

Review text: '''{lamp_review}'''
"""
pos_neg_prompt = [{"role": "user", "content": pos_neg_content}]

identify_emotions_content = f"""
Identify a list of emotions that the writer of the following review is expressing. Include no more than five items in the list. Format your answer as a list of lower-case words separated by commas.

Review text: '''{lamp_review}'''
"""
identify_emotions_prompt = [{"role": "user", "content": identify_emotions_content}]

identify_anger_content = f"""
Is the writer of the following review expressing anger? The review is delimited with triple backticks. Give your answer as either yes or no.

Review text: '''{lamp_review}'''
"""
identify_anger_prompt = [{"role": "user", "content": identify_emotions_content}]

extract_data_content = f"""
Identify the following items from the review text: 
- Item purchased by reviewer
- Company that made the item

The review is delimited with triple backticks. Format your response as a JSON object with "Item" and "Brand" as the keys. 
If the information isn't present, use "unknown" as the value.
Make your response as short as possible.
  
Review text: '''{lamp_review}'''
"""
extract_data_prompt = [{"role": "user", "content": extract_data_content}]

extract_multiple_sentiment_content = f"""
Identify the following items from the review text: 
- Sentiment (positive or negative)
- Is the reviewer expressing anger? (true or false)
- Item purchased by reviewer
- Company that made the item

The review is delimited with triple backticks. Format your response as a JSON object with "Sentiment", "Anger", "Item" and "Brand" as the keys.
If the information isn't present, use "unknown" as the value.
Make your response as short as possible.
Format the Anger value as a boolean.

Review text: '''{lamp_review}'''
"""
extract_multiple_sentiment_prompt = [{"role": "user", "content": extract_multiple_sentiment_content}]


#Inferring topics
story = """
In a recent survey conducted by the government, public sector employees were asked to rate their level of satisfaction with the department they work at. The results revealed that NASA was the most popular department with a satisfaction rating of 95%.

One NASA employee, John Smith, commented on the findings, stating, "I'm not surprised that NASA came out on top. It's a great place to work with amazing people and incredible opportunities. I'm proud to be a part of such an innovative organization."

The results were also welcomed by NASA's management team, with Director Tom Johnson stating, "We are thrilled to hear that our employees are satisfied with their work at NASA. We have a talented and dedicated team who work tirelessly to achieve our goals, and it's fantastic to see that their hard work is paying off."

The survey also revealed that the Social Security Administration had the lowest satisfaction rating, with only 45% of employees indicating they were satisfied with their job. The government has pledged to address the concerns raised by employees in the survey and work towards improving job satisfaction across all departments.
"""

find_topics_content = f"""
Determine five topics that are being discussed in the following text, which is delimited by triple backticks.

Make each item one or two words long. 

Format your response as an array of items separated by commas.

Text sample: '''{story}'''
"""
find_topics_prompt = [{"role": "user", "content": find_topics_content}]

create_alert_featuring_topic_content = f"""
Determine whether each item in the following list of topics is a topic in the text below, which is delimited with triple backticks.

Give your answer in JSON format with the topic as the key and the value 0 or 1 for each property.
List of topics: {", ".join(["nasa", "local government", "engineering", "employee satisfaction", "federal government"])}

Text sample: '''{story}'''
"""
create_alert_featuring_topic_prompt = [{"role": "user", "content": create_alert_featuring_topic_content}]

# Call with chosen prompt
async def get_response_and_iterate():
    response = await get_completion(create_alert_featuring_topic_prompt)
    for key, value in json.loads(response).items():
        if value == 1:
            print("Alert! New story about", key)

async def get_response():
    response = await get_completion(find_topics_prompt)
    print(response)

asyncio.run(get_response())
