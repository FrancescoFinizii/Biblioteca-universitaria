from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.uic import loadUi

from Controller.gestioneRiviste import GestioneRiviste


class AggiungiRivista(QDialog):

    def __init__(self):
        super(AggiungiRivista, self).__init__()
        loadUi("View/Amministratore/UI files/aggiungi-modifica rivista.ui", self)
        self.confermaButton.clicked.connect(self.aggiungiRivista)
        self.annullaButton.clicked.connect(self.close)


    def aggiungiRivista(self):
        if self.notEmpty(self.titoloInput) and self.notEmpty(self.autoreInput) and self.notEmpty(self.editoreInput) and self.notEmpty(self.ISSNInput) and self.notEmpty(self.annoPubblicazioneInput) and self.notEmpty(self.volumeInput) and self.notEmpty(self.numeroInput):
            if all(x.isalpha() or x.isspace() or x == "." or x == "," for x in self.autoreInput.text()):
                if all(x.isalpha() or x.isspace() for x in self.editoreInput.text()):
                    if self.annoPubblicazioneInput.text().isdigit():
                        if self.ISSNInput.text().isdigit():
                            if len(self.ISSNInput.text()) == 8:
                                if self.volumeInput.text().isdigit():
                                    if self.numeroInput.text().isdigit():
                                        if GestioneRiviste.getDocumento(self.ISSNInput.text()) == None:
                                            GestioneRiviste.aggiungiDocumento(autore=self.autoreInput.text(),
                                                                              descrizione=self.descrizioneInput.toPlainText(),
                                                                              disponibilita=self.quantitaInput.value(),
                                                                              editore=self.editoreInput.text(),
                                                                              lingua=self.linguaInput.currentText(),
                                                                              titolo=self.titoloInput.text(),
                                                                              annoPubblicazione=self.annoPubblicazioneInput.text(),
                                                                              volume=self.volumeInput.text(),
                                                                              numero=self.numeroInput.text(),
                                                                              ISSN=self.ISSNInput.text())
                                            self.accept()
                                        else:
                                            msgBox = QMessageBox()
                                            msgBox.setIcon(QMessageBox.Warning)
                                            msgBox.setStandardButtons(QMessageBox.Ok)
                                            msgBox.setWindowTitle("Errore")
                                            msgBox.setText("Aggiunta documento fallita\nIl codice ISSN è associato a un'altro documento")
                                            msgBox.exec_()
                                    else:
                                        self.errorLabel.setText("Numero non valido")
                                else:
                                    self.errorLabel.setText("Volume non valido")
                            else:
                                self.errorLabel.setText("il codice ISSN deve contenere 8 cifre")
                        else:
                            self.errorLabel.setText("ISSN non valido")
                    else:
                        self.errorLabel.setText("Anno pubblicazione non valido")
                else:
                    self.errorLabel.setText("L'editore può contenere solo caratteri alfabetici")
            else:
                self.errorLabel.setText("L'autore contiene caratteri non validi")
        else:
            self.errorLabel.setText("Non tutti i campi sono compilati")


    @staticmethod
    def notEmpty(obj):
        if not(obj.text().isspace()) and obj.text() != "":
            return True
        else:
            return False
