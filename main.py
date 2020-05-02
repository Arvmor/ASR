from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
#**************************************************************************
chromedriver = "chromedriver.exe" # your chrome driver path
#**************************************************************************

#login
driver = webdriver.Chrome(chromedriver)
url = "your skyroom link url"
driver.get(url)
time.sleep(1)
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="username"]').send_keys("username")
driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("password")
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="btn_login"]').click()
