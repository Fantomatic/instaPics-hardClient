from sys
from azure.storage.blob import BlobService
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from pictureflow import *
from os

#Récupère toutes les images en local dans le currentDir
def getAllPictures():
	blob = getblobService()
	listPictures = PictureFlow()
	#list blob
	blobs = []
	marker = None
	#Télécharge les images
	while True:
	    batch = blob_service.list_blobs(blobService, marker=marker)
	    blobs.extend(batch)
	    if not batch.next_marker:
	        break
	    marker = batch.next_marker
	#Met en dictionnaire tout les paths des fichiers d'images téléchargé et le retourne
	for blob in blobs:
	    blob_service.get_blob_to_path('userimgtable', blob, blob.name)
	listPics = [i for i in os.listdir('.') if os.path.isfile(i)]
	return listPics

#Upload dans un blob d'une image dont le path est sélectionné avec un nom aléatoire
def uploadImage(path):
	blob = getblobService()
	blob.put_block_blob_from_path(
    'imgblob',
    random.seed(20000),
    path,
    x_ms_blob_content_type='image/png'
)