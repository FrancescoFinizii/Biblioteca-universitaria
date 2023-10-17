class Prenotazione:


    def __init__(self, matricolaStudente, sede, data, oraInizio, oraFine):
        self.matricolaStudente = matricolaStudente
        self.sede = sede
        self.data = data
        self.oraInizio = oraInizio
        self.oraFine = oraFine


    #getter


    def getSede(self):
        return self.sede


    def getMatricolaStudente(self):
        return self.matricolaStudente


    def getData(self):
        return self.data


    def getOraInizio(self):
        return self.oraInizio


    def getOraFine(self):
        return self.oraFine
