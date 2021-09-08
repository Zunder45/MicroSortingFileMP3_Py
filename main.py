import os, argparse, sys
import audoiFiles as af
import logg as log 
import gui 




def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("-p","--path", help="Путь к каталогу, где будут сортироватся файлы")# добавление аргументов
    parser.add_argument("-f",help="Каталог, из которого будут взяты файлы")
    parser.add_argument("-u","--unknown",help="Брать файлы с неизвестными исполнителями",action="store_const", const="True")
    parser.add_argument("-s",help="Пропускать 'Продолжить'",action="store_const", const="True")
    parser.add_argument("-g","--gui", help="GUI", action="store_const", const="True") 
    parser.add_argument("--nocolor", action="store_const", const="True")


    arg = parser.parse_args()


    log.nocolor = arg.nocolor


    if arg.path == None: # Если флаг -p пусть то 
        path = os.getcwd() # Получение пути текущего каталога
    elif arg.path == "?":
        path = gui.popup_selectFolder("Путь где будет сортировка (-p)")
    else:
        path = arg.path

    if arg.f == None:
        pathFrom = path
    elif arg.f == "?":
        pathFrom = gui.popup_selectFolder("Путь к файлам (-f)")
    else:
        pathFrom = arg.f



    if arg.gui == None:
        if af.scan(pathFrom =  pathFrom,unknown = arg.unknown):
            if not arg.s:
                while(True):
                        print("\nПродолжить?(д/н)") 
                        inp = input()
                        if inp == "" or inp == "д" or inp == "Д" or inp == "y" or inp == "Y":
                            break
                        elif  inp == "н" or inp == "Н" or inp == "n" or inp == "N":
                            sys.exit(0)
                        else:
                            continue
            af.sort(path = path)
    else: 
        gui.run(pathFromDir = pathFrom,pathDirInput = path)
    

if __name__ == "__main__":
    main()