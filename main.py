import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
time.sleep(5)
driver.get("https://practicetestautomation.com/practice-test-login/")
time.sleep(10)
username_locator = driver.find_element(By.ID, "username")
password_locator = driver.find_element(By.NAME, "password")
submit_button_locator = driver.find_element(By.XPATH, "/html//button[@id='submit']")