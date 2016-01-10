import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *



#Page de connexion avec aucun password. 
class Login(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.textName = QtGui.QLineEdit(self)
        self.buttonLogin = QtGui.QPushButton('Login', self)
        self.buttonLogin.clicked.connect(self.handleLogin)
        self.layout = QtGui.QVBoxLayout(self)
        #Textbox pour le nom d'utilisateur
        self.layout.addWidget(self.textName)
        #Bouton qui gère le login
        self.layout.addWidget(self.buttonLogin)

    #Connection utilisateur avec création d'utilisateur si il n'existe pas.
    def handleLogin(self):
        table = gettableService()
        task={'username: '+ self.textName.text()}
        table.insert_or_replace_entity('usertable', '1', task)
        QtGui.QMessageBox.warning(
        self, 'Warning', 'Creation of your account')
        self.accept()