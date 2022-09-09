# https://adventofcode.com/2015/day/15


def read_file(filename):
    # Read file data from file
    with open(filename) as file:
        data = file.readlines()
    return data

filename = "day_14_input.txt"
data = read_file(filename)

combos = []

# Need to optimize this instead of bruteforcing
# Number of teaspoons 
for i in range(0,101):
    for j in range(0,101):
        for k in range(0,101):
            for l in range(0,101):
                if i + j + k + l == 100:
                    combos.append([i, j, k, l])

print(len(combos))

cookie_scores = []

ing = []
#add ing properties

"""Frosting: capacity 4, durability -2, flavor 0, texture 0, calories 5
Candy: capacity 0, durability 5, flavor -1, texture 0, calories 8
Butterscotch: capacity -1, durability 0, flavor 5, texture 0, calories 6
Sugar: capacity 0, durability 0, flavor -2, texture 2, calories 1"""
ing.append([4,-2,0,0,5])
ing.append([0,5,-1,0,8])
ing.append([-1,0,5,0,6])
ing.append([0,0,-2,2,1])

calorie_condition = 0 

for combo in combos:
    tsp1 = combo[0]
    tsp2 = combo[1]
    tsp3 = combo[2]
    tsp4 = combo[3]
    
    capacity_total = 0
    durability_total = 0
    flavor_total = 0
    texture_total = 0
    
    if ((tsp1 * ing[0][4]) + (tsp2 * ing[1][4]) + (tsp3 * ing[2][4]) + (tsp4 * ing[3][4])) < 501:
        calorie_condition += 1
    else:
        continue

    capacity_total = (tsp1 * ing[0][0]) +( tsp2 * ing[1][0]) + (tsp3 * ing[2][0]) + (tsp4 * ing[3][0])
    durability_total = (tsp1 * ing[0][1]) +( tsp2 * ing[1][1]) + (tsp3 * ing[2][1]) + (tsp4 * ing[3][1])
    flavor_total = (tsp1 * ing[0][2]) +( tsp2 * ing[1][2]) + (tsp3 * ing[2][2]) + (tsp4 * ing[3][2])
    texture_total = (tsp1 * ing[0][3]) +( tsp2 * ing[1][3]) + (tsp3 * ing[2][3]) + (tsp4 * ing[3][3])

    if (capacity_total < 0) or (durability_total < 0) or (flavor_total < 0) or (texture_total < 0):
        continue
    else:
        cookie_scores.append(capacity_total * durability_total * flavor_total * texture_total)


print(max(cookie_scores))
