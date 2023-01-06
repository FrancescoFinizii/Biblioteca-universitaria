from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi


class VisualizzaLibro(QDialog):

    def __init__(self, libro):
        super(VisualizzaLibro, self).__init__()
        loadUi("View/Amministratore/UI files/visualizza libro.ui", self)
        self.chiudiButton.clicked.connect(self.close)
        self.titolo.setText(libro.getTitolo())
        self.autore.setText(libro.getAutore())
        self.editore.setText(libro.getEditore())
        self.lingua.setText(libro.getLingua())
        self.annoPubblicazione.setText(libro.getAnnoPubblicazione())
        self.genere.setText(libro.getGenere())
        self.ISBN.setText(libro.getID())
        self.quantita.setText(str(libro.getDisponibilita()))
        self.descrizione.setText(libro.getDescrizione())