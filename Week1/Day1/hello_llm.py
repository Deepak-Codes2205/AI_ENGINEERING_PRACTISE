import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

my_api_key=os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("API Key not found")

client = Groq(api_key=my_api_key)
model = "openai/gpt-oss-120b"
role = "user"
prompt = "Who is Padho with Pratyush and what does he teaches"

# Message require role and content to be passed in the message object. 
# The role can be user, assistant or system. 
# The content is the prompt that you want to send to the model.
message = {
    "role": role,
    "content": prompt    
}

messages = [message]
response = client.chat.completions.create(
    model=model,
    messages=messages
)
print(response)


print("########################################################################")
answer = response.choices[0].message.content
print("Answer is " + answer)