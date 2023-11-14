from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import hashlib

with open("Encrypted5", "rb") as files:
    iv = files.read(16)
    ct = files.read()

with open("R5.py", "rb") as files:
    content = files.read()
    k = hashlib.md5(content).digest()

cipher = AES.new(k, AES.MODE_CBC, iv)
pt = unpad(cipher.decrypt(ct), AES.block_size)

with open("Q5Decrypted.txt", "wb") as files:
    files.write(pt)