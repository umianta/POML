from poml import poml
import openai
import os 
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
# Process the POML file into structured messages
messages = poml("example.poml" ,context=None, stylesheet=None, chat=True, output_file=None, format='openai_chat', extra_args=None)

response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=messages
)

print("OpenAI resoponse :", response["choices"][0]["message"]["content"])
