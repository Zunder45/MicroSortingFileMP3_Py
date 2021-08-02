import PySimpleGUI as sg
from colorama import Fore

class Log():


    out = "c"

    def __switch(self,message,typeMessage):
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
            if self.out == "c":
                return dictPrint[typeMessage]
            else:
                return dictPrintNoColor[typeMessage]



    def pr(self,message,typeMessage = "n"):

        if self.out == "c":
            print(self.__switch(message,typeMessage))
        elif self.out == "g":
            sg.Print(self.__switch(message,typeMessage))

        
    def pop(self,message,typeMessage = "n"):
        sg.popup(self.__switch(message,typeMessage))