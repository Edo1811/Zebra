#Zebra Base Operating System Version Alpha 0.3
#by GEA innovations studio

#Global editable variables are UPPERCASE. Temporary editable variables are mixed case. Constants and functions are lowercase or contain "__func_"

sumVAR = None
subVAR = None

memory = []
register = [False]

#__func_ means that the function must not be called by the user. More in Alpha0.2

def regedit(pos, value):
    print("Warning: Editing this could change settings in an unwanted way!")
    register[pos] = value

def memoryedit(pos, value):
    try:
        memory[int(pos)] = value
    except IndexError:
        memory.append(value)

def quit():
    print("""
----------------------------------------------------------------------------------------------------------------
Thanks for using GEA innovation's Zebra basic operating system!
                        (c) GEA innovation Studios
    """)
    register[0] = True

def help():
    print("""
Zebra Alpha 0.2.1

Functions Documentation:
regedit  (pos, value)
changes settings inside the program - Does nothing in 0.2.1
(pos: Set the position of the changed setting. Adding setting is not possible and is useless because it doesn't affect the code itself.
value: change the value associated to the setting on the position given.)

memoryedit  (pos, value)
edits the memory. Warning: In 0.2.1 the memory gets reset every time the program runs.
(pos: the position where the memory gets edited.
value: set/change the value on the selected position)

quit  ()
quits the program

help ()
shows this message

showstorage  (arg1)
shows the saved storage. arg1 takes mem or memory to show the memory and reg/register to show the actual register
put your argument in "" here

func1  (a, b)
shows the parameters entered

sum (a, b, do)
sums the parameter a with parameter b. do takes print or savetemp. Savetemp saves the result in a temporary variable "sumVAR".
This variable cannot be saved directly to the memory in this version. In version 0.3 you can enter saveperm and the result is going
to be saved in the memory list.

""")

def showstorage(arg1):
    if arg1.lower() == "mem" or "memory":
        print(memory)
    elif arg1.lower() == "reg" or "register":
        print(register)

def func1(a, b):
    print(f"You called function 1 with arguments: a={a}, b={b}")

def sum(a, b, do):
    SUM = int(a) + int(b)
    if do == "print":
        print(SUM)
    elif do == "savetemp":
        sumVAR = SUM
    elif do == "saveperm":
        memnum = input("Save result in: ")
        memoryedit(memnum, SUM)

def sub(a, b, do):
    SUB = int(a) - int(b)
    if str(do) == "print":
        print(SUB)
    elif str(do) == "savetemp":
        subVAR = SUB
    elif str(do) == "saveperm":
        memnum = input("Save result in: ")
        memoryedit(memnum, SUB)

def __main_():
    function_name = input("Enter the function name to execute: ")

    if function_name in globals() and callable(globals()[function_name]):
        function_to_execute = globals()[function_name]
        
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
    while True:
        if register[0] == False:
            __main_()
        else:
            break
