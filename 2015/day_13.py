# https://adventofcode.com/2015/day/13

import itertools as it

def read_file(filename):
    # Read file data from file
    with open(filename) as file:
        data = file.readlines()
    return data

filename = "day_13_input.txt"
data = read_file(filename)

seating = []

for i in data:
    ip_split = i.split()
    first_person = ip_split[0]
    next_person = ip_split[-1].replace(".","")
    seating_metrics = []
    seating_metrics.append(first_person)
    if "gain" in i:
        seating_metrics.append(int(ip_split[3]))
        seating_metrics.append(next_person)
    else:
        seating_metrics.append(-abs(int(ip_split[3])))
        seating_metrics.append(next_person)
    seating.append(seating_metrics)
        
happiness_chart = {}
for i in data:
    ip_split = i.split()
    first_person = ip_split[0]
    next_person = ip_split[-1].replace(".","")
    if "gain" in i:
        happiness_chart[first_person + next_person] = int(ip_split[3])
    else:
        happiness_chart[first_person + next_person] = -abs(int(ip_split[3]))



print(happiness_chart)
people_present = [] 
for i in seating:
    people_present.append(i[0])

people_present = sorted(list(set(people_present)))
print(people_present)

# Circular permutations
# Keep one person fixed and move others for different combinations
fixed_person = people_present[0]
people_present = people_present[1:]

all_combinations =  list(it.permutations(people_present,len(people_present)))
all_combinations = [list(x) for x in all_combinations]
for combination in all_combinations:
    combination.insert(0,fixed_person)

#print(all_combinations)

# calculate happyness change
all_happiness_chg = []

for combination in all_combinations:
    happyness_chng = 0 
    for i in range(1,len(combination)-1):
        leftperson = combination[i] + combination[i-1] 
        rightperson = combination[i] + combination[i+1]
        happyness_chng += happiness_chart[leftperson] 
        happyness_chng += happiness_chart[rightperson]
    #edge cases
    
    #person sitting on first 
    fperson = combination[0] + combination[-1]
    #left side
    happyness_chng += happiness_chart[fperson]
    #right side 
    fperson = combination[0] + combination[1]
    happyness_chng += happiness_chart[fperson]

    #person sitting on last
    #print(len(combination))

    lperson = combination[len(combination)-1] + combination[-2]
    happyness_chng += happiness_chart[lperson]
    lperson = combination[len(combination)-1] + combination[0]
    happyness_chng += happiness_chart[lperson]
    
    all_happiness_chg.append(happyness_chng)

#print("All happines " + str(all_happiness_chg))
print(max(all_happiness_chg))