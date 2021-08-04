import PySimpleGUI as sg
from colorama import Fore




out = "c"
nocolor = False

def __switch(message,typeMessage):
        dictPrint = {
            "n": message,
            "o": Fore.LIGHTGREEN_EX + "[OK]  " + message + Fore.RESET,
            "a": Fore.LIGHTYELLOW_EX+"[ATTENTION]  " + message + Fore.RESET,
            "e": Fore.LIGHTRED_EX + "[ERROR]  " + message + Fore.RESET
        }
        dictPrintNoColor = {
            "n": message,
            "o": "[OK]  " + message,
            "a": "[ATTENTION]  " + message,
            "e": "[ERROR]  " + message
        }
        if out == "c" and not nocolor:
            return dictPrint[typeMessage]
        elif nocolor:
            return dictPrintNoColor[typeMessage]
        else:
            return dictPrintNoColor[typeMessage]




def pr(message,typeMessage = "n"):

    if out == "c":
        print(__switch(message,typeMessage))
    elif out == "g":
        sg.Print(__switch(message,typeMessage))

    
def pop(message,typeMessage = "n"):
    sg.popup(__switch(message,typeMessage))