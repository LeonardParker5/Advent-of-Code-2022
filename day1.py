#######################
# Advent of Code 2022 #
# DAY 1               #
#######################

import pandas as pd

##########
# PART 1 #
##########

file = open('Inputs/day1input.txt', 'r')

biggest_elf = 0
current_elf = 0

for line in file:
    if(line == "\n"):
        if current_elf > biggest_elf:
            biggest_elf = current_elf
        current_elf = 0
        continue
    current_elf += int(line)

print("Most calories carried by an elf is " + str(biggest_elf))

##########
# PART 2 #
##########

file = open('Inputs/day1input.txt', 'r')

biggest_elves = [0, 0, 0]
current_elf = 0

for line in file:
    if(line == "\n"):
        biggest_elves.sort()
        if current_elf > biggest_elves[0]:
            biggest_elves[0] = current_elf
        current_elf = 0
        continue
    current_elf += int(line)

print("Calorie total carried by the top 3 elves is " + str(sum(biggest_elves)))

#############
# ~FOR FUN~ #
#############

file = open('Inputs/day1input.txt', 'r')

elves = []
current_elf = 0

for line in file:
    if(line == "\n"):
        elves.append(current_elf)
        current_elf = 0
        continue
    current_elf += int(line)

elves.sort()
df = pd.DataFrame(elves)
ax = df.plot.line()
ax.set_xlabel("# of Elves")
ax.set_ylabel("# of Calories")
