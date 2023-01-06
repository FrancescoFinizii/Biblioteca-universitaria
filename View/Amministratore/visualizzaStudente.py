from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi


class VisualizzaStudente(QDialog):

    def __init__(self, studente):
        super(VisualizzaStudente, self).__init__()
        loadUi("View/Amministratore/UI files/visualizza studente.ui", self)
        self.chiudiButton.clicked.connect(self.close)
        self.matricola.setText(studente.getMatricola())
        self.nome.setText(studente.getNome())
        self.cognome.setText(studente.getCognome())
        self.dataNascita.setText(studente.getDataNascita().strftime("%d/%m/%y"))
        if studente.getSospeso() == True:
            self.stato.setText("Account sospeso")
        else:
            self.stato.setText("Account attivo")


