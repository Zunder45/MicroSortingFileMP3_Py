from colorama import Fore

nocolor = False

def __switch(message,typeMessage):
        dictPrint = {
            "n": message,
            "o": Fore.LIGHTGREEN_EX + "[OK]  " + message + Fore.WHITE,
            "a": Fore.LIGHTYELLOW_EX+"[ATTENTION]  " + message + Fore.WHITE,
            "e": Fore.LIGHTRED_EX + "[ERROR]  " + message + Fore.WHITE
        }
        dictPrintNoColor = {
            "n": message,
            "o": "[OK]  " + message,
            "a": "[ATTENTION]  " + message,
            "e": "[ERROR]  " + message
        }
        if not nocolor:
            return dictPrint[typeMessage]
        else:
            return dictPrintNoColor[typeMessage]
def pr(message,typeMessage = "n"):
        print(__switch(message,typeMessage))