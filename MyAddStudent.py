import random
from AddStudentInfor import Ui_Dialog
from PyQt6 import QtWidgets, QtCore
from PyQt6.QtWidgets import*
from Windown import Ui_MainWindow
import datetime
import sqlite3
from PyQt6.QtGui import QIcon

class AddStudent(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon("icon.png"))
        self.ui.saveAddStudent.clicked.connect(self.saveFucntion)
        self.ui.backButton.clicked.connect(self.backFunction)
        self.show()

    def saveFucntion(self):

        try:
            # connect database
            self.con = sqlite3.connect('studentManageDB.db')
            self.cur = self.con.cursor()

            # get data
            code = f"{datetime.datetime.now().year}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}"
            name = self.ui.studentName.text()
            dob = self.ui.dateStu.date().toString("yyyy-MM-dd")
            address = self.ui.studentAddress.text()
            major = self.ui.studentMajor.text()
            class_name = self.ui.studentClass.text()
            program = self.ui.studentProgram.text()
            uni_years = self.ui.studentUni.text()
            email = f"{code}@eaut.edu.vn"
            add_at = datetime.datetime.now().strftime("%Y-%m-%d")

            # Kiểm tra xem thông tin có đầy đủ hay không
            if not name or not dob or not address or not major or not class_name or not program or not uni_years:
                # QMessageBox.warning(self, "Lỗi", "Vui lòng điền đầy đủ thông tin sản phẩm")
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText("Please fill out the information completely")
                msg.setWindowTitle("Notification")
                msg.setWindowIcon(QIcon("icon.png"))
                msg.exec_()
                return

            # transmit data
            query = f"Insert into sinh_vien(code, name, DoB, email, address, major, class, program, uni_years, add_at) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
            values = (code, name.title(), dob, email, address.title(), major.upper(), class_name.upper(), program.capitalize(), uni_years, add_at)
            self.cur.execute(query, values)
            self.con.commit()
            self.con.close()

            QMessageBox.information(self, 'Message', 'Success')

            self.ui.studentName.setText('')
            self.ui.dateStu.date().toString("yyyy-MM-dd")
            self.ui.studentAddress.setText('')
            self.ui.studentMajor.setText('')
            self.ui.studentClass.setText('')
            self.ui.studentProgram.setText('')
            self.ui.studentUni.setText('')
            # self.ui.groupStudentBox.setCurrentIndex(0)
        except:
            QMessageBox.information(self, 'Message', 'Please fill out the information completely')


    def backFunction(self):
        self.close()
