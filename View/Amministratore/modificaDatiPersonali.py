from datetime import date

from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi

from Controller.gestioneAmministratori import GestioneAmministratori
from View.Amministratore import adminDashboard


class ModificaDatiPersonali(QDialog):


    def __init__(self):
        super(ModificaDatiPersonali, self).__init__()
        loadUi("View/Amministratore/UI files/modifica amministratore.ui", self)
        self.modificaButton.clicked.connect(self.modificaDatiPersonali)
        self.annullaButton.clicked.connect(self.close)
        self.matricola.setText(adminDashboard.amministratore.getMatricola())
        self.nomeInput.setText(adminDashboard.amministratore.getNome())
        self.cognomeInput.setText(adminDashboard.amministratore.getCognome())
        self.dataNascitaInput.setDate(QDate(adminDashboard.amministratore.getDataNascita().year,
                                            adminDashboard.amministratore.getDataNascita().month,
                                            adminDashboard.amministratore.getDataNascita().day))
        self.ruoloInput.setCurrentText(adminDashboard.amministratore.getRuolo())


    def modificaDatiPersonali(self):
        if not(self.nomeInput.text().isspace()) and self.nomeInput.text() != "" and not(self.cognomeInput.text().isspace()) and self.cognomeInput.text() != "":
            if self.nomeInput.text().isalpha():
                if self.cognomeInput.text().isalpha():
                    GestioneAmministratori.modificaUtente(nome=self.nomeInput.text(),
                                                          cognome=self.cognomeInput.text(),
                                                          matricola=self.matricola.text(),
                                                          password=adminDashboard.amministratore.getPassword(),
                                                          dataNascita=date(year=int(self.dataNascitaInput.date().toString("yyyy")),
                                                                           month=int(self.dataNascitaInput.date().toString("MM")),
                                                                           day=int(self.dataNascitaInput.date().toString("dd"))),
                                                          ruolo=self.ruoloInput.currentText())
                    self.accept()
                else:
                    self.errorLabel.setText("Cognome non valido")
            else:
                self.errorLabel.setText("Nome non valido")
        else:
            self.errorLabel.setText("Non tutti i campi sono compilati")