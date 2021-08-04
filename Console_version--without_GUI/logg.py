from colorama import Fore


class Log():
    def __switch(self,message,typeMessage):
            dictPrint = {
                "n": message,
                "o": Fore.LIGHTGREEN_EX + "[OK]  " + message + Fore.WHITE,
                "a": Fore.LIGHTYELLOW_EX+"[ATTENTION]  " + message + Fore.WHITE,
                "e": Fore.LIGHTRED_EX + "[ERROR]  " + message + Fore.WHITE
            }
            return dictPrint[typeMessage]
            
    def pr(self,message,typeMessage = "n"):
            print(self.__switch(message,typeMessage))