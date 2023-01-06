import os
import pickle

from Controller.gestioneUtenti import GestioneUtenti
from Model.amministratore import Amministratore


class GestioneAmministratori(GestioneUtenti):

 
    @staticmethod
    def aggiungiUtente(nome, cognome, matricola, password, dataNascita, ruolo):
        amministratore = Amministratore(nome, cognome, matricola, password, dataNascita, ruolo)
        if os.path.isfile("Dati/Amministratori.pickle"):
            with open("Dati/Amministratori.pickle", "rb") as f:
                amministratori = pickle.load(f)
        else:
            amministratori = {}
        amministratori[amministratore.matricola] = amministratore
        with open("Dati/Amministratori.pickle", "wb") as f:
            pickle.dump(amministratori, f, pickle.HIGHEST_PROTOCOL)


    @staticmethod
    def modificaUtente(nome, cognome, matricola, password, dataNascita, ruolo):
        with open("Dati/Amministratori.pickle", "rb") as f:
            amministratori = pickle.load(f)
            amministratori[matricola].setNome(nome)
            amministratori[matricola].setCognome(cognome)
            amministratori[matricola].setPassword(password)
            amministratori[matricola].setDataNascita(dataNascita)
            amministratori[matricola].setRuolo(ruolo)
        with open("Dati/Amministratori.pickle", "wb") as f:
            pickle.dump(amministratori, f, pickle.HIGHEST_PROTOCOL)



    @staticmethod
    def rimuoviUtente(matricola):
        if os.path.isfile("Dati/Amministratori.pickle"):
            with open("Dati/Amministratori.pickle", "rb") as f:
                amministratori = pickle.load(f)
                del amministratori[matricola]
            with open("Dati/Amministratori.pickle", "wb") as f:
                pickle.dump(amministratori, f, pickle.HIGHEST_PROTOCOL)


    @staticmethod
    def getUtente(matricola):
        if os.path.isfile("Dati/Amministratori.pickle"):
            with open("Dati/Amministratori.pickle", "rb") as f:
                amministratori = dict(pickle.load(f))
                return amministratori.get(matricola, None)
        else:
            return None


    @staticmethod
    def ricercaUtenteMatricola(matricola):
        lista = []
        if os.path.isfile("Dati/Amministratori.pickle"):
            with open("Dati/Amministratori.pickle", "rb") as f:
                amministratori = dict(pickle.load(f))
                for amministratore in amministratori.values():
                    if matricola in amministratore.getMatricola():
                        lista.append(amministratore)
        return lista


    @staticmethod
    def ricercaUtenteNomeCognome(nomeCognome):
        lista = []
        if os.path.isfile("Dati/Amministratori.pickle"):
            with open("Dati/Amministratori.pickle", "rb") as f:
                amministratori = dict(pickle.load(f))
                for amministratore in amministratori.values():
                    if nomeCognome in amministratore.getNome() + " " + amministratore.getCognome():
                        lista.append(amministratore)
        return lista


