import os
import random
import json

with open('trivia_dict.json', 'r') as file:
    trivia_dict = json.load(file)
    trivia_chosen = random.choice(trivia_dict)
print('''

┏━━┓
┗┫┣┛
╋┃┃╋┏━┓╋┏━━┓┏┓┏━━┓┏┓┏━━┓
╋┃┃╋┃┏┓┓┃┏━┛┣┫┃┏┓┃┣┫┃┏┓┃
┏┫┣┓┃┃┃┃┃┗━┓┃┃┃┗┛┃┃┃┃┗┛┃
┗━━┛┗┛┗┛┗━━┛┗┛┃┏━┛┗┛┗━━┛
╋╋╋╋╋╋╋╋╋╋╋╋╋╋┃┃
╋╋╋╋╋╋╋╋╋╋╋╋╋╋┗┛

Incipio Dictionary Viewer by Namekinek0 - ver. 0.2 -- Powered by the Websters Unabridged Dictionary \n %s
''' % trivia_chosen)
def start():
    exit = {"--exit", "-e"}
    help = {"--help", "-h"}
    version = {"--version", "-v"}
    word = input("Enter a command or search for a word (type --help for a list of commands): ")
    word = word.lower()
    if word in exit:
        os.abort()
    if word in help:
        from help import print_help
        print_help()
        print("\n")
        start()
    if word in version:
        print("Incipio Dictionary Viewer ver. 0.2")
        print("\n")
        start()
    if word[0] == "-":
        print("Command not found, try again.")
        print("\n")
        start()
    from check import read_dict
    read_dict(word)
    print("\n")
    start()
start()
