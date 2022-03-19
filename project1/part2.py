import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends.openssl.backend import backend
import binascii
wordArr = []
file = open("words.txt", "r")
while file:
    word  = file.readline().strip()
    if len(word) <= 16:
        wordArr.append(bytes(word))
    if word == "":
        break
file.close() 

Plaintext =  b"This is a top secret." +  b'\x0b'*11
Ciphertext = "8d20e5056a8d24d0462ce74e4904c1b513e10d1df4a2ef2ad4540fae1ca0aaf9"
iv = b'\x00'*16
totWords = len(wordArr)


for x in range(0, totWords):
    key = wordArr[x]
    if len(key) != 16:
        while len(key) != 16:
            key += b'\x20'
            #print(x)
            if len(key) == 16:
                break;
    
    encryptor = Cipher(algorithms.AES(key), modes.CBC(iv), backend).encryptor()
   
    ct = encryptor.update(Plaintext) + encryptor.finalize()

    if (binascii.hexlify(ct) == Ciphertext):
        print("The key is: " + key.decode('UTF-8'))
    
    