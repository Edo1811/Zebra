import ollama

# Inizializza una lista per memorizzare i messaggi
context = [
    {"role": "system", "content": "Tu ti chiami Sara. "},
    {"role": "user", "content": "Come ti chiami? Rispondi solo con \"Ciao! Io mi chiamo [Nome]. Cosa posso fare per te?\" senza aggiungere o cambiare altro"}
]

response = ollama.chat(model='gemma:2b', messages=context)
print(response['message']['content'])

# Esegui un ciclo di conversazione
while True:
    user_input = input("Tu: ")
    if user_input.lower() == 'quit':
        break
    elif user_input.lower() == 'info':
        print("This is ZebraAI. Core: Gemma AI trained by Google. ")
        break
    reply = get_response(user_input)
    print(f"Zebra AI: {reply}")
