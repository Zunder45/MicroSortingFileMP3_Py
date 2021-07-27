from colorama import Fore


def pr(message,typeMessage = "n"):
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
