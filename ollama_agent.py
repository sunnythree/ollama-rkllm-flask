import os
os.environ['HF_ENDPOINT']='https://hf-mirror.com'
from llama_index.llms.ollama import Ollama
from dotenv import load_dotenv
load_dotenv()
from llama_index.core.agent import ReActAgent
from llama_index.core.tools import FunctionTool
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex, Settings
from llama_index.core.tools import QueryEngineTool
from llama_index.embeddings.huggingface import HuggingFaceEmbedding


# settings
Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-base-en-v1.5")
Settings.llm = Ollama(model="llama3.2", base_url="http://192.168.31.137:8080", request_timeout=60)

# function tools
def multiply(a: float, b: float) -> float:
    """Multiply two numbers and returns the product"""
    print("multiply called")
    return a * b

multiply_tool = FunctionTool.from_defaults(fn=multiply)

def add(a: float, b: float) -> float:
    """Add two numbers and returns the sum"""
    print("add called")
    return a + b

add_tool = FunctionTool.from_defaults(fn=add)

# rag pipeline
documents = SimpleDirectoryReader("./data").load_data()
index = VectorStoreIndex.from_documents(documents)
query_engine = index.as_query_engine()

# response = query_engine.query("What was the total amount of the 2023 Canadian federal budget?")
# print(response)

# rag pipeline as a tool
budget_tool = QueryEngineTool.from_defaults(
    query_engine,
    name="canadian_budget_2023",
    description="A RAG engine with some basic facts about the 2023 Canadian federal budget."
)

agent = ReActAgent.from_tools([multiply_tool, add_tool], verbose=True, max_iterations=30)

response = agent.chat("What is 20+(2*4)? you must use a tool to calculate every step.")

print(response)
