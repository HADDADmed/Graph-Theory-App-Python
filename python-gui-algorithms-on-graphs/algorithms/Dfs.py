import os
import numpy as np
from PyQt5.QtWidgets import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import networkx as nx
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QSize, Qt
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dfs(QWidget):
    def setupUi(self, MainWindow, nodesNumber, matrix, graphType,StartNode):
        print(matrix)
        self.matrix = matrix
        self.graphType = graphType
        self.nodesNumber = nodesNumber
        self.details = ""
        self.source = StartNode
        self.source = 'A'
        self.MainWindow = MainWindow
        self.setWindowTitle('Dfs')
        
        self.MainWindow.setObjectName("DFS")
        self.MainWindow.resize(845, 581)

        font = QtGui.QFont()
        font.setBold(True)
        font.setFamily("Calibri")
        font.setPointSize(8)
        
        
        font = QtGui.QFont()
        font.setBold(True)
        font.setFamily("Calibri")
        font.setPointSize(15)
        
        
        self.centralwidget = QtWidgets.QWidget(self.MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.label_0 = QtWidgets.QLabel(self.MainWindow)
        self.label_0.setGeometry(QtCore.QRect(0, 0, 845, 581))
        self.label_0.setFont(font)
        self.label_0.setStyleSheet("background-image: url(C:/Users/mohhd/Desktop/Tkinter-Designer-master/ProjectPython/build/assets/frame0/image_1.png); background-color: #D1CFFF;")
        self.label_0.setObjectName("label_0")
        

        self.label_0_0 = QtWidgets.QLabel(self.MainWindow)
        self.label_0_0.setGeometry(QtCore.QRect(530, 550, 303, 17))
        self.label_0_0.setStyleSheet("background-image: url(C:/Users/mohhd/Desktop/Images/image_2.png);")
        self.label_0_0.setObjectName("label_0_0")
        
        
        
        
        
       
        
        
        
        
        
        # recuperer le sommet
        # self.display()
        # afficher le chemain

        # self.setGeometry(100, 100, 800, 600)
        # self.setWindowTitle('Bfs')

        # grid = QGridLayout()
        # self.setLayout(grid)

        # self.figure = plt.figure()
        # self.canvas = FigureCanvas(self.figure)
        # grid.addWidget(self.canvas, 0, 1, 9, 9)



        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('Bfs')

        grid = QGridLayout()
        self.setLayout(grid)

        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        grid.addWidget(self.canvas, 0, 1, 9, 9)
        
        
        self.plot()
        # self.show()
        if os.path.exists("python-gui-algorithms-on-graphs/assets/GrapheDrawPngs/graphAfterAlgo.png"):
            os.remove("python-gui-algorithms-on-graphs/assets/GrapheDrawPngs/graphAfterAlgo.png")
        plt.savefig('python-gui-algorithms-on-graphs/assets/GrapheDrawPngs/graphAfterAlgo.png')
        # self.show()


        
        
        self.graph_label = QtWidgets.QLabel(self.MainWindow)
        self.graph_label.setGeometry(140, 100, 650, 441)
        pixmap2 = QPixmap('python-gui-algorithms-on-graphs/assets/GrapheDrawPngs/graphAfterAlgo.png').scaled(self.graph_label.width(), self.graph_label.height(), Qt.KeepAspectRatio)
        self.graph_label.setPixmap(pixmap2)
        
        self.label_1 = QtWidgets.QLabel(self.MainWindow)
        self.label_1.setGeometry(QtCore.QRect(140, 10, 590, 80))
        self.label_1.setStyleSheet("background-color: white;")
        self.label_1.setObjectName("label_1")
        self.label_1.setFont(font)
        self.label_1.setText("Parcours en Largeure  Dfs : " + str(self.tab))
        
        
    def plot(self):
        global G

        mat = np.array(self.matrix)

        G = nx.from_numpy_array(mat, create_using=nx.DiGraph)
           
        mapping = {}
        for i in range(int(self.nodesNumber)):
            mapping[i] = chr(65 + i)

        nx.relabel_nodes(G, mapping, copy=False)

        # affichage d'arbre DFS si le graphe est direct
        tree = nx.dfs_tree(G, source=self.source)
        print(tree.edges())

        # create table of nodes DFS
        self.tab = []
        flag=0
        for edg in tree.edges():
            if(flag == 0) :
                self.tab.append(edg[0])
            flag = 1
            self.tab.append(edg[1])

        nx.relabel_nodes(tree, mapping, copy=False)

        nx.draw(tree, with_labels=True)
            
    # def display(self):
    #     src, pressed = QInputDialog.getText(self.MainWindow, "Sommet Depart", "Entrer un Sommet : ")
    #     if pressed:
    #         print(str(src))
    #         self.source = src

    # def showPath(self):
    #     msg = QMessageBox()
    #     msg.setIcon(QMessageBox.Information)
    #     msg.setText("Parcours en Profondeur")
    #     msg.setInformativeText("DFS:  "+str(self.tab))
    #     msg.setWindowTitle("DFS")
    #     msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    #     msg.exec_()
    
if __name__ == '__main__':

    import sys
    app = QApplication(sys.argv)
    app.aboutToQuit.connect(app.deleteLater)
    app.setStyle(QStyleFactory.create("gtk"))
    screen = Ui_Dfs()
    sys.exit(app.exec_())
