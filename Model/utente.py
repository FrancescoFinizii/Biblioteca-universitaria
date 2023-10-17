class Utente:


    def __init__(self, nome, cognome, matricola, password, dataNascita):
        self.nome = nome
        self.cognome = cognome
        self.matricola = matricola
        self.password = password
        self.dataNascita = dataNascita


    #setter

    def setNome(self, nome):
        self.nome = nome


    def setCognome(self, cognome):
        self.cognome = cognome


    def setPassword(self, password):
        self.password = password


    def setDataNascita(self, dataNascita):
        self.dataNascita = dataNascita



    #getter


    def getNome(self):
        return self.nome


    def getCognome(self):
        return self.cognome


    def getMatricola(self):
        return self.matricola


    def getPassword(self):
        return self.password


    def getDataNascita(self):
        return self.dataNascita