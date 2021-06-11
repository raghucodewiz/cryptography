# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 12:40:41 2021

@author: singh
"""
from Crypto.Cipher import AES  #Works

def pad(entry):
    padded = entry+(16-len(entry)%16)*'['
    return(padded)

plain_text='Bali is paradise'
plain_text = pad(plain_text)
plain_text=plain_text.encode('UTF-8')
key='1234'
key=pad(key)
key=key.encode('UTF-8')

cipher = AES.new(key, AES.MODE_ECB)
ciphertext = cipher.encrypt(plain_text)
print(ciphertext)

cipher2=AES.new(key, AES.MODE_ECB)
data=cipher.decrypt(ciphertext)

data=data.decode('UTF-8')
unpad = data.find('[')
data = data[:unpad]
print('decoded text = ', data)