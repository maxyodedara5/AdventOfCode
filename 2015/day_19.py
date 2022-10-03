# https://adventofcode.com/2015/day/19
import sys
from functools import cache
import random

def read_file(filename):
    # Read file data from file
    with open(filename) as file:
        data = file.readlines()
    return data

filename = "day_19_input.txt"
data = read_file(filename)

replacements = []

for i in range(len(data)-2):
    data_split = data[i].split()
    term = data_split[0]
    replacement = data_split[2]
    replacements.append([term, replacement])

repl_str = data[-1]

@cache
def find_occurences(term, repl_str):
    len_term = len(term)
    len_final_str = len(repl_str)
    no_of_times = repl_str.count(term)
    indexes = []
    start_pos = 0
    for i in range(no_of_times):
        index = 0
        index = repl_str.find(term,start_pos,len(repl_str))
        indexes.append(index)
        start_pos = len_term + index

    return indexes

def create_combos(term_to_repl, term_to_repl_with, repl_str, indexes, diff_combos):
    """
    replace CD with XYZ

    prev term = 0: index
    after term = index + termoflen : -1

    new term = prev term + XYZ + after term
    0 1 2 3 4 5 6 7 8
    A B C D E F G H I
    """
    term_len = len(term_to_repl)
    term_to_repl_with_len = len(term_to_repl_with)
    for index in indexes:
        prev_part = repl_str[0:index]
        after_part = repl_str[index + term_len :]
        combo = prev_part + term_to_repl_with + after_part
        if combo in diff_combos:
            diff_combos[combo] += 1
        else:
            diff_combos[combo] = 1

# Part 1 
diff_combos = {}
def part1(diff_combos):
    for i in replacements:
        if i[0] in repl_str:
            indexes = find_occurences(i[0],repl_str)
            create_combos(i[0], i[1], repl_str, indexes, diff_combos)
            # create new combos

    return diff_combos

# To find Part 1 
# print(len(diff_combos))

# Part 2 
#print(replacements)
#print(repl_str)
# Tried different approaches but last solution was thorwing things at wall 
# and seeing which stick
# Apparently randomized input sticks here 
# A better approach would be to find the pattern in input or do greedy algo 


found = False
count = 0
random.shuffle(replacements)
while( found != True):
    
    for i in replacements:
        random.shuffle(replacements)
        if i[1] in repl_str:
            #print(f"{i[1]} found {repl_str.count(i[1])} times")
            print(f"{i[0]} will replace {i[1]} at {repl_str.find(i[1])} curLen {len(repl_str)}")
            index = repl_str.find(i[1])
            prev_part = repl_str[0:index]
            after_part = repl_str[index + len(i[1]) :]
            repl_str = prev_part + i[0] + after_part
            count += 1
            if i[0] == "e":
                print(count)
                break
        else:
            random.shuffle(replacements)

            
            
