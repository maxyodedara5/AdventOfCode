# https://adventofcode.com/2015/day/7

from functools import cache
from re import A
import numpy as np

def read_file(filename):
    # Read file data from file
    with open(filename) as file:
        data = file.readlines()
    return data


filename = "day_7_input.txt"
data = read_file(filename)

inslist = {}
value_ins = {}
size_ins = {}
def parseins(data):
    for instructions in data:
        ins_splits = instructions.strip().split(" ")
        inslist[ins_splits[-1]] = ins_splits
        value_ins[ins_splits[-1]] = -1
        size_ins[ins_splits[-1]] = len(ins_splits)

def opcalc(op1, op2, oper):
    if oper == 'AND':
        return op1 & op2 
    elif oper == 'OR':
        return op1 | op2 
    elif oper == 'LSHIFT':
        return op1 << op2 
    elif oper == 'RSHIFT':
        return op1 >> op2
    else:
        print("DOIEVERCOMEHERE")
    

@cache
def tofind(varname):
    if value_ins[varname] != -1 :
        return value_ins[varname]
    
    insplits = inslist[varname] 
    

    #print(varname + " > " + str(insplits))
    if len(insplits) == 5:
        # operation with 2 operands
        op1 = insplits[0]
        op2 = insplits[2]
        oper = insplits[1]
        
        if not op1.isnumeric():
            op1 = tofind(op1)
        
        if not op2.isnumeric():
            op2 = tofind(op2)

        op1 = str(op1)
        op2 = str(op2)
        if op1.isnumeric() and op2.isnumeric():
            #print(opcalc(int(op1), int(op2), oper))
            return opcalc(int(op1), int(op2), oper)


    if len(insplits) == 4:
        # single operand operations
        op1 = insplits[1]
        oper = insplits[0]
        
        if oper == 'NOT':
            if not op1.isnumeric():
                op1 = tofind(op1)

            value_ins[insplits[3]] = (int(op1) ^ 65535)
            return (int(op1) ^ 65535)
        else:
            print("NO ESCAPE")

    if len(insplits) == 3:
        # value assigns
        if not insplits[0].isnumeric():
            insplits[0] = tofind(insplits[0])
        
        #updating value in index
        value_ins[insplits[2]] = int(insplits[0])
        return int(insplits[0])

    print("DOIEVERCOME HERE ___________________")


parseins(data)


print(tofind("a"))


"""
### Other way around 
print(inslist)
#print(value_ins)
print(size_ins)



def parentsof(var):
    parents = []
    for value,ins in inslist.items():
        if var in ins:
            if value != var:
                parents.append(value)
    
    return parents


for ins,size in size_ins.items():
    if size == 3 :
        print(ins)

while (value_ins["a"] == -1):
    pass

print(parentsof("b"))
print(parentsof("c"))"""