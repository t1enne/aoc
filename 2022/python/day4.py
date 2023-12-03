#!/usr/bin/python3
file = open("./inputs/input4.prod.txt", "r")


# contained = 0
#
# for line in file.read().splitlines():
#     pair = line.split(",")
#     first = {
#         "s": int(pair[0].split("-")[0]),
#         "e": int(pair[0].split("-")[1]),
#     }
#     second = {
#         "s": int(pair[1].split("-")[0]),
#         "e": int(pair[1].split("-")[1]),
#     }
#     if first["s"] <= second["s"] and second["e"] <= first["e"]:
#         contained += 1
#     elif second["s"] <= first["s"] and first["e"] <= second["e"]:
#         contained += 1
#
# print(contained)

# PART 2

overlap = 0

for line in file.read().splitlines():
    pair = line.split(",")
    first = {
        "s": int(pair[0].split("-")[0]),
        "e": int(pair[0].split("-")[1]),
    }
    second = {
        "s": int(pair[1].split("-")[0]),
        "e": int(pair[1].split("-")[1]),
    }

    if max(first["s"], second["s"]) <= min(second["e"], first["e"]):
        overlap += 1

print(overlap)
