# https://adventofcode.com/2022/day/2

def read_file(filename):
    # Read file data from file
    with open(filename) as file:
        data = file.readlines()
    return data


filename = "day_2_input.txt"
data = read_file(filename)

data = [i.strip() for i in data]
print(len(data))
print(data[0])


score = 0
for i in data:
    opponent_selected, self_selected = i.split()
    outcome = "W/L/D"

    if self_selected == "X":
        self_selected = "A"
    elif self_selected == "Y":
        self_selected = "B"
    elif self_selected == "Z":
        self_selected = "C"

    if opponent_selected == self_selected:
        outcome = "D"
    elif opponent_selected == "A" and self_selected == "B":
        outcome = "W"
    elif opponent_selected == "B" and self_selected == "C":
        outcome = "W"
    elif opponent_selected == "C" and self_selected == "A":
        outcome = "W"
    else:
        outcome = "L"

    if outcome == "W":
        score += 6
    elif outcome == "L":
        score += 0
    elif outcome == "D":
        score += 3

    if self_selected == "A":
        score += 1
    elif self_selected == "B":
        score += 2
    elif self_selected == "C":
        score += 3


# Solution 1 
print(score)
score = 0
for i in data:
    opponent_selected, to_do = i.split()

    if to_do == "X":
        to_do = "L"
    elif to_do == "Y":
        to_do = "D"
    elif to_do == "Z":
        to_do = "W"

    if to_do == "W":
        if opponent_selected == "A":
            to_select = "B"
        elif opponent_selected == "B":
            to_select = "C"
        elif opponent_selected == "C":
            to_select = "A"

    if to_do == "D":
        to_select = opponent_selected


    if to_do == "L":
        if opponent_selected == "A":
            to_select = "C"
        elif opponent_selected == "B":
            to_select = "A"
        elif opponent_selected == "C":
            to_select = "B"

    
    if to_do == "W":
        score += 6
    elif to_do == "L":
        score += 0
    elif to_do == "D":
        score += 3

    if to_select == "A":
        score += 1
    elif to_select == "B":
        score += 2
    elif to_select == "C":
        score += 3

# Solution 2 
print(score)