#!/usr/bin/python3
file = open("./inputs/input5.prod.txt", "r")

stacks: list[list[str]] = []


def parse_stacks(stack: str):
    lines = stack.splitlines()[:-1]
    lines.reverse()
    for line in lines:
        ci = 0
        idx = 0
        while ci < len(line):
            if len(stacks) == idx:
                stacks.append([])
            box = line[ci + 1]
            if box != " ":
                stacks[idx].append(box)
            ci += 4
            idx += 1


# PART 1
# def run_commands(cmds: str):
#     for cmd in cmds.splitlines():
#         split = cmd.split(" ")
#         amount = int(split[1])
#         fr = int(split[3]) - 1
#         to = int(split[5]) - 1
#
#         i = 0
#         while i < amount:
#             box = stacks[fr].pop()
#             stacks[to].append(box)
#             i += 1


# PART 2
def run_commands(cmds: str):
    for cmd in cmds.splitlines():
        split = cmd.split(" ")
        amount = int(split[1])
        fr = int(split[3]) - 1
        to = int(split[5]) - 1

        i = 0
        to_move = []
        while i < amount:
            to_move.append(stacks[fr].pop())
            i += 1

        to_move.reverse()
        stacks[to].extend(to_move)


split = file.read().split("\n\n")
result = ""
parse_stacks(split[0])
run_commands(split[1])
for i, _ in enumerate(stacks):
    result += "".join(stacks[i][-1:])

print(result)
