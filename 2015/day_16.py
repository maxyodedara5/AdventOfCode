# https://adventofcode.com/2015/day/16


def read_file(filename):
    # Read file data from file
    with open(filename) as file:
        data = file.readlines()
    return data

filename = "day_16_input.txt"
data = read_file(filename)

sue_info = {}

for i in data:
    i_s = i.split(":")
    sue_name = i_s[0]
    split_pos = i.find(":")
    sue_value = i[split_pos + 1:]
    
    sue_values = sue_value.split(",")
    sue_things = {}
    for value in sue_values:
        name, qty = value.split(": ")
        sue_things[name.strip()] = int(qty)
    sue_info[i_s[0]] = sue_things

our_sue = {
"children": 3,
"cats": 7,
"samoyeds": 2,
"pomeranians": 3,
"akitas": 0,
"vizslas": 0,
"goldfish": 5,
"trees": 3,
"cars": 2,
"perfumes": 1
}

def can_this_be_our_sue(potential_sue):
    p_sue_things = set(potential_sue.keys())
    our_sue_things = set(our_sue.keys())
    common_things = p_sue_things.intersection(our_sue_things)
    #print(p_sue_things,our_sue_things)
    #print(common_things)
    for item in common_things:
        #print(item,potential_sue[item],our_sue[item])
        if item == "cats" or item == "trees":
            if potential_sue[item] < our_sue[item]:
                return False
        
        if item == "pomeranians" or item == "goldfish" :
            if potential_sue[item] > our_sue[item]:
                return False

        if item not in ["cats", "trees", "pomeranians", "goldfish"]:
            if potential_sue[item] != our_sue[item]:
                return False

    return True

for sue in sue_info:
    #print(sue)
    if (can_this_be_our_sue(sue_info[sue])):
        print(sue)


