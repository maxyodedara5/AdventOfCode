# https://adventofcode.com/2022/day/4

def read_file(filename):
    # Read file data from file
    with open(filename) as file:
        data = file.readlines()
    return data


filename = "day_4_input.txt"
data = read_file(filename)

data = [i.strip() for i in data]

fully_in_range = 0 
partially_in_range = 0 

for i in data:
    elf1_pair, elf2_pair = i.split(",")
    elf1_point1, elf1_point2 = elf1_pair.split("-")
    elf2_point1, elf2_point2 = elf2_pair.split("-")

    elf1_point1 = int(elf1_point1)
    elf1_point2 = int(elf1_point2)
    elf2_point1 = int(elf2_point1)
    elf2_point2 = int(elf2_point2)

    elf1_range = [*range(elf1_point1,elf1_point2 + 1,1)]
    elf2_range = [*range(elf2_point1,elf2_point2 + 1,1)]
    
    # 11 12 . 21 22
    if elf1_point1 in elf2_range and elf1_point2 in elf2_range:
        fully_in_range += 1
    elif elf2_point1 in elf1_range and elf2_point2 in elf1_range:
        fully_in_range += 1

    # Part 2 
    overlap = list(set(elf1_range).intersection(elf2_range))
    if len(overlap ) > 0:
        partially_in_range += 1

print(f"Part 1 Fully in range : {fully_in_range}")
print(f"Part 2 Partially in range : {partially_in_range}")
