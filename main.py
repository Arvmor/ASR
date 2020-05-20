# replace your skyroom class URL, username and password
# move your chromedriver.exe to same path
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pyautogui


def sendMessage(text):
    driver.find_element(
        By.XPATH, '//*[@id="sidebar"]/div[4]/div[2]/div/div[2]/div[3]/div[1]').send_keys(text)
    pyautogui.press('enter')


chromedriver = "chromedriver.exe"  # your chromedriver.exe path
driver = webdriver.Chrome(chromedriver)


# login
url = "your skyroom link url"  # change your class URL link
driver.get(url)
time.sleep(2)
# change your username
driver.find_element(By.XPATH, '//*[@id="username"]').send_keys("username")
# change your password
driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("password")
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="btn_login"]').click()
sendMessage("Salam")
