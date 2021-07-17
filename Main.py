import os, sys, eyed3, argparse
import AudoiFiles, GUI

parser = argparse.ArgumentParser()

parser.add_argument("-p","--path", help="Directory path")# добавление аргументов
parser.add_argument("-g","--gui", help="GUI", action="store_const", const="True")

arg = parser.parse_args()




if arg.gui:
    GUI.run()
else:
    if arg.path == None: # Если флаг -p пусть то:
        # files = os.listdir() # Список файлов тек каталога 
        path = os.getcwd() # Получение пути текущего каталога
        AudoiFiles.sort(path)
    else:
        # os.chdir(arg.path) # Переход в директорию 
        # # files = os.listdir() # Массив с файлами
        # path = os.getcwd() # Получение пути текущего каталога
        AudoiFiles.sort(arg.path)

