from PyQt5 import QtCore, QtWidgets,QtGui
from partials.GraphT import Ui_Graph

class Ui_Matrix(object):
    def openWindow(self, Ui_Window, matrix, nodesNumber, graphType):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Window
        self.ui.setupUi(self.window,nodesNumber,matrix, graphType)
        self.window.show()

    def setupUi(self, MainWindow, nodesNumber, graphType):
        print(nodesNumber, graphType)
        self.nodesNumber = nodesNumber
        self.graphType = graphType
        
        
        font = QtGui.QFont()
        font.setBold(True)
        font.setFamily("Calibri")
        font.setPointSize(15)

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(845, 581)
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
        
        match nodesNumber:
            case 1:
                widthVar= 80
                heightVar= 60
                Xvar = 350
                Yvar =230
            case 2:
                widthVar= 130
                heightVar= 90
                Xvar = 355
                Yvar = 230
            case 3:
                widthVar= 175
                heightVar= 125
                Xvar = 310
                Yvar = 200
            case 4:
                widthVar= 230
                heightVar= 160
                Xvar = 245
                Yvar = 150
            case 5:
                widthVar= 270
                heightVar= 190
                Xvar = 270
                Yvar = 180
            case _:
                widthVar= 440
                heightVar= 311
                Xvar = 230
                Yvar = 90
                
                
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(Xvar-80, Yvar-80, 150, 150))
        self.label_1.setStyleSheet("background-image: url(C:/Users/mohhd/Desktop/Images/image_3_2.png);")
        self.label_1.setObjectName("label_1")
        
        
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(Xvar, Yvar, widthVar, heightVar))
        self.tableWidget.setStyleSheet("font: 12pt \"Calibri\";")
        self.tableWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setStyleSheet("background-color: rgb(255, 255, 240);")
        self.tableWidget.setColumnCount(nodesNumber)
        self.tableWidget.setRowCount(nodesNumber)

        for i in range(nodesNumber):
            item = QtWidgets.QTableWidgetItem()
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.tableWidget.setVerticalHeaderItem(i, item)

            item = QtWidgets.QTableWidgetItem()
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.tableWidget.setHorizontalHeaderItem(i, item)

            item = QtWidgets.QTableWidgetItem()
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.tableWidget.setItem(i, i, item)
            for j in range(nodesNumber):
                item = QtWidgets.QTableWidgetItem()
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tableWidget.setItem(i, j, item)

        self.tableWidget.horizontalHeader().setDefaultSectionSize(50)

        self.makeGraphBtn = QtWidgets.QPushButton(self.centralwidget)
        self.makeGraphBtn.setGeometry(QtCore.QRect(Xvar+int(widthVar/2)-int(65), Yvar+heightVar +30, 131, 41))
        self.makeGraphBtn.setObjectName("makeGraphBtn")
        self.makeGraphBtn.setStyleSheet("background-color: #0000FF; color: #FFFFFF; font-weight: bold; font-size: 30;")
        self.makeGraphBtn.clicked.connect(self.buildGraph)

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Matrice"))

        self.makeGraphBtn.setText(_translate("MainWindow", "Ok"))

        for i in range(self.nodesNumber):
            item = self.tableWidget.verticalHeaderItem(i)
            item.setText(_translate("MainWindow", chr(65 + i)))

            item = self.tableWidget.horizontalHeaderItem(i)
            item.setText(_translate("MainWindow", chr(65 + i)))

            item = self.tableWidget.item(i, i)
            item.setText(_translate("MainWindow", "0"))

    def buildGraph(self):
        matrix = []
        for i in range(self.nodesNumber):
            m = []
            for j in range(self.nodesNumber):
                m.append(int(self.tableWidget.item(i, j).text()))
            matrix.append(m)
        self.openWindow(Ui_Graph(),matrix,self.nodesNumber , self.graphType)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Matrix = QtWidgets.QMainWindow()
    Matrix.setFixedSize(845,581)
    ui = Ui_Matrix()
    ui.setupUi(Matrix)
    Matrix.show()
    sys.exit(app.exec_())
