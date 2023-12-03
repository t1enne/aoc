#!/usr/bin/python3
from collections import defaultdict

file = open("./inputs/input7.prod.txt", "r").read().strip()
sizes = defaultdict(int)
path: list[str] = []


def visit(line: str, path: list[str]):
    goto = line.split()[2]
    if goto == "..":
        path.pop()
    else:
        path.append(goto)


for line in file.splitlines():
    if line.startswith("$ cd"):
        visit(line, path)
    elif line.startswith("$ ls") or line.startswith("dir"):
        continue
    else:
        size, file = line.split(" ")
        for i, dir in enumerate(path):
            p = tuple(path[: i + 1])
            sizes[p] += int(size)

# PART 1

part_1 = 0
for size in sizes.values():
    if size < 100000:
        part_1 += size

print(part_1)

# PART 2
total = 70000000
needed = 30000000
to_delete = needed - (total - sizes[tuple(["/"])])

part_2 = total
for size in sizes.values():
    if to_delete < size and size < part_2:
        part_2 = size

print(part_2)
