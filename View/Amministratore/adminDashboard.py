import os
import sys

from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi

from Controller.gestioneAmministratori import GestioneAmministratori
from View.Amministratore.catalogo import Catalogo
from View.Amministratore.prenotazioni import Prenotazioni
from View.Amministratore.prestiti import Prestiti
from View.Amministratore.profilo import Profilo


class AdminDashboard(QMainWindow):

    amministratore = None

    def __init__(self, utente):
        super(AdminDashboard, self).__init__()
        loadUi("View/Amministratore/UI files/dashboard.ui", self)
        global amministratore
        amministratore = utente
        self.homeButton.clicked.connect(self.goToHome)
        self.catalogoButton.clicked.connect(self.goToCatalogo)
        self.profiloButton.clicked.connect(self.goToProfiloPage)
        self.prestitiButton.clicked.connect(self.goToPrestiti)
        self.prenotazioniButton.clicked.connect(self.goToPrenotazioni)
        self.logoutButton.clicked.connect(self.logout)
        self.exitButton.clicked.connect(self.close)


    def goToHome(self):
        self.stackedWidget.setCurrentIndex(0)


    def goToCatalogo(self):
        catalogo = Catalogo()
        self.stackedWidget.insertWidget(1, catalogo)
        self.stackedWidget.setCurrentIndex(1)


    def goToPrestiti(self):
        prestiti = Prestiti()
        self.stackedWidget.insertWidget(2, prestiti)
        self.stackedWidget.setCurrentIndex(2)


    def goToPrenotazioni(self):
        prenotazioni = Prenotazioni()
        self.stackedWidget.insertWidget(3, prenotazioni)
        self.stackedWidget.setCurrentIndex(3)


    def goToProfiloPage(self):
        global amministratore
        if amministratore == None:
            self.logout()
        amministratore = GestioneAmministratori.getUtente(amministratore.getMatricola())
        self.profilo = Profilo()
        self.profilo.sigg.connect(self.goToProfiloPage)
        self.stackedWidget.insertWidget(4, self.profilo)
        self.stackedWidget.setCurrentIndex(4)


    def logout(self):
        self.close()
        os.execl(sys.executable, sys.executable, *sys.argv)