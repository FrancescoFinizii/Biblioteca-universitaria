from Model.documento import Documento


class Libro(Documento):


    def __init__(self, titolo, autore, editore, lingua, annoPubblicazione, disponibilita, descrizione, ISBN, genere):
        super().__init__(titolo, autore, editore, lingua, annoPubblicazione, disponibilita, descrizione, ISBN)
        self.genere = genere


    def setGenere(self, genere):
        self.genere = genere


    def getGenere(self):
        return self.genere