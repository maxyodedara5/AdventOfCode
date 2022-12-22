# https://adventofcode.com/2022/day/3

def read_file(filename):
    # Read file data from file
    with open(filename) as file:
        data = file.readlines()
    return data


filename = "day_3_input.txt"
data = read_file(filename)

data = [i.strip() for i in data]


common = set()
final_list = []
for i in data:
    half_items = len(i) // 2
    for item in i[0:half_items]:
        if item in i[half_items:]:
            common.add(item)
            #print(item)
    #print(common)
    final_list.extend(list(common))
    common.clear()


print(f"Final list len : {len(final_list)}")
priorities = "abcdefghijklmnopqrstuvwxyz"
p_map = {}
num = 1 
for i in priorities:
    p_map[i] = num
    p_map[i.upper()] = num + 26
    num += 1

total = 0 
for i in final_list:
    total += p_map[i]

print(f"Part1 Total of priorities : {total}")

# Part 2 
ranks_found = []
for num in range(0,len(data),3):
    elv1 = data[num]
    elv2 = data[num + 1]
    elv3 = data[num + 2]

    for item in elv1:
        if item in elv2 and item in elv3:
            ranks_found.append(item)
            break

total = 0 
for i in ranks_found:
    total += p_map[i]

print(f"Ranks found len : {len(ranks_found)}")
print(f"Part2 Total of rank/badge priorities : {total}")
