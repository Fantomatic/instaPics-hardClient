import sys
from PyQt4 import QtGui

class Login(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.textName = QtGui.QLineEdit(self)
        self.buttonLogin = QtGui.QPushButton('Login', self)
        self.buttonLogin.clicked.connect(self.handleLogin)
        layout = QtGui.QVBoxLayout(self)
        layout.addWidget(self.textName)
        layout.addWidget(self.buttonLogin)

    def handleLogin(self):
        table = gettableService()
        task={'username: '+ self.textName.text()}
        table.insert_or_replace_entity('usertable', '1', task)
        QtGui.QMessageBox.warning(
        self, 'Warning', 'Creation of you account')
        self.accept()