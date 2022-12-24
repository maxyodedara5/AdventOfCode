# https://adventofcode.com/2022/day/6

def read_file(filename):
    # Read file data from file
    with open(filename) as file:
        data = file.readlines()
    return data


filename = "day_6_input.txt"
data = read_file(filename)
data = [i.strip() for i in data]

print(len(data[0]))


def is_packet_marker(snippet):
    snippet = set(snippet)
    if len(snippet) != 4:
        return False
    else:
        return True

def is_msg_marker(snippet):
    snippet = set(snippet)
    if len(snippet) != 14:
        return False
    else:
        return True

# Part 1 Solution
for i,num in enumerate(range(len(data[0]) - 3)):
    if (is_packet_marker(data[0][i:4+i])):
        print(num + 4, data[0][i:4+i])
        break

# Part 2 Solution
for i,num in enumerate(range(len(data[0]) - 13)):
    if (is_msg_marker(data[0][i:14+i])):
        print(num + 14, data[0][i:14+i])
        break