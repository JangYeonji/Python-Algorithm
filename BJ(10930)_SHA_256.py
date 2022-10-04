#15분/15분
import hashlib

s = input()
h = hashlib.new('sha256')
h.update(bytes(s,"utf-8"))
print(h.hexdigest())


