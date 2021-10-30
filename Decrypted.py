from subprocess import check_output
import os
from cryptography.fernet import Fernet
import sys
from colorama import init,Fore

def start_Decrypt(file_encrypt,file_key,type_file,name_new_file):
    
    file_full_encrypt = file_encrypt+".Notixer"
    if type_file[0] != ".":
        print("dont forget to add . first of type of file !! ")
        sys.exit(0)

    def decrypt(filename, key):
        """
        Given a filename (str) and key (bytes), it decrypts the file and write it
        """
        f = Fernet(key)
        with open(filename, "rb") as file:
            # read the encrypted data
            encrypted_data = file.read()
        # decrypt data file
        decrypted_data = f.decrypt(encrypted_data)
        # write the original file
        new_file = open(name_new_file+type_file, "wb")
        new_file.write(decrypted_data)
        new_file.close()
        #delete the encrypt file
        os.remove(file_full_encrypt)
        print(Fore.WHITE+file_full_encrypt +Fore.RED+   "    ------ >   "+Fore.WHITE+"   [Decrypted] ")
    decrypt(file_full_encrypt,file_key)