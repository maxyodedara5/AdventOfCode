# https://adventofcode.com/2015/day/5

def read_file(filename):
    # Read file data from file
    with open(filename) as file:
        data = file.readlines()
    return data


filename = "day_5_input.txt"
data = read_file(filename)


def vowelcheck(strck):
    vowels = ['a','e','i','o','u']
    total_vowels = 0
    for letter in vowels:
        total_vowels += strck.count(letter)
        if letter in strck:
            if strck.count(letter) >= 3:
                return True
    
    if total_vowels >= 3:
        return True
    return False

def double_letter_check(strck):
    for i in range(0,len(strck) -1):
        if strck[i] == strck[i+1]:
            return True
    
    return False

def badltr(strck):
    badletters = ['ab', 'cd', 'pq', 'xy']
    for letters in badletters:
        if letters in strck:
            return False

    return True

"""nicestring = 0 
for strck in data:
    if vowelcheck(strck) and double_letter_check(strck) and badltr(strck):
        nicestring += 1 

print(nicestring)
"""

def repeatcheck(strck):
    for i in range(len(strck) -2):
        if strck.count(strck[i:i+2]) >=2 :
            return True
    
    return False

def middlecheck(strck):
    for i in range(len(strck) - 2):
        if strck[i] == strck[i+2]:
            return True

    return False

nicestring = 0 
for strck in data:
    if middlecheck(strck) and repeatcheck(strck):
        nicestring += 1 

print(nicestring)

