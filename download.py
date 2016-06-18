import requests

import threading

# Obtain the link through 1. LocalDB 2. Scraping ######

download_link = ""
headers = ""

# HEAD REQUEST TO KNOW THE SIZE OF THE FILE TO BE DOWNLOADED. #######


download_status = {}


class myThread(threading.Thread):
	"""docstring for myThread"""
        global url
        
	def __init__(self, threadId, drange):
		self.content_length = kwargs['length']
	        self.url = url
                self.drange = drange
	        super(myThread, self).__init__()
                
	def run(self):
                download(self.threadId, self.drange, self.url)
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



class DownloadFile(object):
        def __init__(self,**kwargs):
                self.url = kwargs['url']
                self.count = kwargs['count']
                self.size = None
                self.threads = []
                
        def find_headers(self):
                global headers = requests.head(download_link).headers
                self.size = head_response['Content-length'] if head_response['Content-length'] else None
            
                
        def add_to_queue(self):
                threads = []
                partition = (self.size)/4
                for i in xrange(4):
                        thread = myThread(i, [i*partition, (i+1)*partition])
                        threads.append(thread)

        def start_download(self):
                for thread in self.threads:
                        thread.start()

        def wait_for_complete(self):
                for thread in self.threads:
                        thread.join()
                
        
def download(threadId, drange, url):
        headers = {"Range":"{0}-{1}".format(drange[0], drange[1])}
        size = drange[1] - drange[0]
        req = requests.get(url, headers=headers, stream=True)
        download_status[size] = size
        download_status[threadId] = 0
        for data in req.iter_content():
                download_status[threadId] += len(req)
                # The download status must be updated in the global variable
                # and must be shown by kivy in the form of a progress bar.

####  TODO  ####

# 1. Handling Exceptions.
# 2. Error logging.
# 3. Merging the files
