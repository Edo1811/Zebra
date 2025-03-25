import ollama

response = ollama.chat(model='mistral', messages=[{"role": "user", "content": "Ciao, come stai?"}])
print(response['message']['content'])
