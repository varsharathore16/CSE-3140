import sys
import subprocess
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

with open(sys.argv[1], 'rb') as f:
    ct = f.read()

idfile = sys.argv[1][:-10] + '.ID'

x = subprocess.Popen(["python3", "AD6.py", f"{idfile}"], stdout=subprocess.PIPE)
AES_key = x.stdout.read()  

cipher = AES.new(AES_key, AES.MODE_CBC)

pt = unpad(cipher.decrypt(ct), AES.block_size)

file = sys.argv[1][:-10]

with open(file, 'wb') as f:
    f.write(pt[16:])