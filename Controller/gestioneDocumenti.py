from abc import abstractmethod


class GestioneDocumenti():


    @abstractmethod
    def aggiungiDocumento(self):
        pass


    @abstractmethod
    def modificaDocumento(self):
        pass


    @abstractmethod
    def rimuoviDocumento(self, ID):
        pass


    @abstractmethod
    def incrementaQuantita(self, ID):
        pass


    @abstractmethod
    def decrementaQuantita(self, ID):
        pass


    @abstractmethod
    def getDocumento(self, ID):
        pass


    @abstractmethod
    def ricercaDocumentoPerTitolo(self, titolo):
        pass


    @abstractmethod
    def ricercaDocumentoPerAutore(self, autore):
        pass



