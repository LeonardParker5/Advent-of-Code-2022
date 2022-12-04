#######################
# Advent of Code 2022 #
# DAY 4               #
#######################

import re

##############
# PART 1 & 2 #
##############

file = open('Inputs/day4input.txt', 'r')

count, overlap_count = 0, 0
for line in file:
    nums = re.findall(r'\d+', line)
    elf1_list = [*range(int(nums[0]), int(nums[1])+1)]
    elf2_list = [*range(int(nums[2]), int(nums[3])+1)]
    if set(elf1_list).issubset(elf2_list) or set(elf2_list).issubset(elf1_list):
        count += 1
    if not set(elf1_list).isdisjoint(elf2_list):
        overlap_count += 1

print("Number of complete overlaps is " + str(count))
print("Number of partial overlaps is " + str(overlap_count))


# ###
# 5 LINER FOR FUN
# ###

file, count, overlap_count = open('Inputs/day4input.txt', 'r'), 0, 0
for line in file:
    if set([*range(int(re.findall(r'\d+', line)[0]), int(re.findall(r'\d+', line)[1])+1)]).issubset([*range(int(re.findall(r'\d+', line)[2]), int(re.findall(r'\d+', line)[3])+1)]) or set([*range(int(re.findall(r'\d+', line)[2]), int(re.findall(r'\d+', line)[3])+1)]).issubset([*range(int(re.findall(r'\d+', line)[0]), int(re.findall(r'\d+', line)[1])+1)]): count+=1
    if not set([*range(int(re.findall(r'\d+', line)[0]), int(re.findall(r'\d+', line)[1])+1)]).isdisjoint([*range(int(re.findall(r'\d+', line)[2]), int(re.findall(r'\d+', line)[3])+1)]): overlap_count+=1
print("Number of complete overlaps is " + str(count) + " and number of partial overlaps is " + str(overlap_count))