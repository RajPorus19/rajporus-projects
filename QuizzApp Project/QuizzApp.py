# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import random

class Ui_MyApp(object):
    
    def setupUi(self, MyApp):
        MyApp.setObjectName("MyApp")
        MyApp.resize(656, 520)
        self.centralwidget = QtWidgets.QWidget(MyApp)
        self.centralwidget.setObjectName("centralwidget")
        self.button1 = QtWidgets.QPushButton(self.centralwidget)
        self.button1.setGeometry(QtCore.QRect(550, 410, 81, 51))
        self.button1.setObjectName("button1")

        self.button1.clicked.connect(self.startQuizz)

        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(30, 40, 641, 131))
        self.label1.setObjectName("label1")
        self.buttonA = QtWidgets.QPushButton(self.centralwidget)
        self.buttonA.setGeometry(QtCore.QRect(160, 290, 91, 41))
        self.buttonA.setText("")
        self.buttonA.setObjectName("buttonA")

        self.buttonA.clicked.connect(self.functionA)

        self.buttonC = QtWidgets.QPushButton(self.centralwidget)
        self.buttonC.setGeometry(QtCore.QRect(160, 370, 91, 41))
        self.buttonC.setText("")
        self.buttonC.setObjectName("buttonC")

        self.buttonC.clicked.connect(self.functionC)

        self.buttonB = QtWidgets.QPushButton(self.centralwidget)
        self.buttonB.setGeometry(QtCore.QRect(370, 290, 91, 41))
        self.buttonB.setText("")
        self.buttonB.setObjectName("buttonB")

        self.buttonB.clicked.connect(self.functionB)

        self.buttonD = QtWidgets.QPushButton(self.centralwidget)
        self.buttonD.setGeometry(QtCore.QRect(370, 370, 91, 41))
        self.buttonD.setText("")
        self.buttonD.setObjectName("buttonD")

        self.buttonD.clicked.connect(self.functionD)

        self.question = QtWidgets.QLabel(self.centralwidget)
        self.question.setGeometry(QtCore.QRect(140, 190, 381, 61))
        self.question.setText("")
        self.question.setObjectName("question")
        MyApp.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MyApp)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 656, 21))
        self.menubar.setObjectName("menubar")
        self.menuMyQuizzApp = QtWidgets.QMenu(self.menubar)
        self.menuMyQuizzApp.setObjectName("menuMyQuizzApp")
        MyApp.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MyApp)
        self.statusbar.setObjectName("statusbar")
        MyApp.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuMyQuizzApp.menuAction())

        self.retranslateUi(MyApp)
        QtCore.QMetaObject.connectSlotsByName(MyApp)

    def retranslateUi(self, MyApp):
        _translate = QtCore.QCoreApplication.translate
        MyApp.setWindowTitle(_translate("MyApp", "TheApp"))
        self.button1.setText(_translate("MyApp", "start the quizz"))
        self.label1.setText(_translate("MyApp", "<html><head/><body><p><span style=\" font-size:72pt;\">The quizz app</span></p></body></html>"))
        self.menuMyQuizzApp.setTitle(_translate("MyApp", "MyQuizzApp"))
    
    def startQuizz(self):
        capitalDict = {"AFGHANISTAN":"KABUL",
        "ALBANIA":"TIRANA",
        "ALGERIA":"ALGIERS",
        "ANDORRA":"ANDORRA LA VELLA",
        "ANGOLA":"LUANDA",
        "ANTIGUA & BARBUDA":"SAINT JOHN'S",
        "ARGENTINA":"BUENOS AIRES",
        "ARMENIA":"YEREVAN",
        "AUSTRALIA":"CANBERRA",
        "AUSTRIA":"VIENNA",
        "AZERBAIJAN":"BAKU",
        "BAHAMAS":"NASSAU",
        "BAHRAIN":"MANAMA",
        "BANGLADESH":"DHAKA",
        "BARBADOS":"BRIDGETOWN",
        "BELARUS":"MINSK",
        "BELGIUM":"BRUSSELS",
        "BELIZE":"BELMOPAN",
        "BENIN":"PORTO-NOVO",
        "BHUTAN":"THIMPHU",
        "BOLIVIA":"SUCRE",
        "BOSNIA & HERZEGOVINA":"SARAJEVO",
        "BOTSWANA":"GABORONE",
        "BRAZIL":"BRASILIA",
        "BRUNEI":"BANDAR SERI BEGAWAN",
        "BULGARIA":"SOFIA",
        "BURKINA FASO":"OUAGADOUGOU",
        "BURUNDI":"BUJUMBURA",
        "CABO VERDE":"PRAIA"}

        randomCountry = random.choice(list(capitalDict))
        randomCapital = capitalDict.get(randomCountry)
        choiceList = [randomCapital,capitalDict.get(random.choice(list(capitalDict))),capitalDict.get(random.choice(list(capitalDict))),capitalDict.get(random.choice(list(capitalDict)))]
        newList = random.sample(choiceList,4)
        self.question.setText("What is the capital of "+randomCountry+" ?")
        self.buttonA.setText(newList[0])
        self.buttonB.setText(newList[1])
        self.buttonC.setText(newList[2])
        self.buttonD.setText(newList[3])
        global globalCapital 
        globalCapital = randomCapital


    def functionA(self):
        if self.buttonA.text() == globalCapital:
            print("You won !")
            self.startQuizz()
        else:
            print("You are wrong !")
    def functionB(self):
        if self.buttonB.text() == globalCapital:
            print("You won !")
            self.startQuizz()
        else:
            print("You are wrong !")
    def functionC(self):
        if self.buttonC.text() == globalCapital:
            print("You won !")
            self.startQuizz()
        else:
            print("You are wrong !")
    def functionD(self):
        if self.buttonD.text() == globalCapital:
            print("You won !")
            self.startQuizz()
        else:
            print("You are wrong !")




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MyApp = QtWidgets.QMainWindow()
    ui = Ui_MyApp()
    ui.setupUi(MyApp)
    MyApp.show()
    sys.exit(app.exec_())
