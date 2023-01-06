import os
import pickle

from Controller.gestioneDocumenti import GestioneDocumenti
from Model.libro import Libro


class GestioneLibri(GestioneDocumenti):


    @staticmethod
    def aggiungiDocumento(titolo, autore, editore, lingua, annoPubblicazione, disponibilita, descrizione, ISBN, genere):
        libro = Libro(titolo, autore, editore, lingua, annoPubblicazione, disponibilita, descrizione, ISBN, genere)
        if os.path.isfile("Dati/Libri.pickle"):
            with open("Dati/Libri.pickle", "rb") as f:
                libri = pickle.load(f)
        else:
            libri = {}
        libri[libro.getID()] = libro
        with open("Dati/Libri.pickle", "wb") as f:
            pickle.dump(libri, f, pickle.HIGHEST_PROTOCOL)


    @staticmethod
    def modificaDocumento(ISBN, titolo, autore, editore, lingua, annoPubblicazione, disponibilita, descrizione, genere):
        with open("Dati/Libri.pickle", "rb") as f:
            libri = pickle.load(f)
            libri[ISBN].setTitolo(titolo)
            libri[ISBN].setAutore(autore)
            libri[ISBN].setEditore(editore)
            libri[ISBN].setLingua(lingua)
            libri[ISBN].setAnnoPubblicazione(annoPubblicazione)
            libri[ISBN].setDisponibilita(disponibilita)
            libri[ISBN].setDescrizione(descrizione)
            libri[ISBN].setGenere(genere)
        with open("Dati/Libri.pickle", "wb") as f:
            pickle.dump(libri, f, pickle.HIGHEST_PROTOCOL)


    @staticmethod
    def rimuoviDocumento(ISBN):
        with open("Dati/Libri.pickle", "rb") as f:
            libri = pickle.load(f)
            del libri[ISBN]
        with open("Dati/Libri.pickle", "wb") as f:
            pickle.dump(libri, f, pickle.HIGHEST_PROTOCOL)


    @staticmethod
    def incrementaQuantita(ISBN):
        with open("Dati/Libri.pickle", "rb") as f:
            libri = pickle.load(f)
            libri[ISBN].setDisponibilita(libri[ISBN].getDisponibilita() + 1)
        with open("Dati/Libri.pickle", "wb") as f:
            pickle.dump(libri, f, pickle.HIGHEST_PROTOCOL)


    @staticmethod
    def decrementaQuantita(ISBN):
        with open("Dati/Libri.pickle", "rb") as f:
            libri = pickle.load(f)
            libri[ISBN].setDisponibilita(libri[ISBN].getDisponibilita() - 1)
        with open("Dati/Libri.pickle", "wb") as f:
            pickle.dump(libri, f, pickle.HIGHEST_PROTOCOL)


    @staticmethod
    def getDocumento(ISBN):
        if os.path.isfile("Dati/Libri.pickle"):
            with open("Dati/Libri.pickle", "rb") as f:
                libri = dict(pickle.load(f))
                return libri.get(ISBN, None)
        else:
            return None


    @staticmethod
    def ricercaDocumentoPerTitolo(titolo):
        lista = []
        if os.path.isfile("Dati/Libri.pickle"):
            with open("Dati/Libri.pickle", "rb") as f:
                libri = pickle.load(f)
                for libro in libri.values():
                    if titolo in libro.getTitolo():
                        lista.append(libro)
        return lista


    @staticmethod
    def ricercaDocumentoPerAutore(autore):
        lista = []
        if os.path.isfile("Dati/Libri.pickle"):
            with open("Dati/Libri.pickle", "rb") as f:
                libri = dict(pickle.load(f))
                for libro in libri.values():
                    if autore in libro.getAutore():
                        lista.append(libro)
        return lista

