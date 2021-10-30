import zipfile
from colorama import init,Fore
#______________________________________________________________
def start_zip(wordlist,zip_file):
    """This func use for crack password of zip files"""
# initialize the Zip File object
    zip_file = zipfile.ZipFile(zip_file)
# count the number of words in this wordlist
    n_words = len(list(open(wordlist, "rb")))
# print the total number of passwords
    print("Total passwords to test :", n_words)
#______________________________________________________________
    with open(wordlist, "rb") as password:
        for word in password:
            try:
                zip_file.extractall(pwd=word)
            except:
                continue
            else:
                print(Fore.GREEN+"[+] "+Fore.WHITE+"Password found :"+Fore.GREEN, word.decode())
                exit(0)
    print(Fore.RED+"[!] "+Fore.WHITE+"Password not found")
#______________________________________________________________