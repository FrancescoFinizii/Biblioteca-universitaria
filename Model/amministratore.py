from Model.utente import Utente


class Amministratore(Utente):


    def __init__(self, nome, cognome, matricola, password, dataNascita, ruolo):
        super().__init__(nome, cognome, matricola, password, dataNascita)
        self.ruolo = ruolo


    def setRuolo(self, ruolo):
        self.ruolo = ruolo


    def getRuolo(self):
        return self.ruolo