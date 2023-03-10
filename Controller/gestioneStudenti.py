import os
import pickle

from Controller.gestioneUtenti import GestioneUtenti
from Model.studente import Studente


class GestioneStudenti(GestioneUtenti):

    dir_path = os.path.dirname(os.path.dirname(__file__))
    percorsoFile = os.path.join(dir_path, 'Dati', "Studenti.pickle")


    @staticmethod
    def aggiungiUtente(nome, cognome, matricola, password, dataNascita):
        studente = Studente(nome, cognome, matricola, password, dataNascita)
        if os.path.isfile(GestioneStudenti.percorsoFile):
            with open(GestioneStudenti.percorsoFile, "rb") as f:
                studenti = pickle.load(f)
        else:
            studenti = {}
        studenti[matricola] = studente
        with open(GestioneStudenti.percorsoFile, "wb") as f:
            pickle.dump(studenti, f, pickle.HIGHEST_PROTOCOL)


    @staticmethod
    def modificaUtente(nome, cognome, matricola, password, dataNascita):
        if os.path.isfile(GestioneStudenti.percorsoFile):
            with open(GestioneStudenti.percorsoFile, "rb") as f:
                studenti = pickle.load(f)
                studenti[matricola].setNome(nome)
                studenti[matricola].setCognome(cognome)
                studenti[matricola].setPassword(password)
                studenti[matricola].setDataNascita(dataNascita)
            with open(GestioneStudenti.percorsoFile, "wb") as f:
                pickle.dump(studenti, f, pickle.HIGHEST_PROTOCOL)


    @staticmethod
    def rimuoviUtente(matricola):
        if os.path.isfile(GestioneStudenti.percorsoFile):
            with open(GestioneStudenti.percorsoFile, "rb") as f:
                studenti = pickle.load(f)
                del studenti[matricola]
            with open(GestioneStudenti.percorsoFile, "wb") as f:
                pickle.dump(studenti, f, pickle.HIGHEST_PROTOCOL)


    @staticmethod
    def getUtente(matricola):
        if os.path.isfile(GestioneStudenti.percorsoFile):
            with open(GestioneStudenti.percorsoFile, "rb") as f:
                studenti = pickle.load(f)
                return studenti.get(matricola, None)
        else:
            return None


    @staticmethod
    def ricercaUtenteMatricola(matricola):
        lista = []
        if os.path.isfile(GestioneStudenti.percorsoFile):
            with open(GestioneStudenti.percorsoFile, "rb") as f:
                studenti = dict(pickle.load(f))
                for studente in studenti.values():
                    if matricola in studente.getMatricola():
                        lista.append(studente)
        return lista


    @staticmethod
    def ricercaUtenteNomeCognome(nomeCognome):
        lista = []
        if os.path.isfile(GestioneStudenti.percorsoFile):
            with open(GestioneStudenti.percorsoFile, "rb") as f:
                studenti = dict(pickle.load(f))
                for studente in studenti.values():
                    if nomeCognome in studente.getNome() + " " + studente.getCognome():
                        lista.append(studente)
        return lista

    @staticmethod
    def sospendiAccount(matricola):
        with open(GestioneStudenti.percorsoFile, "rb") as f:
            studenti = pickle.load(f)
            studenti[matricola].setSospeso(True)
        with open(GestioneStudenti.percorsoFile, "wb") as f:
            pickle.dump(studenti, f, pickle.HIGHEST_PROTOCOL)

    @staticmethod
    def attivaAccount(matricola):
        with open(GestioneStudenti.percorsoFile, "rb") as f:
            studenti = pickle.load(f)
            studenti[matricola].setSospeso(False)
        with open(GestioneStudenti.percorsoFile, "wb") as f:
            pickle.dump(studenti, f, pickle.HIGHEST_PROTOCOL)