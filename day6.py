#######################
# Advent of Code 2022 #
# DAY 6               #
#######################

##############
# PART 1 & 2 #
##############

file = open('Inputs/day6input.txt', 'r')

#BUFFER_SIZE = 4  # PART 1
BUFFER_SIZE = 14 # PART 2
count = 0
buffer = []

for line in file:
    for i in line:
        if len(buffer) != BUFFER_SIZE:
            buffer.append(i)
            count += 1
        else:
            buffer.pop(0)
            buffer.append(i)
            count += 1
            if len(buffer) == len(set(buffer)): break

print("First marker after character " + str(count))