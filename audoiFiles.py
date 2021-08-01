import os, sys,eyed3
import logg
from logging import getLogger

getLogger().setLevel('ERROR')



__audio_list = []

def clear():
   __audio_list.clear() 

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
                try:
                    if af.tag.artist != None: # если в фаеле указано имя артиста 
                        auFl = {
                            'artist':af.tag.artist,
                            'fileName':f,
                            'pathName':fp
                        }
                        __audio_list.append(auFl) # добавляем его в массив
                        logg.pr(auFl['pathName']+"   ["+auFl['fileName']+"]","o")

                    else:
                        if unknown:
                            auFl = {
                                'artist':"Неизвестный исполнитель",
                                'fileName':f,
                                'pathName':fp
                            }
                            __audio_list.append(auFl)
                            logg.pr(auFl['pathName'] +"   ["+auFl['fileName']+"]      !Артист не найден!","a")
                        else:
                            logg.pr(fp+"     !Артист не найден! Пропускаем!","a")
                except:
                    logg.pr("Err 4 (Проблема с файлом) "+fp,"e")

        logg.pr("\nКоличество файлов: " + str(len(__audio_list))) 
        
    except:
        logg.pr("Err 2 ","e")
        sys.exit(1)
    if len(__audio_list) < 1:
        return False
    return True
        


def sort(path):
    logg.pr("Создание каталогов и перемещение файлов...")
    try:
        os.chdir(path)
    except:
        logg.pr("Err 1 (Ошибка пути)","e")
        sys.exit(1)
    try:
        for i in __audio_list:
            name = i['fileName']
            art = i['artist']
            pathName = i['pathName']
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
        sys.exit(1)
    __audio_list.clear()