import requests



###### Obtain the link through 1. LocalDB 2. Scraping ######

download_link = ""

###### HEAD REQUEST TO KNOW THE SIZE OF THE FILE TO BE DOWNLOADED. #######

head_response = requests.head(download_link)

content_length = head_response['content-length'] if head_response['content-length'] else None


##### CODE TO SPAWN THREADS AND START DOWNLOADING #####

