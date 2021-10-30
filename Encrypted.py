from subprocess import check_output
import os
from cryptography.fernet import Fernet
from colorama import init,Fore

def start_Encrypt(file_normal):
# make the key :
    key = Fernet.generate_key()
    print("this is your key : \n")
    print(key)
    Encrcrypt = Fernet(key)
# save key in key.txt 
    with open("key.txt","w") as r:
        r.write(str(key))
    print(Fore.WHITE+"\nkey was save in : "+Fore.GREEN+"key.txt\n")
    dirlist =  open(file_normal, "rb") 
    data = dirlist.read()
#Encrypt data file
    enc_data = Encrcrypt.encrypt(data)
    new_file = open(file_normal+".Notixer", "wb")
    new_file.write(enc_data)
    dirlist.close()
    new_file.close()
    os.remove(file_normal)
    print(Fore.LIGHTWHITE_EX + file_normal +   Fore.LIGHTRED_EX+"     ------ >   "+Fore.LIGHTWHITE_EX+"   [Encrypted] ")