from abc import abstractmethod


class GestioneUtenti:

    @abstractmethod
    def aggiungiUtente(self):
        pass


    @abstractmethod
    def modificaUtente(self):
        pass


    @abstractmethod
    def rimuoviUtente(self, matricola):
        pass


    @abstractmethod
    def getUtente(self, matricola):
        pass



    @abstractmethod
    def ricercaUtenteMatricola(self, matricola):
        pass


    @abstractmethod
    def ricercaUtenteNomeCognome(self, nomeCognome):
        pass


