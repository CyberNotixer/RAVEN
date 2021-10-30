from colorama import Fore,init
import requests
import subprocess
import socket
#______________________________________________________________
def start_ip():
    init()
#Getting local ip
    hostname = socket.gethostname()
    ip_local = (socket.gethostbyname(hostname))
#Getting public ip
    http = requests.get("https://api.ipify.org/").text


    print(Fore.GREEN+"[+] "+Fore.LIGHTCYAN_EX+"your local ip = "+Fore.WHITE+ip_local)
    print(Fore.GREEN+"[+] "+Fore.LIGHTCYAN_EX+"your public ip = "+Fore.WHITE+http)
#______________________________________________________________