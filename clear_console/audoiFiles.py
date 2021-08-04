import os, sys,eyed3

import logg as log

from logging import getLogger


getLogger().setLevel('ERROR')

__audio_list = []

def scan(pathFrom, unknown = False):
    try:
        os.chdir(pathFrom)
    except:
        log.pr("Err 1 (Ошибка пути)","e")
        sys.exit(1)
        
    files = os.listdir(pathFrom)
    log.pr("Поиск файлов в " + pathFrom)
    try:
        for f in files:
            sep = os.sep
            fp = pathFrom+sep+f
            if os.path.isdir(fp) != True and os.path.splitext(fp)[1] == ".mp3": # если это файл и имеет раширение .mp3
                af = eyed3.load(fp)
                try:
                    if af.tag.artist != None: # если в фаеле указано имя артиста 
                        auFl = {
                            'artist':af.tag.artist,
                            'fileName':f,
                            'pathName':fp
                        } # создаем словарь 
                        __audio_list.append(auFl) # добавляем его в массив
                        log.pr(auFl['pathName']+"   ["+auFl['artist']+"]","o")
                    else:
                        if unknown:
                            auFl = {
                                'artist':"Неизвестный исполнитель",
                                'fileName':f,
                                'pathName':fp
                            }
                            __audio_list.append(auFl)
                            log.pr(auFl['pathName'] +"   ["+auFl['artist']+"]      !Артист не найден!","a")
                        else:
                            log.pr(fp+"     !Артист не найден! Пропускаем!","a")
                except:
                    log.pr("Err 4 (Проблема с файлом) "+fp,"e")
        log.pr("\nКоличество файлов: " + str(len(__audio_list))) 
    except:
        log.pr("Err 2 ","e")
        sys.exit(1)
    if len(__audio_list) < 1:
        sys.exit(1)
        


def sort(path):
    log.pr("Создание каталогов и перемещение файлов...")
    try:
        os.chdir(path)
    except:
        log.pr("Err 1 (Ошибка пути)","e")
        sys.exit(1)
    try:
        sep = os.sep
        for i in __audio_list:
            name = i['fileName']
            art = i['artist']
            pathName = i['pathName'] 
            try:
                os.replace(pathName,os.path.join(path,art,name))
                log.pr(pathName + " ---> " + art,"o")
            except(Exception):
                try:
                    os.mkdir(path+sep+art)
                    log.pr("Создан каталог: " + os.path.join(path,art),"o")
                    os.replace(pathName,path + os.path.join(path,art,name))
                    log.pr(pathName + " ---> " + art,"o")
                except(Exception):
                    log.pr(pathName + "    -x->   " + art,"e")


        log.pr("Готово","o")
    except(Exception):
        log.pr("err 3","e")