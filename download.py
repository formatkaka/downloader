import requests

import threading

# Obtain the link through 1. LocalDB 2. Scraping ######

download_link = ""

# HEAD REQUEST TO KNOW THE SIZE OF THE FILE TO BE DOWNLOADED. #######

head_response = requests.head(download_link).headers

content_length = head_response[
    'Content-length'] if head_response['Content-length'] else None


# CODE TO SPAWN THREADS AND START DOWNLOADING #####

class myThread(threading.Thread):
	"""docstring for myThread"""
	def __init__(self, **kwargs):
		super(myThread, self).__init__()
		self.content_length = kwargs['length']
		self.number_of_threads = kwargs['threads'] 
	
	def download(self):
		""" code to download 
			1. Setting headers.
			2. Spawning threads.
			3. Making requests.
			4. Validate if all threads get proper response.
			5. If proper , proceed with download.
			6. Some error handling.
			7. Merge the threads.
			8. Save the search)if new) to database.
			"""
		pass

