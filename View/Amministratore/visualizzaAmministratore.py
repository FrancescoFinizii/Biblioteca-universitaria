from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi


class VisualizzaAmministratore(QDialog):

    def __init__(self, amministratore):
        super(VisualizzaAmministratore, self).__init__()
        loadUi("View/Amministratore/UI files/visualizza amministratore.ui", self)
        self.chiudiButton.clicked.connect(self.close)
        self.matricola.setText(amministratore.getMatricola())
        self.nome.setText(amministratore.getNome())
        self.cognome.setText(amministratore.getCognome())
        self.dataNascita.setText(amministratore.getDataNascita().strftime("%d/%m/%y"))
        self.ruolo.setText(amministratore.getRuolo())
