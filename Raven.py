from colorama import init,Fore
import sys
import os
from Zip import start_zip
from time import sleep
from ip import start_ip
from Encrypted import start_Encrypt
from Decrypted import start_Decrypt

#________________________________________________________________________

def baner():
    print(Fore.RED+"""8888888b.                                      
888   Y88b                                     
888    888                                     
888   d88P  8888b.  888  888  .d88b.  88888b.  
8888888P"      "88b 888  888 d8P  Y8b 888 "88b 
888 T88b   .d888888 Y88  88P 88888888 888  888 
888  T88b  888  888  Y8bd8P  Y8b.     888  888 
888   T88b "Y888888   Y88P    "Y8888  888  888""")

def info():
    print(Fore.WHITE+"""
1_Windows_Password\n
2_Encrypt\n
3_Decrypt\n
4_Zip_Cracker\n
5_Ip_system\n
6_Close
""")
#________________________________________________________________________

try:
    import subprocess
except ModuleNotFoundError:
    print("Please install subprocess !")

try:
    import cryptography.fernet
except ModuleNotFoundError:
    print("Please install cryptography !")

try:
    import zipfile
except ModuleNotFoundError:
    print("Please install zipfile !")

try:
    import sqlite3
except ModuleNotFoundError:
    print("Please install sqlite3 !")

try:
    import win32crypt
except ModuleNotFoundError:
    print("Please install win32crypt ! ")

    
try:
    import shutil
except ModuleNotFoundError:
    print("Please install shutil !")
    
try:
    import colorama
except ModuleNotFoundError:
    print("Please install colorama ! ")
    
try:
    import requests
except ModuleNotFoundError:
    print("Please install requests ! ")
    
#________________________________________________________________________
def all_1():
    print(Fore.WHITE + "________________________________________________________________________")
    baner()
    info()
    
all_1()
ask = input(">>> ")

if ask == "":
    print(Fore.RED+"[!]"+Fore.WHITE+" Enter the number :)" )
#________________________________________________________________________
#Zip cracker :
elif ask == "4":
    os.system("cls")
    baner()
    print(Fore.WHITE+"_______________________________________________________________")
    ZIP = input("Enter the name of zip file : ")
    password = input("Enter the name of password list : ")
    start_zip(password,ZIP)
#________________________________________________________________________
#ip
elif ask == "5":
    os.system("cls")
    baner()
    print(Fore.WHITE+"_______________________________________________________________")
    start_ip()
#________________________________________________________________________
#Windows_Password
elif ask == "1":
    os.system("cls")
    baner()
    print(Fore.WHITE+"_______________________________________________________________")
    os.startfile("Windows_Password_Cracker.exe")
#________________________________________________________________________
#Encrypt
elif ask == "2":
    os.system("cls")
    baner()
    print(Fore.WHITE+"_______________________________________________________________")
    normal = input("Enter the name of file : ")
    start_Encrypt(normal)
#________________________________________________________________________
#Decrypt
elif ask == "3":
    os.system("cls")
    baner()
    print(Fore.WHITE+"_______________________________________________________________")
    D_encrypt = input("Enter the name of file : ")
    D_key = input("Enter the key : ")
    D_type = input("Enter the type of file (jpg,mp4,...)  : ")
    D_new_file = input("Enter the name of new file : ")
    start_Decrypt(D_encrypt,D_key,D_type,D_new_file)
#________________________________________________________________________
#Close
elif ask == "6":
    os.system("cls")
    print("\nSee you later"+Fore.RED+" :)")
#________________________________________________________________________