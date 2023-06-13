from login import Ui_Form
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import*
from MyWin import MyWindown
import sqlite3
from PyQt6.QtGui import QIcon

class MyLogin(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon("icon.png"))
        self.ui.loginButton.clicked.connect(self.loginFunction)
        self.show()


    def loginFunction(self):
        # self.con, self.cur = Database.connection.DBconnection.get_connection()
        con = sqlite3.connect('studentManageDB.db')
        cur = con.cursor()
        loginName = self.ui.usernametxt.text()
        password = self.ui.passtxt.text()
        sql = f"SELECT loginName, pass FROM nhan_vien_quan_ly WHERE loginName = '{loginName}' and pass='{password}'"
        cur.execute(sql)
        values = cur.fetchall()
        try:
            key = False
            for i in values:
                for j in range(len(values)):
                    if loginName == i[j] and password == i[j+1]:
                        key = True
                        cur.close()
                        con.close()
                    else:
                        key = False
            if key == True:
                self.close()
                QMessageBox.information(self, 'Message', 'Login success')
                # Turn to windown page
                self.close()
                open = QtWidgets.QWidget()
                self.ui = MyWindown()
                open.show()
            else:
                QMessageBox.information(self, 'Message', 'Login Failed! Read file README plese!')
        except:
            QMessageBox.information(self, 'Message', 'Error!!!')
