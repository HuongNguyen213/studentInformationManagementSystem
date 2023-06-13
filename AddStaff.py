from PyQt6 import QtWidgets
from PyQt6.QtWidgets import*
from AddStaffInfor import Ui_Form
import datetime
import random
import sqlite3
from PyQt6.QtGui import QIcon

class AddStaff(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon("icon.png"))
        self.ui.saveStaff.clicked.connect(self.saveFucntion)
        self.ui.pushButton.clicked.connect(self.backFunction)
        self.show()


    def saveFucntion(self):
        try:
            # connect database
            self.con = sqlite3.connect('studentManageDB.db')
            self.cur = self.con.cursor()

            # Get the student data from the form
            code = f"{datetime.datetime.now().year}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}"
            name = self.ui.staffName.text()
            dob = self.ui.dateEdit_2.date().toString("yyyy-MM-dd")
            phone = self.ui.staffPhone.text()
            address = self.ui.staffAddress.text()
            log = f"{code}@"
            password = self.ui.staffPass.text()
            email = f"{code}@gmail.com"
            add_at = datetime.datetime.now().strftime("%Y-%m-%d")

            # Kiểm tra xem thông tin sản phẩm có đầy đủ hay không
            if not name or not dob or not phone or not address or not password:
                # QMessageBox.warning(self, "Lỗi", "Vui lòng điền đầy đủ thông tin sản phẩm")
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText("Please fill out the information completely")
                msg.setWindowTitle("Notification")
                msg.setWindowIcon(QIcon("icon.png"))
                msg.exec_()
                return


            query = f"Insert into nhan_vien_quan_ly(code, name, DoB, phone, email, address, loginName, pass, add_at) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"
            values = (code, name.title() , dob, phone, email, address.title() , log, password, add_at)
            self.cur.execute(query, values)
            self.con.commit()
            # self.cur.close()
            self.con.close()

            QMessageBox.information(self, 'Message', 'Success')

            self.ui.staffName.setText('')
            self.ui.dateEdit_2.date().toString("yyyy-MM-dd")
            self.ui.staffPhone.setText('')
            self.ui.staffAddress.setText('')
            self.ui.staffPass.setText('')
        except:
            QMessageBox.information(self, 'Message', 'Please fill out the information completely')

    def backFunction(self):
        self.close()
