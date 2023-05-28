import numpy as np
from PyQt5.QtWidgets import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import networkx as nx
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel
from PyQt5.QtCore import QSize, Qt
import algorithms.Bellman as Bellman
import algorithms.Bfs as Bfs
import algorithms.Dfs as Dfs
import algorithms.Warshall as Warshall
import algorithms.Prim as Prim 
import algorithms.Dijikstra as Dijikstra 
import algorithms.Fulkerson as Fulkerson
import algorithms.Kruskal as Kruskal

import partials.CaracteristiqueT  as CaracteristiqueT





class Ui_Graph(QWidget):
    def openWindow(self, Ui_Window,nodesNumber,matrix,graphType):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Window
        self.ui.setupUi(self.window,nodesNumber,matrix,graphType,self.StartNodeText)
        self.window.show()
        
    def setupUi(self,GrapheW, nodesNumber, matrix, graphType):
        print(matrix)
        self.matrix = matrix
        self.graphType = graphType
        self.nodesNumber = nodesNumber

        # self.setGeometry(100, 100, 800, 600)
        # self.setWindowTitle('Graph')
        
        GrapheW.setObjectName("Graphe Page")
        GrapheW.resize(845, 581)

        font = QtGui.QFont()
        font.setBold(True)
        font.setFamily("Calibri")
        font.setPointSize(8)
        
        font2 = QtGui.QFont()
        font2.setFamily("Bradley Hand")
        font2.setPointSize(9)
        font2.setBold(True)

        self.centralwidget = QtWidgets.QWidget(GrapheW)
        self.centralwidget.setObjectName("centralwidget")
        
        self.label_0 = QtWidgets.QLabel(GrapheW)
        self.label_0.setGeometry(QtCore.QRect(0, 0, 845, 581))
        self.label_0.setFont(font)
        self.label_0.setStyleSheet("background-image: url(C:/Users/mohhd/Desktop/Tkinter-Designer-master/ProjectPython/build/assets/frame0/image_1.png); background-color: #D1CFFF;")
        self.label_0.setObjectName("label_0")
        
        
        self.label_0_0 = QtWidgets.QLabel(GrapheW)
        self.label_0_0.setGeometry(QtCore.QRect(530, 550, 303, 17))
        self.label_0_0.setStyleSheet("background-image: url(C:/Users/mohhd/Desktop/Images/image_2.png);")
        self.label_0_0.setObjectName("label_0_0")


        grid = QGridLayout()
        self.setLayout(grid)

        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        grid.addWidget(self.canvas, 0, 1, 9, 9)

        self.plot()

        if os.path.exists("python-gui-algorithms-on-graphs/assets/GrapheDrawPngs/graph.png"):
            os.remove("python-gui-algorithms-on-graphs/assets/GrapheDrawPngs/graph.png")
        plt.savefig('python-gui-algorithms-on-graphs/assets/GrapheDrawPngs/graph.png')
        # self.show()
        
        self.graph_label = QtWidgets.QLabel(GrapheW)
        self.graph_label.setGeometry(165, 50, 670, 450)
        self.graph_label.setStyleSheet("background-color: #FFFFFF; border: 2px solid black;")
        pixmap = QPixmap('python-gui-algorithms-on-graphs/assets/GrapheDrawPngs/graph.png').scaled(self.graph_label.width(), self.graph_label.height(), Qt.KeepAspectRatio)
        self.graph_label.setPixmap(pixmap)
        
        self.ShowInfoGrapheButton = QtWidgets.QPushButton(GrapheW)
        self.ShowInfoGrapheButton.setGeometry(QtCore.QRect(360, 10, 300, 30))
        self.ShowInfoGrapheButton.setObjectName("ShowInfoGrapheButton")
        self.ShowInfoGrapheButton.setStyleSheet("background-color: #2018C0; color: #FFFFFF; font-weight: bold; font-size: 30;")
        self.ShowInfoGrapheButton.clicked.connect(self.ShowInfoGraphe)
        self.ShowInfoGrapheButton.setText("Show Graphe info")
        
         
        self.label_3 = QtWidgets.QLabel(GrapheW)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 140, 581))
        self.label_3.setStyleSheet("background-color: #FFFFFF; border: 2px solid black;")
        self.label_3.setObjectName("label_3")
        
        #Parcours du graphe
        
         
        self.label_12 = QtWidgets.QLabel(GrapheW)
        self.label_12.setGeometry(QtCore.QRect(0,20, 140, 30))
        self.label_12.setFont(font2)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setStyleSheet("color: #000000;")
        self.label_12.setObjectName("label_12")
        self.label_12.setText("Parcours Du Graphe")
        
        
        self.label_4 = QtWidgets.QPushButton(GrapheW)
        self.label_4.setGeometry(QtCore.QRect(0, 60, 100, 35))
        # self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: blue; color: #FFFFFF;")
        self.label_4.setObjectName("label_4")
        self.label_4.setText("BFS")
        self.label_4.clicked.connect(self.labelClick)
        
        self.BfsAlgo = QtWidgets.QRadioButton(GrapheW)
        self.BfsAlgo.setGeometry(QtCore.QRect(115, 60, 40, 35))
        self.BfsAlgo.setFont(font)
        self.BfsAlgo.setObjectName("BfsAlgo")
        
        self.label_5 = QtWidgets.QPushButton(GrapheW)
        self.label_5.setGeometry(QtCore.QRect(0, 100, 100, 35))
        # self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-color: blue; color: #FFFFFF;")
        self.label_5.setObjectName("label_5")
        self.label_5.setText("DFS")
        self.label_5.clicked.connect(self.labelClick)

        
        self.DfsAlgo = QtWidgets.QRadioButton(GrapheW)
        self.DfsAlgo.setGeometry(QtCore.QRect(115, 100, 40, 35))
        self.DfsAlgo.setFont(font)
        self.DfsAlgo.setObjectName("DfsAlgo")
        
        self.label_6 = QtWidgets.QPushButton(GrapheW)
        self.label_6.setGeometry(QtCore.QRect(0, 140, 100, 35))
        # self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background-color: blue; color: #FFFFFF;")
        self.label_6.setObjectName("label_6")
        self.label_6.setText("WARSHALL")
        self.label_6.clicked.connect(self.labelClick)
        
        self.WarshallAlgo = QtWidgets.QRadioButton(GrapheW)
        self.WarshallAlgo.setGeometry(QtCore.QRect(115, 140, 40, 35))
        self.WarshallAlgo.setFont(font)
        self.WarshallAlgo.setObjectName("WarshallAlgo")
        
        
        #Arbre couvrante minimal 
        
        self.label_13 = QtWidgets.QLabel(GrapheW)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setGeometry(QtCore.QRect(0, 185, 140, 30))
        self.label_13.setFont(font2)
        self.label_13.setStyleSheet("color: #000000;")
        self.label_13.setObjectName("label_13")
        self.label_13.setText("Arbre couvrante\nminimal")
        
        
        self.label_7 = QtWidgets.QPushButton(GrapheW)
        self.label_7.setGeometry(QtCore.QRect(0, 220, 100, 35))
        # self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("background-color: blue; color: #FFFFFF;")
        self.label_7.setObjectName("label_7")
        self.label_7.setText("PRIME")
        self.label_7.clicked.connect(self.labelClick)
        
        self.PrimeAlgo = QtWidgets.QRadioButton(GrapheW)
        self.PrimeAlgo.setGeometry(QtCore.QRect(115, 220, 40, 35))
        self.PrimeAlgo.setFont(font)
        self.PrimeAlgo.setObjectName("PrimeAlgo")
        if self.graphType == "dn" or self.graphType == "un" or self.graphType == "dp":
            self.PrimeAlgo.setEnabled(False)
            self.label_7.setEnabled(False)

            
        
        
        self.label_8 = QtWidgets.QPushButton(GrapheW)
        self.label_8.setGeometry(QtCore.QRect(0, 260, 100, 35))
        # self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("background-color: blue; color: #FFFFFF;")
        self.label_8.setObjectName("label_8")
        self.label_8.setText("KRUKSAL")
        self.label_8.clicked.connect(self.labelClick)
        
        self.KruksalAlgo = QtWidgets.QRadioButton(GrapheW)
        self.KruksalAlgo.setGeometry(QtCore.QRect(115, 260, 40, 35))
        self.KruksalAlgo.setFont(font)      
        self.KruksalAlgo.setObjectName("KruksalAlgo")
        if self.graphType == "dn" or self.graphType == "un" or self.graphType == "dp":
            self.KruksalAlgo.setEnabled(False)
            self.label_8.setEnabled(False)
       
        
        
        #Plus court chemin 

        self.label_14 = QtWidgets.QLabel(GrapheW)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setGeometry(QtCore.QRect(0, 300, 140, 30))
        self.label_14.setFont(font2)
        self.label_14.setStyleSheet("color: #000000;")
        self.label_14.setObjectName("label_14")
        self.label_14.setText("Plus court chemin ")
        
        
        self.label_9 = QtWidgets.QPushButton(GrapheW)
        self.label_9.setGeometry(QtCore.QRect(0, 340, 100, 35))
        # self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("background-color: blue; color: #FFFFFF;")
        self.label_9.setObjectName("label_9")
        self.label_9.setText("DJIKSTRA")
        self.label_9.clicked.connect(self.labelClick)
        
        self.DjikstraAlgo = QtWidgets.QRadioButton(GrapheW)
        self.DjikstraAlgo.setGeometry(QtCore.QRect(115, 340, 40, 35))
        self.DjikstraAlgo.setFont(font)       
        self.DjikstraAlgo.setObjectName("DjikstraAlgo")
        
        if self.graphType == "dn" or self.graphType == "un":
            self.DjikstraAlgo.setEnabled(False)
            self.label_9.setEnabled(False)
        for i in range(self.nodesNumber):
            for j in range(self.nodesNumber):
                if self.matrix[i][j] < 0:
                    self.DjikstraAlgo.setEnabled(False)
                    self.label_9.setEnabled(False)
        
        
        self.label_10 = QtWidgets.QPushButton(GrapheW)
        self.label_10.setGeometry(QtCore.QRect(0, 380, 100, 35))
        # self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("background-color: blue; color: #FFFFFF;")
        self.label_10.setObjectName("label_10")
        self.label_10.setText("BELMAN-FORD")
        self.label_10.clicked.connect(self.labelClick)
        
        
        self.BellmanFordAlgo = QtWidgets.QRadioButton(GrapheW)
        self.BellmanFordAlgo.setGeometry(QtCore.QRect(115, 380, 40, 35))
        self.BellmanFordAlgo.setFont(font2)
        self.BellmanFordAlgo.setObjectName("BellmanFordAlgo")
        if self.graphType == "dn" or self.graphType == "un":
            self.BellmanFordAlgo.setEnabled(False)
            self.label_10.setEnabled(False)
        
        
        #minimiser le cout 
        
        self.label_14 = QtWidgets.QLabel(GrapheW)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setGeometry(QtCore.QRect(0, 420, 140, 30))
        self.label_14.setFont(font2)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setStyleSheet("color: #000000;")
        self.label_14.setObjectName("label_14")
        self.label_14.setText("minimiser le cout ")
        
        self.label_11 = QtWidgets.QPushButton(GrapheW)
        self.label_11.setGeometry(QtCore.QRect(0, 460, 100, 35))
        # self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("background-color: blue; color: #FFFFFF;")
        self.label_11.setObjectName("label_11")
        self.label_11.setText("FORD-FORKENSON")
        self.label_11.clicked.connect(self.labelClick)
        
        
        self.FordFokensonAlgo = QtWidgets.QRadioButton(GrapheW)
        self.FordFokensonAlgo.setGeometry(QtCore.QRect(115, 460, 40, 35))
        self.FordFokensonAlgo.setFont(font)
        self.FordFokensonAlgo.setObjectName("FordFokensonAlgo")
        if self.graphType == "dn" or self.graphType == "un":
            self.FordFokensonAlgo.setEnabled(False)
            self.label_11.setEnabled(False)
        
        
        
        self.label_15 = QtWidgets.QLabel(GrapheW)
        self.label_15.setGeometry(QtCore.QRect(10, 510, 100, 35))
        self.label_15.setFont(font2)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setStyleSheet("color: #000000;")
        self.label_15.setObjectName("label_15")
        self.label_15.setText("Start Node")
        
        self.StartNode = QtWidgets.QLineEdit(GrapheW)
        self.StartNode.setGeometry(QtCore.QRect(20,540, 100, 30))
        self.StartNode.setObjectName("StartNode")
        self.StartNode.setText('A')

        self.RunButton = QtWidgets.QPushButton(GrapheW)
        self.RunButton.setGeometry(QtCore.QRect(446, 510, 140, 31))
        self.RunButton.setObjectName("RunButton")
        self.RunButton.setStyleSheet("background-color: blue; color: #FFFFFF; font-weight: bold; font-size: 30;")
        self.RunButton.setText("Run Algorithme")
        self.RunButton.setFont(font)
        self.RunButton.clicked.connect(self.OpenAlgorithme)
        
        
        self.StartNodeText = str(self.StartNode.text())


    def plot(self):
        global G

        mat = np.array(self.matrix)
        if self.graphType == "dn":
            G = nx.from_numpy_array(mat, create_using=nx.DiGraph)
        if self.graphType == "un":
            G = nx.from_numpy_array(mat, create_using=nx.Graph)
        if self.graphType == "dp":
            G = nx.from_numpy_array(mat, create_using=nx.DiGraph)
        if self.graphType == "up":
            G = nx.from_numpy_array(mat, create_using=nx.Graph)

        mapping = {}
        for i in range(int(self.nodesNumber)):
            mapping[i] = chr(65 + i)

        nx.relabel_nodes(G, mapping, copy=False)

        if self.graphType == "dp" or self.graphType == "up":
            layout = nx.spring_layout(G)
            nx.draw(G, layout, with_labels=True)
            labels = nx.get_edge_attributes(G, 'weight')
            nx.draw_networkx_edge_labels(G, pos=layout, edge_labels=labels)

        if self.graphType == "dn" or self.graphType == "un":
            nx.draw(G, with_labels=True)
            # self.canvas.draw_idle()
     
     
    def labelClick(self):
        button = self.sender()
        if button.objectName() == "label_4":
            self.BfsAlgo.setChecked(True)   
        elif button.objectName() == "label_5":
            self.DfsAlgo.setChecked(True)
        elif button.objectName() == "label_6":
            self.WarshallAlgo.setChecked(True)
        elif button.objectName() == "label_7":
            self.PrimeAlgo.setChecked(True)
        elif button.objectName() == "label_8":
            self.KruksalAlgo.setChecked(True)
        elif button.objectName() == "label_9":
            self.DjikstraAlgo.setChecked(True)
        elif button.objectName() == "label_10":
            self.BellmanFordAlgo.setChecked(True)
        elif button.objectName() == "label_11":
            self.FordFokensonAlgo.setChecked(True)
        
    def ShowInfoGraphe(self):
        self.openWindow(CaracteristiqueT.Ui_Charac(),self.matrix,self.nodesNumber , self.graphType)
     
    def OpenAlgorithme(self):
        if self.BfsAlgo.isChecked():
            self.window = QtWidgets.QMainWindow()
            self.ui = Bfs.Ui_Bfs(self.window)
            self.ui.setupUi(self.window, self.nodesNumber, self.matrix, self.graphType,self.StartNodeText)
            self.window.show()
            
        if self.DfsAlgo.isChecked():
             self.window = QtWidgets.QMainWindow()
             self.ui = Dfs.Ui_Dfs()
             self.ui.setupUi(self.window, self.nodesNumber, self.matrix, self.graphType,self.StartNodeText)
             self.window.show()
             
        if self.WarshallAlgo.isChecked():
            self.window = QtWidgets.QMainWindow()
            self.ui = Warshall.Ui_Warshall()
            self.ui.setupUi(self.window,self.nodesNumber, self.matrix, self.graphType)
            self.window.show()
            
        if self.PrimeAlgo.isChecked():
            self.ui =Prim.Ui_Prim()
            self.ui.setupUi(Prim.Ui_Prim(), self.nodesNumber, self.matrix, self.graphType)
            
        if self.KruksalAlgo.isChecked():
            self.ui =Kruskal.Ui_Kruskal()
            self.ui.setupUi(self.nodesNumber, self.matrix, self.graphType)
            
        if self.DjikstraAlgo.isChecked():
            self.openWindow(Dijikstra.Ui_Dijikstra(),self.nodesNumber, self.matrix, self.graphType)
        
        if self.BellmanFordAlgo.isChecked():
            self.openWindow(Bellman.Ui_Bellman(),self.nodesNumber, self.matrix, self.graphType)
            
        if self.FordFokensonAlgo.isChecked():
            self.openWindow(Fulkerson.Ui_Fulkerson())
            

    # def bfs(self):
    #     self.window = QtWidgets.QMainWindow()
    #     self.ui = Bfs.Ui_Bfs(self.window)
    #     self.ui.setupUi(self.window, self.nodesNumber, self.matrix, self.graphType)
    #     self.window.show()
        
    # def dfs(self):
    #     self.ui = Dfs.Ui_Dfs()
    #     self.ui.setupUi(Ui_Dfs(), self.nodesNumber, self.matrix, self.graphType)
        
    # def warshall(self):
    #     self.ui = Warshall.Ui_Warshall()
    #     self.ui.setupUi(self.nodesNumber, self.matrix, self.graphType)
        
    # def bellman(self):
    #     self.openWindow(Bellman.Ui_Bellman())


        
    # def prim(self):
        # self.ui = Ui_Prim()
        # self.ui.setupUi(Ui_Prim(), self.nodesNumber, self.matrix, self.graphType)


    # def kruskal(self):
    #     self.ui = Ui_Kruskal()
    #     self.ui.setupUi(self.nodesNumber, self.matrix, self.graphType)

    # def dijkstra(self):
    #     self.openWindow(Ui_Dijikstra())

    # def fulkerson(self):
    #     self.openWindow(Ui_Fulkerson())      

if __name__ == '__main__':

    import sys
    
    app = QApplication(sys.argv)
    
    app = QtWidgets.QApplication(sys.argv)
    
    GrapheW = QtWidgets.QMainWindow()
    GrapheW.setFixedSize(845,581)
    
    ui =  Ui_Graph()
    ui.setupUi(GrapheW)
    
    # graph_label = QLabel(GrapheW)
    # graph_label.setGeometry(10, 10, 800, 400)
    # pixmap = QPixmap('graph.png').scaled(graph_label.width(), graph_label.height(), Qt.KeepAspectRatio)
    # graph_label.setPixmap(pixmap)

    
    # GrapheW.show()
    sys.exit(app.exec_())
    
    
    # app.aboutToQuit.connect(app.deleteLater)
    # app.setStyle(QStyleFactory.create("gtk"))
    
    # sys.exit(app.exec_())
