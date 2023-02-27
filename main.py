import locale
import sys
import time
import schedule

from PyQt5.QtWidgets import QApplication
from Controller.gestioneSchedule import GestioneSchedule
from View.Generale.login import Login

schedule.every().day.at("00:00").do(GestioneSchedule.backup)
schedule.every().day.at("00:00").do(GestioneSchedule.sospensioneAccount)
schedule.every().day.at("19:30").do(GestioneSchedule.scadenzaPrenotazioni)
schedule.every().monday.at("00:00").do(GestioneSchedule.azzeraPrenotazioni)


if __name__ == '__main__':
    closing = False
    locale.setlocale(locale.LC_ALL, "it_IT.utf8")
    app = QApplication(sys.argv)
    login = Login()
    login.stackedWidget.setCurrentIndex(0)
    login.show()
    try:
        sys.exit(app.exec_())
    except:
        print("Exting")
        closing = True
    while 1:
        schedule.run_pending()
        if closing:
            break
        time.sleep(10)





