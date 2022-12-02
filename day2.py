#######################
# Advent of Code 2022 #
# DAY 2               #
#######################

##########
# PART 1 #
##########

#rock = 1, paper = 2, scissors = 3
#lose = 0, draw = 3, win = 6
file = open('Inputs/day2input.txt', 'r')
score = 0
point_guide = {"A X": 4, "A Y": 8, "A Z": 3,
               "B X": 1, "B Y": 5, "B Z": 9,
               "C X": 7, "C Y": 2, "C Z": 6}

for line in file:
    score += point_guide.get(line.strip())

print("Part 1 final score is " + str(score))

##########
# PART 2 #
##########

#X = lose, Y = draw, Z = win
file = open('Inputs/day2input.txt', 'r')
score = 0
point_guide = {"A X": 3, "A Y": 4, "A Z": 8,
               "B X": 1, "B Y": 5, "B Z": 9,
               "C X": 2, "C Y": 6, "C Z": 7}

for line in file:
    score += point_guide.get(line.strip())

print("Part 2 final score is " + str(score))