import os
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
from Crypto.Signature import PKCS1_v1_5

with open('Q3pk.pem', 'rb') as key_f:
    data_f = key_f.read()
key = RSA.import_key(data_f)

signature = PKCS1_v1_5.new(key)

for file in os.listdir('/home/cse/Lab3/Q3files'):
    fp = os.path.join('/home/cse/Lab3/Q3files', file)
    if file.endswith('.sign'):
        continue
    with open(fp, 'rb') as f:
        data = f.read()
        hash = SHA256.new(data)

    sf = file + ".sign"
    sp = os.path.join('/home/cse/Lab3/Q3files', sf)
    with open(sp, 'rb') as sigf:
        sig = sigf.read()
    if signature.verify(hash, sig):
        print(f'{file} is correctly signed')