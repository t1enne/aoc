#!/usr/bin/python3

file = open("./inputs/input2.prod.txt", "r")
score = 0
plays = {"A": 1, "B": 2, "C": 3, "X": 1, "Y": 2, "Z": 3}

# for line in file.read().splitlines():
#     their_k, my_k = line.split(" ")
#     their = plays[their_k]
#     mine = plays[my_k]
#
#     score += mine
#     if mine == their:
#         score += 3
#     elif (mine - their) % 3 == 1:
#         score += 6

# PART 2

for line in file.read().splitlines():
    first, outcome = line.split(" ")
    their = plays[first]

    # score += mine
    if outcome == "X":  # lose
        score += their > 1 and their - 1 or 3
    elif outcome == "Y":  # draw
        score += their + 3
    elif outcome == "Z":  # win
        score += their < 3 and their + 1 or 1
        score += 6

print(score)
