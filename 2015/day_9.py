# https://adventofcode.com/2015/day/9

import numpy as np
import pandas as pd 
import copy

def read_file(filename):
    # Read file data from file
    with open(filename) as file:
        data = file.readlines()
    return data


filename = "day_9_input.txt"
data = read_file(filename)

def checkall(cities):
    for i in cities:
        if cities[i] == 0:
            return False
    return True

cities = []
for i in data:
    ds = i.split()
    if ds[0] not in cities:
        cities.append(ds[0])
    if ds[2] not in cities:
        cities.append(ds[2])

cities = sorted(cities)
grid = np.zeros((len(cities),len(cities)))

print(cities)
cities_map = {}
for num,city in enumerate(cities):
    cities_map[city] = 0

df = pd.DataFrame(grid, cities, cities)

for i in data:
    fromcity = i.split()[0] 
    tocity = i.split()[2]
    df[fromcity][tocity] = int(i.split()[4])
    df[tocity][fromcity] = int(i.split()[4])

print(df)
print(cities_map)

visited_all = checkall(cities_map)
#start with 
"""cities_map['Faerun'] = 1
print("Faerun -> ")
current_city = 'Faerun'"""
# AlphaCentauri  Arbre  Faerun  Norrath  Snowdin  Straylight  Tambi  Tristram
# 867       818         833 815         863 822                 909     842
city = "Tristram"
current_city = city
cities_map[city] = 1
distance_gone = 0 
while(not visited_all):
    current_closest_city = ""
    min_distance = 0
    for i in cities:
        if i != current_city and cities_map[i] == 0:
            if df[current_city][i] > min_distance :
                current_closest_city = i
                min_distance = df[current_city][i]

    #print(current_closest_city + " -> " + str(df[current_city][current_closest_city]))
    distance_gone += df[current_city][current_closest_city]
    cities_map[current_closest_city] = 1
    current_city = current_closest_city
    visited_all = checkall(cities_map)

print(city + str(distance_gone))



"""
current_city = 'AlphaCentauri'
current_closest_city = ""
min_distance = 999
for i in cities:
    if i != current_city and cities_map[i] == 0:
        if df[current_city][i] < min_distance :
            current_closest_city = i
            min_distance = df[current_city][i]
print(current_closest_city)
"""