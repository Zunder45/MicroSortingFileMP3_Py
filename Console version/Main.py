import os, argparse
import AudoiFiles



parser = argparse.ArgumentParser()

parser.add_argument("-p","--path", help="Directory path")# добавление аргументов
parser.add_argument("-f",help="The directory where the files will be taken from")

arg = parser.parse_args()

if arg.path == None: # Если флаг -p пусть то 
    path = os.getcwd() # Получение пути текущего каталога
else:
    path = arg.path
if arg.f == None:
    pathFrom = path
else:
    pathFrom = arg.f

AudoiFiles.sort(path,pathFrom)