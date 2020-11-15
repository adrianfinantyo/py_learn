import random
import os

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

pass_ori = str(input("Masukkan kata sandi yang hendak di pecahkan : "))
pass_length = int(len(pass_ori))
print ("panjang : ", pass_length)
print ("\nTunggu sebentar, kata sandi sedang dipecahkan...\n")
pass_crack = ""
while pass_crack != pass_ori :
    for i in range (0,pass_length) :
            pass_char = random.choice(chars)
            pass_crack = pass_crack + pass_char
    print (list(pass_crack))
    if pass_crack != pass_ori :
        pass_crack = ""
print ("Kata sandi terpecahkan : " + pass_crack + "\n\n")


os.system ("pause")


