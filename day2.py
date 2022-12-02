#######################
# Advent of Code 2022 #
# DAY 2               #
#######################

import pandas as pd
import matplotlib.pyplot as plt

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

#############
# ~FOR FUN~ #
#############

file = open('Inputs/day2input.txt', 'r')
score1 = 0
score2 = 0
score_tracker1 = [0]
score_tracker2 = [0]
point_guide1 = {"A X": 4, "A Y": 8, "A Z": 3,
               "B X": 1, "B Y": 5, "B Z": 9,
               "C X": 7, "C Y": 2, "C Z": 6}
point_guide2 = {"A X": 3, "A Y": 4, "A Z": 8,
               "B X": 1, "B Y": 5, "B Z": 9,
               "C X": 2, "C Y": 6, "C Z": 7}

for line in file:
    score1 += point_guide1.get(line.strip())
    score2 += point_guide2.get(line.strip())
    score_tracker1.append(score1)
    score_tracker2.append(score2)

df = pd.DataFrame({"Part 1": score_tracker1, "Part 2": score_tracker2})
df.plot.line()
