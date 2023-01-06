import locale

from sys import exit, argv
from PyQt5.QtWidgets import QApplication

from View.login import Login


if __name__ == '__main__':
    locale.setlocale(locale.LC_ALL, "it")
    app = QApplication(argv)
    login = Login()
    login.stackedWidget.setCurrentIndex(0)
    login.show()
    try:
        exit(app.exec())
    except:
        print("Exting")
