import hashlib

m = hashlib.md5("bgvyzdsv254575".encode('utf-8')).hexdigest()

print(m)

found = True
#found = False
number = 0
hashstring = "bgvyzdsv"
while(found):
    hashstring += str(number)
    number += 1
    m = hashlib.md5(hashstring.encode('utf-8')).hexdigest()
    if number % 1000 == 0:
        print(number)
    if m[0:6] == '000000':
        found = False
        print(hashstring)
    hashstring = "bgvyzdsv" 