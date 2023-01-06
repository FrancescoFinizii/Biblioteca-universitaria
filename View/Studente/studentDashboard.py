import os
import sys

from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi

from Controller.gestioneStudenti import GestioneStudenti
from View.Studente.catalogoUtente import CatalogoUtente
from View.Studente.prenotazione import Prenotazione
from View.Studente.profilo import Profilo


class StudentDashboard(QMainWindow):

    studente = None

    def __init__(self, utente):
        super(StudentDashboard, self).__init__()
        loadUi("View/Studente/UI files/dashboard.ui", self)
        global studente
        studente = utente
        self.homeButton.clicked.connect(self.goToHomePage)
        self.catalogoButton.clicked.connect(self.goToCatalogoPage)
        self.prenotazioniButton.clicked.connect(self.goToPrenotazioniPage)
        self.profiloButton.clicked.connect(self.goToProfiloPage)
        self.logoutButton.clicked.connect(self.logout)
        self.exitButton.clicked.connect(self.close)


    def goToHomePage(self):
        self.stackedWidget.setCurrentIndex(0)


    def goToCatalogoPage(self):
        catalogo = CatalogoUtente()
        self.stackedWidget.insertWidget(1, catalogo)
        self.stackedWidget.setCurrentIndex(1)


    def goToPrenotazioniPage(self):
        prenotazione = Prenotazione()
        self.stackedWidget.insertWidget(2, prenotazione)
        self.stackedWidget.setCurrentIndex(2)


    def goToProfiloPage(self):
        global studente
        if studente == None:
            self.logout()
        studente = GestioneStudenti.getUtente(studente.getMatricola())
        self.profilo = Profilo()
        self.profilo.sig.connect(self.goToProfiloPage)
        self.stackedWidget.insertWidget(3, self.profilo)
        self.stackedWidget.setCurrentIndex(3)


    def logout(self):
        self.close()
        os.execl(sys.executable, sys.executable, *sys.argv)

