from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi

from Controller.gestioneLibri import GestioneLibri
from Controller.gestioneRiviste import GestioneRiviste
from View.Amministratore.visualizzaLibro import VisualizzaLibro
from View.Amministratore.visualizzaRivista import VisualizzaRivista


class VisualizzaPrestito(QDialog):

    def __init__(self, prestito):
        super(VisualizzaPrestito, self).__init__()
        loadUi("View/Studente/UI files/visualizza prestito.ui", self)
        self.codice.setText(prestito.getCodice())
        self.matricola.setText(prestito.getMatricolaStudente())
        self.dataInizio.setText(prestito.getDataInizio().strftime("%d/%m/%Y"))
        self.dataScadenza.setText(prestito.getDataScadenza().strftime("%d/%m/%Y"))
        self.documento.setText(prestito.getDocumento().getID())
        self.chiudiButton.clicked.connect(self.close)
        self.visualizzaDocumentoButton.clicked.connect(self.visualizzaDocumento)


    def visualizzaDocumento(self):
        if GestioneLibri.getDocumento(self.documento.text()) != None:
            self.visualizzaLibro = VisualizzaLibro(GestioneLibri.getDocumento(self.documento.text()))
            self.visualizzaLibro.show()
        else:
            self.visualizzaRivista = VisualizzaRivista(GestioneRiviste.getDocumento(self.documento.text()))
            self.visualizzaRivista.show()
