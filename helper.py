'''helper function'''
import os
from dotenv import load_dotenv
from openai import OpenAI
from prompt import Prompt
load_dotenv()

class BlogGPTHelper(Prompt):
    '''Helper class for BlogGPT'''
    def generate(self, topic, helper_content):
        '''Class for generating blog content'''
        client = OpenAI()
        prompt = Prompt.get_prompt(topic, helper_content)
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content":prompt}],
        )
        return response.choices[0].message.content.strip()
        