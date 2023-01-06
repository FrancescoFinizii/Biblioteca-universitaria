from datetime import date
from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5.uic import loadUi

from Controller.gestioneAmministratori import GestioneAmministratori
from Controller.gestioneStudenti import GestioneStudenti
from View.Amministratore.adminDashboard import AdminDashboard
from View.Studente.studentDashboard import StudentDashboard


class Login(QWidget):


    def __init__(self):
        super(Login, self).__init__()
        loadUi("View/UI files/singin.ui", self)
        self.loginButton.clicked.connect(self.autenticazione)
        self.creaAccountStudenteButton.clicked.connect(self.registrazioneStudente)
        self.creaAccountAmministratoreButton.clicked.connect(self.registrazioneAmministratore)
        self.accediButton.clicked.connect(self.goToLogin)
        self.accediButton_2.clicked.connect(self.goToLogin)
        self.registrazioneStudenteButton.clicked.connect(self.goToRegistrazioneStudente)
        self.registrazioneStudenteButton_2.clicked.connect(self.goToRegistrazioneStudente)
        self.registrazioneAmministratoreButton.clicked.connect(self.goToRegistrazioneAmministratore)
        self.registrazioneAmministratoreButton_2.clicked.connect(self.goToRegistrazioneAmministratore)


    def goToLogin(self):
        self.stackedWidget.setCurrentIndex(0)


    def goToRegistrazioneStudente(self):
        self.stackedWidget.setCurrentIndex(1)


    def goToRegistrazioneAmministratore(self):
        self.stackedWidget.setCurrentIndex(2)


    def autenticazione(self):
        if self.notEmpty(self.matricolaInput) and self.notEmpty(self.passwordInput):
            if self.matricolaInput.text().isdigit():
                if GestioneStudenti.getUtente(self.matricolaInput.text()) != None and GestioneStudenti.getUtente(self.matricolaInput.text()).getPassword()  == self.passwordInput.text():
                    self.errorLabel.setText("")
                    self.goToStudentDashboard(GestioneStudenti.getUtente(self.matricolaInput.text()))
                elif GestioneAmministratori.getUtente(self.matricolaInput.text()) != None and GestioneAmministratori.getUtente(self.matricolaInput.text()).getPassword()  == self.passwordInput.text():
                    self.errorLabel.setText("")
                    self.goToAdminDashboard(GestioneAmministratori.getUtente(self.matricolaInput.text()))
                else:
                    self.errorLabel.setText("Credenziali non valide")
            else:
                self.errorLabel.setText("Matricola non valida")
        else:
            self.errorLabel.setText("Non tutti i campi sono compilati")


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


    def registrazioneAmministratore(self):
        if self.notEmpty(self.nome_input_2) and self.notEmpty(self.cognome_input_2) and self.notEmpty(self.matricola_input_2) and self.notEmpty(self.password_input_2) and self.notEmpty(self.conferma_password_input_2) and self.notEmpty(self.codiceConferma_input):
            if self.nome_input_2.text().isalpha() and self.cognome_input_2.text().isalpha():
                if self.matricola_input_2.text().isdigit():
                    if self.password_input_2.text().isalnum and self.conferma_password_input_2.text().isalnum():
                        if len(self.password_input_2.text()) >= 8:
                            if self.password_input_2.text() == self.conferma_password_input_2.text():
                                if self.codiceConferma_input.text() == "1234":
                                    if GestioneAmministratori.getUtente(self.matricola_input_2.text()) == None:
                                        GestioneAmministratori.aggiungiUtente(nome=self.nome_input_2.text(),
                                                                              cognome=self.cognome_input_2.text(),
                                                                              matricola=self.matricola_input_2.text(),
                                                                              password=self.password_input_2.text(),
                                                                              dataNascita=date(year=int(self.dataDiNascitaInput_2.date().toString("yyyy")),
                                                                                               month=int(self.dataDiNascitaInput_2.date().toString("MM")),
                                                                                               day=int(self.dataDiNascitaInput_2.date().toString("dd"))),
                                                                              ruolo=self.ruolo_input.currentText())
                                        self.goToAdminDashboard(GestioneAmministratori.getUtente(self.matricola_input_2.text()))
                                    else:
                                        msgBox = QMessageBox()
                                        msgBox.setIcon(QMessageBox.Warning)
                                        msgBox.setStandardButtons(QMessageBox.Ok)
                                        msgBox.setWindowTitle("Errore")
                                        msgBox.setText("Registrazione amministratore fallita\nLa matricola inserita è associata a un'altro account")
                                        msgBox.exec_()
                                else:
                                    self.error_label_2.setText("Codice di sicurezza errato")
                            else:
                                self.error_label_2.setText("Le due password non corrispondono")
                        else:
                            self.error_label_2.setText("La password deve essere compresa tra gli 8 e i 32 caratteri")
                    else:
                        self.error_label_2.setText("La password può contenere solo caratteri alfanumerici")
                else:
                    self.error_label_2.setText("Matricola non valida")
            else:
                self.error_label_2.setText("Nome e/o cognome non validi")
        else:
            self.error_label_2.setText("Non tutti i campi sono compilati")


    @staticmethod
    def notEmpty(obj):
        if not(obj.text().isspace()) and obj.text() != "":
            return True
        else:
            return False


    def goToStudentDashboard(self, studente):
        self.close()
        self.studentDashboard = StudentDashboard(studente)
        self.studentDashboard.show()


    def goToAdminDashboard(self, amministratore):
        self.close()
        self.adminDashboard = AdminDashboard(amministratore)
        self.adminDashboard.show()
