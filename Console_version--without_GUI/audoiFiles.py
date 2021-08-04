import os, sys,eyed3

from logg import Log
from logging import getLogger


getLogger().setLevel('ERROR')


class AudoiFiles():

    __audio_list = []
    __log = Log()

    def scan(self,pathFrom, unknown = False):
        try:
            os.chdir(pathFrom)
        except:
            self.__log.pr("Err 1 (Ошибка пути)","e")
            sys.exit(1)
            
        files = os.listdir(pathFrom)
        self.__log.pr("Поиск файлов в " + pathFrom)
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
                            self.__audio_list.append(auFl) # добавляем его в массив
                            self.__log.pr(auFl['pathName']+"   ["+auFl['artist']+"]","o")
                        else:
                            if unknown:
                                auFl = {
                                    'artist':"Неизвестный исполнитель",
                                    'fileName':f,
                                    'pathName':fp
                                }
                                self.__audio_list.append(auFl)
                                self.__log.pr(auFl['pathName'] +"   ["+auFl['artist']+"]      !Артист не найден!","a")
                            else:
                                self.__log.pr(fp+"     !Артист не найден! Пропускаем!","a")
                    except:
                        self.__log.pr("Err 4 (Проблема с файлом) "+fp,"e")
            self.__log.pr("\nКоличество файлов: " + str(len(self.__audio_list))) 
        except:
            self.__log.pr("Err 2 ","e")
            sys.exit(1)
        if len(self.__audio_list) < 1:
            sys.exit(1)
            


    def sort(self,path):
        self.__log.pr("Создание каталогов и перемещение файлов...")
        try:
            os.chdir(path)
        except:
            self.__log.pr("Err 1 (Ошибка пути)","e")
            sys.exit(1)
        try:
            sep = os.sep
            for i in self.__audio_list:
                name = i['fileName']
                art = i['artist']
                pathName = i['pathName'] 
                try:
                    os.replace(pathName,os.path.join(path,art,name))
                    self.__log.pr(pathName + " ---> " + art,"o")
                except(Exception):
                    try:
                        os.mkdir(path+sep+art)
                        self.__log.pr("Создан каталог: " + os.path.join(path,art),"o")
                        os.replace(pathName,path + os.path.join(path,art,name))
                        self.__log.pr(pathName + " ---> " + art,"o")
                    except(Exception):
                        self.__log.pr(pathName + "    -x->   " + art,"e")


            self.__log.pr("Готово","o")
        except(Exception):
            self.__log.pr("err 3","e")