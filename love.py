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


with open("thekey.key" ,"rb") as key:
        secretkey = key.read()
#         dycrypt now XDD
#secretphrase = "morgana"
#user_phrase = input("put the solution here\n")
#if user_phrase  == secretphrase:
for file in files:
        with open(file, "rb") as thefile:
                contents =thefile.read()
        contents_decrypted = Fernet(secretkey).decrypt(contents)
        with open(file ,"wb") as thefile:
                thefile.write(contents_decrypted)
#                print("u get it u should install lol now u knew morgana")
#else:
#        print("sorry , wrong answer try again ^^")
