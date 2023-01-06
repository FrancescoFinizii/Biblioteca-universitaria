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


class CatalogoUtente(QWidget):

    def __init__(self):
        super(CatalogoUtente, self).__init__()
        loadUi("View/Studente/UI files/catalogo utente.ui", self)
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
        if self.checkBoxDisponibili.isChecked():
            for documento in listaDocumenti:
                if documento.getDisponibilita() < 1:
                    del documento
        if self.ordinamento.currentText() == "Titolo A-Z":
            listaDocumenti.sort(key=lambda d: d.getTitolo())
        else:
            listaDocumenti.sort(key=lambda d: d.getTitolo(), reverse=True)
        row = 0
        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(len(listaDocumenti))
        for documento in listaDocumenti:
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(documento.getTitolo()))
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(documento.getAutore()))
            self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(documento.getID()))
            self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(str(documento.getDisponibilita())))
            self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(documento.__class__.__name__))
            row += 1


    def goToVisualizzaDocumento(self):
        if self.tableWidget.currentItem() != None:
            if self.tableWidget.item(self.tableWidget.currentRow(), 4).text() == "Libro":
                self.visualizzaLibro = VisualizzaLibro(GestioneLibri.getDocumento(self.tableWidget.item(self.tableWidget.currentRow(), 2).text()))
                self.visualizzaLibro.show()
            else:
                self.visualizzaRivista = VisualizzaRivista(GestioneRiviste.getDocumento(self.tableWidget.item(self.tableWidget.currentRow(), 2).text()))
                self.visualizzaRivista.show()


    def prenotaDocumento(self):
        if self.tableWidget.currentItem() != None:
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.setWindowTitle("Prestito non effettuato")
            if len(GestionePrestiti.ricercaPrestitoPerMatricola(studentDashboard.studente.getMatricola())) < 2:
                if int(self.tableWidget.item(self.tableWidget.currentRow(), 3).text()) >0:
                    if len(GestionePrestiti.ricercaPrestitoPerMatricola(studentDashboard.studente.getMatricola())) == 1 and \
                            GestionePrestiti.ricercaPrestitoPerMatricola(studentDashboard.studente.getMatricola())[0].getDocumento().getID() == self.tableWidget.item(self.tableWidget.currentRow(), 2).text():
                        msgBox.setText("Prestito non possibile.\nHai già prenotato il seguente documento")
                        msgBox.exec()
                    else:
                        msgBox.setIcon(QMessageBox.Question)
                        msgBox.setWindowTitle("Conferma Prestito")
                        msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
                        msgBox.setText("Confermare il prestito")
                        if msgBox.exec_() == QMessageBox.Yes:
                            inizio = date.today()
                            inizio = inizio + timedelta(days= 7-inizio.weekday() if inizio.weekday()>4 else 1)
                            if self.tableWidget.item(self.tableWidget.currentRow(), 4).text() == "Libro":
                                GestioneLibri.decrementaQuantita(self.tableWidget.item(self.tableWidget.currentRow(), 2).text())
                                GestionePrestiti.aggiungiPrestito(matricolaStudente=studentDashboard.studente.getMatricola(),
                                                                  dataInizio=inizio,
                                                                  documento=GestioneLibri.getDocumento(self.tableWidget.item(self.tableWidget.currentRow(), 2).text()))

                            else:
                                GestioneRiviste.decrementaQuantita(self.tableWidget.item(self.tableWidget.currentRow(), 2).text())
                                GestionePrestiti.aggiungiPrestito(matricolaStudente=studentDashboard.studente.getMatricola(),
                                                                  dataInizio=inizio,
                                                                  documento=GestioneRiviste.getDocumento(self.tableWidget.item(self.tableWidget.currentRow(), 2).text()))
                            msgBox.setIcon(QMessageBox.Information)
                            msgBox.setStandardButtons(QMessageBox.Ok)
                            msgBox.setText("Prestito effettuato")
                            msgBox.exec()
                            self.ricercaDocumenti()
                else:
                    msgBox.setText("Prestito non disponibile.\nIl documento selezionato non è disponibile")
                    msgBox.exec()
            else:
                msgBox.setText("Limite prestiti raggiunto.\nImpossibile prenotare il seguente documento")
                msgBox.exec()
