import datetime
from unittest import TestCase
from Model.libro import Libro
from Model.studente import Studente
from Model.rivista import Rivista
from Model.amministratore import Amministratore
from Controller.gestioneRiviste import GestioneRiviste
from Controller.gestionePrestiti import GestionePrestiti
from Controller.gestioneAmministratori import GestioneAmministratori
from Controller.gestioneStudenti import GestioneStudenti
from Controller.gestioneLibri import GestioneLibri

class Test(TestCase):


    def setUp(self):
        GestioneStudenti.aggiungiUtente('Kristian', 'Likaj', '1097605', '12345678', datetime.date(2000, 10, 10))

    def test_studente(self):
        self.assertIsInstance(GestioneStudenti.getUtente('1097605'), Studente)

    def test_amministratore(self):
        GestioneAmministratori.aggiungiUtente('Mario', 'Rossi', '12345678', 'asdfghjkl', datetime.date(1970, 11, 11),
                                              'amministratore')
        self.assertIsInstance(GestioneAmministratori.getUtente('12345678'), Amministratore)


    def test_libro(self):
        GestioneLibri.aggiungiDocumento('Follia', 'Patrick McGrath', 'Adelphi', 'italiano', '2012', '2', 'bellissimo','1234567891234','Romanzo')
        self.assertIsInstance(GestioneLibri.getDocumento('1234567891234'), Libro)

    def test_riviste(self):
        GestioneRiviste.aggiungiDocumento('Focus', 'Rossi', 'Mario', 'italiano', '2012','1','scientifico','98765432','3','2')
        self.assertIsInstance(GestioneRiviste.getDocumento('98765432'), Rivista)

    def test_prestito_libro(self):
        libro = GestioneLibri.getDocumento('1234567891234')
        prestitoLibro = GestionePrestiti.aggiungiPrestito('1097605', datetime.date.today(), libro)
        prestiti = GestionePrestiti.ricercaPrestitoPerMatricola('1097605')
        self.assertIsInstance(GestionePrestiti.getPrestito(prestiti[0].getCodice()), Prestito)
        GestionePrestiti.rimuoviPrestito(prestiti[0].getCodice())
        self.assertIsNone(GestionePrestiti.getPrestito(prestiti[0].getCodice()))

    def test_prestito_rivista(self):
        rivista = GestioneRiviste.getDocumento('98765432')
        prestitoRivista = GestioneRiviste.aggiungiPrestito('1097605', datetime.date.today(), rivista)
        prestiti = GestionePrestiti.ricercaPrestitoPerMatricola('1097605')
        self.assertIsInstance(GestionePrestiti.getPrestito(prestiti[0].getCodice()), Prestito)
        GestionePrestiti.rimuoviPrestito(prestiti[0].getCodice())
        self.assertIsNone(GestionePrestiti.getPrestito(prestiti[0].getCodice()))
