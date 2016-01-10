import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from pictureflow import *
from main_windows.py import MainWindows
from connection_windows.py import Login

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    if Login().exec_() == QtGui.QDialog.Accepted:
        window = MainWindows()
        window.show()
        sys.exit(app.exec_())