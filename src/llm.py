import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from config import LLM_MODEL, TEMPERATURE

load_dotenv()

def get_llm():
    return ChatOpenAI(
        model=LLM_MODEL,
        api_key=os.getenv("OPENROUTER_API_KEY"),
        base_url="https://openrouter.ai/api/v1",
        temperature=TEMPERATURE
        
    )

