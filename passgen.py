import random
import os

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890-=!@#$%^&*()_+`~;':"",./<>?"
stat = "y"

while stat == "Y" or stat == "y" :
    os.system("cls")
    password_length = int(input("Berapa panjangan kata sandi yang diinginkan : "))
    password_count = int(input("Berapa banyak kata sandi : "))
    for i in range (0,password_count):
        password = ""
        for i in range (0,password_length):
            password_char = random.choice(chars)
            password      = password + password_char
        print ("Kata sandi : ", password)
    print ("\n")
    stat = str(input("Ketik (Y/y) untuk melanjutkan : "))
