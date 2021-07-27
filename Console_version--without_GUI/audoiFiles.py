import os, sys,eyed3
import logg

from logging import getLogger



class __AudioFile():
    """Информация аудиофайла"""
    def __init__(self,artist,fileName,pathName):
        self.artist = artist
        self.fileName = fileName
        self.filePath = pathName



getLogger().setLevel('ERROR')




audio_arr = []


def scan(pathFrom, unknown = False):
    try:

        os.chdir(pathFrom)
    except:
        logg.pr("Err 1 (Ошибка пути)","e")
        sys.exit(1)
        
    files = os.listdir(pathFrom)
    logg.pr("Поиск файлов в " + pathFrom)
    try:
        for f in files:
            fp = pathFrom+"/"+f
            if os.path.isdir(fp) != True and os.path.splitext(fp)[1] == ".mp3": # если это файл и имеет раширение .mp3
                af = eyed3.load(fp)
                if af.tag.artist != None: # если в фаеле указано имя артиста 
                    auFl = __AudioFile(af.tag.artist, f, fp) # создаем объект 
                    audio_arr.append(auFl) # добавляем его в массив
                    logg.pr(auFl.filePath+"   ["+auFl.artist+"]","o")
                else:
                    if unknown:
                        auFl = __AudioFile("Неизвестный исполнитель", f, fp)
                        audio_arr.append(auFl)
                        logg.pr(auFl.filePath+"   ["+auFl.artist+"]      !Артист не найден!","a")
                    else:
                        logg.pr(fp+"     !Артист не найден! Пропускаем!","a")
        logg.pr("\nКоличество файлов: " + str(len(audio_arr))) 
    except:
        logg.pr("Err 2 ","e")
        sys.exit(1)
    if len(audio_arr) < 1:
        sys.exit(1)


def sort(path):
    logg.pr("Создание каталогов и перемещение файлов...")
    try:
        os.chdir(path)
    except:
        logg.pr("Err 1 (Ошибка пути)","e")
        sys.exit(1)
    try:
        for i in audio_arr:
            name = i.fileName
            art = i.artist
            pathName = i.filePath
            try:
                os.replace(pathName,path+"/"+art+"/"+name)
                logg.pr(pathName+" ---> "+ art,"o")
            except(Exception):
                try:
                    os.mkdir(path+"/"+art)
                    logg.pr("Создан каталог: "+path+"/"+art,"o")
                    os.replace(pathName,path+"/"+art+"/"+name)
                    logg.pr(pathName+" ---> "+ art,"o")
                except(Exception):
                    logg.pr(pathName+"    -x->   "+ art,"e")


        logg.pr("Готово","o")
    except(Exception):
        logg.pr("err 3","e")