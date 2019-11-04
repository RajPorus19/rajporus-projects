from PyQt5 import QtCore, QtGui, QtWidgets
import sys

if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	bt1 = QtWidgets.QPushButton('this a button')

	bt1.clicked.connect(sys.exit)


	bt1.show()
	app.exec_()