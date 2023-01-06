from datetime import date
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi

from Controller.gestioneStudenti import GestioneStudenti
from View.Studente import studentDashboard


class ModificaDatiPersonali(QDialog):


    def __init__(self):
        super(ModificaDatiPersonali, self).__init__()
        loadUi("View/Studente/UI files/modifica studente.ui", self)
        self.modificaButton.clicked.connect(self.modificaDatiPersonali)
        self.annullaButton.clicked.connect(self.close)
        self.matricola.setText(studentDashboard.studente.getMatricola())
        self.nomeInput.setText(studentDashboard.studente.getNome())
        self.cognomeInput.setText(studentDashboard.studente.getCognome())
        self.dataNascitaInput.setDate(QDate(studentDashboard.studente.getDataNascita().year,
                                            studentDashboard.studente.getDataNascita().month,
                                            studentDashboard.studente.getDataNascita().day))

    def modificaDatiPersonali(self):
        if not(self.nomeInput.text().isspace()) and self.nomeInput.text() != "" and not(self.cognomeInput.text().isspace()) and self.cognomeInput.text() != "":
            if self.nomeInput.text().isalpha():
                if self.cognomeInput.text().isalpha():
                    GestioneStudenti.modificaUtente(nome=self.nomeInput.text(),
                                                    cognome=self.cognomeInput.text(),
                                                    matricola=studentDashboard.studente.getMatricola(),
                                                    password=studentDashboard.studente.getPassword(),
                                                    dataNascita=date(year=int(self.dataNascitaInput.date().toString("yyyy")),
                                                                     month=int(self.dataNascitaInput.date().toString("MM")),
                                                                     day=int(self.dataNascitaInput.date().toString("dd"))))
                    self.accept()
                else:
                    self.errorLabel.setText("Cognome non valido")
            else:
                self.errorLabel.setText("Nome non valido")
        else:
            self.errorLabel.setText("Non tutti i campi sono compilati")