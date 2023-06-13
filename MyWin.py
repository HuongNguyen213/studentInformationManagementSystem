import sys
from Windown import Ui_MainWindow
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import*
from MyAddStudent import AddStudent
from AddStudentInfor import Ui_Dialog
from AddStaff import AddStaff
import datetime
import sqlite3
from exit import MyExit
from xlrd import *
from xlsxwriter import *
from PyQt6.QtGui import QIcon

class MyWindown(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon("icon.png"))
        self.ui.updateButton_3.clicked.connect(self.updateStudent)
        self.ui.updateStaffButton.clicked.connect(self.updateStaff)
        self.ui.deleteButton_6.clicked.connect(self.deleteStudent)
        self.ui.deleteStaffButton.clicked.connect(self.deleteStaff)
        self.ui.refreshButton_5.clicked.connect(self.showStudentData)
        self.ui.refreshButton.clicked.connect(self.refreshStaff)
        self.ui.editButton_4.clicked.connect(self.editStudent)
        self.ui.editStaffButton.clicked.connect(self.editStaff)
        self.ui.pushButton_7.clicked.connect(self.searchStu)
        self.ui.searchStaffButton.clicked.connect(self.searchStaff)
        self.ui.exitButton_2.clicked.connect(self.exitFunction)
        self.ui.pushButton_13.clicked.connect(self.exitFunction)
        self.ui.exportStu.clicked.connect(self.exportStuFunction)
        self.ui.exportSta.clicked.connect(self.exportStaffFunction)
        self.showStudentData()
        self.showStaffData()
        self.show()

    def exportStuFunction(self):
        try:
            self.conn = sqlite3.connect('studentManageDB.db')
            self.cur = self.conn.cursor()
            sql = f"Select code, name, DoB, email, address, major, class, program, uni_years from sinh_vien where delete_at is NULL"
            self.cur.execute(sql)
            data = self.cur.fetchall()
            stu = Workbook('Student.xlsx')
            sheet1 = stu.add_worksheet()

            sheet1.write(0, 0, 'ID')
            sheet1.write(0, 1, 'Name')
            sheet1.write(0, 2, 'DoB')
            sheet1.write(0, 3, 'email')
            sheet1.write(0, 4, 'address')
            sheet1.write(0, 5, 'major')
            sheet1.write(0, 6, 'class')
            sheet1.write(0, 7, 'program')
            sheet1.write(0, 8, 'uni_years')

            row_number = 1
            for row in data:
                column_number = 0
                for item in row:
                    sheet1.write(row_number, column_number, str(item))
                    column_number += 1
                row_number += 1

            stu.close()
            self.statusBar().showMessage('Student Report Created Successfully')
        except:
            self.statusBar().showMessage('Error')


    def exportStaffFunction(self):
        try:
            self.conn = sqlite3.connect('studentManageDB.db')
            self.cur = self.conn.cursor()
            sql = f"Select code, name, DoB, phone, email, address from nhan_vien_quan_ly where delete_at is NULL and code <> 'admin'"
            self.cur.execute(sql)
            data = self.cur.fetchall()
            staff = Workbook('Staff_Manage.xlsx')
            sheet1 = staff.add_worksheet()

            sheet1.write(0, 0, 'ID')
            sheet1.write(0, 1, 'Name')
            sheet1.write(0, 2, 'DoB')
            sheet1.write(0, 3, 'phone')
            sheet1.write(0, 4, 'email')
            sheet1.write(0, 5, 'address')

            row_number = 1
            for row in data:
                column_number = 0
                for item in row:
                    sheet1.write(row_number, column_number, str(item))
                    column_number += 1
                row_number += 1

            staff.close()
            self.statusBar().showMessage('Staff Report Created Successfully')
        except:
            self.statusBar().showMessage('Error')

    # show table data to gui
    def showStudentData(self):
        try:
            self.con = sqlite3.connect('studentManageDB.db')
            self.cur = self.con.cursor()
            sql = f"Select code, name, DoB, email, address, major, class, program, uni_years from sinh_vien where delete_at is NULL"
            self.cur.execute(sql)
            values = self.cur.fetchall()
            self.ui.tableStu.setRowCount(0)
            for row, form in enumerate(values):
                self.ui.tableStu.insertRow(row)
                for column, item in enumerate(form):
                    self.ui.tableStu.setItem(row, column, QTableWidgetItem(str(item)))
            self.con.close()
        except:
            QMessageBox.information(self, 'Message', 'The showStudentData Function Error!!!')

    # Show table staff data
    def showStaffData(self):
        try:
            self.con = sqlite3.connect('studentManageDB.db')
            self.cur = self.con.cursor()
            sql = f"Select code, name, DoB, phone, email, address, loginName, pass from nhan_vien_quan_ly where delete_at is NULL and code <> 'admin'"
            self.cur.execute(sql)
            values = self.cur.fetchall()
            self.ui.tableWidget_2.setRowCount(0)
            for row, form in enumerate(values):
                self.ui.tableWidget_2.insertRow(row)
                for column, item in enumerate(form):
                    self.ui.tableWidget_2.setItem(row, column, QTableWidgetItem(str(item)))
            self.con.close()
        except:
            QMessageBox.information(self, 'Message', 'The showStaffData Function Error!!!')

    # insert student
    def updateStudent(self):
        try:
            open = QtWidgets.QDialog()
            self.ui2 = AddStudent()
            open.show()
        except:
            QMessageBox.information(self, 'Message', 'The updateStudentData Function Error!!!')

    # insert Staff
    def updateStaff(self):
        try:
            # self.close()
            openStaff = QtWidgets.QWidget()
            self.ui1 = AddStaff()
            openStaff.show()
        except:
            QMessageBox.information(self, 'Message', 'The updateStafftData Function Error!!!')

    # delete Student
    def deleteStudent(self):
        try:
            selected_row = self.ui.tableStu.currentRow()
            code = self.ui.tableStu.item(selected_row, 0).text()
            # print(selected_row)
            # print(code)
            delete_at = datetime.datetime.now().strftime("%Y-%m-%d")

            self.con = sqlite3.connect('studentManageDB.db')
            self.cur = self.con.cursor()
            query = f"Update sinh_vien Set delete_at = '{delete_at}' WHERE code = '{code}'"
            self.cur.execute(query)
            self.con.commit()
            # self.cur.close()
            self.con.close()
            QMessageBox.information(self, 'Message', 'Success')
        except:
            QMessageBox.information(self, 'Message', 'Delete failed')

    # delete Staff
    def deleteStaff(self):
        try:
            selected_row = self.ui.tableWidget_2.currentRow()
            code = self.ui.tableWidget_2.item(selected_row, 0).text()
            # print(selected_row)
            # print(code)
            delete_at = datetime.datetime.now().strftime("%Y-%m-%d")
            self.con = sqlite3.connect('studentManageDB.db')
            self.cur = self.con.cursor()
            query = f"Update nhan_vien_quan_ly Set delete_at = '{delete_at}' WHERE code = '{code}'"
            self.cur.execute(query)
            self.con.commit()
            # self.cur.close()
            self.con.close()
            QMessageBox.information(self, 'Message', 'Success')
        except:
            QMessageBox.information(self, 'Message', 'Delete failed')

    # edit Student
    def editStudent(self):
        try:
            update_at = datetime.datetime.now().strftime("%Y-%m-%d")
            try:
                for row in range(self.ui.tableStu.rowCount()):
                    code = self.ui.tableStu.item(row, 0).text()
                    name = self.ui.tableStu.item(row, 1).text()
                    dob = self.ui.tableStu.item(row, 2).text()
                    address = self.ui.tableStu.item(row, 4).text()
                    major = self.ui.tableStu.item(row, 5).text()
                    clas = self.ui.tableStu.item(row, 6).text()
                    program = self.ui.tableStu.item(row, 7).text()
                    uni = self.ui.tableStu.item(row, 8).text()

                # connect Db
                self.con = sqlite3.connect('studentManageDB.db')
                self.cur = self.con.cursor()

                # transmit data
                query = f"Update sinh_vien Set update_at = '{update_at}', name = '{name}', DoB = '{dob}', address = '{address}', major ='{major}', class ='{clas}', program = '{program}', uni_years = '{uni}'  WHERE delete_at is NULL and code = '{code}'"
                self.cur.execute(query)
                self.con.commit()
                # cur.close()
                self.con.close()
                # self.ui.tableStu.currentRow().setText(str(self))
                QMessageBox.information(self, 'Message', 'Success')
            except:
                QMessageBox.information(self, 'Message', 'edit failed')
        except:
            QMessageBox.information(self, 'Message', 'edit failed')

    # edit Staff
    def editStaff(self):
        try:
            update_at = datetime.datetime.now().strftime("%Y-%m-%d")
            try:
                for row in range(self.ui.tableWidget_2.rowCount()):
                    code = self.ui.tableWidget_2.item(row, 0).text()
                    name = self.ui.tableWidget_2.item(row, 1).text()
                    dob = self.ui.tableWidget_2.item(row, 2).text()
                    phone = self.ui.tableWidget_2.item(row, 3).text()
                    address = self.ui.tableWidget_2.item(row, 5).text()
                    password = self.ui.tableWidget_2.item(row, 7).text()

                self.con = sqlite3.connect('studentManageDB.db')
                self.cur = self.con.cursor()
                query = f"Update nhan_vien_quan_ly Set update_at = '{update_at}', name = '{name}', DoB = '{dob}', phone = '{phone}', address = '{address}', pass ='{password}' WHERE delete_at is NULL and code = '{code}'"
                self.cur.execute(query)
                self.con.commit()
                self.con.close()
                # self.ui.tableWidget_2.currentRow().setText(str(self))
                QMessageBox.information(self, 'Message', 'Success')
            except:
                QMessageBox.information(self, 'Message', 'edit failed')
        except:
            QMessageBox.information(self, 'Message', 'edit failed')

    # search student
    def searchStu(self):
        try:
            if self.ui.tableStu.rowCount() > 0:
                self.ui.tableStu.removeRow(self.ui.tableStu.rowCount() - 1)
            con = sqlite3.connect('studentManageDB.db')
            cur = con.cursor()
            chooseItem = self.ui.comboBox_2.itemText(self.ui.comboBox_2.currentIndex())
            temp = self.ui.lineEdit_3.text()
            query = f"Select code, name, DoB, email, address, major, class, program, uni_years from sinh_vien where {chooseItem} = '{temp}' and delete_at is NULL"
            cur.execute(query)
            values = cur.fetchall()
            self.ui.tableStu.setRowCount(0)
            for row, form in enumerate(values):
                self.ui.tableStu.insertRow(row)
                for column, item in enumerate(form):
                    self.ui.tableStu.setItem(row, column, QTableWidgetItem(str(item)))
            self.ui.lineEdit_3.setText("")
        except:
            QMessageBox.information(self, 'Message', 'Search Error!!!')

    def searchStaff(self):
        try:
            if self.ui.tableWidget_2.rowCount() > 0:
                self.ui.tableWidget_2.removeRow(self.ui.tableWidget_2.rowCount() - 1)
            con = sqlite3.connect('studentManageDB.db')
            cur = con.cursor()
            chooseItem = self.ui.comboBox.itemText(self.ui.comboBox.currentIndex())
            temp = self.ui.lineEdit_4.text()
            query = f"Select code, name, DoB, phone, email, address, loginName, pass from nhan_vien_quan_ly where {chooseItem} = '{temp}' and delete_at is NULL"
            cur.execute(query)
            values = cur.fetchall()
            self.ui.tableWidget_2.setRowCount(0)
            for row, form in enumerate(values):
                self.ui.tableWidget_2.insertRow(row)
                for column, item in enumerate(form):
                    self.ui.tableWidget_2.setItem(row, column, QTableWidgetItem(str(item)))
            self.ui.lineEdit_4.setText("")
        except:
            QMessageBox.information(self, 'Message', 'Search Error!!!')

    # refresh Student data
    def refreshStudent(self):
        if self.ui.tableStu.rowCount() > 0:
            self.ui.tableStu.removeRow(self.ui.tableStu.rowCount()-1)
        self.showStudentData()

    # refresh Staff data
    def refreshStaff(self):
        if self.ui.tableWidget_2.rowCount() > 0:
            self.ui.tableWidget_2.removeRow(self.ui.tableWidget_2.rowCount()-1)
        self.showStaffData()

    # exit application
    def exitFunction(self):
        try:
            ex = QtWidgets.QWidget()
            self.ui4 = MyExit()
            ex.show()
        except:
            print("Errol")