import sys
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

# Private RSA key in string format
pk_str = """-----BEGIN RSA PRIVATE KEY-----
MIIEogIBAAKCAQEAyTAVm/wXDvUR6BNTS8Fl/siCklVjpDouqhpR1WJCsG1tjfv0
VZL4AsQF4QY/DkHYQNU4CRElZ+OyUdG531h6310wUYrWy6YZMPrylFfjCoL1SdGV
Pc7TdglWmdGu+/48/a+g6/Fkccxsv/c3NY7HIgDLBqEEMNFC1ARu5D21z/q0rzAR
bt/yzXk8F7yNs54FW0d3wdElIGGCUb4Z2JYLKHGxJzQoUCznw41HuhSyk7HFK+7K
+r3IN/LaO/8qDvKBu9NVwYrFF0isD/86R7B8U2eCv2S7p4B0G7ZElgYOtZQC+1kf
GlWWpInB6EQhJ33i8zDm2/9nh5IIKKMqdW59vwIDAQABAoIBAGGOanwX8opzNbqm
XFa4sh+o1P/mXgnNmMEtQA9LtXDdrykRSrqQKKkWqo8iO0NLlHRjr+ddpBjLZbWd
EBeITRSwmHSB8YQQx9hjZ2udbl+zfwPLmCW/e/SZtJ+j+MkC0Epndo3SoNU5vmYb
l27mDBOl9M0DGQgfANvURn1wmw/88rMDN8mzSnE+l9GKC4RWkbpRFqXRbbSNQmlo
/U4TnK8YTJ5+mDp7P0V2AD8CY/xz4caGXAw4jSjQh70vfkeAr0mAV1pKDC51Hj6u
OhiMmbHY0mO3/DqayHV2vnJnHOGLrKd/IMaEZteqGnbXqf/zJsQFTMw3mfpOAh35
pTMXmeECgYEA4I5SPFtoXYx58ItdEEdys2Hhkz2hekUOt7uJKc7RN2ELOOTxCfgP
LytctrVp1ARFvLg6b14eSQy9Oj37Lz88LUhZ4gH2qkzuuPhvTk0cbdb5XOrZMmFK
TO9e4TAK38p08YPmrw8DIhI1rQLgkxG/OVsUTagQXEJ3kVFNawwcADECgYEA5VwV
i/SpZ+23wrTKCpYdPQndfrOynZbZzdgIwTnxNSpz1hvPmEw/DqnKAScPVMtGxAxd
omRZf4+BLq8ZxkfWj+qQWPEysS9f6cPmj9s8f3iE5R1v/pNeSSI++vz0k0tdmC35
LIyGZSsvPf8PqCf1FKDFX531dGmvIrdfQo8rUO8CgYAWbB+qBzaUoMJMUp4oUfoS
D2QG39CP9PVTQ1ae5hfd/8KvG6014Z8ihqHrXJIEqaiM/5hWJn+/q5X5itbaEOZh
XygaeTe4KZZsweHbX7fHAABGVuz5Kt3QcNZ4heOQFRc4RoNyV31omYjijbb++Hav
s3iDiJSZocluqT+hwMPLAQKBgFTEJJ52DMoBPEH0iRtCgYnWhIrYJPJDFzoRVqL7
JB9PEkKWQrH5s/BaZfLpGaxv+DZqj4x94+nWAptbUX5LfIvx1+lXMzHy3VLK+QI/
t2sxAoSezY5brqP+ySH/rPBnES82BnolcWIghLQ3+PRf2B8IkAmXmmisynJdLRKv
UQX3AoGAWvtvfLEVegoJV9z3ADQEObjfnUN79R9Q3YvD6rSq5AwZ4gClEMgdCAvo
gddaF/eYGqBMtjvr0saUGKtsPQKvagbuVznwt6Bp/kAOHSb+rCUsUB6qzVl6weA1
6cZMS/7cj9/cDVlv5vLm0Uz0UQZKXocfAHUWbfUMzhylfmpd7x8=
-----END RSA PRIVATE KEY-----"""

pk = RSA.importKey(pk_str)

with open(sys.argv[1], 'rb') as file:
    enc = file.read()

AES_key = PKCS1_OAEP.new(pk).decrypt(enc)

sys.stdout.buffer.write(AES_key)