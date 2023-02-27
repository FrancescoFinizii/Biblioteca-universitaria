import datetime
import locale
from unittest import TestCase

from Controller.gestionePrenotazioni import GestionePrenotazioni
from Model.libro import Libro
from Model.prenotazione import Prenotazione
from Model.prestito import Prestito
from Model.studente import Studente
from Model.rivista import Rivista
from Model.amministratore import Amministratore
from Controller.gestioneRiviste import GestioneRiviste
from Controller.gestionePrestiti import GestionePrestiti
from Controller.gestioneAmministratori import GestioneAmministratori
from Controller.gestioneStudenti import GestioneStudenti
from Controller.gestioneLibri import GestioneLibri

class Test(TestCase):


    def test_studente(self):
        #aggiunta studente
        GestioneStudenti.aggiungiUtente('Kristian', 'Likaj', '1097605', '12345678', datetime.date(2000, 10, 10))
        self.assertIsInstance(GestioneStudenti.getUtente('1097605'), Studente)

        #verifica modifiche studente
        GestioneStudenti.modificaUtente('Kristian', 'Likaj', '1097605', 'password', datetime.date(2000, 10, 10))
        self.assertEqual(GestioneStudenti.getUtente("1097605").getPassword(), "password")

        #rimozione studente
        GestioneStudenti.rimuoviUtente("1097605")
        self.assertIsNone(GestioneStudenti.getUtente("1097605"))


    def test_amministratore(self):
        # aggiunta amministratore
        GestioneAmministratori.aggiungiUtente('Mario', 'Rossi', '12345678', 'asdfghjkl', datetime.date(1970, 11, 11),
                                              'Assistente')
        self.assertIsInstance(GestioneAmministratori.getUtente('12345678'), Amministratore)

        # verifica modifiche amministratore
        GestioneAmministratori.modificaUtente('Mario', 'Rossi', '12345678', 'password', datetime.date(1970, 11, 11),
                                              'Assistente')
        self.assertEqual(GestioneAmministratori.getUtente("12345678").getPassword(), "password")

        # rimozione amministratore
        GestioneAmministratori.rimuoviUtente("12345678")
        self.assertIsNone(GestioneAmministratori.getUtente("12345678"))


    def test_libro(self):
        #aggiunta libro
        GestioneLibri.aggiungiDocumento('Follia', 'Patrick McGrath', 'Adelphi', 'italiano', '2012', 2, 'bellissimo',
                                        '1234567891234', 'Romanzo')
        self.assertIsInstance(GestioneLibri.getDocumento('1234567891234'), Libro)

        #verifica modifica libro
        GestioneLibri.modificaDocumento('1234567891234', 'Follia', 'Patrick McGrath', 'Adelphi', 'italiano', '2012',
                                        2, 'consigliato', 'Romanzo')
        self.assertEqual(GestioneLibri.getDocumento('1234567891234').getDescrizione(), "consigliato")

        #verifica incremento quantità
        quantitaIniziale = GestioneLibri.getDocumento("1234567891234").getDisponibilita()
        GestioneLibri.incrementaQuantita("1234567891234")
        self.assertEqual(GestioneLibri.getDocumento('1234567891234').getDisponibilita(), quantitaIniziale + 1)

        # verifica decremento quantità
        GestioneLibri.decrementaQuantita("1234567891234")
        self.assertEqual(GestioneLibri.getDocumento('1234567891234').getDisponibilita(), quantitaIniziale)

        #rimozione libro
        GestioneLibri.rimuoviDocumento("1234567891234")
        self.assertIsNone(GestioneLibri.getDocumento('1234567891234'))


    def test_rivista(self):
        # aggiunta rivista
        GestioneRiviste.aggiungiDocumento('Follia', 'Patrick McGrath', 'Adelphi', 'italiano', '2012', 2, 'bellissimo',
                                        '12341234', 1, 3)
        self.assertIsInstance(GestioneRiviste.getDocumento('12341234'), Rivista)

        # verifica modifica rivista
        GestioneRiviste.modificaDocumento('12341234', 'Follia', 'Patrick McGrath', 'Adelphi', 'italiano', '2012', 2,
                                        'consigliato', 1, 3)
        self.assertEqual(GestioneRiviste.getDocumento('12341234').getDescrizione(), "consigliato")

        # verifica incremento quantità
        quantitaIniziale = GestioneRiviste.getDocumento("12341234").getDisponibilita()
        GestioneRiviste.incrementaQuantita("12341234")
        self.assertEqual(GestioneRiviste.getDocumento('12341234').getDisponibilita(), quantitaIniziale + 1)

        # verifica decremento quantità
        GestioneRiviste.decrementaQuantita("12341234")
        self.assertEqual(GestioneRiviste.getDocumento('12341234').getDisponibilita(), quantitaIniziale)

        # rimozione rivista
        GestioneRiviste.rimuoviDocumento("12341234")
        self.assertIsNone(GestioneRiviste.getDocumento('12341234'))


    def test_prestito(self):
        #aggiungi prestito
        GestioneLibri.aggiungiDocumento('Follia', 'Patrick McGrath', 'Adelphi', 'italiano', '2012', 2, 'bellissimo',
                                        '1234567891234', 'Romanzo')
        GestioneStudenti.aggiungiUtente('Kristian', 'Likaj', '1097605', '12345678', datetime.date(2000, 10, 10))
        libro = GestioneLibri.getDocumento('1234567891234')
        dataInizio = datetime.date.today()
        dataScadenza = dataInizio + datetime.timedelta(days = 30)
        GestionePrestiti.aggiungiPrestito('1097605', dataInizio, libro)
        prestiti = GestionePrestiti.ricercaPrestitoPerMatricola('1097605')
        self.assertIsInstance(prestiti[0], Prestito)

        #modifica prestito
        GestionePrestiti.prorogaScadenzaPrestito(prestiti[0].getCodice())
        self.assertEqual(prestiti[0].getDataScadenza(), dataScadenza)

        #rimozione prestito
        GestionePrestiti.rimuoviPrestito(prestiti[0].getCodice())
        self.assertIsNone(GestionePrestiti.getPrestito(prestiti[0].getCodice()))


    def test_prenotazione(self):
        #aggiunta prenotazione
        GestioneStudenti.aggiungiUtente('Kristian', 'Likaj', '1097605', '12345678', datetime.date(2000, 10, 10))
        locale.setlocale(locale.LC_ALL, "it_IT.utf8")
        adesso = datetime.datetime.now()
        oraInizio = datetime.time(hour=adesso.hour, minute=adesso.minute, second=adesso.second)
        oraFine = adesso + datetime.timedelta(minutes=30)
        GestionePrenotazioni.aggiungiPrenotazione("1097605", "Biblioteca Tecnico-Scientifica-Biomedica",
                                                  datetime.date.today(), oraInizio, oraFine)
        self.assertIsInstance(GestionePrenotazioni.getPrenotazione("1097605"), Prenotazione)

        #rimozione prenotazione
        GestionePrenotazioni.rimuoviPrenotazione("1097605")
        self.assertIsNone(GestionePrenotazioni.getPrenotazione("1097605"))
        GestioneStudenti.rimuoviUtente("1097605")


