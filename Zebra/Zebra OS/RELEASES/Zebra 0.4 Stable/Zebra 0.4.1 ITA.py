# Versione italiana

# Le variabili globali modificabili sono in MAIUSCOLO. Le variabili temporanee modificabili sono miste. Le costanti e le funzioni sono minuscole o contengono "__func_"
import os
import json

MEMORY_FILE = "memory.txt"

sumVAR = None
subVAR = None

memory = []
register = [False]

#__func_ significa che la funzione non deve essere chiamata dall'utente.

def __save_memory_():
    if memory != []:
        with open(MEMORY_FILE, "w") as file:
            json.dump(memory, file)
        print("Memoria salvata con successo.")

def __load_memory_():
    global memory
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as file:
            memory = json.load(file)
        print("Memoria caricata con successo.")
    else:
        print("Nessun file di memoria trovato. Avvio da zero.")

def regedit(pos, value):
    print("Attenzione: Modificare questo potrebbe cambiare le impostazioni in modo indesiderato!")
    register[pos] = value

def memoryedit(pos, value):
    try:
        memory[int(pos)] = value
    except IndexError:
        memory.append(value)

def run():
    register[0] = False
    __load_memory_()
    while True:
        __main_()

def quit():
    __save_memory_()
    print("""
----------------------------------------------------------------------------------------------------------------
Grazie per aver utilizzato il sistema operativo Zebra basic di GEA innovation!
                        (c) GEA innovation Studios
    """)
    register[0] = True

def help():
    print("""
Zebra Alpha 0.4.1

Documentazione delle funzioni:
regedit  (pos, valore)
modifica le impostazioni del programma
Pos=0: Accetta True o False. Cambia lo stato del programma. False=Non chiudere, True=Chiudere. Usa quit() invece di modificare direttamente il registro per evitare problemi alle prestazioni future.
(pos: imposta la posizione dell'impostazione da cambiare.
valore: cambia il valore associato all'impostazione alla posizione data.)

memoryedit  (pos, valore)
modifica la memoria. La memoria viene salvata anche dopo la chiusura del programma
(pos: la posizione in cui modificare la memoria.
valore: imposta/cambia il valore alla posizione selezionata)

ATTENZIONE: Quando inserisci una posizione per salvare un valore in memoria o nel registro, usa 0 per la prima posizione, 1 per la seconda, e così via.

quit  ()
chiude il programma

run  ()
Avvia il programma

help ()
mostra questo messaggio

showstorage  (arg1)
mostra la memoria salvata. arg1 accetta "mem" o "memory" per mostrare la memoria e "reg" o "register" per mostrare il registro.
Inserisci il tuo argomento tra "" qui

func1  (a, b)
mostra i parametri inseriti

sum (a, b, do)
somma il parametro a al parametro b. "do" accetta "print" o "savetemp". "Savetemp" salva il risultato in una variabile temporanea "sumVAR".
Con "saveperm" puoi salvare il risultato nella lista memoria. Inserisci la posizione in cui salvare il risultato.
"Do" deve essere inserito tra "".

sub (a, b, do)
sottrae il parametro b dal parametro a. "do" accetta "print" o "savetemp". "Savetemp" salva il risultato in una variabile temporanea "subVAR".
Con "saveperm" puoi salvare il risultato nella lista memoria. Inserisci la posizione in cui salvare il risultato.
"Do" deve essere inserito tra "".

reset  ()
Reimposta memoria e registro. Le variabili temporanee non vengono resettate. Richiede conferma con "1", "yes" o "positive".

NOVITÀ 0.4!:
La memoria e il registro vengono salvati alla chiusura del programma e riaperti nella sessione successiva. Per reimpostare la memoria o il registro usa reset().
""")

def showstorage(arg1):
    if arg1.lower() == "mem" or "memory":
        print(memory)
    elif arg1.lower() == "reg" or "register":
        print(register)

def reset():
    global memory
    global register
    localConfirm = input("Tutte le variabili e azioni di questa sessione saranno resettate. Vuoi procedere?")
    if localConfirm.lower() == "1" or "yes" or "positive":
        try:
            os.remove(MEMORY_FILE)
            print(f"Il file '{MEMORY_FILE}' è stato eliminato con successo.")
        except FileNotFoundError:
            print(f"Il file '{MEMORY_FILE}' non esiste.")
        except PermissionError:
            print(f"Permesso negato: impossibile eliminare '{MEMORY_FILE}'.")
        except Exception as e:
            print(f"Si è verificato un errore durante l'eliminazione di '{MEMORY_FILE}': {e}")
        memory = []
        register = [False]
        print("Programma resettato")

def func1(a, b):
    print(f"Hai chiamato la funzione 1 con argomenti: a={a}, b={b}")

def sum(a, b, do):
    localSUM = int(a) + int(b)
    if do == "print":
        print(localSUM)
    elif do == "savetemp":
        sumVAR = localSUM
    elif do == "saveperm":
        memnum = input("Salvare il risultato in: ")
        memoryedit(memnum, localSUM)

def sub(a, b, do):
    localSUB = int(a) - int(b)
    if do == "print":
        print(localSUB)
    elif do == "savetemp":
        subVAR = localSUB
    elif do == "saveperm":
        memnum = input("Salvare il risultato in: ")
        memoryedit(memnum, localSUB)

def __main_():
    function_name = input("Inserisci il nome della funzione da eseguire: ")

    if function_name in globals() and callable(globals()[function_name]):
        function_to_execute = globals()[function_name]
        args = input("Inserisci gli argomenti posizionali separati da spazio: ").split()
        kwargs_input = input("Inserisci argomenti con chiave (formato chiave=valore) separati da spazio: ").split()
        kwargs = {kv.split('=')[0]: kv.split('=')[1] for kv in kwargs_input}
        try:
            function_to_execute(*args, **kwargs)
        except TypeError as e:
            print(f"Errore nell'esecuzione della funzione: {e}")
    else:
        print("Funzione non trovata o non valida.")

if __name__ == "__main__":
    __load_memory_()
    while True:
        if register[0] == False:
            __main_()
        else:
            break
