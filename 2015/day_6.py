# https://adventofcode.com/2015/day/6

import numpy as np

def read_file(filename):
    # Read file data from file
    with open(filename) as file:
        data = file.readlines()
    return data


filename = "day_6_input.txt"
data = read_file(filename)


grid = np.zeros((1000,1000))

def calcRect(i):
    i_s = i.split()
    co = []
    
    for letters in i_s:
        if "," in letters:
            co.append(letters)

    numbers = []
    for num in co:
        num1 , num2 = num.split(',')
        numbers.append(int(num1))
        numbers.append(int(num2))
    
    return numbers[0],numbers[1],numbers[2],numbers[3]

def parseins(data):
    for i in data:
        
        if "on" in i:
            str_len, str_height, length, height = calcRect(i)
            for h in range(str_height,height+1):
                for l in range(str_len,length+1):
                    grid[h,l] += 1

        if "off" in i:
            str_len, str_height, length, height = calcRect(i)
            for h in range(str_height,height+1):
                for l in range(str_len,length+1):
                    if grid[h,l] != 0 :
                        grid[h,l] -= 1

        if "toggle" in i:
            str_len, str_height, length, height = calcRect(i)
            for h in range(str_height,height+1):
                for l in range(str_len,length+1):
                    grid[h,l] += 2
        """print()
        printgrid(grid)
        print(np.count_nonzero(grid == 1))"""



def printgrid(grid):
    print(grid)


"""# 11 to 22
str_len = 2 
str_height = 2
length = 3
height = 3

str_len, str_height, length, height = calcRect(i)
for h in range(str_height,height+1):
    for l in range(str_len,length+1):
        grid[h,l] = 5"""


parseins(data)
print(np.sum(grid))
