# Written by Eugene Chan, ID:1902208

import osmnx as ox
from main import mapCall as mc
from PyQt5 import QtCore, QtGui, QtWidgets
class Ui_MainWindow(object): #GUI
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(659, 646)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 741, 641))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.PointABox = QtWidgets.QLineEdit(self.tab)
        self.PointABox.setGeometry(QtCore.QRect(120, 70, 261, 20))
        self.PointABox.setObjectName("PointABox")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(230, 40, 47, 13))
        self.label.setObjectName("label")
        self.lbl_EnterCoordinates = QtWidgets.QLabel(self.tab)
        self.lbl_EnterCoordinates.setGeometry(QtCore.QRect(210, 10, 241, 20))
        self.lbl_EnterCoordinates.setObjectName("lbl_EnterCoordinates")
        self.PointBBox = QtWidgets.QLineEdit(self.tab)
        self.PointBBox.setGeometry(QtCore.QRect(120, 140, 261, 20))
        self.PointBBox.setObjectName("PointBBox")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(240, 110, 61, 16))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(120, 210, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.on_click)
        self.tabWidget.addTab(self.tab, "")
        self.tab_POI = QtWidgets.QWidget()
        self.tab_POI.setObjectName("tab_POI")
        self.tableWidget = QtWidgets.QTableWidget(self.tab_POI)
        self.tableWidget.setGeometry(QtCore.QRect(50, 110, 501, 321))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(10)
        self.tableWidget.cellClicked.connect(self.openGo)
        self.label_3 = QtWidgets.QLabel(self.tab_POI)
        self.label_3.setGeometry(QtCore.QRect(190, 10, 181, 20))
        self.label_3.setObjectName("label_3")
        self.SecondTabTextBox = QtWidgets.QLineEdit(self.tab_POI)
        self.SecondTabTextBox.setGeometry(QtCore.QRect(140, 40, 261, 20))
        self.SecondTabTextBox.setObjectName("SecondTabTextBox")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_POI)
        self.pushButton_2.setGeometry(QtCore.QRect(220, 70, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.getTable)
        self.tabWidget.addTab(self.tab_POI, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ShortestPath "))
        self.label.setText(_translate("MainWindow", "Point A"))
        self.lbl_EnterCoordinates.setText(_translate("MainWindow", "Enter the coordinates "))
        self.label_2.setText(_translate("MainWindow", "Point B"))
       
        self.pushButton.setText(_translate("MainWindow", "OK"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Get By Coordinates"))
        self.label_3.setText(_translate("MainWindow", "Enter your coordinates here"))
        self.pushButton_2.setText(_translate("MainWindow", "Ok"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_POI), _translate("MainWindow", "Go to Point of Interest"))
      

    def on_click(self):#When coordinates are selected load window
        sA = self.PointABox.text().split(",")
        dA=self.PointBBox.text().split(",")
      
        D=mc()
        D.getRoute(sA[0],sA[1],dA[0],dA[1])     
        
        
    def getTable(self): #Populate table with  the top 10 nearest amenties
     
         queryRes=self.SecondTabTextBox.text().split(",")
         queryTable = ox.pois_from_point((float(queryRes[0]),float(queryRes[1])),distance=3000,amenities=['restaurant'])
         cols=['name','geometry']
         counter=0
         for i in range(10):
             self.tableWidget.setItem(i,0, QtWidgets.QTableWidgetItem(str(queryTable[cols].head(10).values.item(counter))))
             counter+=1
             self.tableWidget.setItem(i,1, QtWidgets.QTableWidgetItem(str(queryTable[cols].head(10).values.item(counter))))
             counter+=1
             
    def openGo(self,row,col):#When the row is clicked perform routing
       
        queryRes=self.SecondTabTextBox.text().split(",")
        finaltext=self.tableWidget.item(row,1).text().replace("POINT (","")
        finaltext=finaltext.replace(")","")
        destQuery=finaltext.split(" ")
        D=mc()
        D.getRoute(queryRes[0],queryRes[1],destQuery[1],destQuery[0])   
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

