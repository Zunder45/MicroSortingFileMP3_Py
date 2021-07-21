import os, sys,eyed3, argparse
import Logg
from colorama import Fore
from logging import getLogger

def exit():
    sys.exit(1)


class AudioFile():
    """Информация аудиофайла"""
    def __init__(self,artist,fileName,pathName):
        self.artist = artist
        self.fileName = fileName
        self.filePath = pathName



getLogger().setLevel('ERROR')


def sort(path,pathFrom):
    audio_arr= []
    try:
        os.chdir(path)
    except:
        Logg.pr("Err 2","e")
        exit()
        
    files = os.listdir(pathFrom)
    try:
        
        Logg.pr("Поиск файлов в " + pathFrom)

        for f in files:

            fp = pathFrom+"/"+f
            

            if os.path.isdir(fp) != True and os.path.splitext(fp)[1] == ".mp3": # если это файл и имеет раширение .mp3
                af = eyed3.load(fp)
                if af.tag.artist != None: # если в фаеле указано имя артиста 
                    auFl = AudioFile(af.tag.artist, f, fp) # создаем объект 
                    audio_arr.append(auFl) # добавляем его в массив
                    Logg.pr(auFl.filePath+"   ["+auFl.artist+"]","o")
                else:
                    auFl = AudioFile("Неизвестный исполнитель", f, fp)
                    audio_arr.append(auFl)
                    Logg.pr(auFl.filePath+"   ["+auFl.artist+"]      !Артист не найлен!","a")

        Logg.pr("\nКоличество файлов: " + str(len(audio_arr))) 
            
        if len(audio_arr) < 1:
            exit()

        
        while(True):
            Logg.pr("\nПродолжить?(д/н)") 
            inp = input()
            if inp == "" or inp == "д" or inp == "Д" or inp == "y" or inp == "Y":
                break
            elif  inp == "н" or inp == "Н" or inp == "n" or inp == "N":
                exit()
            else:
                continue

        Logg.pr("Создание каталогов и перемещение файлов...")
        for i in audio_arr:
            name = i.fileName
            art = i.artist
            pathName = i.filePath
            try:
                Logg.pr(pathName+"  {"+ path+art+"/"+name+"}")
                os.replace(pathName,path+"/"+art+"/"+name)
                Logg.pr(pathName+" ---> "+ art,"o")
            except(Exception):
                try:
                    os.mkdir(path+"/"+art)
                    Logg.pr("Создан каталог: "+pathName+"/"+art,"o")
                    os.replace(pathName,path+"/"+art+"/"+name)
                    Logg.pr(pathName+" ---> "+ art,"o")
                except(Exception):
                    Logg.pr(pathName+"    -x->   "+ art,"e")


        Logg.pr(path,"o")
    except(Exception):
        Logg.pr("err 1","e")