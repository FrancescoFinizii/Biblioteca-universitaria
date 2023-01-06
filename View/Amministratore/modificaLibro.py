from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi

from Controller.gestioneLibri import GestioneLibri


class ModificaLibro(QDialog):


    def __init__(self, libro):
        super(ModificaLibro, self).__init__()
        loadUi("View/Amministratore/UI files/aggiungi-modifica libro.ui", self)
        self.confermaButton.clicked.connect(self.modificaLibro)
        self.annullaButton.clicked.connect(self.close)
        self.ISBNInput.setReadOnly(True)
        self.titoloInput.setText(libro.getTitolo())
        self.autoreInput.setText(libro.getAutore())
        self.editoreInput.setText(libro.getEditore())
        self.linguaInput.setCurrentText(libro.getLingua())
        self.annoPubblicazioneInput.setText(libro.getAnnoPubblicazione())
        self.genereInput.setText(libro.getGenere())
        self.ISBNInput.setText(libro.getID())
        self.quantitaInput.setValue(libro.getDisponibilita())
        self.descrizioneInput.setText(libro.getDescrizione())


    def modificaLibro(self):
        if self.notEmpty(self.titoloInput) and self.notEmpty(self.autoreInput) and self.notEmpty(self.editoreInput) and self.notEmpty(self.annoPubblicazioneInput) and self.notEmpty(self.genereInput):
            if all(x.isalpha() or x.isspace() or x == "." or x == "," for x in self.autoreInput.text()):
                if all(x.isalpha() or x.isspace() for x in self.editoreInput.text()):
                    if self.annoPubblicazioneInput.text().isdigit():
                        if all(x.isalpha() or x.isspace() for x in self.genereInput.text()):
                            GestioneLibri.modificaDocumento(titolo=self.titoloInput.text(),
                                                            autore=self.autoreInput.text(),
                                                            descrizione=self.descrizioneInput.toPlainText(),
                                                            disponibilita=self.quantitaInput.value(),
                                                            editore=self.editoreInput.text(),
                                                            lingua=self.linguaInput.currentText(),
                                                            annoPubblicazione=self.annoPubblicazioneInput.text(),
                                                            genere=self.genereInput.text(),
                                                            ISBN=self.ISBNInput.text())
                            self.accept()
                        else:
                            self.errorLabel.setText("Genere non valido")
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


