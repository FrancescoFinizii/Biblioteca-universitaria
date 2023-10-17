import json
import os
import pickle
import datetime

from Controller.gestioneLibri import GestioneLibri
from Controller.gestioneRiviste import GestioneRiviste
from Controller.gestioneStudenti import GestioneStudenti
from Model.prestito import Prestito

class GestionePrestiti:

    dir_path = os.path.dirname(os.path.dirname(__file__))
    percorsoFile = os.path.join(dir_path, 'Dati', "Prestiti.pickle")
    percorsoJSONFIle = os.path.join(dir_path, 'config.json')

    @staticmethod
    def aggiungiPrestito(matricolaStudente, dataInizio, documento):
        with open(GestionePrestiti.percorsoJSONFIle, "r") as f:
            jsonFile = json.load(f)
        numeroPrestiti = jsonFile["numeroPrestiti"]
        jsonFile["numeroPrestiti"] += 1
        with open(GestionePrestiti.percorsoJSONFIle, "w") as f:
            json.dump(jsonFile, f)
        dataScadenza = dataInizio + datetime.timedelta(days=30)
        prestito = Prestito(str(numeroPrestiti), matricolaStudente, dataInizio, dataScadenza, documento)
        if os.path.isfile(GestionePrestiti.percorsoFile):
            with open(GestionePrestiti.percorsoFile, "rb") as f:
                prestiti = pickle.load(f)
        else:
            prestiti = {}
        prestiti[str(numeroPrestiti)] = prestito
        if type(documento).__name__ == "Libro":
            GestioneLibri.decrementaQuantita(documento.getID())
        else:
            GestioneRiviste.decrementaQuantita(documento.getID())
        with open(GestionePrestiti.percorsoFile, "wb") as f:
            pickle.dump(prestiti, f, pickle.HIGHEST_PROTOCOL)


    @staticmethod
    def prorogaScadenzaPrestito(codice):
        with open(GestionePrestiti.percorsoFile, "rb") as f:
            prestiti = pickle.load(f)
            prestiti[codice].setDataScadenza(prestiti[codice].getDataScadenza() + datetime.timedelta(days=7))
            prestiti[codice].setProrogato(True)
        with open(GestionePrestiti.percorsoFile, "wb") as f:
            pickle.dump(prestiti, f, pickle.HIGHEST_PROTOCOL)


    @staticmethod
    def rimuoviPrestito(codice):
        with open(GestionePrestiti.percorsoFile, "rb") as f:
            prestiti = pickle.load(f)
            if type(prestiti[codice].getDocumento()).__name__ == "Libro":
                GestioneLibri.incrementaQuantita(prestiti[codice].getDocumento().getID())
            else:
                GestioneRiviste.incrementaQuantita(prestiti[codice].getDocumento().getID())
            if prestiti[codice].getDataScadenza() < datetime.date.today():
                GestioneStudenti.attivaAccount(prestiti[codice].getMatricolaStudente())
            del prestiti[codice]
        with open(GestionePrestiti.percorsoFile, "wb") as f:
            pickle.dump(prestiti, f, pickle.HIGHEST_PROTOCOL)


    @staticmethod
    def getPrestito(codice):
        if os.path.isfile(GestionePrestiti.percorsoFile):
            with open(GestionePrestiti.percorsoFile, "rb") as f:
                prestiti = pickle.load(f)
                return prestiti.get(codice, None)
        else:
            return None


    @staticmethod
    def ricercaPrestitoPerMatricola(matricolaStudente):
        lista = []
        if os.path.isfile(GestionePrestiti.percorsoFile):
            with open(GestionePrestiti.percorsoFile, "rb") as f:
                prestiti = pickle.load(f)
                for prestito in prestiti.values():
                    if matricolaStudente in prestito.getMatricolaStudente():
                        lista.append(prestito)
        return lista


    @staticmethod
    def ricercaPrestitoPerCodice(codice):
        lista = []
        if os.path.isfile(GestionePrestiti.percorsoFile):
            with open(GestionePrestiti.percorsoFile, "rb") as f:
                prestiti = pickle.load(f)
                for prestito in prestiti.values():
                    if codice in prestito.getCodice():
                        lista.append(prestito)
        return lista