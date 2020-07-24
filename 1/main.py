from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Firefox()
driver.get('https://www.google.com')
elem = driver.find_element_by_name('q')
elem.send_keys('Software Engineering')
elem.send_keys(Keys.RETURN)
sleep(2)
driver.close()

# Scenario 1
# driver = webdriver.Firefox()
# driver.get('https://www.google.com')
# elem = driver.find_element_by_name('q')
# elem.send_keys('Software Engineering')
# elem.send_keys(Keys.RETURN)
# sleep(2)
# driver.close()
