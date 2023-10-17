import json
import os
import pickle
from datetime import time

from Model.prenotazione import Prenotazione


class GestionePrenotazioni:

    dir_path = os.path.dirname(os.path.dirname(__file__))
    percorsoFile = os.path.join(dir_path, 'Dati', "Prenotazioni.pickle")
    percorsoJSONFile = os.path.join(dir_path, 'Dati', "prenotazioni.json")

    @staticmethod
    def aggiungiPrenotazione(matricolaStudente, sede, data, oraInizio, oraFine):
        prenotazione = Prenotazione(matricolaStudente, sede, data, oraInizio, oraFine)
        if os.path.isfile(GestionePrenotazioni.percorsoFile):
            with open(GestionePrenotazioni.percorsoFile, "rb") as f:
                prenotazioni = pickle.load(f)
        else:
            prenotazioni = {}
        prenotazioni[matricolaStudente] = prenotazione
        with open(GestionePrenotazioni.percorsoFile, "wb") as f:
            pickle.dump(prenotazioni, f, pickle.HIGHEST_PROTOCOL)
        with open(GestionePrenotazioni.percorsoJSONFile, "r") as f:
            jsonFile = json.load(f)
        turni = list(jsonFile[sede][data.strftime("%A")[0:3]].keys())
        bool = False
        for turno in turni:
            if bool == True and time(hour=int(turno[6:8]), minute=int(turno[9:11])) <= oraFine:
                jsonFile[sede][data.strftime("%A")[0:3]][turno] += 1
            if time(hour=int(turno[0:2]), minute=int(turno[3:5])) == oraInizio:
                bool = True
                jsonFile[sede][data.strftime("%A")[0:3]][turno] += 1
        with open(GestionePrenotazioni.percorsoJSONFile, "w") as f:
            json.dump(jsonFile, f)


    @staticmethod
    def rimuoviPrenotazione(matricolaStudente):
        with open(GestionePrenotazioni.percorsoFile, "rb") as f:
            prenotazioni = pickle.load(f)
            sede = prenotazioni[matricolaStudente].getSede()
            data = prenotazioni[matricolaStudente].getData()
            oraInizio = prenotazioni[matricolaStudente].getOraInizio()
            oraFine = prenotazioni[matricolaStudente].getOraFine()
            del prenotazioni[matricolaStudente]
        with open(GestionePrenotazioni.percorsoFile, "wb") as f:
            pickle.dump(prenotazioni, f, pickle.HIGHEST_PROTOCOL)
        with open(GestionePrenotazioni.percorsoJSONFile, "r") as f:
            jsonFile = json.load(f)
        turni = list(jsonFile[sede][data.strftime("%A")[0:3]].keys())
        bool = False
        for turno in turni:
            if bool == True and time(hour=int(turno[6:8]), minute=int(turno[9:11])) <= oraFine:
                jsonFile[sede][data.strftime("%A")[0:3]][turno] -= 1
            if time(hour=int(turno[0:2]), minute=int(turno[3:5])) == oraInizio:
                bool = True
                jsonFile[sede][data.strftime("%A")[0:3]][turno] -= 1
        with open(GestionePrenotazioni.percorsoJSONFile, "w") as f:
            json.dump(jsonFile, f)



    @staticmethod
    def getPrenotazione(matricolaStudente):
        if os.path.isfile(GestionePrenotazioni.percorsoFile):
            with open(GestionePrenotazioni.percorsoFile, "rb") as f:
                prenotazioni = pickle.load(f)
                return prenotazioni.get(matricolaStudente, None)
        else:
            return None


    @staticmethod
    def ricercaPrenotazione(matricolaStudente, sede):
        lista = []
        if os.path.isfile(GestionePrenotazioni.percorsoFile):
            with open(GestionePrenotazioni.percorsoFile, "rb") as f:
                prenotazioni = pickle.load(f)
                for prenotazione in prenotazioni.values():
                    if matricolaStudente in prenotazione.getMatricolaStudente():
                        if sede != "Tutte le sedi":
                            if prenotazione.getSede() == sede:
                                lista.append(prenotazione)
                        else:
                            lista.append(prenotazione)
        return lista
