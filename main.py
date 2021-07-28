import os, argparse, sys
import audoiFiles, gui, logg

parser = argparse.ArgumentParser()

parser.add_argument("-p","--path", help="Directory path")# добавление аргументов
parser.add_argument("-f",help="Каталог, из которого будут взяты файлы")
parser.add_argument("-u","--unknown",help="Брать файлы с неизвестными исполнителями",action="store_const", const="True")
parser.add_argument("-s",help="Пропускать 'Продолжить'",action="store_const", const="True")
parser.add_argument("-g","--gui", help="GUI", action="store_const", const="True") 

arg = parser.parse_args()



if arg.path == None: # Если флаг -p пусть то 
    path = os.getcwd() # Получение пути текущего каталога
elif arg.path == "?":
    path = gui.popup_selectFolder("Путь где будет сортировка")
else:
    path = arg.path

if arg.f == None:
    pathFrom = path
elif arg.f == "?":
    pathFrom = gui.popup_selectFolder("Путь к файлам")
else:
    pathFrom = arg.f

if arg.gui == None:

    audoiFiles.scan(pathFrom =  pathFrom,unknown= arg.unknown)

    if not arg.s:
        while(True):
                logg.pr("\nПродолжить?(д/н)") 
                inp = input()
                if inp == "" or inp == "д" or inp == "Д" or inp == "y" or inp == "Y":
                    break
                elif  inp == "н" or inp == "Н" or inp == "n" or inp == "N":
                    sys.exit(1)
                else:
                    continue

    audoiFiles.sort(path = path)

else: 
    gui.run(pathFromDir = pathFrom,pathDirInput = path)