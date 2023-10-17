import datetime
import json

from PyQt5.QtCore import QDate
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QPushButton, QGridLayout, QMessageBox
from PyQt5.uic import loadUi

from Controller.gestionePrenotazioni import GestionePrenotazioni
from View.Studente import studentDashboard


class Prenotazione(QWidget):

    def __init__(self):
        super(Prenotazione, self).__init__()
        loadUi("View/Studente/UI files/prenotazione.ui", self)
        self.effettuaPrenotazioneButton.clicked.connect(self.aggiungiPrenotazione)
        self.calendarWidget.selectionChanged.connect(self.getPrenotazioniDisponibili)
        self.sedeInput.currentTextChanged.connect(self.getPrenotazioniDisponibili)
        self.setDateRange()
        self.getPrenotazioniDisponibili()

    def setDateRange(self):
        adesso = datetime.datetime.now()
        # considero l'orario della biblioteca dal LUN al VEN dalle 8.30 alle 19.00
        # oltre le 6:30 non è più possibile effettuare una prenotazione
        orarioChiusura = adesso.replace(hour=18, minute=30, second=0, microsecond=0)
        if adesso >= orarioChiusura:
            # nel caso in cui siano passate le 6:30 le prenotazioni iniziano dal giorno seguente
            adesso = datetime.date.today() + datetime.timedelta(days=1)
        if adesso.weekday() > 4:
            adesso = datetime.date.today() + datetime.timedelta(days=7 - adesso.weekday())
        # Ciascun utente può effettuare una prenotazione a distanza massima di 3 giorni FERIALI dal giorno corrente
        giornoLimite = self.aggiungiGiorniFeriali(adesso, 2)
        # imposto il range di date in cui è possibile prenotarsi
        inizio = QDate(adesso.year, adesso.month, adesso.day)
        fine = QDate(giornoLimite.year, giornoLimite.month, giornoLimite.day)
        self.calendarWidget.setMinimumDate(inizio)
        self.calendarWidget.setMaximumDate(fine)


    def getPrenotazioniDisponibili(self):
        self.widgetButton.deleteLater()

        # imposto il widget dei bottoni come GridLayout
        self.widgetButton = QWidget()
        grid = QGridLayout()
        self.widgetButton.setLayout(grid)

        self.widgetContainer.layout().addWidget(self.widgetButton)

        giornoSelezionato = self.calendarWidget.selectedDate().toString("ddd")

        self.listaBottoni = []

        if giornoSelezionato != "sab" and giornoSelezionato != "dom":
            self.errorLabel.setText("")

            with open("Dati/prenotazioni.json", "r") as f:
                jsonFile = json.load(f)

            # lista fasce orarie biblioteca
            self.fasciaOraria = list(jsonFile[self.sedeInput.currentText()][giornoSelezionato].keys())

            # lista numero studenti prenotati nelle singole fasce orarie
            studentiFascia = list(jsonFile[self.sedeInput.currentText()][giornoSelezionato].values())

            # posizione dei bottoni all'interno del GridLayout
            posizioneBottoni = [(i, j) for i in range(7) for j in range(3)]

            with open("config.json", "r") as p:
                configJson = json.load(p)
            postiMax = configJson["postiMax"][self.sedeInput.currentText()]

            now = datetime.datetime.now()
            numBtn = 0
            for i in range(21):
                numBtn += 1
                if studentiFascia[i] < postiMax:
                        if now.strftime("%A")[0:3] == giornoSelezionato:
                            if now.time() < datetime.time(hour=int(self.fasciaOraria[i][0:2]), minute=int(self.fasciaOraria[i][3:5])):
                                self.aggiungiBottone(self.fasciaOraria[i], posizioneBottoni[i], numBtn)
                        else:
                            self.aggiungiBottone(self.fasciaOraria[i], posizioneBottoni[i], numBtn)
        else:
            self.errorLabel.setText("Nessuna prenotazione disponibile")


    def aggiungiBottone(self, fasciaOraria, posizioneBottone, btnID):
        button = QPushButton(fasciaOraria, self)
        button.setObjectName('Button-{}'.format(btnID))
        button.setStyleSheet("QPushButton#{}".format(button.objectName()) +
                             "{border: 1px solid;\nbackground-color: rgb(230, 230, 230);\nborder-radius: 5px;\nborder-color:rgb(0, 0, 0);\n}" +
                             "\nQPushButton#{}:hover".format(
                                 button.objectName()) + "\n{background-color:rgb(147, 147, 147);\n}" +
                             "\nQPushButton#{}:checked".format(
                                 button.objectName()) + "\n{background-color:rgb(147, 147, 147);\n}")
        button.setFont(QFont('Times', 12))
        button.setCheckable(True)
        self.listaBottoni.append(button)
        self.widgetButton.layout().addWidget(button, *posizioneBottone)


    def aggiungiPrenotazione(self):

        # lista ID bottoni selezionati (la lista è ordinata in ordine crescente)
        lista = []

        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Warning)
        msgBox.setWindowTitle("Errore prenotazione")
        msgBox.setDefaultButton(QMessageBox.Ok)

        for btn in self.listaBottoni:
            if btn.isChecked():
                # aggiungo l'ID del bottone alla lista
                lista.append(int(btn.objectName()[7:len(btn.objectName())]))
        # la lista può contenere al massimo 4 elementi poichè il turno non può oltrepassare le 2 ore (ogni fascia oraria dure 30 min)
        if len(lista) <= 4:
            if lista != []:
                # se la lista contiene un insieme di numeri consecutivi allora i bottoni selezionati sono consecutivi
                if lista == list(range(min(lista), max(lista) + 1)):

                    data = datetime.date(year=int(self.calendarWidget.selectedDate().toString("yyyy")),
                                             month=int(self.calendarWidget.selectedDate().toString("M")),
                                             day=int(self.calendarWidget.selectedDate().toString("d")))

                    oraInzio = datetime.time(hour=int(self.fasciaOraria[(lista[0] - 1)][0:2]),
                                             minute=int(self.fasciaOraria[(lista[0] - 1)][3:5]))

                    oraFine = oraInzio.replace(hour=int(self.fasciaOraria[(lista[-1] - 1)][6:8]),
                                               minute=int(self.fasciaOraria[(lista[-1] - 1)][9:11]))

                    if GestionePrenotazioni.getPrenotazione(studentDashboard.studente.getMatricola()) == None:
                        GestionePrenotazioni.aggiungiPrenotazione(
                            matricolaStudente=studentDashboard.studente.getMatricola(),
                            sede=self.sedeInput.currentText(),
                            data=data,
                            oraInizio=oraInzio,
                            oraFine=oraFine)
                        msgBox.setIcon(QMessageBox.Information)
                        msgBox.setDefaultButton(QMessageBox.Ok)
                        msgBox.setWindowTitle("Prenotazione effettuata")
                        msgBox.setText("La tua prenotazione è stata aggiunta con successo")
                    else:
                        conferma = QMessageBox()
                        conferma.setIcon(QMessageBox.Question)
                        conferma.setText('Prenotazione già esistente')
                        conferma.setText("Hai già effettuato una prenotazione\nDesideri sostituire quella già esistente")
                        conferma.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
                        if conferma.exec() == QMessageBox.Yes:
                            GestionePrenotazioni.rimuoviPrenotazione(studentDashboard.studente.getMatricola())
                            GestionePrenotazioni.aggiungiPrenotazione(
                                matricolaStudente=studentDashboard.studente.getMatricola(),
                                sede=self.sedeInput.currentText(),
                                data=data,
                                oraInizio=oraInzio,
                                oraFine=oraFine)
                            msgBox.setIcon(QMessageBox.Information)
                            msgBox.setDefaultButton(QMessageBox.Ok)
                            msgBox.setWindowTitle("Prenotazione effettuata")
                            msgBox.setText("La tua prenotazione è stata aggiunta con successo")
                        else:
                            msgBox.setIcon(QMessageBox.Information)
                            msgBox.setDefaultButton(QMessageBox.Ok)
                            msgBox.setText("Prenotazione non effettuata")
                else:
                    msgBox.setText("Le fasce orarie devono essere consecutive\nPrenotazione non effettuata")
            else:
                msgBox.setText("Nessuna fascia selezionata\nPrenotazione impossibile")
        else:
            msgBox.setText("Limite fasce orarie superato (MAX:4)\nPrenotazione non effettuata")
        msgBox.exec()

    @staticmethod
    def aggiungiGiorniFeriali(data, numeroGiorni):
        while numeroGiorni > 0:
            data += datetime.timedelta(days=1)
            if data.weekday() > 4:  # SAB = 5, DOM = 6
                continue
            else:
                numeroGiorni -= 1
        return data
