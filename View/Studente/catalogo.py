from datetime import timedelta, date

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5.uic import loadUi

from Controller.gestioneLibri import GestioneLibri
from Controller.gestionePrestiti import GestionePrestiti
from Controller.gestioneRiviste import GestioneRiviste
from View.Amministratore.visualizzaLibro import VisualizzaLibro
from View.Amministratore.visualizzaRivista import VisualizzaRivista
from View.Studente import studentDashboard


class Catalogo(QWidget):

    def __init__(self):
        super(Catalogo, self).__init__()
        loadUi("View/Studente/UI files/catalogo.ui", self)
        self.searchInput.returnPressed.connect(self.ricercaDocumenti)
        self.prenotaDocumentoButton.clicked.connect(self.prenotaDocumento)
        self.visualizzaDocumentoButton.clicked.connect(self.goToVisualizzaDocumento)
        self.ordinamento.currentTextChanged.connect(self.ricercaDocumenti)
        self.cercaPer.currentTextChanged.connect(self.ricercaDocumenti)
        self.cercaIn.currentTextChanged.connect(self.ricercaDocumenti)
        self.checkBoxDisponibili.stateChanged.connect(self.ricercaDocumenti)
        self.tableWidget.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
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


    def goToVisualizzaDocumento(self):
        if self.tableWidget.currentItem() != None:
            if self.tableWidget.item(self.tableWidget.currentRow(), 4).text() == "Libro":
                visualizzaLibro = VisualizzaLibro(GestioneLibri.getDocumento(self.tableWidget.item(self.tableWidget.currentRow(), 2).text()))
                visualizzaLibro.exec_()
            else:
                visualizzaRivista = VisualizzaRivista(GestioneRiviste.getDocumento(self.tableWidget.item(self.tableWidget.currentRow(), 2).text()))
                visualizzaRivista.exec_()


    def prenotaDocumento(self):
        if self.tableWidget.currentItem() != None:
            if len(GestionePrestiti.ricercaPrestitoPerMatricola(studentDashboard.studente.getMatricola())) < 2:
                if int(self.tableWidget.item(self.tableWidget.currentRow(), 3).text()) >0:
                    if len(GestionePrestiti.ricercaPrestitoPerMatricola(studentDashboard.studente.getMatricola())) == 1 and \
                            GestionePrestiti.ricercaPrestitoPerMatricola(studentDashboard.studente.getMatricola())[0].getDocumento().getID() == self.tableWidget.item(self.tableWidget.currentRow(), 2).text():
                        msgBox = QMessageBox(QMessageBox.Warning, "Prestito non effettuato",
                                             "Prestito non possibile.\nHai già prenotato il seguente documento")
                        msgBox.exec()
                    else:
                        msgBox = QMessageBox(QMessageBox.Question, "Conferma Prestito",
                                             "Confermare il prestito", QMessageBox.Yes | QMessageBox.No)
                        if msgBox.exec_() == QMessageBox.Yes:
                            inizio = date.today()
                            inizio = inizio + timedelta(days= 7-inizio.weekday() if inizio.weekday()>4 else 1)
                            if self.tableWidget.item(self.tableWidget.currentRow(), 4).text() == "Libro":
                                GestionePrestiti.aggiungiPrestito(matricolaStudente=studentDashboard.studente.getMatricola(),
                                                                  dataInizio=inizio,
                                                                  documento=GestioneLibri.getDocumento(self.tableWidget.item(self.tableWidget.currentRow(), 2).text()))
                            else:
                                GestionePrestiti.aggiungiPrestito(matricolaStudente=studentDashboard.studente.getMatricola(),
                                                                  dataInizio=inizio,
                                                                  documento=GestioneRiviste.getDocumento(self.tableWidget.item(self.tableWidget.currentRow(), 2).text()))
                            msgBox = QMessageBox(QMessageBox.Information, "Conferma Prestito", "Prestito effettuato", QMessageBox.Ok)
                            msgBox.exec()
                            self.ricercaDocumenti()
                else:
                    msgBox = QMessageBox(QMessageBox.Warning, "Prestito non effettuato",
                                         "Prestito non disponibile.\nIl documento selezionato non è disponibile")
                    msgBox.exec()
            else:
                msgBox = QMessageBox(QMessageBox.Warning, "Prestito non effettuato",
                                     "Limite prestiti raggiunto.\nImpossibile prenotare il seguente documento")
                msgBox.exec()
