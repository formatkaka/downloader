import requests

import threading

import shutil

from clint.textui import progress as pr
# Obtain the link through 1. LocalDB 2. Scraping ######

url = ""
head_response = ""

# HEAD REQUEST TO KNOW THE SIZE OF THE FILE TO BE DOWNLOADED. #######


download_status = {}


class myThread(threading.Thread):
    """docstring for myThread"""
    global url
        
    def __init__(self, threadId, drange, url):
        self.url = url
        self.threadId   = threadId
        self.drange = drange
        super(myThread, self).__init__()
                
    def run(self):
        return download(self.threadId, self.drange, self.url), self.threadId
        # print "Here"
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
                
		



class DownloadFile(object):

    global url
        
    def __init__(self,**kwargs):
        self.url = kwargs['url']
        self.count = 5
        self.size = None
        self.threads = []
        url = kwargs['url']
            
    def find_headers(self):
        global head_response
        print "Finding headers..."
        head_response = requests.head(self.url).headers
        self.size = head_response['Content-length'] if head_response['Content-length'] else None
        print head_response
            
    def add_to_queue(self):
        threads = []
        partition = int(self.size)/4
        for i in xrange(4):
                thread = myThread(i, [i*partition, (i+1)*partition], self.url)
                threads.append(thread)
        # print threads
        self.threads = threads

    def start_download(self):
        # global i
        for th in self.threads:
            th.start()
                
                
    def wait_for_complete(self):
        for thread in self.threads:
                thread.join()
        print "Exiting"
                
    def download_file(self):
        self.find_headers()
        self.add_to_queue()
        self.start_download()
        self.wait_for_complete()
        
                
        
def download(threadId, drange, url):
    headers = {"Range":"bytes={0}-{1}".format(drange[0], drange[1])}
    print headers
    
    size = drange[1] - drange[0]
    print "Starting Thread {0}".format(threadId)
    req = requests.get(url, headers=headers, stream=True)

    download_status[size] = size
    download_status[threadId] = 0
    # return req
    with open('test{0}.pdf'.format(threadId), 'w') as f:
        for r in pr.bar(req.iter_content(chunk_size=2048), expected_size=(size/2048)+1):
            if r:
                # print "{0}  {1}".format(threadId)
                f.write(r)
                f.flush()
    # if(req.status_code == 206):
    
        # req.raw.decode_content = True 
        

    # print req.headers['content-length']
    # for data in req.iter_content():
    #    download_status[threadId] += len(data)
       # print "Here"
       # print download_status
            # The download status must be updated in the global variable
            # and must be shown by kivy in the form of a progress bar.

####  TODO  ####

# 1. Handling Exceptions.
# 2. Error logging.
# 3. Merging the files

# df = DownloadFile(url="http://redirector.googlevideo.com/videoplayback?gcr=us&sparams=clen%2Cdur%2Cgcr%2Cgir%2Cid%2Cinitcwndbps%2Cip%2Cipbits%2Citag%2Ckeepalive%2Clmt%2Cmime%2Cmm%2Cmn%2Cms%2Cmv%2Cnh%2Cpl%2Csource%2Cupn%2Cxtags%2Cexpire&dur=203.400&key=yt6&fexp=9407015%2C9413209%2C9414823%2C9416126%2C9416891%2C9419452%2C9422596%2C9428398%2C9431012%2C9431718%2C9432049%2C9433096%2C9433223%2C9433946%2C9435526%2C9435666%2C9435693%2C9435699%2C9435876%2C9435958%2C9436015%2C9436345%2C9437066%2C9437228%2C9437553%2C9437742%2C9439585%2C9439652&itag=133&nh=IgpwcjAzLmlhZDA3KgkxMjcuMC4wLjE&mime=video%2Fmp4&expire=1467139959&lmt=1466153352724170&upn=lebHZuFpw8U&sver=3&clen=6228056&source=youtube&id=o-AGMznEXDNVIcFITAuZ3uulNXBDl0qK-KRqVrGhPq_XEe&mn=sn-p5qlsnez&mm=31&mv=m&keepalive=yes&ip=2a03%3A8180%3A1001%3A16a%3A%3A8ee1&pl=40&ms=au&ipbits=0&xtags=tx%3D9431718&gir=yes&initcwndbps=3455000&mt=1467118008&signature=0A0C12BD7F6919EF4362AF0C270312AF4694FB5F.09373031A64B8FBF80BBA3A0F145E0AA23C7B683&title=Ilahi+Yeh+Jawaani+Hai+Deewani+Full+Video+Song+%7C+Ranbir+Kapoor%2C+Deepika+Padukone")
df = DownloadFile(url = "http://www.souravsengupta.com/int2pro2014/python/LPTHW.pdf")
#df.url = "

df.download_file()

#df.find_headers()
#print "Found Headers...."

#df.add_to_queue()
#print "Added to queue...."


#print df.threads

#df.start_download()
#print "Downloading..."
