# https://adventofcode.com/2015/day/14



def read_file(filename):
    # Read file data from file
    with open(filename) as file:
        data = file.readlines()
    return data

filename = "day_14_input.txt"
data = read_file(filename)

reindeer_chart = []
for i in data:
    i_split = i.split()
    name = i_split[0]
    speed = i_split[3]
    sprint_time = i_split[6]
    rest_time = i_split[-2]
    reindeer_data = [name, int(speed), int(sprint_time), int(rest_time)]
    reindeer_chart.append(reindeer_data)


seconds_passed = 2503
max_distance_all = []
for i in reindeer_chart:
    times_ran = int(seconds_passed / (i[2] + i[3]))
    #print(i[0],i[1],i[2],i[3],(i[2] + i[3]),times_ran)
    #print(times_ran)
    seconds_left = int(seconds_passed % (i[2] + i[3]))
    #print("Seconds left " + str(seconds_left))
    seconds_can_still_run = seconds_left - i[2]
    #print("Times ran " + str(times_ran))
    if seconds_can_still_run > 0 : 
        #print("Full sprint once more")
        times_ran += 1
        d_ran = times_ran * i[1] * i[2]
    else:
        #print("Partial sprint")
        seconds_can_still_run = seconds_left
        d_ran = times_ran * i[1] * i[2]
        addition_d = i[1] * seconds_can_still_run
        d_ran += addition_d

    #print(seconds_can_still_run)
    max_distance_all.append(d_ran)
    
print(max(max_distance_all))

## Bursts lead point calc 
# Part 2

"""
While for each second 
current_sec 

reindeer_status = running resting stamina 
reindeer_points = {} add all names 
check_who_in_lead add points to that every second 

"""

def check_who_in_lead(distances_traveled_so_far, reindeer_points):
    lead_distance = max(distances_traveled_so_far.values())
    for i in distances_traveled_so_far:
        if distances_traveled_so_far[i] == lead_distance:
            reindeer_points[i] += 1

distances_traveled_so_far = {}
reindeer_points = {}
reindeer_status = {}
for i in reindeer_chart:
    distances_traveled_so_far[i[0]] = 0
    reindeer_points[i[0]] = 0
    reindeer_status[i[0]] = {"status":"Ready" ,
                             "stamina": i[2], 
                             "speed": i[1], 
                             "resttime": i[3],
                             "rested": 0,
                             "left_stamina": i[2]}

current_second = 0
while (current_second != 2503 ):
    #distance logic
    for i in reindeer_status:
        if (reindeer_status[i]['status']) == 'Ready':
            distances_traveled_so_far[i] += (1 * reindeer_status[i]['speed'])
            reindeer_status[i]['left_stamina'] -= 1
            if reindeer_status[i]['left_stamina'] == 0:
                reindeer_status[i]['status'] = 'Resting'
        else:
            reindeer_status[i]['rested'] += 1
            if reindeer_status[i]['rested'] == reindeer_status[i]['resttime']:
                reindeer_status[i]['status'] = 'Ready'
                reindeer_status[i]['left_stamina'] = reindeer_status[i]['stamina']
                reindeer_status[i]['rested'] = 0


    #award points to reindeers 
    check_who_in_lead(distances_traveled_so_far,reindeer_points)
    current_second += 1 

#print(distances_traveled_so_far)
for i in reindeer_status:
    print(i,reindeer_status[i])
    print(distances_traveled_so_far[i], reindeer_points[i])