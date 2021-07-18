import os, sys,eyed3
from posixpath import pardir
import Logg
from colorama import Fore
from logging import getLogger

getLogger().setLevel('ERROR')

class AudioFile():
    """Информация аудиофайла"""
    def __init__(self,artist,fileName,pathName):
        self.artist = artist
        self.fileName = fileName
        self.filePath = pathName


path = ""
files = []




def sort(path,out = "c"):
    audio_arr= []
    os.chdir(path)
    files = os.listdir()
    try:
        Logg.pr("Поиск файлов в " + path+"\n",out=out)

        for f in files:

            fp = path+"/"+f
            if os.path.isdir(f) != True and os.path.splitext(fp)[1] == ".mp3": # если это файл и имеет раширение .mp3
                af = eyed3.load(f)
                if af.tag.artist != None: # если в фаеле указано имя артиста 
                    auFl = AudioFile(af.tag.artist, f, fp) # создаем объект 
                    audio_arr.append(auFl) # добавляем его в массив
                    Logg.pr(auFl.filePath+"   ["+auFl.artist+"]","o",out)
                else:
                    auFl = AudioFile("Неизвестный исполнитель", f, fp)
                    audio_arr.append(auFl)
                    Logg.pr(auFl.filePath+"   ["+auFl.artist+"]      !Артист не найлен!","a",out)
        Logg.pr("\nКоличество файлов: " + str(len(audio_arr)),out=out) 

        if out == "c":
                
            if len(audio_arr) < 1:
                sys.exit(1)
            while(True):
                Logg.pr("\nПродолжить?(д/н)") 
                inp = input()
                if inp == "" or inp == "д" or inp == "Д" or inp == "y" or inp == "Y":
                    break
                elif  inp == "н" or inp == "Н" or inp == "n" or inp == "N":
                    sys.exit(1)
                else:
                    continue

        Logg.pr("Создание каталогов и перемещение файлов...",out=out)
        for i in audio_arr:
            name = i.fileName
            art = i.artist
            pathName = i.filePath
            try:
                os.replace(pathName,art+"/"+name)
                Logg.pr("Файл перемещен: "+pathName+" ---> "+ art,"o",out)
            except(Exception):
                try:
                    os.mkdir(path+"/"+art)
                    Logg.pr("Создан каталог: "+path+"/"+art,"o",out)
                    os.replace(pathName,art+"/"+name)
                    Logg.pr("Файл перемещен: "+pathName+" ---> "+ art,"o",out)
                except(Exception):
                    Logg.pr(pathName+"    -x->   "+ art,"e",out)

    
        Logg.pr(path,"o",out)
        Logg.pop(path,"o")
    except(Exception):
        Logg.pr("err","e",out)
        if out == "g":
            Logg.pop("err","e")

