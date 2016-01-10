import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from main_windows.py import MainWindows
from connection_windows.py import Login

#Lance une boite de dialogue de connexion et renvoie sur la main windows
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    if Login().exec_() == QtGui.QDialog.Accepted:
        window = MainWindows()
        window.show()
        sys.exit(app.exec_())