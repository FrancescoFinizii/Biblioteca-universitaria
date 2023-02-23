import datetime
import json
import os
import pickle
import shutil
import sys
from datetime import date

from Controller.gestionePrenotazioni import GestionePrenotazioni
from Controller.gestioneStudenti import GestioneStudenti


class GestioneSchedule:


    @staticmethod
    def backup():
        os.chdir(sys.path[0])
        file_name = date.today().strftime("%d_%b_%Y_")
        dst_dir = "Backup/" + file_name
        try:
            shutil.copytree("Dati", dst_dir)
            print("Backup eseguito con successo")
        except FileNotFoundError:
            print("Si è verificato un errore. Backup non eseguito")


    @staticmethod
    def sospensioneAccount():
        with open("Dati/Prestiti.pickle", "rb") as f:
            prestiti = pickle.load(f)
            for prestito in prestiti.values():
                if datetime.date.today() > prestito.getDataScadenza():
                    GestioneStudenti.sospendiAccount(prestito.getMatricolaStudente())


    @staticmethod
    def scadenzaPrenotazioni():
        with open("Dati/Prenotazioni.pickle", "rb") as f:
            prenotazioni = pickle.load(f)
            for prenotazione in prenotazioni.values():
                if datetime.date.today() == prenotazione.getData() and datetime.datetime.now().time() > prenotazione.getOraFine():
                    GestionePrenotazioni.rimuoviPrenotazione(prenotazione.getMatricolaStudente())


    @staticmethod
    def azzeraPrenotazioni():
        with open("Dati/prenotazioni.json", "r") as f:
            jsonFile = json.load(f)
            for sede in jsonFile:
                for giorno in jsonFile[sede]:
                    for turno in jsonFile[sede][giorno]:
                        jsonFile[sede][giorno][turno] = 0
        with open("Dati/prenotazioni.json", "w") as f:
            json.dump(jsonFile, f)
