# https://adventofcode.com/2015/day/2

def read_file(filename):
    # Read file data from file
    with open(filename) as file:
        data = file.readlines()
    return data


filename = "day_2_input.txt"
data = read_file(filename)


total_wrapping = 0 
total_ribbon = 0 

for present in data:
    l, w, h = present.split("x")
    l = int(l)
    w = int(w)
    h = int(h)
    slack = max(l,w,h)
    dimensions = [l,w,h]
    dimensions.sort()
    slack = dimensions[0] * dimensions[1]

    total_wrapping += 2*l*w + 2*w*h + 2*h*l + slack

    #ribbon calculation
    ribbon = dimensions[0] * 2 + dimensions[1] * 2
    bow = dimensions[0] * dimensions[1] * dimensions[2]
    total_ribbon += ribbon + bow

print(total_wrapping)
print(total_ribbon)
