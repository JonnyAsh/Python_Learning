import hashlib
crypt = hashlib.sha256()
crypt.update(b"hello, world")

print(crypt.hexdigest())