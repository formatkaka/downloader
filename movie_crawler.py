from selenium import webdriver

from selenium.webdriver.common.keys import Keys

quality_req = "720"

# Web driver instance
driver = webdriver.Firefox()

# Opening page and search for movie.

driver.get("http://www.khatrimaza.org/index.html")

elem = driver.find_element_by_xpath("//input[@name='hladany_vyraz']")

elem.send_keys("3 idiots")

driver.find_element_by_xpath("//input[@value='SEARCH MOVIES']").click()

# Check for quality

my_links = driver.find_elements_by_partial_link_text("s")

# my_links2 = driver.find_elements_by_tag_name('a')

print my_links




