from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QHeaderView
from PyQt5.uic import loadUi

from Controller.gestionePrenotazioni import GestionePrenotazioni


class Prenotazioni(QWidget):


    def __init__(self):
        super(Prenotazioni, self).__init__()
        loadUi("View/Amministratore/UI files/gestione prenotazioni.ui", self)
        self.searchInput.returnPressed.connect(self.ricercaPrenotazioni)
        self.sedeInput.currentTextChanged.connect(self.ricercaPrenotazioni)
        self.ordineData.currentTextChanged.connect(self.ricercaPrenotazioni)
        self.tableWidget.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.ricercaPrenotazioni()


    def ricercaPrenotazioni(self):
        listaPrenotazioni = GestionePrenotazioni.ricercaPrenotazione(self.searchInput.text(), self.sedeInput.currentText())
        if self.ordineData.currentText() == "Crescente":
            listaPrenotazioni = sorted(listaPrenotazioni, key=lambda d: (d.getData(), d.getOraInizio()))
        else:
            listaPrenotazioni = sorted(listaPrenotazioni, key=lambda d: (d.getData(), d.getOraInizio()), reverse=True)
        row = 0
        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(len(listaPrenotazioni))
        for prenotazione in listaPrenotazioni:
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(prenotazione.getMatricolaStudente()))
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(prenotazione.getData().strftime("%d/%m/%Y")))
            self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(prenotazione.getOraInizio().strftime("%H:%M")))
            self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(prenotazione.getOraFine().strftime("%H:%M")))
            self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(prenotazione.getSede()))
            row += 1
