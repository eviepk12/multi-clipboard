import sys
import json
import clipboard 

SAVED_DATA = "clipboard.json"

def save_items(filepath, data):
    with open(filepath, "w") as f:
        json.dump(data, f)

def load_items(filepath):
    try:
        with open(filepath, "r") as f:
            data=json.load(f)
            return data
    except:
        return {}

if len(sys.argv) == 2:
    command = sys.argv[1]
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
        print("------------------------------------------------------------------")
        print("List of commands: ")
        print("------------------------------------------------------------------")
        print("1. Save (save the current thing in your clipboard to a given key)") 
        print("2. Load (load the given key you put in into your clipboard)") 
        print("3. List (list all the keys in the json file)")
        print("4. Help (prints documentation on how to use the program)")

    else:
        print("Unknown Command")
else:
    print("Pass the correct command")