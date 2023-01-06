from PyQt5 import QtWidgets
from PyQt5.QtCore import QDate, pyqtSignal
from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5.uic import loadUi

from Controller.gestioneAmministratori import GestioneAmministratori
from Controller.gestioneStudenti import GestioneStudenti
from View.Amministratore import adminDashboard
from View.Amministratore.modificaDatiPersonali import ModificaDatiPersonali
from View.Amministratore.modificaPassword import ModificaPassword
from View.Amministratore.visualizzaAmministratore import VisualizzaAmministratore
from View.Amministratore.visualizzaStudente import VisualizzaStudente


class Profilo(QWidget):

    sigg = pyqtSignal()


    def __init__(self):
        super(Profilo, self).__init__()
        loadUi("View/Amministratore/UI files/profilo.ui", self)
        self.modificaProfiloButton.clicked.connect(self.modificaDatiAnagrafici)
        self.modificaPasswordButton.clicked.connect(self.modificaPassword)
        self.eliminaAccountButton.clicked.connect(self.eliminaAccount)
        self.visualizzaUtenteButton.clicked.connect(self.goToVisualizzaUtente)
        self.searchInput.returnPressed.connect(self.ricercaUtenti)
        self.cercaPer.currentTextChanged.connect(self.ricercaUtenti)
        self.cercaIn.currentTextChanged.connect(self.ricercaUtenti)
        self.tableWidget.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)

        self.matricola.setText(adminDashboard.amministratore.getMatricola())
        self.nome.setText(adminDashboard.amministratore.getNome())
        self.cognome.setText(adminDashboard.amministratore.getCognome())
        self.dataNascita.setDate(QDate(adminDashboard.amministratore.getDataNascita().year, adminDashboard.amministratore.getDataNascita().month, adminDashboard.amministratore.getDataNascita().day))
        self.ruolo.setText(adminDashboard.amministratore.getRuolo())


    def modificaDatiAnagrafici(self):
        self.modificaDatiPersonali = ModificaDatiPersonali()
        if self.modificaDatiPersonali.exec_():
            self.close()


    def modificaPassword(self):
        self.modificaPassword = ModificaPassword()
        if self.modificaPassword.exec_():
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


    def ricercaUtenti(self):
        if self.cercaIn.currentText() == "Studenti":
            if self.cercaPer.currentText() == "Matricola":
                listaUtenti = GestioneStudenti.ricercaUtenteMatricola(self.searchInput.text())
            else:
                listaUtenti = GestioneStudenti.ricercaUtenteNomeCognome(self.searchInput.text())
        elif self.cercaIn.currentText() == "Amministratori":
            if self.cercaPer.currentText() == "Matricola":
                listaUtenti = GestioneAmministratori.ricercaUtenteMatricola(self.searchInput.text())
            else:
                listaUtenti = GestioneAmministratori.ricercaUtenteNomeCognome(self.searchInput.text())
        else:
            if self.cercaPer.currentText() == "Matricola":
                listaUtenti = GestioneStudenti.ricercaUtenteMatricola(self.searchInput.text()) + GestioneAmministratori.ricercaUtenteMatricola(self.searchInput.text())
            else:
                listaUtenti = GestioneStudenti.ricercaUtenteNomeCognome(self.searchInput.text()) + GestioneAmministratori.ricercaUtenteNomeCognome(self.searchInput.text())
        row = 0
        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(len(listaUtenti))
        for utente in listaUtenti:
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(utente.getMatricola()))
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(utente.getNome()))
            self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(utente.getCognome()))
            self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(utente.__class__.__name__))
            row += 1


    def goToVisualizzaUtente(self):
        if self.tableWidget.currentItem() != None:
            if self.tableWidget.item(self.tableWidget.currentRow(), 3).text() == "Studente":
                self.visualizzaUtente = VisualizzaStudente(GestioneStudenti.getUtente(self.tableWidget.item(self.tableWidget.currentRow(), 0).text()))
            else:
                self.visualizzaUtente = VisualizzaAmministratore(GestioneAmministratori.getUtente(self.tableWidget.item(self.tableWidget.currentRow(), 0).text()))
            self.visualizzaUtente.show()


    def closeEvent(self, event):
        self.sigg.emit()


