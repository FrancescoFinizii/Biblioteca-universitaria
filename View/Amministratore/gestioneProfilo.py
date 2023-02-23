from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5.uic import loadUi

from Controller.gestioneAmministratori import GestioneAmministratori
from View.Amministratore import adminDashboard
from View.Amministratore.modificaDatiPersonali import ModificaDatiPersonali
from View.Amministratore.modificaPassword import ModificaPassword

class GestioneProfilo(QWidget):

    sigg = pyqtSignal()

    def __init__(self):
        super(GestioneProfilo, self).__init__()
        loadUi("View/Amministratore/UI files/gestione profilo.ui", self)
        self.modificaProfiloButton.clicked.connect(self.modificaDatiAnagrafici)
        self.modificaPasswordButton.clicked.connect(self.modificaPassword)
        self.eliminaAccountButton.clicked.connect(self.eliminaAccount)
        self.matricola.setText(adminDashboard.amministratore.getMatricola())
        self.nome.setText(adminDashboard.amministratore.getNome())
        self.cognome.setText(adminDashboard.amministratore.getCognome())
        self.dataNascita.setText(adminDashboard.amministratore.getDataNascita().strftime("%d/%m/%y"))
        self.ruolo.setText(adminDashboard.amministratore.getRuolo())


    def modificaDatiAnagrafici(self):
        modificaDatiPersonali = ModificaDatiPersonali()
        if modificaDatiPersonali.exec_():
            self.close()


    def modificaPassword(self):
        modificaPassword = ModificaPassword()
        if modificaPassword.exec_():
            self.close()


    def eliminaAccount(self):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Critical)
        msgBox.setWindowTitle("Cancellazione account")
        msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msgBox.setText("Sei sicuro di cancellare il tuo account?")
        if msgBox.exec_() == QMessageBox.Yes:
            GestioneAmministratori.rimuoviUtente(adminDashboard.amministratore.getMatricola())
            adminDashboard.amministratore = None
            self.close()


    def closeEvent(self, event):
        self.sigg.emit()
