
from PyQt5 import  QtGui,QtWidgets
from tkGUI import Ui_MainWindow
import sys


class mainWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = mainWin()
    myapp.show()
    sys.exit(app.exec_())

