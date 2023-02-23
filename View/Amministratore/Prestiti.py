from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5.uic import loadUi


from Controller.gestionePrestiti import GestionePrestiti

class Prestiti(QWidget):


    def __init__(self):
        super(Prestiti, self).__init__()
        loadUi("View/Amministratore/UI files/gestione prestiti.ui", self)
        self.concludiPrestitoButton.clicked.connect(self.terminaPrestito)
        self.searchInput.returnPressed.connect(self.ricercaPrestiti)
        self.cercaPer.currentTextChanged.connect(self.ricercaPrestiti)
        self.tableWidget.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.ricercaPrestiti()


    def ricercaPrestiti(self):
        if self.cercaPer.currentText() == "Codice":
            listaPrestiti = GestionePrestiti.ricercaPrestitoPerCodice(self.searchInput.text())
        else:
            listaPrestiti = GestionePrestiti.ricercaPrestitoPerMatricola(self.searchInput.text())
        row = 0
        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(len(listaPrestiti))
        for prestito in listaPrestiti:
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(prestito.getCodice()))
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(prestito.getMatricolaStudente()))
            self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(prestito.getDocumento().getID()))
            self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(prestito.getDataScadenza().strftime("%d/%m/%Y")))
            row += 1


    def terminaPrestito(self):
        if self.tableWidget.currentItem() != None:
            GestionePrestiti.rimuoviPrestito(self.tableWidget.item(self.tableWidget.currentRow(), 0).text())
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setDefaultButton(QMessageBox.Ok)
            msgBox.setText("Prestito terminato con successo")
            msgBox.exec()
        self.ricercaPrestiti()
