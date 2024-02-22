from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome()

driver.get("https://accounts-auth0.topcoder.com/#!/member?retUrl=http://www.topcoder.com/")
time.sleep(50)

element = driver.find_element_by_name("username")
element.click()
element.send_keys("this_is_my_username")

element = driver.find_element_by_name("password")
element.click()
element.send_keys("this_is_my_password")
