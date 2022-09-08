# https://adventofcode.com/2015/day/8


import ast
from base64 import decode
from hashlib import new


def read_file(filename):
    # Read file data from file
    with open(filename) as file:
        data = file.readlines()
    return data

filename = "day_8_input.txt"
data = read_file(filename)


string_len = 0 
string_literal_len = 0 


for i in data:
    string_len += len(i)-1
    #print(len(i)-1)
    string_literal_len += len(eval(i))
    #print(len(eval(i)))

print(string_len)
print(string_literal_len)
print(string_len - string_literal_len)


string_len = 0 
string_literal_len = 0

for i in data:
    string_len += len(i)-1
    #print(i)

    newstr = []
    for j in i:
        if j == '"':
            newstr.append('/')
            newstr.append('"')
        elif j == '\\':
            newstr.append('/')
            newstr.append('/')
        else:
            newstr.append(j)
    #print(len(newstr) + 1)
    string_literal_len += len(newstr) + 1

print(string_len)
print(string_literal_len)
print(string_literal_len - string_len)
