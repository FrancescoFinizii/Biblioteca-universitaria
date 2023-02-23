import json
from datetime import date
from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5.uic import loadUi

from Controller.gestioneAmministratori import GestioneAmministratori
from View.Amministratore.adminDashboard import AdminDashboard


class RegistrazioneAmministratore(QWidget):


    def __init__(self, parent):
        super(RegistrazioneAmministratore, self).__init__(parent)
        loadUi("View/Generale/UI files/registrazione amministratore.ui", self)
        self.creaAccountAmministratoreButton.clicked.connect(self.registrazioneAmministratore)
        self.registrazioneStudenteButton_2.clicked.connect(self.parent().goToRegistrazioneStudente)
        self.accediButton_2.clicked.connect(self.parent().goToLogin)


    def registrazioneAmministratore(self):
        if self.notEmpty(self.nome_input_2) and self.notEmpty(self.cognome_input_2) and self.notEmpty(self.matricola_input_2) \
                and self.notEmpty(self.password_input_2) and self.notEmpty(self.conferma_password_input_2) and self.notEmpty(self.codiceConferma_input):
            if self.nome_input_2.text().isalpha() and self.cognome_input_2.text().isalpha():
                if self.matricola_input_2.text().isdigit():
                    if self.password_input_2.text().isalnum and self.conferma_password_input_2.text().isalnum():
                        if len(self.password_input_2.text()) >= 8:
                            if self.password_input_2.text() == self.conferma_password_input_2.text():
                                with open("config.json", "r") as f:
                                    jsonFile = json.load(f)
                                    codiceConferma = jsonFile["secureCode"]
                                if self.codiceConferma_input.text() == codiceConferma:
                                    if GestioneAmministratori.getUtente(self.matricola_input_2.text()) == None:
                                        GestioneAmministratori.aggiungiUtente(nome=self.nome_input_2.text(),
                                                                              cognome=self.cognome_input_2.text(),
                                                                              matricola=self.matricola_input_2.text(),
                                                                              password=self.password_input_2.text(),
                                                                              dataNascita=date(year=int(self.dataDiNascitaInput_2.date().toString("yyyy")),
                                                                                               month=int(self.dataDiNascitaInput_2.date().toString("MM")),
                                                                                               day=int(self.dataDiNascitaInput_2.date().toString("dd"))),
                                                                              ruolo=self.ruolo_input.currentText())
                                        self.goToAdminDashboard(GestioneAmministratori.getUtente(self.matricola_input_2.text()))
                                    else:

                                        msgBox = QMessageBox()
                                        msgBox.setIcon(QMessageBox.Warning)
                                        msgBox.setStandardButtons(QMessageBox.Ok)
                                        msgBox.setWindowTitle("Errore")
                                        msgBox.setText("Registrazione amministratore fallita\nLa matricola inserita è associata a un'altro account")
                                        msgBox.exec_()
                                else:
                                    self.error_label_2.setText("Codice di sicurezza errato")
                            else:
                                self.error_label_2.setText("Le due password non corrispondono")
                        else:
                            self.error_label_2.setText("La password deve essere compresa tra gli 8 e i 32 caratteri")
                    else:
                        self.error_label_2.setText("La password può contenere solo caratteri alfanumerici")
                else:
                    self.error_label_2.setText("Matricola non valida")
            else:
                self.error_label_2.setText("Nome e/o cognome non validi")
        else:
            self.error_label_2.setText("Non tutti i campi sono compilati")



    def goToAdminDashboard(self, amministratore):
        self.close()
        self.adminDashboard = AdminDashboard(amministratore)
        self.adminDashboard.show()


    @staticmethod
    def notEmpty(obj):
        if not(obj.text().isspace()) and obj.text() != "":
            return True
        else:
            return False