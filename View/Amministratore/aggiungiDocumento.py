from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi

from View.Amministratore.aggiungiLibro import AggiungiLibro
from View.Amministratore.aggiungiRivista import AggiungiRivista


class AggiungiDocumento(QDialog):

    def __init__(self):
        super(AggiungiDocumento, self).__init__()
        loadUi("View/Amministratore/UI files/aggiungi documento.ui", self)
        self.confermaButton.clicked.connect(self.goToNextPage)
        self.annullaButton.clicked.connect(self.close)

    def goToNextPage(self):
        if self.tipologiaDocumento.currentText() == "Libro":
            self.aggiungiLibro = AggiungiLibro()
            if self.aggiungiLibro.exec_():
                self.accept()
        elif self.tipologiaDocumento.currentText() == "Rivista":
            self.aggiungiRivista = AggiungiRivista()
            if self.aggiungiRivista.exec_():
                self.accept()