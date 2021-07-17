import os, argparse
import AudoiFiles, GUI

parser = argparse.ArgumentParser()

parser.add_argument("-p","--path", help="Directory path")# добавление аргументов
parser.add_argument("-g","--gui", help="GUI", action="store_const", const="True") 

arg = parser.parse_args()




if arg.gui:
    if arg.path == None: 
        GUI.run()
    else:
        GUI.run(arg.path)

else:
    if arg.path == None: # Если флаг -p пусть то 
        path = os.getcwd() # Получение пути текущего каталога
        AudoiFiles.sort(path)
    else:
        AudoiFiles.sort(arg.path)

