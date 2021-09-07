import PySimpleGUI as sg
from colorama import Fore




nocolor = False

def __switch(message,typeMessage, popup = False):
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

        if popup:
            return dictPrintNoColor[typeMessage]
        else:
            if not nocolor:
                return dictPrint[typeMessage]
            else:
                return dictPrintNoColor[typeMessage]





def pr(message,typeMessage = "n"):
    print(__switch(message,typeMessage))

    
def pop(message,typeMessage = "n"):
    sg.popup(__switch(message,typeMessage, popup = True))