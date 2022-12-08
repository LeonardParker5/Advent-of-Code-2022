#######################
# Advent of Code 2022 #
# DAY 8               #
#######################

##########
# PART 1 #
##########

file = open('Inputs/day8input.txt', 'r')
trees = []
count = 0

for line in file:
    trees.append([])
    for i in line:
        if i.isnumeric(): trees[count].append(int(i))
    count += 1

#print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in trees]))

visible = 0

for x in range(0, len(trees)):
    for y in range(0, len(trees[x])):
        current_height = trees[x][y]
        #
        # CHECK PATH TO THE LEFT
        #
        if y == 0:
            visible += 1
            continue
        else:
            path_exists = True
            for i in range(0, y):
                if trees[x][i] >= current_height:
                    path_exists = False
            if path_exists:
                visible += 1
                continue
        
        #
        # CHECK PATH TO THE RIGHT
        #
        if y+1 == len(trees[x]):
            visible += 1
            continue
        else:
            path_exists = True
            for i in range(y+1, len(trees[x])):
                if trees[x][i] >= current_height:
                    path_exists = False
            if path_exists:
                visible += 1
                continue
        
        #
        # CHECK PATH TO THE TOP
        #
        if x == 0:
            visible += 1
            continue
        else:
            path_exists = True
            for i in range(0, x):
                if trees[i][y] >= current_height:
                    path_exists = False
            if path_exists:
                visible += 1
                continue
        
        #
        # CHECK PATH TO THE BOTTOM
        #
        if x+1 == len(trees):
            visible += 1
            continue
        else:
            path_exists = True
            for i in range(x+1, len(trees)):
                if trees[i][y] >= current_height:
                    path_exists = False
            if path_exists:
                visible += 1
                continue

print("Number of visible trees is " + str(visible))

##########
# PART 2 #
##########
