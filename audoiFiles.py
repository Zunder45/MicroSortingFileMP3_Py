import os, sys,eyed3
import logg
from logging import getLogger

getLogger().setLevel('ERROR')

class __AudioFile():
    """Информация аудиофайла"""
    def __init__(self,artist,fileName,pathName):
        self.artist = artist
        self.fileName = fileName
        self.filePath = pathName



audio_arr = []

def clear():
   audio_arr.clear() 

def scan(pathFrom, unknown = False,out = "c"):
    while True:
        try:
            os.chdir(pathFrom)
        except:
            logg.pr("Err 1 (Ошибка пути)","e", out=out)
            sys.exit(1)
            
        files = os.listdir(pathFrom)
        logg.pr("Поиск файлов в " + pathFrom, out=out)
        try:
            for f in files:
                fp = pathFrom+"/"+f
                
                if os.path.isdir(fp) != True and os.path.splitext(fp)[1] == ".mp3": # если это файл и имеет раширение .mp3
                    af = eyed3.load(fp)
                    try:
                        if af.tag.artist != None: # если в фаеле указано имя артиста 
                            auFl = __AudioFile(af.tag.artist, f, fp) # создаем объект 
                            audio_arr.append(auFl) # добавляем его в массив
                            logg.pr(auFl.filePath+"   ["+auFl.artist+"]","o", out=out)
                        else:
                            if unknown:
                                auFl = __AudioFile("Неизвестный исполнитель", f, fp)
                                audio_arr.append(auFl)
                                logg.pr(auFl.filePath+"   ["+auFl.artist+"]      !Артист не найден!","a", out=out)
                            else:
                                logg.pr(fp+"     !Артист не найден! Пропускаем!","a", out=out)
                    except:
                        logg.pr("Err 4 (Проблема с файлом) "+fp,"e")

            logg.pr("\nКоличество файлов: " + str(len(audio_arr)), out=out) 
            
        except:
            logg.pr("Err 2 ","e", out=out)
            sys.exit(1)
        break
        


def sort(path, out = "c"):
    logg.pr("Создание каталогов и перемещение файлов...", out=out)
    try:
        os.chdir(path)
    except:
        logg.pr("Err 1 (Ошибка пути)","e", out=out)
        sys.exit(1)
    try:
        for i in audio_arr:
            name = i.fileName
            art = i.artist
            pathName = i.filePath
            try:
                os.replace(pathName,path+"/"+art+"/"+name)
                logg.pr(pathName+" ---> "+ art,"o", out=out)
            except(Exception):
                try:
                    os.mkdir(path+"/"+art)
                    logg.pr("Создан каталог: "+path+"/"+art,"o", out=out)
                    os.replace(pathName,path+"/"+art+"/"+name)
                    logg.pr(pathName+" ---> "+ art,"o", out=out)
                except(Exception):
                    logg.pr(pathName+"    -x->   "+ art,"e", out=out)


        logg.pr("Готово","o", out=out)
    except(Exception):
        logg.pr("err 3","e", out=out)
    audio_arr.clear()