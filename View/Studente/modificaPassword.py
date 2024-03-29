from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi

from Controller.gestioneStudenti import GestioneStudenti
from View.Studente import studentDashboard


class ModificaPassword(QDialog):


    def __init__(self):
        super(ModificaPassword, self).__init__()
        loadUi("View/Amministratore/UI files/cambia password.ui", self)
        self.modificaButton.clicked.connect(self.modificaPassword)
        self.annullaButton.clicked.connect(self.close)


    def modificaPassword(self):
        if not(self.password.text().isspace()) and self.password.text() != "" and not(self.nuovaPassword.text().isspace()) and self.nuovaPassword.text() != "" and not(self.confermaNuovaPassword.text().isspace()) and self.confermaNuovaPassword.text() != "":
            if self.nuovaPassword.text().isalnum and self.confermaNuovaPassword.text().isalnum():
                if 8 <= len(self.nuovaPassword.text()) <= 32:
                    if self.nuovaPassword.text() == self.confermaNuovaPassword.text():
                        if self.password.text() == studentDashboard.studente.getPassword():
                            GestioneStudenti.modificaUtente(nome=studentDashboard.studente.getNome(),
                                                            cognome=studentDashboard.studente.getCognome(),
                                                            matricola=studentDashboard.studente.getMatricola(),
                                                            password=self.nuovaPassword.text(),
                                                            dataNascita=studentDashboard.studente.getDataNascita())
                            self.accept()
                        else:
                            self.errorLabel.setText("Impossibile cambiare password")
                    else:
                        self.errorLabel.setText("Le due password non corrispondono")
                else:
                    self.errorLabel.setText("La password deve essere compresa tra gli 8 e i 32 caratteri")
            else:
                self.erroLabel.setText("La password può contenere solo caratteri alfanumerici")
        else:
            self.errorLabel.setText("Non tutti i campi sono compilati")
