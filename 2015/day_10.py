# https://adventofcode.com/2015/day/10

input_str = "3113322113"
#nput_str = "0123456789"
new_str = []

"""for i in range(0,40):
    current_num  = 1 

    for c in range(0,len(input_str)-1):
        if input_str[c] == input_str[c+1]:
            current_num += 1
        else:
            new_str += current_num * input_str[c]
            current_num = 0
"""
for i in range(0,50):
    #print(input_str)
    current_num = 1
    for c in range(0,len(input_str)-1):
        #print(c," ",input_str[c], " ", input_str[c+1], "->" , new_str)
        if input_str[c] == input_str[c+1]:
            current_num += 1
        else:
            new_str.append(str(current_num))
            new_str.append(input_str[c])
            current_num = 1

    # Last scenario
    if input_str[-2] == input_str[-1]:
        #current_num += 1
        new_str.append(str(current_num))
        new_str.append(input_str[-1])
        
    else:
        new_str.append("1")
        new_str.append(input_str[-1])
    
    print(i,len(new_str))
    input_str = new_str 
    new_str = []


