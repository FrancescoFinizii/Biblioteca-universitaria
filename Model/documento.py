class Documento:


    def __init__(self, titolo, autore, editore, lingua, annoPubblicazione, disponibilita, descrizione, ID):
        self.titolo = titolo
        self.autore = autore
        self.editore = editore
        self.lingua = lingua
        self.annoPubblicazione = annoPubblicazione
        self.disponibilita = disponibilita
        self.descrizione = descrizione
        self.ID = ID


    #setter

    def setTitolo(self, titolo):
        self.titolo = titolo


    def setAutore(self, autore):
        self.autore = autore


    def setEditore(self, editore):
        self.editore = editore


    def setLingua(self, lingua):
        self.lingua = lingua


    def setAnnoPubblicazione(self, annoPubblicazione):
        self.annoPubblicazione = annoPubblicazione


    def setDisponibilita(self, disponibilita):
        self.disponibilita = disponibilita


    def setDescrizione(self, descrizione):
        self.descrizione = descrizione



    #getter


    def getTitolo(self):
        return self.titolo


    def getAutore(self):
        return self.autore


    def getEditore(self):
        return self.editore


    def getLingua(self):
        return self.lingua


    def getAnnoPubblicazione(self):
        return self.annoPubblicazione


    def getDisponibilita(self):
        return self.disponibilita


    def getDescrizione(self):
        return self.descrizione


    def getID(self):
        return self.ID



