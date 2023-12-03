#!/usr/bin/python3
import string


def get_index(letter):
    try:
        idx = string.ascii_lowercase.index(letter) + 1
    except ValueError:
        idx = string.ascii_uppercase.index(letter) + 27
    return idx


file = open("./inputs/input3.sample.txt", "r")

map = {}
priorities = 0

for line in file.read().splitlines():
    for i, l in enumerate(line):
        if i == 0:
            map = {}

        if i < len(line) / 2:
            map[l] = 1

        if l in map and i > len(line) / 2:
            idx = get_index(l)
            print(idx, l)
            priorities += idx


# PART 2
