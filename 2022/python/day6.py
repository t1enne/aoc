#!/usr/bin/python3
file = open("./inputs/input6.prod.txt", "r")

buffer = file.read().strip()
marker = 0
min_chars = 14  # 4 for part 1

unique_chars = ""
i = 0
while i < len(buffer):
    char = buffer[i]
    if char in unique_chars:
        idx = unique_chars.find(char) + 1
        unique_chars = unique_chars[idx:]

    unique_chars += char

    if len(unique_chars) == min_chars:
        marker = i + 1
        break
    i += 1

print(marker)
