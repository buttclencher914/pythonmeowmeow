import PySimpleGUI as sg
import numpy as np
import osmnx as ox
import networkx as nx
from sklearn.neighbors import KDTree
import folium
import matplotlib.pyplot as plt
import overpy as oy

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uiVer1.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
      
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(659, 646)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        
        self.centralwidget.setObjectName("centralwidget")
        
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(140, 250, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.on_click)
        
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(140, 220, 121, 31))
        self.checkBox.setObjectName("checkBox")
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(250, 80, 47, 13))
        self.label.setObjectName("label")
        
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(250, 150, 61, 16))
        self.label_2.setObjectName("label_2")
        
        self.PointABox = QtWidgets.QLineEdit(self.centralwidget)
        self.PointABox.setGeometry(QtCore.QRect(140, 100, 261, 20))
        self.PointABox.setObjectName("PointABox")
        
        self.PointBBox = QtWidgets.QLineEdit(self.centralwidget)
        self.PointBBox.setGeometry(QtCore.QRect(140, 180, 261, 20))
        self.PointBBox.setObjectName("PointBBox")
        
        self.lbl_EnterCoordinates = QtWidgets.QLabel(self.centralwidget)
        self.lbl_EnterCoordinates.setGeometry(QtCore.QRect(210, 20, 151, 20))
        self.lbl_EnterCoordinates.setObjectName("lbl_EnterCoordinates")
        
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 310, 431, 181))
        self.label_3.setObjectName("label_3")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 659, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        old_market = (1.40525,103.90233)
        G = ox.graph_from_point(old_market, distance=1000)# quick plot
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ShortestPath "))
        self.pushButton.setText(_translate("MainWindow", "OK"))
        self.checkBox.setText(_translate("MainWindow", "Use sheltered Path"))
        self.label.setText(_translate("MainWindow", "Point A"))
        self.label_2.setText(_translate("MainWindow", "Point B"))
        self.lbl_EnterCoordinates.setText(_translate("MainWindow", "Enter the coordinates "))
        k=ox.plot_graph(G, fig_height=10, fig_width=10, edge_color='black')
        self.label_3.setText(k)
        
    def on_click(self):
        sourceArea = self.PointABox.text()
        destArea=self.PointBBox.text()
        print(sourceArea)
        print(destArea)
        #QMessageBox.question(self, 'Message - pythonspot.com', "You typed: " + sourceArea+" and "+destArea, QMessageBox.Ok, QMessageBox.Ok)
       

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

