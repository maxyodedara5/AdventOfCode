# https://adventofcode.com/2015/day/12

import json

def read_file(filename):
    # Read file data from file
    with open(filename) as file:
        data = file.read()
        data = json.loads(data)
        print(type(data))
    return data


filename = "day_12_input.json"
data = read_file(filename)

int_sum = 0
def check_root(data):
    #print("came here")
    #print(type(data))
    if isinstance(data, list):
        for i in data:
            check_root(i)
    elif isinstance(data, dict):
        if "red" not in data.values():
            # Condition for part 2
            for i in data:
                check_root(data[i])
    elif isinstance(data, int):
        global int_sum 
        int_sum += data
    else:
        print(type(data))
        #print("Not handled")

check_root(data)
print(int_sum)
