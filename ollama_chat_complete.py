from llama_index.llms.ollama import Ollama

# init ollama
ollama = Ollama(model="rkllm_chat", base_url="http://192.168.31.137:8080", request_timeout=500)

# ask question
question = "who are you?"

# get answer
# For processing text content in a streaming manner
result = ollama.complete(question)
print(result)

