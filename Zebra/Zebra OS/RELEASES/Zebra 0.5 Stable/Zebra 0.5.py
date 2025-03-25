import os
import sys
import json
import math
import tkinter as tk
from tkinter import scrolledtext
from datetime import datetime
from colorama import Fore, Back, Style

MEMORY_DIR = "Saved ZData"
MEMORY_FILE = os.path.join(MEMORY_DIR, "memory.json")

debug_mode = False
sumVAR = None
subVAR = None
memory = []
register = [False, False]

def __save_memory_():
    if not os.path.exists(MEMORY_DIR):
        os.makedirs(MEMORY_DIR)
    if memory:
        with open(MEMORY_FILE, "w") as file:
            json.dump(memory, file)
        log("Memory saved successfully.")

def __load_memory_():
    global memory
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as file:
            memory = json.load(file)
        log("Memory loaded successfully.")
    else:
        log("No memory file found. Starting fresh.")

def log(message):
    output_area.insert(tk.END, message + "\n")
    output_area.see(tk.END)

def execute_command():
    command = input_area.get()
    input_area.delete(0, tk.END)
    __main_(command)

def regedit(pos, value):
    log("Warning: Editing this could change settings in an unwanted way!")
    register[int(pos)] = value

def memoryedit(pos, value):
    try:
        if isinstance(value, (int, float)):
            memory[int(pos)] = value
    except IndexError:
        memory.append(value)

def delmemory(pos):
    try:
        del memory[int(pos)]
        log(f"Deleted memory position {pos}.")
    except IndexError:
        log("Invalid memory position.")

def quit():
    register[0] = True
    __save_memory_()
    log("Thanks for using Zebra OS!")
    root.destroy()
    sys.exit()

def help():
    help_text = """
    Zebra OS - Available Commands:
    - regedit <pos> <value>: Edit a register value.
    - memoryedit <pos> <value>: Edit a memory value.
    - delmemory <pos>: Delete a memory position.
    - quit: Exit the program and save progress.
    - help: Show this help message.
    - showstorage <mem|reg>: Display memory or register contents.
    - sum <a> <b>: Calculate sum.
    - sub <a> <b>: Calculate subtraction.
    - mul <a> <b>: Calculate multiplication.
    - div <a> <b>: Calculate division.
    - reset: Reset memory and registers.
    - println <text>: Print text to the shell.
    - __save_memory_: Save the current state to a file.
    - timestamp: Show current date and time.
    - clear: Clear shell output.
    - listcommands: Show available commands.
    - toggledebug: Enable/Disable debug mode.
    """
    log(help_text)

def listcommands():
    commands = ["regedit", "memoryedit", "delmemory", "quit", "help", "showstorage", "sum", "sub", "mul", "div", "reset", "println", "timestamp", "clear", "listcommands", "toggledebug"]
    log("Available commands: " + ", ".join(commands))

def showstorage(arg1="mem"):
    if arg1.lower() in ["mem", "memory"]:
        log(str(memory))
    elif arg1.lower() in ["reg", "register"]:
        log(str(register))

def reset():
    global memory, register
    memory = []
    register = [False, False]
    log("Program reset")

def sum(a, b):
    log(str(int(a) + int(b)))

def sub(a, b):
    log(str(int(a) - int(b)))

def mul(a, b):
    log(str(int(a) * int(b)))

def div(a, b):
    if int(b) == 0:
        log("Division by zero is not allowed.")
    else:
        log(str(int(a) / int(b)))

def println(text, text_color=None, text_style=None):
    # Set default color and style
    #color = text_color if text_color else Fore.WHITE
    #style = text_style if text_style else ""
    
    # Print the styled text
    #log(f"{color}{style}{text}{Style.RESET_ALL}")
    log(text)

def timestamp():
    log("Current timestamp: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

def clear():
    output_area.delete('1.0', tk.END)

def toggledebug():
    global debug_mode
    debug_mode = not debug_mode
    log(f"Debug mode {'enabled' if debug_mode else 'disabled'}.")

def repeat(repeat_count, command):
    for _ in range(int(repeat_count)):
        exec(command)

def advanced_operations(operation, number, secondary=1):
    if operation == 'power':
        exponent = float(secondary)
        return number ** exponent
    elif operation == 'sqrt':
        return math.sqrt(number)
    elif operation == 'mod':
        mod_value = float(secondary)
        return number % mod_value
    else:
        return "Invalid operation!"

def __main_(command):
    args = command.split()
    if not args:
        return
    cmd = args[0]
    params = args[1:]
    
    if cmd in globals() and callable(globals()[cmd]):
        try:
            globals()[cmd](*params)
        except TypeError as e:
            log(f"Error: {e}")
    else:
        log("Unknown command")

root = tk.Tk()
root.title("Zebra OS")

output_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=130, height=30)
output_area.pack()

input_area = tk.Entry(root, width=100)
input_area.pack()
input_area.bind("<Return>", lambda event: execute_command())

execute_button = tk.Button(root, text="Execute", command=execute_command)
execute_button.pack()
quit_button = tk.Button(root, text="Quit", command=quit)
quit_button.pack()

__load_memory_()
root.mainloop()


