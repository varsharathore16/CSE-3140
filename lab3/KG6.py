from Crypto.PublicKey import RSA
import os

key = RSA.generate(2048)
if not os.path.exists("Solutions"):
    os.makedirs("Solutions")

with open("Solutions/e.key", "wb") as file:
    file.write(key.publickey().exportKey())
with open("Solutions/d.key", "wb") as file:
    file.write(key.exportKey())