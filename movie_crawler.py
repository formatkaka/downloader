from selenium import webdriver

from selenium.webdriver.common.keys import Keys

import re

import thread

quality_req = "720"

# Web driver instance
driver = webdriver.Firefox()

Opening page and search for movie.

	driver.get("http://www.khatrimaza.org/index.html")

	elem = driver.find_element_by_xpath("//input[@name='hladany_vyraz']")

	elem.send_keys("3 idiots")

	driver.find_element_by_xpath("//input[@value='SEARCH MOVIES']").click()

Check for quality

driver.get('http://www.khatrimaza.org/search.html?hladany_vyraz=3+idiots&spid=140945873&sph=e961d7fa8fedef889872545094109f8f&submit=SEARCH+MOVIES')

my_links = driver.find_elements_by_partial_link_text("s")
regex_movie = re.compile(r'(\d)+.html')
# print type(my_links[0])
movies = [link.get_attribute("href") for link in my_links if regex_movie.search(link.get_attribute("href"))]

def find_link_quality(quality, movies):
	""" FUnction to find suitables link of required quality"""
	pass

page_1_links = find_link_quality(quality_req, movies)

page_1_links = movies[1:4]
print page_1_links

def find_link(t_id, link):
	""" Find suitable download links available """
	print page_1_links
	page_2 = driver.get(page_1_links[0])
	elem = driver.find_elements_by_partial_link_text("s")
	regex_movie_2 = re.compile(r'site_(\d)+.html')
	links = [link for link in elem if regex_movie_2.search(link.get_attribute("href"))]
	links[0].click()

find_link(1, "a")

driver.get('http://www.khatrimaza.org/site_32352.html')

def find_download_links_1():
	""" Find downloadable links available across servers. """
	dwn_links = driver.find_elements_by_xpath("//div[@class='Az']")
	for link in dwn_links:
		foo = link.find_element_by_tag_name('a')
		foo.click()
		break

def find_download_links():
	""" Find downloadable links available across servers. """
	dwn_links = driver.find_elements_by_tag_name('a')
	dwn = [link.get_attribute("href") for link in dwn_links if link.get_attribute("href").startswith("http://")]
	print dwn

find_download_links()
############ Webdriver is not THREAD-SAFE #############
# try:
# 	for t_id,link in enumerate(page_1_links):
# 		thread.start_new_thread(find_link , (t_id, link))
# except Exception, e:
# 	print e