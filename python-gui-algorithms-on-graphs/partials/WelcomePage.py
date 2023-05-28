from PyQt5 import QtCore, QtGui, QtWidgets
from partials.Matrix import Ui_Matrix

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel
from PyQt5.QtCore import QSize, Qt


class Ui_WelcomePage(object):
    def openWindow(self, Ui_Window, nodesNumber, graphType):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Window
        self.ui.setupUi(self.window, nodesNumber, graphType)
        self.window.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Welcome Page")
        MainWindow.resize(845, 581)

        font = QtGui.QFont()
        font.setBold(True)
        font.setFamily("Calibri")
        font.setPointSize(15)
        
        font2 = QtGui.QFont()
        font2.setFamily("Bradley Hand")
        font2.setPointSize(24)
        font2.setBold(True)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.label_0 = QtWidgets.QLabel(self.centralwidget)
        self.label_0.setGeometry(QtCore.QRect(0, 0, 845, 581))
        self.label_0.setFont(font)
        self.label_0.setStyleSheet("background-image: url(C:/Users/mohhd/Desktop/Tkinter-Designer-master/ProjectPython/build/assets/frame0/image_1.png); background-color: #D1CFFF;")
        self.label_0.setObjectName("label_0")
        
        
        self.label_0_0 = QtWidgets.QLabel(self.centralwidget)
        self.label_0_0.setGeometry(QtCore.QRect(530, 550, 303, 17))
        self.label_0_0.setStyleSheet("background-image: url(C:/Users/mohhd/Desktop/Images/image_2.png);")
        self.label_0_0.setObjectName("label_0_0")
        
        
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 140, 250, 50))
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(87, 30, 600, 100))
        self.label_3.setFont(font2)
        self.label_3.setObjectName("label_3")
        self.label_3.setText("Graph Type Selection: \nChoose Orientation and Other Info :")
        

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(71, 180, 700, 250))
        self.label_5.setStyleSheet("background-color: #F0F0F0;")
        self.label_5.setFont(font2)
        self.label_5.setFrameStyle(QtWidgets.QFrame.Box | QtWidgets.QFrame.Plain)
        self.label_5.setObjectName("label_5")
        
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(245, 370, 200, 50))
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        
        self.NotOrientedAndWeighted = QtWidgets.QRadioButton(self.centralwidget)
        self.NotOrientedAndWeighted.setGeometry(QtCore.QRect(500, 220, 200, 50))
        self.NotOrientedAndWeighted.setFont(font)
        self.NotOrientedAndWeighted.setObjectName("NotOrientedAndWeighted")

        self.NotOrientedAndNotWeighted = QtWidgets.QRadioButton(self.centralwidget)
        self.NotOrientedAndNotWeighted.setGeometry(QtCore.QRect(180,220, 200, 50))
        self.NotOrientedAndNotWeighted.setFont(font)
        self.NotOrientedAndNotWeighted.setObjectName("NotOrientedAndNotWeighted")

        self.OrientedAndNotWeighted = QtWidgets.QRadioButton(self.centralwidget)
        self.OrientedAndNotWeighted.setGeometry(QtCore.QRect(180, 290, 200, 50))
        self.OrientedAndNotWeighted.setFont(font)
        self.OrientedAndNotWeighted.setObjectName("OrientedAndNotWeighted")

        self.OrientedAndWeighted = QtWidgets.QRadioButton(self.centralwidget)
        self.OrientedAndWeighted.setGeometry(QtCore.QRect(500, 290,200, 50))
        self.OrientedAndWeighted.setFont(font)
        self.OrientedAndWeighted.setObjectName("OrientedAndWeighted")

        self.nodesNumber = QtWidgets.QLineEdit(self.centralwidget)
        self.nodesNumber.setGeometry(QtCore.QRect(420,388, 113, 20))
        self.nodesNumber.setObjectName("nodesNumber")

        self.graphInfoBtn = QtWidgets.QPushButton(self.centralwidget)
        self.graphInfoBtn.setGeometry(QtCore.QRect(370, 450, 101, 31))
        self.graphInfoBtn.setObjectName("graphInfoBtn")
        self.graphInfoBtn.setStyleSheet("background-color: #0000FF; color: #FFFFFF; font-weight: bold; font-size: 30;")

        self.graphInfoBtn.clicked.connect(self.openMatrix)

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Accueil"))
        self.label_4.setText(_translate("MainWindow", "L\'ordre du graphe :"))
        self.label_2.setText(_translate("MainWindow", "Choisir le type de graphe :"))
        self.graphInfoBtn.setText(_translate("MainWindow", "OK"))
        self.NotOrientedAndWeighted.setText(_translate("MainWindow", "Non orienté et\n pondéré"))
        self.NotOrientedAndNotWeighted.setText(_translate("MainWindow", "Non orienté et\nnon pondéré"))
        self.OrientedAndNotWeighted.setText(_translate("MainWindow", "Orienté et\nnon pondéré"))
        self.OrientedAndWeighted.setText(_translate("MainWindow", "Orienté et\npondéré"))

    def openMatrix(self):
        global graphType
        nodesNumber = int(self.nodesNumber.text())
        if self.OrientedAndWeighted.isChecked():
            graphType = "dp"
        if self.OrientedAndNotWeighted.isChecked():
            graphType = "dn"
        if self.NotOrientedAndWeighted.isChecked():
            graphType = "up"
        if self.NotOrientedAndNotWeighted.isChecked():
            graphType = "un"

        self.openWindow(Ui_Matrix(), nodesNumber, graphType)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WelcomePage = QtWidgets.QMainWindow()
    WelcomePage.setFixedSize(845, 581)
    ui = Ui_WelcomePage()
    ui.setupUi(WelcomePage)
    WelcomePage.show()
    sys.exit(app.exec_())
