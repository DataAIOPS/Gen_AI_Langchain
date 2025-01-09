from dotenv import load_dotenv
import os
load_dotenv()

LANGCHAIN_API_KEY = os.getenv('LANGCHAIN_API_KEY')  # or os.environ['API_KEY']
LANGCHAIN_PROJECT = os.getenv('LANGCHAIN_PROJECT')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

from langchain_openai import ChatOpenAI

llm = ChatOpenAI()

print(llm.invoke("Hello, world!"))
