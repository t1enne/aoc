import time


file = open("./inputs/input9.sample.txt", "r").read().strip()

visited: list[tuple[int, int]] = [(0, 0)]  # starting point
head = [0, 0]
tail = [0, 0]
moves = {"L": (0, -1), "R": (0, 1), "U": (1, -1), "D": (1, 1)}


# def move(dir: str):
# if coords not in visited:
#     visited.append(coords)

for line in file.splitlines():
    direction, steps = line.split(" ")
    print(f"dir: {direction}, steps: {steps}")
    axis, sign = moves[direction]
    head[axis] += sign * int(steps)
    print(head)


print(len(visited))
