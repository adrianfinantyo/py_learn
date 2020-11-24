import os

def utama ():
    print ("\t" + r" ________________________________________________________________________ ")
    print ("\t" + r"|     _______ ______  _____ _______   _____ _____ _   _  _____   _ _     |")
    print ("\t" + r"|    |__   __|  ____|/ ____|__   __| |  __ \_   _| \ | |/ ____| | | |    |")
    print ("\t" + r"|       | |  | |__  | (___    | |    | |__) || | |  \| | |  __  | | |    |")
    print ("\t" + r"|       | |  |  __|  \___ \   | |    |  ___/ | | | . ` | | |_ | | | |    |")
    print ("\t" + r"|       | |  | |____ ____) |  | |    | |    _| |_| |\  | |__| | |_|_|    |")
    print ("\t" + r"|       |_|  |______|_____/   |_|    |_|   |_____|_| \_|\_____| (_|_)    |")
    print ("\t" + r"|                                                                        |")
    print ("\t" + r"|                             by : Adrian F.                             |")
    print ("\t" + r"|________________________________________________________________________|")

    print ("\n\nTekan angka untuk melakukan test ping!")
    print ("[1] Google.com")
    print ("[2] 8.8.8.8")
    print ("[0] EXIT Program")
    ping = int(input("Test ping ke : "))
    if (ping == 1):
        os.system ("cls")
        os.system ("ping -t google.com")
    elif (ping == 2):
        os.system ("cls")
        os.system ("ping -t 8.8.8.8")
    elif (ping == 0):
        os.system ("exit")
    else:
        print ("Maaf input anda salah, silahkan diulangi")
        os.system ("pause")
        utama ()

# MAIN MODUL
utama ()