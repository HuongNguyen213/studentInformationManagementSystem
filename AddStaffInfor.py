# Form implementation generated from reading ui file 'AddStaffInfor.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1000, 406)
        Form.setStyleSheet("background-color: rgb(169, 193, 235);\n"
"alternate-background-color: rgb(162, 185, 226);")
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(-110, -1, 1111, 141))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("sms.PNG"))
        self.label.setObjectName("label")
        self.groupBox = QtWidgets.QGroupBox(parent=Form)
        self.groupBox.setGeometry(QtCore.QRect(20, 160, 961, 191))
        self.groupBox.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(168, 192, 234);")
        self.groupBox.setObjectName("groupBox")
        self.label_3 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(30, 40, 111, 31))
        self.label_3.setObjectName("label_3")
        self.staffName = QtWidgets.QLineEdit(parent=self.groupBox)
        self.staffName.setGeometry(QtCore.QRect(160, 40, 241, 31))
        self.staffName.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(238, 238, 238);")
        self.staffName.setObjectName("staffName")
        self.label_4 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(30, 90, 111, 31))
        self.label_4.setObjectName("label_4")
        self.staffPhone = QtWidgets.QLineEdit(parent=self.groupBox)
        self.staffPhone.setGeometry(QtCore.QRect(160, 140, 241, 31))
        self.staffPhone.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(238, 238, 238);")
        self.staffPhone.setObjectName("staffPhone")
        self.label_5 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(30, 140, 111, 31))
        self.label_5.setObjectName("label_5")
        self.dateEdit_2 = QtWidgets.QDateEdit(parent=self.groupBox)
        self.dateEdit_2.setGeometry(QtCore.QRect(160, 90, 241, 31))
        self.dateEdit_2.setStyleSheet("background-color: rgb(238, 238, 238);")
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.label_7 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(560, 40, 111, 31))
        self.label_7.setObjectName("label_7")
        self.label_9 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_9.setGeometry(QtCore.QRect(560, 90, 111, 31))
        self.label_9.setObjectName("label_9")
        self.staffPass = QtWidgets.QLineEdit(parent=self.groupBox)
        self.staffPass.setGeometry(QtCore.QRect(710, 90, 241, 31))
        self.staffPass.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(238, 238, 238);")
        self.staffPass.setObjectName("staffPass")
        self.staffAddress = QtWidgets.QLineEdit(parent=self.groupBox)
        self.staffAddress.setGeometry(QtCore.QRect(710, 40, 241, 31))
        self.staffAddress.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(238, 238, 238);")
        self.staffAddress.setObjectName("staffAddress")
        self.saveStaff = QtWidgets.QPushButton(parent=self.groupBox)
        self.saveStaff.setGeometry(QtCore.QRect(820, 140, 131, 31))
        self.saveStaff.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(220, 220, 220);")
        self.saveStaff.setObjectName("saveStaff")
        self.pushButton = QtWidgets.QPushButton(parent=Form)
        self.pushButton.setGeometry(QtCore.QRect(840, 360, 131, 31))
        self.pushButton.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(220, 220, 220);")
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox.setTitle(_translate("Form", "Add Staff  Information"))
        self.label_3.setText(_translate("Form", "Staff name:"))
        self.label_4.setText(_translate("Form", "Date of birth:"))
        self.label_5.setText(_translate("Form", "Phone:"))
        self.label_7.setText(_translate("Form", "Address:"))
        self.label_9.setText(_translate("Form", "Password:"))
        self.saveStaff.setText(_translate("Form", "Save"))
        self.pushButton.setText(_translate("Form", "Back"))