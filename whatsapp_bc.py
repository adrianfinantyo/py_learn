from selenium import webdriver
import os
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options)
driver.get ('https://web.whatsapp.com/')
print ("Masukkan pesan yang ingin disiarkan :")
pesan = str(input())
input("Tekan apa saja untuk melanjutkan!")

kon_list = "C:\\Dev\\py_learn\\kontak.txt"
os.path.exists(kon_list)
k = open (kon_list, 'r')

for kontak in k :
    print (kontak) 
    driver.implicitly_wait(10)
    driver.get ('https://web.whatsapp.com/send?phone=' + kontak + '&text=' + pesan.replace(" ","+") + '&app_absent=0')
    button = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[3]/button/span')
    button.click()