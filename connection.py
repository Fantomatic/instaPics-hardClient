from azure.storage.blob import BlobService

#retourne la connexion au blob des images
def getblobService():
	return BlobService(account_name='blackngram', account_key='yqki9JL7AzfpQQow6uInDN4pmpAxg/bVJR1/f0lYe4NFlrVGlRlUEKVb8pjrKNc6MWSuKJSWOJiIYR00nxWjSQ==')

#retourne la connexion à la table des utilisateurs
def gettableService():
	return TableService(account_name='blackngram', account_key='yqki9JL7AzfpQQow6uInDN4pmpAxg/bVJR1/f0lYe4NFlrVGlRlUEKVb8pjrKNc6MWSuKJSWOJiIYR00nxWjSQ==')