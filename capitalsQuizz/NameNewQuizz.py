# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newquizz.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import os,sys

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(320, 174)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 10, 251, 61))
        self.label.setObjectName("label")
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(80, 80, 160, 80))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.quizzNameLineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.quizzNameLineEdit.setObjectName("quizzNameLineEdit")
        self.verticalLayout.addWidget(self.quizzNameLineEdit)
        self.enterButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.enterButton.setObjectName("enterButton")
        self.verticalLayout.addWidget(self.enterButton)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.enterButton.clicked.connect(self.getNewQuizz)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Enter the name of your quizz</span></p></body></html>"))
        self.quizzNameLineEdit.setPlaceholderText(_translate("Form", "History, Capitals, etc..."))
        self.enterButton.setText(_translate("Form", "Enter"))
    def getNewQuizz(self):
        fileName = (self.quizzNameLineEdit.text()+".txt").replace(" ","_")
        os.system("touch "+fileName)
        with open("allTheQuizzes.txt", "a") as text_file:
            text_file.write(fileName)
        sys.exit()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

