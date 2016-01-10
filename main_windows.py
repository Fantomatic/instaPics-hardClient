from sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from pictureflow import *

class MainWindows(QWidget):
    def __init__(self):
        QFrame.__init__(self)
        self.setWindowTitle('picturesAzure')
        self.setMinimumWidth(400)
        self.layout = QGridLayout()

        
        refreshButton = QPushButton("Refresh")
        uploadButton = QPushButton("Upload Pictures")
        imagesPanel = PictureFlow()

        self.layout.addWidget(refreshButton, 1, 0)
        self.layout.addWidget(uploadButton, 1, 1)
        self.layout.addWidget(imagesPanel, 2, 1)
        self.refreshButton()

    def refreshButton(self): 
        listPics = getAllPictures(self.serviceBlob)
        for i in listPics:
            if i.endswith('jpg') or i.endswith('.png'):
                imagesPanel.addSlide(QPixmap('os.curdir'+'%s',i))

    def uploadButton(self):
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