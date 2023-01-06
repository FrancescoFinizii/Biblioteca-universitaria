from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi

from Controller.gestioneRiviste import GestioneRiviste


class ModificaRivista(QDialog):


    def __init__(self, rivista):
        super(ModificaRivista, self).__init__()
        loadUi("View/Amministratore/UI files/aggiungi-modifica rivista.ui", self)
        self.confermaButton.clicked.connect(self.modificaRivista)
        self.annullaButton.clicked.connect(self.close)
        self.ISSNInput.setReadOnly(True)
        self.titoloInput.setText(rivista.getTitolo())
        self.autoreInput.setText(rivista.getAutore())
        self.editoreInput.setText(rivista.getEditore())
        self.linguaInput.setCurrentText(rivista.getLingua())
        self.annoPubblicazioneInput.setText(rivista.getAnnoPubblicazione())
        self.ISSNInput.setText(rivista.getID())
        self.volumeInput.setText(rivista.getVolume())
        self.numeroInput.setText(rivista.getNumero())
        self.quantitaInput.setValue(rivista.getDisponibilita())
        self.descrizioneInput.setText(rivista.getDescrizione())


    def modificaRivista(self):
        if self.notEmpty(self.titoloInput) and self.notEmpty(self.autoreInput) and self.notEmpty(self.editoreInput) and self.notEmpty(self.annoPubblicazioneInput) and self.notEmpty(self.volumeInput) and self.notEmpty(self.numeroInput):
            if all(x.isalpha() or x.isspace() or x == "." or x == "," for x in self.autoreInput.text()):
                if all(x.isalpha() or x.isspace() for x in self.editoreInput.text()):
                    if self.annoPubblicazioneInput.text().isdigit():
                        if self.volumeInput.text().isdigit():
                            if self.numeroInput.text().isdigit():
                                GestioneRiviste.modificaDocumento(autore=self.autoreInput.text(),
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
                                self.errorLabel.setText("Numero non valido")
                        else:
                            self.errorLabel.setText("Volume non valido")
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