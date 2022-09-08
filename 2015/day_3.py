# https://adventofcode.com/2015/day/3

def read_file(filename):
    # Read file data from file
    with open(filename) as file:
        data = file.readlines()
    return data


filename = "day_3_input.txt"
data = read_file(filename)

santastring = ""
robotstring = ""
for index, pos in enumerate(data[0]):
    if index % 2 == 0:
        santastring += pos
    else:
        robotstring += pos


print(len(santastring),len(robotstring))

positions_index = set()
x = 0 
y = 0 

positions_index.add((x,y))
for pos in robotstring:

    if pos == '>':
        x += 1
        positions_index.add((x,y))
    
    if pos == '<':
        x -= 1
        positions_index.add((x,y))
    
    if pos == '^':
        y += 1
        positions_index.add((x,y))
    
    if pos == 'v':
        y -= 1
        positions_index.add((x,y))
    
print(len(positions_index))



x = 0 
y = 0 

positions_index.add((x,y))
for pos in santastring:

    if pos == '>':
        x += 1
        positions_index.add((x,y))
    
    if pos == '<':
        x -= 1
        positions_index.add((x,y))
    
    if pos == '^':
        y += 1
        positions_index.add((x,y))
    
    if pos == 'v':
        y -= 1
        positions_index.add((x,y))
    
print(len(positions_index))