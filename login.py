# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(623, 366)
        Form.setStyleSheet("")
        self.label_2 = QtWidgets.QLabel(parent=Form)
        self.label_2.setGeometry(QtCore.QRect(30, 138, 131, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.passtxt = QtWidgets.QLineEdit(parent=Form)
        self.passtxt.setGeometry(QtCore.QRect(190, 190, 391, 41))
        self.passtxt.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.passtxt.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.passtxt.setObjectName("passtxt")
        self.usernametxt = QtWidgets.QLineEdit(parent=Form)
        self.usernametxt.setGeometry(QtCore.QRect(190, 130, 391, 41))
        self.usernametxt.setObjectName("usernametxt")
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(340, 30, 111, 51))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(26)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label.setFont(font)
        self.label.setStyleSheet("font: 75 26pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(parent=Form)
        self.label_3.setGeometry(QtCore.QRect(30, 190, 121, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.loginButton = QtWidgets.QPushButton(parent=Form)
        self.loginButton.setGeometry(QtCore.QRect(490, 280, 81, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.loginButton.setFont(font)
        self.loginButton.setObjectName("loginButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "User Name"))
        self.label.setText(_translate("Form", "Login"))
        self.label_3.setText(_translate("Form", "Password"))
        self.loginButton.setText(_translate("Form", "Login"))
