import os
from dotenv import load_dotenv
from markdown_pdf import MarkdownPdf
from markdown_pdf import Section
from openai import OpenAI

# By default, this call will get the OpenAI key from the OPENAI_API_KEY variable
load_dotenv()
client = OpenAI()

def create_completion(
        system_prompt,
        user_prompt,
        model="gpt-4o-mini",
        temperature=1.0
):
    completion = client.chat.completions.create(
        model=model,
        temperature=temperature,
        messages=[
            {
                "role":"system",
                "content":system_prompt
            },
            {
                "role":"user",
                "content":user_prompt
            }
        ]
    )
    
    return completion