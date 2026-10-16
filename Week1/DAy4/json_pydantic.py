import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
my_api_key=os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("API key not found. Please set the GROQ_API_KEY environment variable.")

client=Groq(api_key=my_api_key)

model = "openai/gpt-oss-20b"
role="user"



# Structure it
from pydantic import BaseModel

class Ticket(BaseModel):
    name:str
    email:str
    issue:str

#Schema means a system/framework that defines the structure of data, 
schema=Ticket.model_json_schema()

response_format={
    "type": "json_object"
}

system_prompt=f"""
Extract the personal information from the ticket strictly based on this schema and give a json output.
{schema}
"""

message_system = {
    "role": "system",
    "content": system_prompt
}

text="Hello My name is Raj. Yesterday I got 24 years old, I have an iphone which is not working at all. My address is delhi. My email is abc@gmail.com. My contact number is 82134565543"

prompt=f"""
This is a customer ticket. Please extract the personal information from this.
{text}
"""
# message me role and content
message={
    "role": role,
    "content": prompt
}

messages=[message_system,message]

response = client.chat.completions.create(model=model, messages=messages, response_format=response_format)

answer=response.choices[0].message.content
print(answer)


# How to read this answer
import json
raw_json=answer
data_file=json.loads(raw_json)
ticket=Ticket(**data_file)


# This data can be passed further
print(ticket.name)
print(ticket.email)
print(ticket.issue)


#Homework

# take resume in pdf or word
# have hr give you a list of things like skill, experience, projects
# extract these from resume 
# match against the hr list
# generate a percentage of matching or not