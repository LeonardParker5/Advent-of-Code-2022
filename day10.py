#######################
# Advent of Code 2022 # 
# DAY 10              # 
#######################

##########
# PART 1 #
##########

CYCLE_CHECKS = [20, 60, 100, 140, 180, 220]

def check_cycle(cycle, strength):
    if cycle in CYCLE_CHECKS:
        return cycle * strength
    else:
        return 0

file = open('Inputs/day10input.txt', 'r')

cycle = 0
strength = 1
strength_sum = 0

for line in file:
    command = line.split()
    if command[0] == "addx":
        cycle += 1
        strength_sum += check_cycle(cycle, strength)
        cycle += 1
        strength_sum += check_cycle(cycle, strength)
        strength += int(command[1])
    if command[0] == "noop":
        cycle += 1
        strength_sum += check_cycle(cycle, strength)

print("Sum of six signal strengths is " + str(strength_sum))