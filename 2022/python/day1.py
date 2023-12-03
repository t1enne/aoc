#!/usr/bin/python3


# file = open("./inputs/input1.prod.txt", "r")
# max_bag = 0
# bag = 0
# for line in file.read().splitlines():
#     if line == "":
#         max_bag = max(max_bag, bag)
#         bag = 0
#         continue
#
#     bag += int(line)
#
# print(max_bag)
# file.close()

# PART 2
file = open("./inputs/input1.prod.txt", "r")
bags: list[int] = list()
bag = 0

for line in file.read().splitlines():
    if line == "":
        bags.append(bag)
        bag = 0
        continue
    bag += int(line)

total = sum(sorted(bags)[-3:])
print(total)
