from datetime import date
from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5.uic import loadUi

from Controller.gestioneStudenti import GestioneStudenti
from View.Studente.studentDashboard import StudentDashboard


class RegistrazioneStudente(QWidget):


    def __init__(self, parent):
        super(RegistrazioneStudente, self).__init__(parent)
        loadUi("View/Generale/UI files/registrazione studente.ui", self)
        self.creaAccountStudenteButton.clicked.connect(self.registrazioneStudente)
        self.accediButton.clicked.connect(self.parent().goToLogin)
        self.registrazioneAmministratoreButton_2.clicked.connect(self.parent().goToRegistrazioneAmministratore)



    def registrazioneStudente(self):
        if self.notEmpty(self.nome_input) and self.notEmpty(self.cognome_input) and self.notEmpty(self.matricola_input) and self.notEmpty(self.password_input) and self.notEmpty(self.conferma_password_input):
            if self.nome_input.text().isalpha() and self.cognome_input.text().isalpha():
                if self.matricola_input.text().isdigit():
                    if self.password_input.text().isalnum and self.conferma_password_input.text().isalnum():
                        if len(self.password_input.text()) >= 8:
                            if self.password_input.text() == self.conferma_password_input.text():
                                if GestioneStudenti.getUtente(self.matricola_input.text()) == None:
                                    GestioneStudenti.aggiungiUtente(nome=self.nome_input.text(),
                                                                    cognome=self.cognome_input.text(),
                                                                    matricola=self.matricola_input.text(),
                                                                    password=self.password_input.text(),
                                                                    dataNascita=date(year=int(self.dataDiNascitaInput.date().toString("yyyy")),
                                                                                     month=int(self.dataDiNascitaInput.date().toString("MM")),
                                                                                     day=int(self.dataDiNascitaInput.date().toString("dd"))))
                                    self.goToStudentDashboard(GestioneStudenti.getUtente(self.matricola_input.text()))
                                else:

                                    msgBox = QMessageBox()
                                    msgBox.setIcon(QMessageBox.Warning)
                                    msgBox.setStandardButtons(QMessageBox.Ok)
                                    msgBox.setWindowTitle("Errore")
                                    msgBox.setText("Registrazione studente fallita\nLa matricola inserita è associata a un'altro account")
                                    msgBox.exec_()
                            else:
                                self.error_label.setText("Le due password non corrispondono")
                        else:
                            self.error_label.setText("La password deve essere compresa tra gli 8 e i 32 caratteri")
                    else:
                        self.error_label.setText("La password può contenere solo caratteri alfanumerici")
                else:
                    self.error_label.setText("Matricola non valida")
            else:
                self.error_label.setText("Nome e/o cognome non validi")
        else:
            self.error_label.setText("Non tutti i campi sono compilati")



    def goToStudentDashboard(self, studente):
        self.close()
        self.studentDashboard = StudentDashboard(studente)
        self.studentDashboard.show()


    @staticmethod
    def notEmpty(obj):
        if not(obj.text().isspace()) and obj.text() != "":
            return True
        else:
            return False
