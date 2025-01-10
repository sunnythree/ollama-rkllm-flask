from llama_index.llms.ollama import Ollama

# 初始化Ollama实例
ollama = Ollama(model="rkllm_chat", base_url="http://192.168.31.137:8080", request_timeout=500)

# 定义问题
question = "who are you？"

# 发送问题并获取回答
# For processing text content in a streaming manner
for completion_response in ollama.stream_complete(question):
    print(completion_response.delta, end='')  # Prints processed text as it's received
print("\n")
