from PyQt5.QtCore import QDate, pyqtSignal
from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5.uic import loadUi

from Controller.gestionePrenotazioni import GestionePrenotazioni
from Controller.gestionePrestiti import GestionePrestiti
from Controller.gestioneStudenti import GestioneStudenti
from View.Studente import studentDashboard
from View.Studente.modificaDatiPersonali import ModificaDatiPersonali
from View.Studente.modificaPassword import ModificaPassword
from View.Studente.visualizzaPrenotazione import VisualizzaPrenotazione
from View.Studente.visualizzaPrestito import VisualizzaPrestito


class Profilo(QWidget):

    sig = pyqtSignal()

    def __init__(self):
        super(Profilo, self).__init__()
        loadUi("View/Studente/UI files/profilo.ui", self)
        self.visualizzaPrestito1Button.clicked.connect(self.visualizzaPrestito1)
        self.prorogaPrestito1Button.clicked.connect(self.prorogaPrestito1)
        self.visualizzaPrestito2Button.clicked.connect(self.visualizzaPrestito2)
        self.prorogaPrestito2Button.clicked.connect(self.prorogaPrestito2)
        self.modificaProfiloButton.clicked.connect(self.modificaDatiAnagrafici)
        self.modificaPasswordButton.clicked.connect(self.modificaPassword)
        self.eliminaAccountButton.clicked.connect(self.eliminaAccount)
        self.visualizzaPrenotazioneButton.clicked.connect(self.visualizzaPrenotazione)
        self.annullaPrenotazioneButton.clicked.connect(self.annullaPrenotazione)

        self.matricola.setText(studentDashboard.studente.getMatricola())
        self.nome.setText(studentDashboard.studente.getNome())
        self.cognome.setText(studentDashboard.studente.getCognome())
        self.dataNascita.setDate(QDate(studentDashboard.studente.getDataNascita().year,
                                       studentDashboard.studente.getDataNascita().month,
                                       studentDashboard.studente.getDataNascita().day))
        match len(GestionePrestiti.ricercaPrestitoPerMatricola(studentDashboard.studente.getMatricola())):
            case 0:
                self.prestito1Widget.deleteLater()
                self.prestito2Widget.deleteLater()
            case 1:
                self.prestitoLabel.deleteLater()
                self.prestito2Widget.deleteLater()
                self.codicePrestito1 = GestionePrestiti.ricercaPrestitoPerMatricola(studentDashboard.studente.getMatricola())[0].getCodice()
                self.prestito1.setText("Prestito n° " + self.codicePrestito1)
                if GestionePrestiti.getPrestito(self.codicePrestito1).getProrogato() == True:
                    self.prorogaPrestito1Button.deleteLater()
            case 2:
                self.prestitoLabel.deleteLater()
                self.codicePrestito1 =GestionePrestiti.ricercaPrestitoPerMatricola(studentDashboard.studente.getMatricola())[0].getCodice()
                self.codicePrestito2 =GestionePrestiti.ricercaPrestitoPerMatricola(studentDashboard.studente.getMatricola())[1].getCodice()
                self.prestito1.setText("Prestito n° " + self.codicePrestito1)
                self.prestito2.setText("Prestito n° " + self.codicePrestito2)
                if GestionePrestiti.getPrestito(self.codicePrestito1).getProrogato() == True:
                    self.prorogaPrestito1Button.deleteLater()
                if GestionePrestiti.getPrestito(self.codicePrestito2).getProrogato() == True:
                    self.prorogaPrestito2Button.deleteLater()
        if GestionePrenotazioni.getPrenotazione(studentDashboard.studente.getMatricola()) == None:
            self.prenotazioniWidget.deleteLater()
        else:
            self.prenotazioneLabel.deleteLater()
            self.prenotazione.setText("Prenotazione")


    def visualizzaPrestito1(self):
        visualizzaPrestito = VisualizzaPrestito(GestionePrestiti.getPrestito(self.codicePrestito1))
        visualizzaPrestito.exec_()


    def prorogaPrestito1(self):
        GestionePrestiti.prorogaScadenzaPrestito(self.codicePrestito1)
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setWindowTitle("Prestito")
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.setText("Prestito prorogato correttamente")
        msgBox.exec()
        self.close()



    def visualizzaPrestito2(self):
        visualizzaPrestito = VisualizzaPrestito(GestionePrestiti.getPrestito(self.codicePrestito2))
        visualizzaPrestito.exec_()


    def prorogaPrestito2(self):
        GestionePrestiti.prorogaScadenzaPrestito(self.codicePrestito2)
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setWindowTitle("Prestito")
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.setText("Prestito prorogato correttamente")
        msgBox.exec()
        self.close()



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
        if GestionePrestiti.ricercaPrestitoPerMatricola(studentDashboard.studente.getMatricola()) == []:
            msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            msgBox.setText("Sei sicuro di cancellare il tuo account?")
            if msgBox.exec_() == QMessageBox.Yes:
                if GestionePrenotazioni.ricercaPrenotazione(studentDashboard.studente.getMatricola()) != None:
                    GestionePrenotazioni.rimuoviPrenotazione(studentDashboard.studente.getMatricola())
                GestioneStudenti.rimuoviUtente(studentDashboard.studente.getMatricola())
                studentDashboard.studente = None
                self.close()
        else:
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.setMaximumWidth(300)
            msgBox.setText(
                "Impossibile rimuovere l'account\nPrima di procedere alla cancellazione del proprio profilo occorre aver concluso tutti i prestiti effettuati")
            msgBox.exec()


    def closeEvent(self, event):
        self.sig.emit()


    def visualizzaPrenotazione(self):
        self.visualizzaPrenotazione = VisualizzaPrenotazione(GestionePrenotazioni.getPrenotazione(studentDashboard.studente.getMatricola()))
        self.visualizzaPrenotazione.exec()


    def annullaPrenotazione(self):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Question)
        msgBox.setWindowTitle("Cancellazione prenotazione")
        msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msgBox.setText("Sei sicuro di rimuovere la prenotazione?")
        if msgBox.exec_() == QMessageBox.Yes:
            GestionePrenotazioni.rimuoviPrenotazione(studentDashboard.studente.getMatricola())
            self.close()



