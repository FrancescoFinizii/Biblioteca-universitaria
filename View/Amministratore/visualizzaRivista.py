from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi


class VisualizzaRivista(QDialog):

    def __init__(self, rivista):
        super(VisualizzaRivista, self).__init__()
        loadUi("View/Amministratore/UI files/visualizza rivista.ui", self)
        self.chiudiButton.clicked.connect(self.close)
        self.titolo.setText(rivista.getTitolo())
        self.autore.setText(rivista.getAutore())
        self.editore.setText(rivista.getEditore())
        self.lingua.setText(rivista.getLingua())
        self.annoPubblicazione.setText(rivista.getAnnoPubblicazione())
        self.ISSN.setText(rivista.getID())
        self.volume.setText(rivista.getVolume())
        self.numero.setText(rivista.getNumero())
        self.quantita.setText(str(rivista.getDisponibilita()))
        self.descrizione.setText(rivista.getDescrizione())
