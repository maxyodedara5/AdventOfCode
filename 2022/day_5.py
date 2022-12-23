# https://adventofcode.com/2022/day/5

def read_file(filename):
    # Read file data from file
    with open(filename) as file:
        data = file.readlines()
    return data


filename = "day_5_input.txt"
data = read_file(filename)

# Print get Grid
for i,num in enumerate(data):
    if len(num) == 1:
        stack_grid = i 
        break

# Number of stacks 
stack_data = data[stack_grid - 1]
stack_data = stack_data.split()
no_of_stacks = stack_data[-1]

stacks = stack_grid - 1
no_of_stacks = int(no_of_stacks)
# Creating stacks (lists) 
for i in range(no_of_stacks):
    exec(f"stack_{i} = list()")

# Parsing grid 
section_counts = len(data[0]) // stacks

for i in range(no_of_stacks):
    prev_pos = 0 
    for j in range(no_of_stacks):
        if (data[i][prev_pos: j * section_counts + section_counts].strip()) != "":
            to_insert = data[i][prev_pos: j * section_counts + section_counts].strip()
            to_insert = to_insert.replace("[","")
            to_insert = to_insert.replace("]","")
            exec(f"stack_{j}.append('{to_insert}')")
        prev_pos =  j * section_counts + section_counts

# Initialize grid / stacks
for i in range(0,no_of_stacks):
    exec(f"stack__{i + 1} = list(stack_{i})")
    exec(f"stack__{i + 1}.reverse()")


# Parsing instructions
# Part 1 
ins = []
for i in data[stack_grid + 1:]:
    ins_s = i.split(" ")
    relevant = [ ins_s[1], ins_s[3], ins_s[5].strip()]
    ins.append(relevant)

# Execute instructions
for i in ins:
    for ele in range(0,int(i[0])):
        exec(f"item_to_push = stack__{int(i[1])}.pop()")
        exec(f"stack__{int(i[2])}.append(item_to_push)")

print("Part 1 : Top of Crates letters : ", end="")
for i in range(0,no_of_stacks):
    exec(f"last_val = stack__{i+1}[-1]")
    print(last_val, end="")


# Part 2 
# Initialize grid / stacks
for i in range(0,no_of_stacks):
    exec(f"stack__{i + 1} = stack_{i}")
    exec(f"stack__{i + 1}.reverse()")

# Execute instructions
for i in ins:
    exec(f"crates = stack__{int(i[1])}[{-int(i[0])}:]")
    exec(f"stack__{int(i[1])} = stack__{int(i[1])}[0:{-int(i[0])}]")
    exec(f"stack__{int(i[2])}.extend(crates)")

print()
print("Part 2 : Top of Crates letters : ", end="")
for i in range(0,no_of_stacks):
    exec(f"last_val = stack__{i+1}[-1]")
    print(last_val, end="")

