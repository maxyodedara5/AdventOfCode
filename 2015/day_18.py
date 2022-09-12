import numpy as np

def read_file(filename):
    # Read file data from file
    with open(filename) as file:
        data = file.readlines()
    return data

filename = "day_18_input.txt"
data = read_file(filename)

two_dimen_array = []

for line in data:
    single_d_array = list(line.strip())
    two_dimen_array.append(single_d_array)

current_grid = np.array(two_dimen_array)
new_grid = np.full((len(two_dimen_array),len(two_dimen_array)),".")
#print(current_grid)

def find_neighbours(sizeofgrid, i, j):
    """
    00 01 02
    10 11 12
    20 21 22

    pos4 is our center
    0 1 2
    3 4 5
    6 7 8
    """
    indices = [
        [i-1,j-1],
        [i-1,j],
        [i-1,j+1],
        [i,j-1],
        [i,j+1],
        [i+1,j-1],
        [i+1,j],
        [i+1,j+1]]
    
    # Remove the egde neighbours
    final_indices = []
    for index in indices:
        a, b = index
        #print(a,b)
        if (a < sizeofgrid) and (a >= 0) and (b < sizeofgrid) and (b >= 0):
            #print("Valid")
            #print((a < sizeofgrid),(a >= 0),(b < sizeofgrid),(b >= 0))
            final_indices.append(index)
        else:
            pass
            #print("Invalid")
            #print((a < sizeofgrid),(a >= 0),(b < sizeofgrid),(b >= 0))

    return final_indices


sizeofgrid = len(single_d_array)
iterations_to_be_done = 100
print("Size of grid ",str(sizeofgrid))

for iteration in range(0,iterations_to_be_done):
    #print("Current grid now ",str(iteration))
    #print(iteration)

    # Part 2 corner lights on state
    current_grid[0][0] = "#"
    current_grid[0][sizeofgrid-1] = "#"
    current_grid[sizeofgrid-1][0] = "#"
    current_grid[sizeofgrid-1][sizeofgrid-1] = "#"

    for x_pos,i in enumerate(current_grid):
        for y_pos,j in enumerate(i):
            # Indexes in grid
            neighbours_indexes = find_neighbours(sizeofgrid, x_pos, y_pos)
            n_on_count = 0 
            
            for n_index in neighbours_indexes:
                if current_grid[n_index[0]][n_index[1]] == "#":
                    n_on_count += 1

            if current_grid[x_pos][y_pos] == ".":
                if n_on_count == 3:
                    new_grid[x_pos][y_pos] = "#"
            else:
                # "#" condition
                if n_on_count == 2 or n_on_count == 3:
                    new_grid[x_pos][y_pos] = "#"
                else:
                    new_grid[x_pos][y_pos] = "."

    # reiterate the new grid
    #print("New Grid", str(iteration))
    #print(new_grid)
    #print("Current Grid post assignment", str(iteration))
    current_grid = new_grid
    new_grid = np.full((len(two_dimen_array),len(two_dimen_array)),".")
    #print(current_grid)

# Number of on lights
print("Number of lights active post iterations")
current_grid[0][0] = "#"
current_grid[0][sizeofgrid-1] = "#"
current_grid[sizeofgrid-1][0] = "#"
current_grid[sizeofgrid-1][sizeofgrid-1] = "#"
print((current_grid == "#").sum())

