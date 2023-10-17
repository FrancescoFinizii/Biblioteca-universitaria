from Model.documento import Documento


class Rivista(Documento):

    def __init__(self, titolo, autore, editore, lingua, annoPubblicazione, disponibilita, descrizione, ISSN, volume, numero):
        super().__init__(titolo, autore, editore, lingua, annoPubblicazione, disponibilita, descrizione, ISSN)
        self.volume = volume
        self.numero = numero


    def setVolume(self, volume):
        self.volume = volume


    def setNumero(self, numero):
        self.numero = numero


    def getVolume(self):
        return self.volume


    def getNumero(self):
        return self.numero

