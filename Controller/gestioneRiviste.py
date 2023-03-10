import os
import pickle

from Controller.gestioneDocumenti import GestioneDocumenti
from Model.rivista import Rivista


class GestioneRiviste(GestioneDocumenti):

    dir_path = os.path.dirname(os.path.dirname(__file__))
    percorsoFile = os.path.join(dir_path, 'Dati', "Riviste.pickle")

    @staticmethod
    def aggiungiDocumento(titolo, autore, editore, lingua, annoPubblicazione, disponibilita, descrizione, ISSN, volume, numero):
        rivista = Rivista(titolo, autore, editore, lingua, annoPubblicazione, disponibilita, descrizione, ISSN, volume, numero)
        if os.path.isfile(GestioneRiviste.percorsoFile):
            with open(GestioneRiviste.percorsoFile, "rb") as f:
                riviste = pickle.load(f)
        else:
            riviste = {}
        riviste[rivista.getID()] = rivista
        with open(GestioneRiviste.percorsoFile, "wb") as f:
            pickle.dump(riviste, f, pickle.HIGHEST_PROTOCOL)


    @staticmethod
    def modificaDocumento(ISSN, titolo, autore, editore, lingua, annoPubblicazione, disponibilita, descrizione, volume, numero):
        if os.path.isfile(GestioneRiviste.percorsoFile):
            with open(GestioneRiviste.percorsoFile, "rb") as f:
                riviste = pickle.load(f)
                riviste[ISSN].setTitolo(titolo)
                riviste[ISSN].setAutore(autore)
                riviste[ISSN].setEditore(editore)
                riviste[ISSN].setLingua(lingua)
                riviste[ISSN].setAnnoPubblicazione(annoPubblicazione)
                riviste[ISSN].setDisponibilita(disponibilita)
                riviste[ISSN].setDescrizione(descrizione)
                riviste[ISSN].setVolume(volume)
                riviste[ISSN].setNumero(numero)
            with open(GestioneRiviste.percorsoFile, "wb") as f:
                pickle.dump(riviste, f, pickle.HIGHEST_PROTOCOL)


    @staticmethod
    def rimuoviDocumento(ISSN):
        if os.path.isfile(GestioneRiviste.percorsoFile):
            with open(GestioneRiviste.percorsoFile, "rb") as f:
                riviste = pickle.load(f)
                del riviste[ISSN]
            with open(GestioneRiviste.percorsoFile, "wb") as f:
                pickle.dump(riviste, f, pickle.HIGHEST_PROTOCOL)


    @staticmethod
    def incrementaQuantita(ISSN):
        with open(GestioneRiviste.percorsoFile, "rb") as f:
            riviste = pickle.load(f)
            riviste[ISSN].setDisponibilita(riviste[ISSN].getDisponibilita() + 1)
        with open(GestioneRiviste.percorsoFile, "wb") as f:
            pickle.dump(riviste, f, pickle.HIGHEST_PROTOCOL)


    @staticmethod
    def decrementaQuantita(ISSN):
        with open(GestioneRiviste.percorsoFile, "rb") as f:
            riviste = pickle.load(f)
            riviste[ISSN].setDisponibilita(riviste[ISSN].getDisponibilita() - 1)
        with open(GestioneRiviste.percorsoFile, "wb") as f:
            pickle.dump(riviste, f, pickle.HIGHEST_PROTOCOL)


    @staticmethod
    def getDocumento(ISSN):
        if os.path.isfile(GestioneRiviste.percorsoFile):
            with open(GestioneRiviste.percorsoFile, "rb") as f:
                riviste = dict(pickle.load(f))
                return riviste.get(ISSN, None)
        else:
            return None


    @staticmethod
    def ricercaDocumentoPerTitolo(titolo):
        lista = []
        if os.path.isfile(GestioneRiviste.percorsoFile):
            with open(GestioneRiviste.percorsoFile, "rb") as f:
                riviste = dict(pickle.load(f))
                for rivista in riviste.values():
                    if titolo in rivista.getTitolo():
                        lista.append(rivista)
        return lista


    @staticmethod
    def ricercaDocumentoPerAutore(autore):
        lista = []
        if os.path.isfile(GestioneRiviste.percorsoFile):
            with open(GestioneRiviste.percorsoFile, "rb") as f:
                riviste = dict(pickle.load(f))
                for rivista in riviste.values():
                    if autore in rivista.getAutore():
                        lista.append(rivista)
        return lista

