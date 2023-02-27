from PyQt5.QtWidgets import QWidget
from PyQt5.uic import loadUi

from Controller.gestioneAmministratori import GestioneAmministratori
from Controller.gestioneStudenti import GestioneStudenti
from View.Amministratore.adminDashboard import AdminDashboard
from View.Generale.registrazioneAmministratore import RegistrazioneAmministratore
from View.Generale.registrazioneStudente import RegistrazioneStudente
from View.Studente.studentDashboard import StudentDashboard



class Login(QWidget):


    def __init__(self):
        super(Login, self).__init__()
        loadUi("View/Generale/UI files/singin.ui", self)
        self.loginButton.clicked.connect(self.autenticazione)
        self.registrazioneStudenteButton.clicked.connect(self.goToRegistrazioneStudente)
        self.registrazioneAmministratoreButton.clicked.connect(self.goToRegistrazioneAmministratore)
        registrazioneStudente = RegistrazioneStudente(self)
        self.stackedWidget.insertWidget(1, registrazioneStudente)
        registrazioneAmministratore = RegistrazioneAmministratore(self)
        self.stackedWidget.insertWidget(2, registrazioneAmministratore)



    def goToLogin(self):
        self.stackedWidget.setCurrentIndex(0)


    def goToRegistrazioneStudente(self):
        self.stackedWidget.setCurrentIndex(1)


    def goToRegistrazioneAmministratore(self):
        self.stackedWidget.setCurrentIndex(2)



    def autenticazione(self):
        if self.notEmpty(self.matricolaInput, self.passwordInput):
            if self.matricolaInput.text().isdigit():
                if GestioneStudenti.getUtente(self.matricolaInput.text()) != None and GestioneStudenti.getUtente(self.matricolaInput.text()).getPassword()  == self.passwordInput.text():
                    if GestioneStudenti.getUtente(self.matricolaInput.text()).getSospeso():
                        self.errorLabel.setText("Account sospeso")
                    else:
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


    def goToStudentDashboard(self, studente):
        self.close()
        self.studentDashboard = StudentDashboard(studente)
        self.studentDashboard.show()


    def goToAdminDashboard(self, amministratore):
        self.close()
        self.adminDashboard = AdminDashboard(amministratore)
        self.adminDashboard.show()



    def notEmpty(self, *obj):
        notEmptyy = True
        for elem in obj:
            if elem.text().isspace() or elem.text() == "":
                notEmptyy = False
        return notEmptyy

