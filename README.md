# ollama-rkllm-flask
Implement the Ollama protocol using rkllm and Flask, supporting the Ollama Chat API and Llama Index Agent.

# chat with complete api
ollama_chat_complete.py

# chat with stream api
ollama_chat_stream.py

# agent
ollama_agent.py

# start server
python ollama_flask_server.py --rkllm_model_path internal.rknn --target_platform rk3588
then following should print:
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:8080
 * Running on http://192.168.31.137:8080
so you can access server by ollama api

