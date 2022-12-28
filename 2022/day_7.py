# https://adventofcode.com/2022/day/7

def read_file(filename):
    # Read file data from file
    with open(filename) as file:
        data = file.readlines()
    return data


filename = "day_7_input.txt"
data = read_file(filename)
data = [i.strip() for i in data]



directories = {}

class FileObj:
    def __init__(self, name, parent_dir, children) -> None:
        self.name = name
        self.parent_dir = parent_dir
        self.children = children
        

# Recursive fx to find sizes 
def addition_of_sizes_within(children):
    total = 0
    for i in children:
        if i[-2:] == "_s":
            #exec(grand_child = i[4:] + "_s.children")
            exec(f"grand_child = {i}.children", globals())
            total += addition_of_sizes_within(grand_child)
        else:
            size_of_file, name_of_file = i.split(" ")
            size_of_file = int(size_of_file)
            total += size_of_file

    return total 
            


dirs_found_till_now = []
current_dir = "root"
prev_dir = "root"
num = 0 
while (num != len(data)):
    if "$" in data[num]:
        # Instruction

        if data[num][0:4] == "$ cd":
            # changing directory
            
            if data[num] == "$ cd ..":
                exec(f"above_lvl = {current_dir}_s.parent_dir")
                current_dir = above_lvl
                exec(f"above_lvl = {current_dir}_s.parent_dir")
                prev_dir = above_lvl
            
            if data[num] != "$ cd ..":
                prev_dir = current_dir
                current_dir = prev_dir + "_" + data[num][5:] 
                
            num += 1
        if data[num] == "$ ls":
            num += 1
            # Listing out all elements
            children_list = []
            while (num != len(data) and "$" not in data[num]):
                if ("dir" in data[num]):
                    dir_prefix, only_dir_name = data[num].split(" ")
                    children_list.append(current_dir + "_" + only_dir_name + "_s")
                else:
                    children_list.append(data[num])
                num += 1
            # Initialize structure of dir systems
            exec(f"{current_dir}_s = FileObj(current_dir,prev_dir,children_list)")
            # need to add all dirs in one structure to find final size 
            dirs_found_till_now.append(current_dir + "_s")
            
#print(dirs_found_till_now)


for i in dirs_found_till_now:
        childn = eval(f"{i}.children")
        total_of_dir = addition_of_sizes_within(childn)
        #print(f"{i} : {total_of_dir}")
        directories[i] = total_of_dir


final_total = 0

for i in directories:
    if directories[i] < 100000:
        final_total += directories[i]


# Part 1
print(final_total)

# Part 2 
total_size_of_filesystem = 70000000
atleast_available = 30000000
current_used_space = 40389918
unused_space = total_size_of_filesystem - current_used_space
directories = {k: v for k, v in sorted(directories.items(), key=lambda item: item[1])}
#directories = {k: v for k, v in sorted(directories.items(), key=lambda item: item[1], reverse=True)}

#print(directories)
for i in directories:
    
    if directories[i] + unused_space > atleast_available:
        print(i,directories[i])
        break


#day_two = min([x for x in list(directories.values()) if (70000000 - 40389918 + x) > 30000000])
#print(day_two)