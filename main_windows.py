from sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from pictureflow import *

#Page principal avec un affichage 3D des images, un boutton de rafraichissement et un bouton d'upload.
class MainWindows(QWidget):
    def __init__(self):
        QFrame.__init__(self)
        self.setWindowTitle('picturesAzure')
        self.setMinimumWidth(400)
        self.layout = QGridLayout()

        #Déclaration de tout les bouton et du panel 3D 
        refreshButton = QPushButton("Refresh")
        refreshButton.clicked.connect(self.refresh_Button)
        uploadButton = QPushButton("Upload Pictures")
        uploadButton.clicked.connect(self.upload_Button)
        imagesPanel = PictureFlow()

        #Positionnement dans la GridLayout
        self.layout.addWidget(refreshButton, 1, 0)
        self.layout.addWidget(uploadButton, 1, 1)
        self.layout.addWidget(imagesPanel, 2, 1)
        #Affichage et téléchargement lors du lancement de la fenêtre des images dans le pictureFlow 
        self.refreshButton()

    #Affiche dans le pictureFlow les images 
    def refresh_Button(self): 
        listPics = getAllPictures(self.serviceBlob)
        for i in listPics:
            if i.endswith('jpg') or i.endswith('.png'):
                imagesPanel.addSlide(QPixmap('os.curdir'+'%s',i))

    #Affiche une boite de dialogue de recherche de fichiers pour les jpg, et l'upload dans le container de blob
    def upload_Button(self):
        fileName = QtGui.QFileDialog.getOpenFileName(
                        self,
                        "Upload an image file",
                        QtCore.QDir.homePath(),
                        "Images Files (*.jpg, *.jpeg, *.gif, *.png)"
                    )
        if fileName:
            uploadImage(fileName)

def run(self):
        # Show the form
        self.show()
        # Run the qt application
        qt_app.exec_()