#Sistema Operativo Base Zebra Versione Alpha 0.3
#by GEA innovations studio

#Le variabili globali modificabili sono in MAIUSCOLO. Le variabili temporanee modificabili sono in misto. Le costanti e le funzioni sono in minuscolo o contengono "__func_"

sumVAR = None
subVAR = None

memoria = []
registro = [False]

#__func_ significa che la funzione non deve essere chiamata dall'utente. Maggiori dettagli in Alpha0.2

def regedit(posizione, valore):
    print("Attenzione: Modificare questo parametro potrebbe cambiare le impostazioni in modo indesiderato!")
    registro[posizione] = valore

def modifica_memoria(posizione, valore):
    try:
        memoria[int(posizione)] = valore
    except IndexError:
        memoria.append(valore)

def esci():
    print("""
----------------------------------------------------------------------------------------------------------------
Grazie per aver utilizzato il sistema operativo di base Zebra di GEA innovation!
                        (c) GEA innovation Studios
    """)
    registro[0] = True

def aiuto():
    print("""
Zebra Alpha 0.2.1

Documentazione delle Funzioni:
regedit  (posizione, valore)
modifica le impostazioni all'interno del programma - Non fa nulla nella versione 0.2.1
(posizione: imposta la posizione della modifica dell'impostazione. Aggiungere un'impostazione non è possibile e non ha senso perché non influisce sul codice stesso.
valore: cambia il valore associato all'impostazione nella posizione data.)

modifica_memoria  (posizione, valore)
modifica la memoria. Attenzione: Nella versione 0.2.1 la memoria viene resettata ogni volta che il programma viene eseguito.
(posizione: la posizione in cui la memoria viene modificata.
valore: imposta/cambia il valore nella posizione selezionata)

esci  ()
esce dal programma

aiuto ()
mostra questo messaggio

mostra_memoria  (arg1)
mostra la memoria salvata. arg1 accetta mem o memoria per mostrare la memoria e reg/registro per mostrare il registro attuale
inserisci il tuo argomento qui ""

funz1  (a, b)
mostra i parametri inseriti

somma (a, b, azione)
somma il parametro a con il parametro b. azione accetta stampa o salva_temp. Salva_temp salva il risultato in una variabile temporanea "sumVAR".
Questa variabile non può essere salvata direttamente nella memoria in questa versione. Nella versione 0.3 puoi inserire salva_perm e il risultato
sarà salvato nella lista della memoria.

""")

def mostra_memoria(arg1):
    if arg1.lower() == "mem" or "memoria":
        print(memoria)
    elif arg1.lower() == "reg" or "registro":
        print(registro)

def funz1(a, b):
    print(f"Hai chiamato la funzione 1 con argomenti: a={a}, b={b}")

def somma(a, b, azione):
    SOMMA = int(a) + int(b)
    if azione == "stampa":
        print(SOMMA)
    elif azione == "salva_temp":
        sumVAR = SOMMA
    elif azione == "salva_perm":
        num_memoria = input("Salva risultato in: ")
        modifica_memoria(num_memoria, SOMMA)

def sottrai(a, b, azione):
    SOTTRAI = int(a) - int(b)
    if str(azione) == "stampa":
        print(SOTTRAI)
    elif str(azione) == "salva_temp":
        subVAR = SOTTRAI
    elif str(azione) == "salva_perm":
        num_memoria = input("Salva risultato in: ")
        modifica_memoria(num_memoria, SOTTRAI)

def __main_():
    nome_funzione = input("Inserisci il nome della funzione da eseguire: ")

    if nome_funzione in globals() and callable(globals()[nome_funzione]):
        funzione_da_eseguire = globals()[nome_funzione]
        
        args = input("Inserisci gli argomenti posizionali separati da spazio: ").split()
        
        kwargs_input = input("Inserisci gli argomenti con parole chiave (formato chiave=valore) separati da spazio: ").split()
        kwargs = {kv.split('=')[0]: kv.split('=')[1] for kv in kwargs_input}
        
        try:
            funzione_da_eseguire(*args, **kwargs)
        except TypeError as e:
            print(f"Errore nell'esecuzione della funzione: {e}")
    else:
        print("Funzione non trovata o non valida.")

if __name__ == "__main__":
    while True:
        if registro[0] == False:
            __main_()
        else:
            exit()
            break
