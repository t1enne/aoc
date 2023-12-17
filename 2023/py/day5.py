import time
from typing import TypedDict
import re


class LineEntry(TypedDict):
    dest: int
    start: int
    r: int


def parse_line(line: str) -> LineEntry:
    vals = list(map(lambda num: int(num), re.findall("\\d+", line)))
    return {"dest": vals[0], "start": vals[1], "r": vals[2]}


def parse_blocks() -> list[list[LineEntry]]:
    blocks: list[list[LineEntry]] = list()
    current_idx = -1
    # parse input into blocks
    for line in input[2:]:
        if line.strip() == "":
            continue

        if line.endswith("map:"):
            blocks.append(list())
            current_idx += 1
            continue

        if current_idx > -1:
            blocks[current_idx].append(parse_line(line))
    for block in blocks:  # sort entries
        block.sort(key=lambda e: e["start"])
    return blocks


def parse_range(range):
    print(range)


def solve_part_one(input: list[str]):
    print("\nDay 5 - Part 1")
    seeds = list(map(lambda num: int(num), re.findall("\\d+", input[0])))
    blocks = parse_blocks()
    # map source vals thru blocks
    to_transform_list = seeds
    for block in blocks:
        new_trsf_list = []
        for src_val in to_transform_list:
            for entry in block:
                entry_end = entry["start"] + entry["r"]
                is_in_range = entry["start"] <= src_val and src_val <= entry_end
                if is_in_range:
                    diff = entry["dest"] - entry["start"]
                    new_trsf_list.append(src_val + diff)
                    break

                if entry == block[-1]:  # if last
                    new_trsf_list.append(src_val)

        to_transform_list = new_trsf_list
    # get the lowest location
    print(min(to_transform_list))


def solve_part_two(input):
    print("\nDay 5 - Part 2")
    u_seed_ranges: list[tuple[int, int]] = list()
    for pair in re.findall("\\d+\\s\\d+", input[0]):
        int_pair = list(map(lambda num: int(num), pair.split(" ")))[:2]
        u_seed_ranges.append(tuple(int_pair))
    seed_ranges = sorted(u_seed_ranges, key=lambda num: num[1])
    blocks = parse_blocks()
    source_ranges = seed_ranges
    print(source_ranges)
    for block in blocks:
        print(block)


input = open("../inputs/05-00.txt", "r").read().strip().splitlines()
solve_part_one(input)
solve_part_two(input)
