import random
import os
import time

chars = "abcdefghijklmnopqrstuvwxyz1234567890"

pass_ori = str(input("Masukkan kata sandi yang hendak di pecahkan : "))
pass_length = int(len(pass_ori))
print ("panjang : ", pass_length)
print ("\nTunggu sebentar, kata sandi sedang dipecahkan...\n")
pass_crack = ""

begin = time.time()
while pass_crack != pass_ori :
    for i in range (0,pass_length) :
            pass_char = random.choice(chars)
            pass_crack = pass_crack + pass_char
    print (list(pass_crack))
    if pass_crack != pass_ori :
        pass_crack = ""
end = time.time()
execution_time = end-begin

print ("\n\nKata sandi terpecahkan : " + pass_crack)
print ("Dipecahkan dalam waktu : ", execution_time + "\n")


os.system ("pause")


