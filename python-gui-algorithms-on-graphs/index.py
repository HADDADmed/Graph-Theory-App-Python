from PyQt5 import QtCore, QtGui, QtWidgets
from partials.Matrix import Ui_Matrix
import partials.WelcomePage as WelcomePage
from PyQt5.QtGui import QPixmap,QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel
from PyQt5.QtCore import QSize, Qt


class Ui_LandigPage(object):
    def openWindow(self, Ui_Window):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Window
        self.ui.setupUi(self.window)
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
        
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(150, 70, 525, 262))
        self.label_1.setStyleSheet("background-image: url(C:/Users/mohhd/Desktop/GrapheTheorieProject/python-gui-algorithms-on-graphs/assets/Images/image_3.png);")
        self.label_1.setObjectName("label_1")
        
        icon = QIcon('C:/Users/mohhd/Desktop/GrapheTheorieProject/python-gui-algorithms-on-graphs/assets/Images/button_1_1.png')

# set the icon on the button
        self.graphInfoBtn = QtWidgets.QPushButton(self.centralwidget)
        self.graphInfoBtn.setIcon(icon)
        self.graphInfoBtn.setIconSize(QtCore.QSize(170, 50))
        self.graphInfoBtn.setGeometry(QtCore.QRect(320, 385, 200, 35))
        self.graphInfoBtn.setObjectName("graphInfoBtn")
        self.graphInfoBtn.setStyleSheet("background-color: #2018C0; color: #FFFFFF; font-weight: bold; font-size: 30;")

        self.graphInfoBtn.clicked.connect(self.openMatrix)
 

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "LANDING PAGE"))

    def openMatrix(self):
        self.openWindow(WelcomePage.Ui_WelcomePage())

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WelcomePageW = QtWidgets.QMainWindow()
    WelcomePageW.setFixedSize(845, 581)
    ui = Ui_LandigPage()
    ui.setupUi(WelcomePageW)
    WelcomePageW.show()
    sys.exit(app.exec_())
