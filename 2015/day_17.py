# https://adventofcode.com/2015/day/17

from itertools import chain, combinations

def read_file(filename):
    # Read file data from file
    with open(filename) as file:
        data = file.readlines()
    return data

filename = "day_17_input.txt"
data = read_file(filename)

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

containers_list = []

for i in data:
    containers_list.append(int(i))

print(len(containers_list))
all_combos = list(powerset(containers_list))
print(len(list(powerset(containers_list))))

"""print(type(all_combos[0]))
all_combos = [list(x) for x in all_combos]
print(type(all_combos[0]))
"""
capacity = 150
valid_combos = 0

valid_combos_len = {}
min_containers = 0
for combo in all_combos:
    addition = 0 
    for num in combo:
        addition += num 
    
    if addition == capacity:
        valid_combos += 1
        
        if len(combo) in valid_combos_len:
            valid_combos_len[len(combo)] += 1
        else:
            valid_combos_len[len(combo)] = 1

        if (len(combo) == 4):
            min_containers += 1

print(valid_combos)
print(valid_combos_len)
print(min_containers)
