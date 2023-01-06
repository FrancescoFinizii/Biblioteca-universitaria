from Model.utente import Utente


class Studente(Utente):


    def __init__(self, nome, cognome, matricola, password, dataNascita):
        super().__init__(nome, cognome, matricola, password, dataNascita)
        self.sospeso = False

    #setter


    def setSospeso(self, sospeso):
        self.sospeso = sospeso


    #getter


    def getSospeso(self):
        return self.sospeso

