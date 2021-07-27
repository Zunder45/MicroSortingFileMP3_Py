import os, sys, argparse
import audoiFiles
import logg


parser = argparse.ArgumentParser()

parser.add_argument("-p","--path", help="Путь к каталогу, где будут сортироватся файлы")# добавление аргументов
parser.add_argument("-f",help="Каталог, из которого будут взяты файлы")
parser.add_argument("-s",help="Пропускать 'Продолжить'",action="store_const", const="True")
parser.add_argument("-u","--unknown",help="Брать файлы с неизвестными исполнителями",action="store_const", const="True")


arg = parser.parse_args()

if arg.path == None: # Если флаг -p пусть то 
    path = os.getcwd() # Получение пути текущего каталога
else:
    path = arg.path
if arg.f == None:
    pathFrom = path
else:
    pathFrom = arg.f


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



