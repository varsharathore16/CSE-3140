from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

input = "Encrypted4"
output = "Q4Decrypted.txt"
key = ".key.txt"

with open(key, "rb") as files:
    k = files.read()

with open(input, "rb") as files:
    iv = files.read(16)
    ct = files.read()

cipher = AES.new(k, AES.MODE_CBC, iv)
pt = unpad(cipher.decrypt(ct), AES.block_size)

with open(output, "wb") as files:
    files.write(pt)