class Prestito:


    def __init__(self, codice, matricolaStudente, dataInizio, dataScadenza, documento):
        self.codice = codice
        self.matricolaStudente = matricolaStudente
        self.dataInizio = dataInizio
        self.dataScadenza = dataScadenza
        self.documento = documento
        self.prorogato = False


    #setter

    def setDataScadenza(self, dataScadenza):
        self.dataScadenza = dataScadenza


    def setProrogato(self, prorogato):
        self.prorogato = prorogato


    #getter

    def getCodice(self):
        return self.codice


    def getMatricolaStudente(self):
        return self.matricolaStudente


    def getDataInizio(self):
        return self.dataInizio


    def getDataScadenza(self):
        return self.dataScadenza


    def getDocumento(self):
        return self.documento


    def getProrogato(self):
        return self.prorogato