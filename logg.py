import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import Titlebar
from colorama import Fore

out = "c"

def pr(message,typeMessage = "n"):
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
            sg.popup_error(message,title="Err")
        else:
            sg.Print(message)
    
def pop(message,typeMessage = "n"):
    if typeMessage == "n":
        sg.popup(message)
    elif typeMessage == "o":
        sg.popup(message,title="ok")
    elif typeMessage == "a":
        sg.popup(message,title="attention")
    elif typeMessage == "e":
        sg.popup(message,title="error")
    else:
        sg.popup(message)