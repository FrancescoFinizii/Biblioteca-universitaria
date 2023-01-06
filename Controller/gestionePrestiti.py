import os
import pickle
from datetime import timedelta

from Model.prestito import Prestito

numeroPrestiti = 0

class GestionePrestiti:

    @staticmethod
    def aggiungiPrestito(matricolaStudente, dataInizio, documento):
        global numeroPrestiti
        numeroPrestiti += 1
        dataScadenza = dataInizio + timedelta(days=30)
        prestito = Prestito(str(numeroPrestiti), matricolaStudente, dataInizio, dataScadenza, documento)
        if os.path.isfile("Dati/Prestiti.pickle"):
            with open("Dati/Prestiti.pickle", "rb") as f:
                prestiti = pickle.load(f)
        else:
            prestiti = {}
        prestiti[str(numeroPrestiti)] = prestito
        with open("Dati/Prestiti.pickle", "wb") as f:
            pickle.dump(prestiti, f, pickle.HIGHEST_PROTOCOL)


    @staticmethod
    def prorogaScadenzaPrestito(codice):
        with open("Dati/Prestiti.pickle", "rb") as f:
            prestiti = pickle.load(f)
            prestiti[codice].setDataScadenza(prestiti[codice].getDataScadenza() + timedelta(days=7))
            prestiti[codice].setProrogato(True)
        with open("Dati/Prestiti.pickle", "wb") as f:
            pickle.dump(prestiti, f, pickle.HIGHEST_PROTOCOL)


    @staticmethod
    def rimuoviPrestito(codice):
        with open("Dati/Prestiti.pickle", "rb") as f:
            prestiti = pickle.load(f)
            del prestiti[codice]
        with open("Dati/Prestiti.pickle", "wb") as f:
            pickle.dump(prestiti, f, pickle.HIGHEST_PROTOCOL)



    @staticmethod
    def getPrestito(codice):
        if os.path.isfile("Dati/Prestiti.pickle"):
            with open("Dati/Prestiti.pickle", "rb") as f:
                prestiti = pickle.load(f)
                return prestiti.get(codice, None)
        else:
            return None


    @staticmethod
    def ricercaPrestitoPerMatricola(matricolaStudente):
        lista = []
        if os.path.isfile("Dati/Prestiti.pickle"):
            with open("Dati/Prestiti.pickle", "rb") as f:
                prestiti = pickle.load(f)
                for prestito in prestiti.values():
                    if matricolaStudente in prestito.getMatricolaStudente():
                        lista.append(prestito)
        return lista


    @staticmethod
    def ricercaPrestitoPerCodice(codice):
        lista = []
        if os.path.isfile("Dati/Prestiti.pickle"):
            with open("Dati/Prestiti.pickle", "rb") as f:
                prestiti = pickle.load(f)
                for prestito in prestiti.values():
                    if codice in prestito.getCodice():
                        lista.append(prestito)
        return lista