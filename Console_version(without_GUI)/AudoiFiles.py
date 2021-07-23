import os, sys,eyed3, argparse
import Logg
from colorama import Fore
from logging import getLogger



class AudioFile():
    """Информация аудиофайла"""
    def __init__(self,artist,fileName,pathName):
        self.artist = artist
        self.fileName = fileName
        self.filePath = pathName



getLogger().setLevel('ERROR')

audio_arr= []


def scan(pathFrom, unknown = False):
    try:
        
        if pathFrom[len(pathFrom)-1] != "/" :
            pathFrom+="/"

        os.chdir(pathFrom)
    except:
        Logg.pr("Err 1 (Ошибка пути)","e")
        sys.exit(1)
        
    files = os.listdir(pathFrom)
    Logg.pr("Поиск файлов в " + pathFrom)
    try:
        for f in files:
            fp = pathFrom+"/"+f
            if os.path.isdir(fp) != True and os.path.splitext(fp)[1] == ".mp3": # если это файл и имеет раширение .mp3
                af = eyed3.load(fp)
                if af.tag.artist != None: # если в фаеле указано имя артиста 
                    auFl = AudioFile(af.tag.artist, f, fp) # создаем объект 
                    audio_arr.append(auFl) # добавляем его в массив
                    Logg.pr(auFl.filePath+"   ["+auFl.artist+"]","o")
                else:
                    if unknown:
                        auFl = AudioFile("Неизвестный исполнитель", f, fp)
                        audio_arr.append(auFl)
                        Logg.pr(auFl.filePath+"   ["+auFl.artist+"]      !Артист не найден!","a")
                    else:
                        Logg.pr(fp+"     !Артист не найден! Пропускаем!","a")
        Logg.pr("\nКоличество файлов: " + str(len(audio_arr))) 
    except:
        Logg.pr("Err 2 ","e")
        sys.exit(1)
    if len(audio_arr) < 1:
        sys.exit(1)


def sort(path):
    Logg.pr("Создание каталогов и перемещение файлов...")
    try:
        if path[len(path)-1] != "/" :
            path+="/"
        os.chdir(path)
    except:
        Logg.pr("Err 1 (Ошибка пути)","e")
        sys.exit(1)
    try:
        for i in audio_arr:
            name = i.fileName
            art = i.artist
            pathName = i.filePath
            try:
                os.replace(pathName,path+"/"+art+"/"+name)
                Logg.pr(pathName+" ---> "+ art,"o")
            except(Exception):
                try:
                    os.mkdir(path+"/"+art)
                    Logg.pr("Создан каталог: "+path+"/"+art,"o")
                    os.replace(pathName,path+"/"+art+"/"+name)
                    Logg.pr(pathName+" ---> "+ art,"o")
                except(Exception):
                    Logg.pr(pathName+"    -x->   "+ art,"e")


        Logg.pr("Готово","o")
    except(Exception):
        Logg.pr("err 3","e")