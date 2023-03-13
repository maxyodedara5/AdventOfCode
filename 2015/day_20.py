from math import sqrt
from functools import cache


@cache
def find_divisors(num):
    limit = int(sqrt(num)) + 1 
    divisors = set()
    for i in range(1,limit):
        if num % i == 0:
            divisors.add(i)
            divisors.add(num // i)

    return sum(divisors)

limit = 3400000
current_sum = 1 
num = 100000
while find_divisors(num) <= limit:
    #print(f"{num} : {find_divisors(num)}")
    num += 1
print(f"{num} : {find_divisors(num)}")
# Part 2 

@cache
def new_find_divisors(num):
    limit = int(sqrt(num)) + 1 
    divisors = set()
    for i in range(1,limit):
        if num % i == 0:
            if i * 50 >= num:
                divisors.add(i)
            if (num // i) * 50 >= num:
                divisors.add(num // i)

    return sum(divisors) * 11

limit = 34000000
num = 500000

while new_find_divisors(num) <= limit:
    #print(f"{num} : {new_find_divisors(num)}")
    num += 1
print(f"{num} : {new_find_divisors(num)}")