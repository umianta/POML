import os
from dotenv import load_dotenv
from poml.integration.langchain import LangchainPomlTemplate
from langchain_community.chat_models import ChatOpenAI

# Load .env
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("API key not found in .env")

# Load POML template
template = LangchainPomlTemplate.from_file("example.poml", speaker_mode=True)
chat_prompt = template.format()

# Initialize ChatOpenAI LLM
llm = ChatOpenAI(model_name="gpt-4", openai_api_key=api_key)

# Generate response using ChatMessage objects
response = llm.generate(chat_prompt.to_messages())

# Print AI output
print("LangChain Response:\n")
print(response.generations[0].message.content)
