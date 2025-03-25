#Zebra Base Operating System Version Alpha 0.4.2
#by GEA innovations studio

#Global editable variables are UPPERCASE. Temporary editable variables are mixed case. Constants and functions are lowercase or contain "__func_"
import os
import json

MEMORY_FILE = "memory.txt"

sumVAR = None
subVAR = None

memory = []
register = [False, False]

#__func_ means that the function must not be called by the user.

def __save_memory_():
    if memory != []:
        with open(MEMORY_FILE, "w") as file:
            json.dump(memory, file)
        print("Memory saved successfully.")

def __load_memory_():
    global memory
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as file:
            memory = json.load(file)
        print("Memory loaded successfully.")
    else:
        print("No memory file found. Starting fresh.")

def regedit(pos, value):
    print("Warning: Editing this could change settings in an unwanted way!")
    register[int(pos)] = value

def memoryedit(pos, value):
    try:
        memory[int(pos)] = value
    except IndexError:
        memory.append(value)

def run():
    register[0] = False
    __load_memory_
    while True:
        __main_()

def quit():
    __save_memory_()
    print("""
----------------------------------------------------------------------------------------------------------------
Thanks for using GEA innovation's Zebra basic operating system!
                        (c) GEA innovation Studios
    """)
    register[0] = True

def help():
    print("""
Zebra Alpha 0.4.2

Functions Documentation:
regedit  (pos, value)
changes settings inside the program
[StatusProgrammQuitting] Pos=0: Takes True or False. Changes the state of the progamm. False=Not quitting, True=Quitting. Quit the program by using quit() instead of the register because it may affect the performance for the next time.
[SkipFunctionAttributes] Pos=1: Takes True or False. 
(pos: Set the position of the changed setting. Adding setting is not possible and is useless because it doesn't affect the code itself.
value: change the value associated to the setting on the position given.)

memoryedit  (pos, value)
edits the memory. The memory saves even after you close the program
(pos: the position where the memory gets edited.
value: set/change the value on the selected position)

WARNING: When entering a position to save a value in memory or in the register you have to use 0 for the first position, 1 for the second position and so on.

quit  ()
quits the program

run  ()
Runs the program

help ()
shows this message

showstorage  (arg1)
shows the saved storage. arg1 takes mem or memory to show the memory and reg/register to show the register.
put your argument in "" here 

func1  (a, b)
shows the parameters entered

sum (a, b, do)
sums the parameter a with parameter b. do takes print or savetemp. Savetemp saves the result in a temporary variable "sumVAR".
With saveperm you can save the result in the memory list. Enter the position where the result has to be saved in the memory.
Do has to be entered in ""

sub (a, b, do)
subtracts the parameter a with parameter b. do takes print or savetemp. Savetemp saves the result in a temporary variable "subVAR".
With saveperm you can save the result in the memory list. Enter the position where the result has to be saved in the memory.
Do has to be entered in ""

mul(a, b, do)
multiplies parameter a with b. do takes print or savetemp. Savetemp saves the result in a temporary variable "subVAR".
With saveperm you can save the result in the memory list. Enter the position where the result has to be saved in the memory.
Do has to be entered in ""

div(a, b, do)
divides a with b. do takes print or savetemp. Savetemp saves the result in a temporary variable "subVAR".
With saveperm you can save the result in the memory list. Enter the position where the result has to be saved in the memory.
Do has to be entered in ""

reset  ()
Resets memory and register. Temporary variables are not getting reset. Needs the user to confirm with "1", "yes" or "positive".

0.4 NEWS!:
Memory and register saves after you close the program. It will be opened in the next session. To reset memory or register content to default use reset  ().
""")

def showstorage(arg1):
    if arg1.lower() == "mem" or "memory":
        print(memory)
    elif arg1.lower() == "reg" or "register":
        print(register)

def reset():
    global memory
    global register
    localConfirm = input("All variables and actions for this session are going to be reset. Do you want to proceed?")
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
        register = [False, False]
        print("Programm reset")

def func1(a, b):
    print(f"You called function 1 with arguments: a={a}, b={b}")

def sum(a, b, do):
    localSUM = int(a) + int(b)
    if do == "print":
        print(localSUM)
    elif do == "savetemp":
        sumVAR = localSUM
    elif do == "saveperm":
        memnum = input("Save result in: ")
        memoryedit(memnum, localSUM)

def sub(a, b, do):
    localSUB = int(a) - int(b)
    if str(do) == "print":
        print(localSUB)
    elif str(do) == "savetemp":
        subVAR = localSUB
    elif str(do) == "saveperm":
        memnum = input("Save result in: ")
        memoryedit(memnum, localSUB)

def div(a, b, do):
    if int(b) == 0:
        print("Division by zero is not allowed.")
        return
    localDIV = int(a) / int(b)
    if str(do) == "print":
        print(localDIV)
    elif str(do) == "savetemp":
        divVAR = localDIV
    elif str(do) == "saveperm":
        memnum = input("Save result in: ")
        memoryedit(memnum, localDIV)

def mul(a, b, do):
    localMUL = int(a) * int(b)
    if str(do) == "print":
        print(localMUL)
    elif str(do) == "savetemp":
        mulVAR = localMUL
    elif str(do) == "saveperm":
        memnum = input("Save result in: ")
        memoryedit(memnum, localMUL)

def __main_():
    function_name = input("Enter the function name to execute: ")

    if function_name in globals() and callable(globals()[function_name]):
        function_to_execute = globals()[function_name]
        if register[1] == False:
            args = input("Enter positional arguments separated by space: ").split()
        
            kwargs_input = input("Enter keyword arguments (format key=value) separated by space: ").split()
            kwargs = {kv.split('=')[0]: kv.split('=')[1] for kv in kwargs_input}
        
        try:
            function_to_execute(*args, **kwargs)
        except TypeError as e:
            print(f"Error executing the function: {e}")
    else:
        print("Function not found or invalid.")

if __name__ == "__main__":
    __load_memory_()
    while True:
        if register[0] == False:
            __main_()
        else:
            break
