# Simple program to save the current copied object in your clipboard to a json key
# Made by enal

import sys
import json
import clipboard 

SAVED_DATA = "clipboard.json"

def save_items(filepath, data): 
    with open(filepath, "w") as f: #"w" means to write, and if there's no existing file to write it will create a new json file
        json.dump(data, f) 

def load_items(filepath):
    try:
        with open(filepath, "r") as f: #"r" means to read
            data=json.load(f)
            return data
    except:
        return {}

if len(sys.argv) == 2: #checks the lenght of the input to make sure it's right, 2 because of the filename and command
    command = sys.argv[1] #ignores the filename and just inputs the command 
    data = load_items(SAVED_DATA) 

    if command == "save":
        key = input("Enter a key you want saved: ")
        data[key] = clipboard.paste()
        save_items(SAVED_DATA, data)
        print("Data Saved!!")

    elif command == "load":
        key = input("Enter a key you want to load/copy: ")
        if key in data:
            clipboard.copy(data[key])
            print("Data copied to your clipboard!!")

        else:
            print("Key does not exist: ")

    elif command == "list":
        print(data)

    elif command == "help":
        print("\n------------------------------------------------------------------")
        print("List of commands: ")
        print("------------------------------------------------------------------ \n")
        print("1. Save (save the current thing in your clipboard to a given key)") 
        print("2. Load (load the given key you put in into your clipboard)") 
        print("3. List (list all the keys in the json file)")
        print("4. Help (prints documentation on how to use the program) \n")

    else:
        print("Unknown Command")
else:
    print("Pass the correct command")