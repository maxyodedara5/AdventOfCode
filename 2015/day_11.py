# https://adventofcode.com/2015/day/11

def valid_password(new_pass):
    # Condition 1 Triples
    # abc , bcd , etc 
    triple_check = False
    for i in range(len(new_pass)-2):
        #print(new_pass[i],(new_pass[i+1]-1),(new_pass[i+2]-2))
        if (new_pass[i] == (new_pass[i+1]-1) == (new_pass[i+2]-2)):
            triple_check = True

    letter_check = True
    # Condition 2 
    if (ord('i') in new_pass or
        ord('o') in new_pass or
        ord('l') in new_pass):
        letter_check = False

    # Condition 3 
    twice_count = 0 
    twice_condition = True
    same_letters = []
    for i in range(len(new_pass)-1):
        if new_pass[i] == new_pass[i+1]:
            if new_pass[i] not in same_letters:
                twice_count += 1
                same_letters.append(new_pass[i])

    if twice_count < 2:
        twice_condition = False

    #print(triple_check,letter_check,twice_condition)
    return (triple_check and letter_check and twice_condition)


def next_possible_pass(new_password):
    new_password[-1] += 1
    try:
        index_z = new_password.index(123)
        contains_overflow = True
        while(contains_overflow):
            new_password[index_z] = ord('a')
            new_password[index_z-1] += 1
            if (123 in new_password):
                contains_overflow = True
                index_z = new_password.index(123)
            else:
                contains_overflow = False
    except:
        #print("Did this happen")
        pass
        
    return new_password


def escape3letters(newpass):
    if newpass.count(105) > 0:
        index_i = newpass.index(105)
        newpass[index_i] += 1
        for i in range(index_i+1,len(newpass)):
            newpass[i] = 97
        #replace all after i and inc 
        return newpass

    if newpass.count(108) > 0:
        index_i = newpass.index(108)
        newpass[index_i] += 1
        for i in range(index_i+1,len(newpass)):
            newpass[i] = 97
        #replace all after i and inc 
        return newpass

    if newpass.count(111) > 0:
        index_i = newpass.index(111)
        newpass[index_i] += 1
        for i in range(index_i+1,len(newpass)):
            newpass[i] = 97
        #replace all after i and inc 
        return newpass
   

input_str = "vzbxkghb"
new_password = [ord(x) for x in input_str]
print(new_password)
print(input_str)

tracker = 0
while(not valid_password(new_password)):
    newpass = next_possible_pass(new_password)
    if (105 or 108 or 111) in newpass:
        newpass = escape3letters(new_password)

    tracker += 1 
    if tracker % 1000 == 0:
        print(tracker)

newpass = [chr(x) for x in newpass]
print("".join(newpass))
