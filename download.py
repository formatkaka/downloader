import requests

import threading

# Obtain the link through 1. LocalDB 2. Scraping ######

url = ""
head_response = ""

# HEAD REQUEST TO KNOW THE SIZE OF THE FILE TO BE DOWNLOADED. #######


download_status = {}

i = 0
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
        self.count = kwargs['count']
        self.size = None
        self.threads = []
        url = kwargs['url']
            
    def find_headers(self):
        global head_response
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
        global i
        for th in self.threads:
            name = "th{0}.mp4".format(i)
            with open(name,"wb"):
                i = i+1;
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
    req = requests.get(url, headers=headers, stream=True)
    download_status[size] = size
    download_status[threadId] = 0
    return req
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

df = DownloadFile(url="http://r5---sn-cnoa-h55e.googlevideo.com/videoplayback?clen=4461773&mime=video%2Fmp4&keepalive=yes&source=youtube&ipbits=0&signature=0521F4FB278F66847F0912E95DA3C0B2B71157A5.150F1D1B458F0BAF35F0248250B93DD0AF287070&itag=160&key=cms1&dur=325.360&sver=3&expire=1467023207&pl=21&gir=yes&sparams=clen,dur,expire,gir,id,initcwndbps,ip,ipbits,ipbypass,itag,keepalive,lmt,mime,mm,mn,ms,mv,nh,pl,source,upn&fexp=9407015%2C9413209%2C9414823%2C9416126%2C9416891%2C9419452%2C9422596%2C9428398%2C9431012%2C9431718%2C9432049%2C9433096%2C9433223%2C9433946%2C9435526%2C9435666%2C9435693%2C9435699%2C9435876%2C9435958%2C9436015%2C9436345%2C9437066%2C9437228%2C9437553%2C9437742%2C9439474%2C9439585%2C9439652&ip=117.213.227.157&lmt=1458185049156504&id=o-ALW9AWjpuV_JI2I6F5QBUkbR1Z-iQoUFYlh8MNqCiqmt&upn=PKLBAlte3YI&title=Haule+Haule+-+Full+Song+%7C+Rab+Ne+Bana+Di+Jodi+%7C+Shah+Rukh+Khan+%7C+Anushka+Sharma&redirect_counter=1&req_id=3e66f5e19a69a3ee&cms_redirect=yes&ipbypass=yes&mm=31&mn=sn-cnoa-h55e&ms=au&mt=1467001411&mv=m", count=5)
#df.url = "

df.download_file()

#df.find_headers()
#print "Found Headers...."

#df.add_to_queue()
#print "Added to queue...."


#print df.threads

#df.start_download()
#print "Downloading..."
