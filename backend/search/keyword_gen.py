import os
from openai import OpenAI
import openai
from typing import List
from django.conf import settings

client = OpenAI(api_key=settings.OPENAI_API_KEY)
# OpenAI.api_key = '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'


def keyword_generation(keyword: str) -> List[str]:
  completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "user",
            "content": f"Generate 10 keywords related to {keyword}.",
        },
    ],
)
  keywords_message = completion.choices[0].message.content
    
    # Splitting the keywords_message string to extract the individual keywords
    # Adjust the split method based on the actual format of the generated message
  keywords = keywords_message.replace('\n', ',').split(',')
    
    # Stripping whitespace and removing empty strings from the list
  keywords = [kwd.strip() for kwd in keywords if kwd.strip()]
  keywords.append(keyword)


  print(keywords) # Debugging purpose, can be deleted when needed
  return keywords
