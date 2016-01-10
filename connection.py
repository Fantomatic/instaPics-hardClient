from azure.storage.blob import BlobService

def getblobService():
	return BlobService(account_name='blackngram', account_key='yqki9JL7AzfpQQow6uInDN4pmpAxg/bVJR1/f0lYe4NFlrVGlRlUEKVb8pjrKNc6MWSuKJSWOJiIYR00nxWjSQ==')

def gettableService():
	return TableService(account_name='blackngram', account_key='yqki9JL7AzfpQQow6uInDN4pmpAxg/bVJR1/f0lYe4NFlrVGlRlUEKVb8pjrKNc6MWSuKJSWOJiIYR00nxWjSQ==')