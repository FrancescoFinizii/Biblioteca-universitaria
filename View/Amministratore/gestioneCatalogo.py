from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5.uic import loadUi

from Controller.gestioneLibri import GestioneLibri
from Controller.gestioneRiviste import GestioneRiviste
from View.Amministratore.aggiungiDocumento import AggiungiDocumento
from View.Amministratore.modificaLibro import ModificaLibro
from View.Amministratore.modificaRivista import ModificaRivista
from View.Amministratore.visualizzaLibro import VisualizzaLibro
from View.Amministratore.visualizzaRivista import VisualizzaRivista


class GestioneCatalogo(QWidget):


    def __init__(self):
        super(GestioneCatalogo, self).__init__()
        loadUi("View/Amministratore/UI files/gestione catalogo.ui", self)
        self.aggiungiDocumentoButton.clicked.connect(self.goToAggiungiDocumento)
        self.modificaDocumentoButton.clicked.connect(self.goToModificaDocumento)
        self.rimuoviDocumentoButton.clicked.connect(self.goToRimuoviDocumento)
        self.apriDocumentoButton.clicked.connect(self.goToVisualizzaDocumento)
        self.searchInput.returnPressed.connect(self.ricercaDocumenti)
        self.ordinamento.currentTextChanged.connect(self.ricercaDocumenti)
        self.cercaPer.currentTextChanged.connect(self.ricercaDocumenti)
        self.cercaIn.currentTextChanged.connect(self.ricercaDocumenti)
        self.checkBoxDisponibili.stateChanged.connect(self.ricercaDocumenti)
        self.tableWidget.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.ricercaDocumenti()


    def goToVisualizzaDocumento(self):
        if self.tableWidget.currentItem() != None:
            if self.tableWidget.item(self.tableWidget.currentRow(), 4).text() == "Libro":
                visualizzaLibro = VisualizzaLibro(GestioneLibri.getDocumento(self.tableWidget.item(self.tableWidget.currentRow(), 2).text()))
                visualizzaLibro.exec_()
            else:
                visualizzaRivista = VisualizzaRivista(GestioneRiviste.getDocumento(self.tableWidget.item(self.tableWidget.currentRow(), 2).text()))
                visualizzaRivista.exec_()


    def goToAggiungiDocumento(self):
        aggiungiDocumento = AggiungiDocumento()
        if aggiungiDocumento.exec_():
            self.ricercaDocumenti()


    def goToModificaDocumento(self):
        if self.tableWidget.currentItem() != None:
            if self.tableWidget.item(self.tableWidget.currentRow(), 4).text() == "Libro":
                modificaLibro = ModificaLibro(GestioneLibri.getDocumento(self.tableWidget.item(self.tableWidget.currentRow(), 2).text()))
                if modificaLibro.exec_():  # accepted
                    self.ricercaDocumenti()
            else:
                modificaRivista = ModificaRivista(GestioneRiviste.getDocumento(self.tableWidget.item(self.tableWidget.currentRow(), 2).text()))
                if modificaRivista.exec_():  # accepted
                    self.ricercaDocumenti()


    def goToRimuoviDocumento(self):
        if self.tableWidget.currentItem() != None:
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Question)
            msgBox.setWindowTitle("Rimuovere documento")
            msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            msgBox.setText("Sei sicuro di rimuovere il documento?")
            if msgBox.exec_() == QMessageBox.Yes:
                if GestioneLibri.getDocumento(self.tableWidget.item(self.tableWidget.currentRow(), 2).text()) != None:
                    GestioneLibri.rimuoviDocumento(self.tableWidget.item(self.tableWidget.currentRow(), 2).text())
                else:
                    GestioneRiviste.rimuoviDocumento(self.tableWidget.item(self.tableWidget.currentRow(), 2).text())
                self.ricercaDocumenti()


    def ricercaDocumenti(self):
        match self.cercaIn.currentText():
            case "Libri":
                if self.cercaPer.currentText() == "Titolo":
                    listaDocumenti = GestioneLibri.ricercaDocumentoPerTitolo(self.searchInput.text())
                else:
                    listaDocumenti = GestioneLibri.ricercaDocumentoPerAutore(self.searchInput.text())
            case "Riviste":
                if self.cercaPer.currentText() == "Titolo":
                    listaDocumenti = GestioneRiviste.ricercaDocumentoPerTitolo(self.searchInput.text())
                else:
                    listaDocumenti = GestioneRiviste.ricercaDocumentoPerAutore(self.searchInput.text())
            case "Tutto il catalogo":
                if self.cercaPer.currentText() == "Titolo":
                    listaDocumenti = GestioneLibri.ricercaDocumentoPerTitolo(self.searchInput.text()) + GestioneRiviste.ricercaDocumentoPerTitolo(self.searchInput.text())
                else:
                    listaDocumenti = GestioneLibri.ricercaDocumentoPerAutore(self.searchInput.text()) + GestioneRiviste.ricercaDocumentoPerAutore(self.searchInput.text())
        lista = []
        if self.checkBoxDisponibili.isChecked():
            for documento in listaDocumenti:
                if documento.getDisponibilita() > 0:
                    lista.append(documento)
        else:
            lista = listaDocumenti
        if self.ordinamento.currentText() == "Titolo A-Z":
            lista.sort(key=lambda d: d.getTitolo())
        else:
            lista.sort(key=lambda d: d.getTitolo(), reverse=True)
        row = 0
        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(len(lista))
        for documento in lista:
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(documento.getTitolo()))
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(documento.getAutore()))
            self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(documento.getID()))
            self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(str(documento.getDisponibilita())))
            self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(documento.__class__.__name__))
            row += 1
