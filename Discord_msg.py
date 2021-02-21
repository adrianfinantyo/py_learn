import requests
import os

# https://discord.com/api/v8/channels/453597493230305291/messages   (bis-kecil-tayo = BO)


# Function berikutnya:
def utama ():
    os.system ("cls")
    print ("[1] SEND Message ke makan-nano-nano (DE)")
    print ("[2] SEND Message ke bis-kecil-tayo (BO)")
    print ("[3] SEND Message ke Zbagas")
    print ("[4] SEND Message ke Javelineou")
    print ("[0] EXIT programs")
    n = int(input("\ncommand : "))
    if (n == 1):
        send_msg1()
    elif (n==2):
        send_msg2()
    elif (n==3):
        send_msg3()
    elif (n==4):
        send_msg4()
    elif (n==0):
        os.system("exit")
    else:
        print ("Perintah salah mohon diulangi!")
        os.system ("pause")
        os.system ("cls")
        utama()

# def status ():
#     os.system ("cls")
#     print ("MASIH NGEBUG ANJG GA BSIA-BISA\n")
#     print ("[1] Online")
#     print ("[2] Idle")
#     print ("[3] Do Not Disturb")
#     print ("[4] Invisible")
#     print ("[0] Cancel")
#     stat = int(input("\nSet status ke : "))

#     header = {
#     'Authorization': 'NDE5MTUyODIzODMwNDQ2MDgw.X2GGVw.B59jEFp9RZeRqqewt_o79wT-uEA'
#     }
#     if (stat == 1):
#         payload = {
#         "status":"online"
#         }
#         r = requests.patch("https://discord.com/api/v8/users/@me/settings", data=payload, headers=header)
#     elif (stat == 2):
#         payload = {
#         "status": "idle"
#         }
#         r = requests.patch("https://discord.com/api/v8/users/@me/settings", data=payload, headers=header)
#     elif (stat == 3):
#         payload = {
#         "status": "dnd"
#         }
#         r = requests.patch("https://discord.com/api/v8/users/@me/settings", data=payload, headers=header)
#     elif (stat == 4):
#         payload = {
#         "status": "invisible"
#         }
#         r = requests.patch("https://dis1cord.com/api/v8/users/@me/settings", data=payload, headers=header)
#     elif (stat == 0):
#         utama()
#     else:
#         print("Input salah!")
#         os.system("pause")
#         status()
#     utama()
        
def send_msg1 ():
    os.system ("cls")
    msg = str(input("Masukkan text : "))
    payload = {
        'content': msg
    }
    header = {
        'Authorization': 'NDE5MTUyODIzODMwNDQ2MDgw.X2GGVw.B59jEFp9RZeRqqewt_o79wT-uEA'
    }
    r = requests.post("https://discord.com/api/v8/channels/453467733766569995/messages", data=payload, headers=header)

    print ("pesan terkirim")
    os.system ("pause")
    utama()

def send_msg2 ():
    os.system ("cls")
    msg = str(input("Masukkan text : "))
    payload = {
        'content': msg
    }
    header = {
        'Authorization': 'NDE5MTUyODIzODMwNDQ2MDgw.X2GGVw.B59jEFp9RZeRqqewt_o79wT-uEA'
    }
    r = requests.post("https://discord.com/api/v8/channels/453597493230305291/messages", data=payload, headers=header)

    print ("pesan terkirim")
    os.system ("pause")
    utama()

def send_msg3 ():
    os.system ("cls")
    msg = str(input("Masukkan text : "))
    payload = {
        'content': msg
    }
    header = {
        'Authorization': 'NDE5MTUyODIzODMwNDQ2MDgw.X2GGVw.B59jEFp9RZeRqqewt_o79wT-uEA'
    }
    r = requests.post("https://discord.com/api/v8/channels/778181893916459031/messages", data=payload, headers=header)

    print ("pesan terkirim")
    os.system ("pause")
    utama()

def send_msg4 ():
    os.system ("cls")
    msg = str(input("Masukkan text : "))
    payload = {
        'content': msg
    }
    header = {
        'Authorization': 'NDE5MTUyODIzODMwNDQ2MDgw.X2GGVw.B59jEFp9RZeRqqewt_o79wT-uEA'
    }
    r = requests.post("https://discord.com/api/v8/channels/778181893916459031/messages", data=payload, headers=header)

    print ("pesan terkirim")
    os.system ("pause")
    utama()

# Awal mula kode 
utama()