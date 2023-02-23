from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi

class VisualizzaPrenotazione(QDialog):


    def __init__(self, prenotazione):
        super(VisualizzaPrenotazione, self).__init__()
        loadUi("View/Studente/UI files/visualizza prenotazione.ui", self)
        self.sede.setText(prenotazione.getSede())
        self.data.setText(prenotazione.getData().strftime("%d/%m/%y"))
        self.oraInizio.setText(prenotazione.getOraInizio().strftime("%H:%M"))
        self.oraFine.setText(prenotazione.getOraFine().strftime("%H:%M"))
        self.chiudiButton.clicked.connect(self.close)
