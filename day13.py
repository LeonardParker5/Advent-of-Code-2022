#######################
# Advent of Code 2022 # 
# DAY 13              # 
#######################

##########
# PART 1 #
##########

def compare_lists(left, right):
    match left, right:
        # both lists are lists
        case list(), list():
            for l, r in zip(left, right):
                if diff := compare_lists(l, r):
                    return diff
            return len(left) - len(right)
        # both are ints, return diff
        case int(), int():
            return left - right
        # int and list
        case int(), list():
            return compare_lists([left], right)
        # list and int
        case list(), int():
            return compare_lists(left, [right])

file = open('Inputs/day13input.txt', 'r')

lists = []
index = 1
index_sum = 0

for line in file:
    if(len(lists) == 2):
        #compare lists then clear
        if compare_lists(lists[0], lists[1]) < 0:
            #print("Pairs at index " + str(index) + " are in the right order")
            index_sum += index
        index += 1
        lists.clear()
        continue
    if (line != "\n"):
        lists.append(eval(line.strip()))

print("Sum of indices is " + str(index_sum))

##########
# PART 2 #
##########
