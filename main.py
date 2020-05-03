# requirements
# pip install selenium
# replace your skyroom class URL, username and password
# move your chromedriver.exe to same path
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

#**************************************************************************
chromedriver = "chromedriver.exe" # your chromedriver.exe path
driver = webdriver.Chrome(chromedriver)
#**************************************************************************

#login
url = "your skyroom link url"
driver.get(url)
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="username"]').send_keys("username")
driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("password")
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="btn_login"]').click()
