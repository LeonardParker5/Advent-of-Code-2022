#######################
# Advent of Code 2022 #
# DAY 3               #
#######################

##########
# PART 1 #
##########

file = open('Inputs/day3input.txt', 'r')

LETTERS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
LETTER_DICT = {}

count = 1
for i in LETTERS:
    LETTER_DICT.update({i:count})
    count += 1

prio_sum = 0
for line in file:
    for i in line[:int(len(line)/2)]:
        if i in line[int(len(line)/2):]:
            prio_sum += LETTER_DICT.get(i)
            break

print("Total priority sum is " + str(prio_sum))

##########
# PART 2 #
##########

file = open('Inputs/day3input.txt', 'r')

badge_sum = 0
for line in file:
    line2, line3 = next(file), next(file)
    for i in line:
        if i in line2 and i in line3:
            badge_sum += LETTER_DICT.get(i)
            break

print("Total badge sum is " + str(badge_sum))