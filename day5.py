#######################
# Advent of Code 2022 #
# DAY 5               #
#######################

import re

##########
# PART 1 #
##########

file = open('Inputs/day5input.txt', 'r')

row1, row2, row3, row4, row5, row6, row7, row8, row9 = ([] for i in range(9))
STACKS = [row1, row2, row3, row4, row5, row6, row7, row8, row9]

for line in file:
    if line == "\n": break
    count = 0
    for i in line:
        if i.isalpha():
            STACKS[int(count/4)].insert(0,i)
        count += 1

for line in file:
    command = re.findall(r'\d+', line)
    for i in range(int(command[0])):
        STACKS[int(command[2]) - 1].append(STACKS[int(command[1]) - 1].pop())

top_crates = ""
for i in STACKS: top_crates += i[-1]
print("Top crate of each row is " + top_crates)
