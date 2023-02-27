import datetime
import json
import os
import pickle
import shutil
from datetime import date

from Controller.gestionePrenotazioni import GestionePrenotazioni
from Controller.gestioneStudenti import GestioneStudenti


class GestioneSchedule:


    dir_path = os.path.dirname(os.path.dirname(__file__))



    @staticmethod
    def backup():
        file_name = date.today().strftime("%d_%b_%Y_")
        percorsoBackup = os.path.join(GestioneSchedule.dir_path, 'Backup', file_name)
        percorsoDati= os.path.join(GestioneSchedule.dir_path, "Dati")
        try:
            shutil.copytree(percorsoDati, percorsoBackup)
            print("Backup eseguito con successo")
        except FileNotFoundError:
            print("Si è verificato un errore. Backup non eseguito")


    @staticmethod
    def sospensioneAccount():
        percorsoPrestiti = os.path.join(GestioneSchedule.dir_path, 'Dati', "Prestiti.pickle")
        with open(percorsoPrestiti, "rb") as f:
            prestiti = pickle.load(f)
            for prestito in prestiti.values():
                if datetime.date.today() > prestito.getDataScadenza():
                    GestioneStudenti.sospendiAccount(prestito.getMatricolaStudente())


    @staticmethod
    def scadenzaPrenotazioni():
        percorsoPrenotazioni = os.path.join(GestioneSchedule.dir_path, 'Dati', "Prenotazioni.pickle")
        with open(percorsoPrenotazioni, "rb") as f:
            prenotazioni = pickle.load(f)
            for prenotazione in prenotazioni.values():
                if datetime.date.today() == prenotazione.getData() and datetime.datetime.now().time() > prenotazione.getOraFine():
                    GestionePrenotazioni.rimuoviPrenotazione(prenotazione.getMatricolaStudente())


    @staticmethod
    def azzeraPrenotazioni():
        percorsoJSONFile = os.path.join(GestioneSchedule.dir_path, 'Dati', "prenotazioni.json")
        with open(percorsoJSONFile, "r") as f:
            jsonFile = json.load(f)
            for sede in jsonFile:
                for giorno in jsonFile[sede]:
                    for turno in jsonFile[sede][giorno]:
                        jsonFile[sede][giorno][turno] = 0
        with open(percorsoJSONFile, "w") as f:
            json.dump(jsonFile, f)
