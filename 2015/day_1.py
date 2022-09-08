# https://adventofcode.com/2015/day/1

def read_file(filename):
    # Read file data from file
    with open(filename) as file:
        data = file.readlines()
    return data


filename = "day1_Alternate.txt"
data = read_file(filename)
print(type(data[0]))

pos_floors = data[0].count('(')
neg_floors = data[0].count(')')

floor_to_go = pos_floors - neg_floors 
print(floor_to_go)

current_floor = 0
for charcount, floor in enumerate(data[0]):
    if floor == '(':
        current_floor += 1
    if floor == ')':
        current_floor -= 1
    if current_floor == -1 :
        print(charcount)
        break