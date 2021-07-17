import PySimpleGUI as sg
from colorama import Fore

def pr(message,typeMessage = "n",out = "c"):
    if out == "c":
        if typeMessage == "n":
            print(message)
        elif typeMessage == "o":
            print(Fore.LIGHTGREEN_EX+"[OK]  "+message+Fore.WHITE)
        elif typeMessage == "a":
            print(Fore.LIGHTYELLOW_EX+"[ATTENTION]  "+message+Fore.WHITE)
        elif typeMessage == "e":
            print(Fore.LIGHTRED_EX,"[ERROR]  "+message+Fore.WHITE)
        else:
            print(message)
    elif out == "g":
        if typeMessage == "n":
            sg.Print(message)
        elif typeMessage == "o":
            sg.Print("[OK]  "+message)
        elif typeMessage == "a":
            sg.Print("[ATTENTION]  "+message)
        elif typeMessage == "e":
            sg.Print("[ERROR]  "+message)
        else:
            sg.Print(message)
    
