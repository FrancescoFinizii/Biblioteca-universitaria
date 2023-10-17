import os
import sys

from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi

from Controller.gestioneAmministratori import GestioneAmministratori
from View.Amministratore.gestioneCatalogo import GestioneCatalogo
from View.Amministratore.Prenotazioni import Prenotazioni
from View.Amministratore.Prestiti import Prestiti
from View.Amministratore.gestioneProfilo import GestioneProfilo
from View.Amministratore.gestioneUtenti import GestioneUtenti



class AdminDashboard(QMainWindow):

    amministratore = None

    def __init__(self, utente):
        super(AdminDashboard, self).__init__()
        loadUi("View/Amministratore/UI files/dashboard.ui", self)
        global amministratore
        amministratore = utente
        self.homeButton.clicked.connect(self.goToHome)
        self.link.clicked.connect(lambda: open("https://github.com/FrancescoFinizii/Biblioteca-universitaria.git"))
        self.catalogoButton.clicked.connect(self.goToCatalogo)
        self.gestioneUteniButton.clicked.connect(self.goToGestioneUteni)
        self.profiloButton.clicked.connect(self.goToProfiloPage)
        self.prestitiButton.clicked.connect(self.goToPrestiti)
        self.prenotazioniButton.clicked.connect(self.goToPrenotazioni)
        self.logoutButton.clicked.connect(self.logout)
        self.exitButton.clicked.connect(self.close)


    def goToHome(self):
        self.stackedWidget.setCurrentIndex(0)


    def goToCatalogo(self):
        catalogo = GestioneCatalogo()
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


    def goToGestioneUteni(self):
        utenti = GestioneUtenti()
        self.stackedWidget.insertWidget(4, utenti)
        self.stackedWidget.setCurrentIndex(4)


    def goToProfiloPage(self):
        global amministratore
        if amministratore == None:
            self.logout()
        amministratore = GestioneAmministratori.getUtente(amministratore.getMatricola())
        self.profilo = GestioneProfilo()
        self.profilo.sigg.connect(self.goToProfiloPage)
        self.stackedWidget.insertWidget(5, self.profilo)
        self.stackedWidget.setCurrentIndex(5)


    def logout(self):
        self.close()
        os.execl(sys.executable, sys.executable, *sys.argv)