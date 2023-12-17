import re

def add_one(dict:dict[int,int], id:int):
    if dict.get(id):
        dict[id] += 1
    else:
        dict[id] = 1

def solve_part_two(lines: list[str]):
    print("Day 4 - Part 2")
    matches_map: dict[int, int] = dict()
    for line in lines:
        colon_idx = line.find(':')
        card_id = int(line[5:colon_idx])
        # add the current card
        add_one(matches_map, card_id)
        game_ints = line[colon_idx+1:].split("|")
        winning_ints = re.findall("\\d+", game_ints[0])
        played_ints = re.findall("\\d+", game_ints[1])
        matches = 0
        for played in played_ints:
            if played in winning_ints:
                matches += 1
        for _ in range(matches_map[ card_id ]):
            for i in range(matches):
                add_one(matches_map, card_id+i+1)

    total = 0
    for  key in matches_map:
        total += matches_map[key]
    print(total)

def solve_part_one(lines: list[str]):
    print("Day 4 - Part 1")
    total = 0
    for line in lines:
        colon_idx = line.find(':')
        game_ints = line[colon_idx+1:].split("|")
        winning_ints = re.findall("\\d+", game_ints[0])
        played_ints = re.findall("\\d+", game_ints[1])
        card_points = 0
        for played in played_ints:
            if played in winning_ints:
                card_points *= 2
                if card_points == 0:
                    card_points = 1
        total += card_points
    print(total)

input = open('../inputs/04-01.txt', 'r').read().strip().splitlines()
solve_part_one(input)
solve_part_two(input)


