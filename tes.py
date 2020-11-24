from selenium import webdriver
import pyautogui
import time
import os

options = webdriver.ChromeOptions() 
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options, executable_path='C:\\chromedriver.exe')
driver.get ('https://google.com/')
teks = "Adrian Finantyo"
pyautogui.typewrite(teks.replace(" ", "_"))
button = driver.find_element_by_xpath('/html/body/div[2]/div[2]/form/div[2]/div[1]/div[3]/center/input[1]')
button.click()