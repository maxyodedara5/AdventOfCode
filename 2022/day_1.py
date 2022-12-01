# https://adventofcode.com/2022/day/1

def read_file(filename):
    # Read file data from file
    with open(filename) as file:
        data = file.readlines()
    return data


filename = "day_1_input.txt"
data = read_file(filename)

data = [i.strip() for i in data]

elves = []
total_elves = 0
calories = 0 
for i in data:
    if i == "":
        # New elf 
        elves.append(calories)
        calories = 0
        total_elves += 1
    else:
        calories += int(i)


# Solution 1 
print(max(elves))

# Solution 2
elves.sort()
print(elves[-1] + elves[-2] + elves[-3])