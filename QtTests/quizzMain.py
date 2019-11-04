# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys,os

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(182, 225)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 160, 171))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)

        self.openNewQuizzButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.openNewQuizzButton.setObjectName("openNewQuizzButton")
        self.openNewQuizzButton.clicked.connect(self.newQuizz)

        self.verticalLayout.addWidget(self.openNewQuizzButton)
        self.openQuizzButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.openQuizzButton.setObjectName("openQuizzButton")
        self.verticalLayout.addWidget(self.openQuizzButton)
        self.editQuizzButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.editQuizzButton.setObjectName("editQuizzButton")
        self.verticalLayout.addWidget(self.editQuizzButton)
        self.exitButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.exitButton.setObjectName("exitButton")
        self.verticalLayout.addWidget(self.exitButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 182, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        
        self.openQuizzButton.clicked.connect(self.openQuizz)
        self.exitButton.clicked.connect(sys.exit)

    def newQuizz(self):
        os.system("python3 NameNewQuizz.py")
    
    def openQuizz(self):
        print("open quizz")
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Quizz maker"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">Quizz maker</span></p></body></html>"))
        self.openNewQuizzButton.setText(_translate("MainWindow", "New quizz"))
        self.openQuizzButton.setText(_translate("MainWindow", "Open quizz"))
        self.editQuizzButton.setText(_translate("MainWindow", "Edit quizz"))
        self.exitButton.setText(_translate("MainWindow", "Exit"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

