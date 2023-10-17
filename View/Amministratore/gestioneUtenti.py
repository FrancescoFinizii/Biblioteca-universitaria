from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget
from PyQt5.uic import loadUi

from Controller.gestioneAmministratori import GestioneAmministratori
from Controller.gestioneStudenti import GestioneStudenti
from View.Amministratore.visualizzaAmministratore import VisualizzaAmministratore
from View.Amministratore.visualizzaStudente import VisualizzaStudente


class GestioneUtenti(QWidget):


    def __init__(self):
        super(GestioneUtenti, self).__init__()
        loadUi("View/Amministratore/UI files/gestione utenti.ui", self)
        self.visualizzaUtenteButton.clicked.connect(self.goToVisualizzaUtente)
        self.searchInput.returnPressed.connect(self.ricercaUtenti)
        self.cercaPer.currentTextChanged.connect(self.ricercaUtenti)
        self.cercaIn.currentTextChanged.connect(self.ricercaUtenti)
        self.tableWidget.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.ricercaUtenti()


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
                visualizzaUtente = VisualizzaStudente(GestioneStudenti.getUtente(self.tableWidget.item(self.tableWidget.currentRow(), 0).text()))
            else:
                visualizzaUtente = VisualizzaAmministratore(GestioneAmministratori.getUtente(self.tableWidget.item(self.tableWidget.currentRow(), 0).text()))
            visualizzaUtente.exec_()
