import os
import numpy as np
from PyQt5.QtWidgets import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import networkx as nx
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QSize, Qt
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Warshall(QWidget):
    def setupUi(self,MainWindow, nodesNumber, matrix, graphType):
        self.graphType = graphType
        self.nodesNumber = nodesNumber
        self.MainWindow = MainWindow
        self.setGeometry(100, 100, 800, 600)
        self.MainWindow.setWindowTitle('Warshall')
        
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
        
        
    
        grid = QGridLayout()
        self.setLayout(grid)

        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        grid.addWidget(self.canvas, 0, 1, 9, 9)

        # Convert to dict
        graph = {}
        for i in range(self.nodesNumber):
            edges = []
            for j in range(self.nodesNumber):
                if matrix[i][j] != 0:
                    edges.append(chr(65 + j))
            graph[chr(65 + i)] = edges

        # Warshall
        new_graph = graph
        pre = 0
        suc = 0
        for n in graph:
            suc = graph[n]
            for m in graph:
                if n in graph[m]:
                    pre = m
                    for s in suc:
                        if s not in graph[pre]:
                            new_graph[pre].append(s)

        # Convert to array
        self.graph = []
        for n in new_graph:
            node = new_graph[n]
            for nodeList in node:
                edge = (n, nodeList[0])
                self.graph.append(edge)

        self.plot()
        # self.show()
        if os.path.exists("python-gui-algorithms-on-graphs/assets/GrapheDrawPngs/graphAfterAlgo.png"):
            os.remove("python-gui-algorithms-on-graphs/assets/GrapheDrawPngs/graphAfterAlgo.png")
        plt.savefig('python-gui-algorithms-on-graphs/assets/GrapheDrawPngs/graphAfterAlgo.png')
        plt.savefig('python-gui-algorithms-on-graphs/assets/GrapheDrawPngs/graphAfterAlgo.png')
        self.graph_label = QtWidgets.QLabel(self.MainWindow)
        self.graph_label.setGeometry(150, 50, 700, 500)
        pixmap2 = QPixmap('python-gui-algorithms-on-graphs/assets/GrapheDrawPngs/graphAfterAlgo.png').scaled(self.graph_label.width(), self.graph_label.height(), Qt.KeepAspectRatio)
        self.graph_label.setPixmap(pixmap2)

    def plot(self):
        global G

        if self.graphType == "dp" or self.graphType == "dn":
            G = nx.DiGraph()
        if self.graphType == "up" or self.graphType == "un":
            G = nx.Graph()

        mapping = {}
        for i in range(int(self.nodesNumber)):
            mapping[i] = chr(65 + i)
        nx.relabel_nodes(G, mapping, copy=False)

        G.add_edges_from(self.graph)
        nx.draw(G, with_labels=True)
        self.canvas.draw_idle()

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    app.aboutToQuit.connect(app.deleteLater)
    app.setStyle(QStyleFactory.create("gtk"))
    screen = Ui_Warshall()
    sys.exit(app.exec_())
