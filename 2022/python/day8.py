from typing import Tuple


with open("./inputs/input8.prod.txt") as f:
    file = f.read().strip()


visible_count = 0
matrix = file.splitlines()
side_l = len(matrix)


def out_of_bounds(coords):
    y, x = coords
    if x == -1 or y == -1 or x == side_l or y == side_l:
        return True
    else:
        return False


# PART 1
# def look(start, deltas):
#     start_tree = int(matrix[start[0]][start[1]])
#     new_coords = (start[0] + deltas[0], start[1] + deltas[1])
#     vis = True
#     distance = new_coords[0] - start[0] + new_coords[1] - start[1]
#
#     while not out_of_bounds(new_coords):
#         next_tree = int(matrix[new_coords[0]][new_coords[1]])
#         if next_tree >= start_tree:
#             vis = False
#             break
#         new_coords = (new_coords[0] + deltas[0], new_coords[1] + deltas[1])
#
#     return vis, distance
#
#
# def is_visible(start: Tuple[int, int]):
#     top = look(start, (-1, 0))
#     if top:
#         return True
#     down = look(start, (1, 0))
#     if down:
#         return True
#     left = look(start, (0, -1))
#     if left:
#         return True
#     right = look(start, (0, 1))
#     return right
#
#
# for lidx, line in enumerate(matrix):
#     for cidx, char in enumerate(line):
#         if is_visible((lidx, cidx)):
#             visible_count += 1
# print(visible_count)

# PART 2

max_distance = 0


def look(start, deltas):
    start_tree = int(matrix[start[0]][start[1]])
    new_coords = (start[0] + deltas[0], start[1] + deltas[1])
    distance = 0

    while not out_of_bounds(new_coords):
        next_tree = int(matrix[new_coords[0]][new_coords[1]])
        if next_tree >= start_tree:
            distance += 1
            break
        new_coords = (new_coords[0] + deltas[0], new_coords[1] + deltas[1])
        distance += 1
    return distance


def is_visible(start: Tuple[int, int]):
    global max_distance
    top = look(start, (-1, 0))
    if top == 0:
        return 0
    down = look(start, (1, 0))
    if down == 0:
        return 0
    left = look(start, (0, -1))
    if left == 0:
        return 0
    right = look(start, (0, 1))
    if right == 0:
        return 0

    return top * down * left * right


for lidx, line in enumerate(matrix):
    for cidx, char in enumerate(line):
        distance = is_visible((lidx, cidx))
        if distance > max_distance:
            max_distance = distance
print(max_distance)
