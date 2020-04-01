import PySimpleGUI as sg
import numpy as np
import osmnx as ox
import networkx as nx
from sklearn.neighbors import KDTree
import folium
import matplotlib.pyplot as plt
import overpy as oy
from main import mapCall as mc
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
        self.lbl_EnterCoordinates.setGeometry(QtCore.QRect(170, 20, 281, 20))
        self.lbl_EnterCoordinates.setObjectName("lbl_EnterCoordinates")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 300, 581, 271))
        self.label_3.setMinimumSize(QtCore.QSize(0, 271))
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
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ShortestPath "))
        self.pushButton.setText(_translate("MainWindow", "OK"))
        self.checkBox.setText(_translate("MainWindow", "Use sheltered Path"))
        self.label.setText(_translate("MainWindow", "Point A"))
        self.label_2.setText(_translate("MainWindow", "Point B"))
        self.lbl_EnterCoordinates.setText(_translate("MainWindow", "Enter the coordinates in this format (Lat,long)"))
         
        
        pixmap = QtGui.QPixmap()
        pixmap.load('C:/Users/User/.spyder-py3/images/{}'.format("PunggolDefault.png"))
        pixmap = pixmap.scaledToHeight(400)
        self.label_3.setPixmap(pixmap)
        self.label_3.show()
        
        #self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><img src=\"C:/Users/User/.spyder-py3/images/PunggolPath.png\"/></p></body></html>"))

    def on_click(self):
        _translate = QtCore.QCoreApplication.translate
        sA = self.PointABox.text().split(",")
        dA=self.PointBBox.text().split(",")
        checkBoxValue=self.checkBox.isChecked();
        D=mc()
        pic=D.getRoute(sA,dA)
        print(pic)
       
        
        pixmap = QtGui.QPixmap()
        pixmap.load('C:/Users/User/.spyder-py3/images/{}'.format(pic))
        pixmap = pixmap.scaledToHeight(400)
       # self.label_3.setText(_translate("MainWindow", imgsrc))
        self.label_3.setPixmap(pixmap)
        self.label_3.show()
        
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

