from sqlalchemy import *


class Worker:
    def __init__(self, name, surname, telegramchatid, isactive=1):
        self.name = name
        self.surname = surname
        self.telegramchatid = telegramchatid
        self.isactive = isactive

    def createWorker(self):
        print('User successfully created!')

    def getWorker(self):
        pass
