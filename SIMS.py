import sys
from MyLog import MyLogin
from PyQt6.QtWidgets import*
import sqlite3


if __name__ == '__main__':
    con = sqlite3.connect('studentManageDB.db')
    app = QApplication(sys.argv)
    log = MyLogin()
    log.show()
    sys.exit(app.exec())
