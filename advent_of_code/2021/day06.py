import os
from enum import Enum
from typing import List, Tuple, Optional, Dict
from pprint import pprint
from dataclasses import dataclass


import click


@click.command()
@click.option('--part', required=True, type=int)
@click.option('--test', is_flag=True)
def solve(part, test):
    solve_map = {1: solve_p1, 2: solve_p2}
    fnc = solve_map[part]
    file_root = f'{__file__.split(".")[0]}'
    real_path = os.path.join(os.getcwd(), f'{file_root}.txt')
    test_path = os.path.join(os.getcwd(), f'{file_root}_test.txt')
    if test:
        print(fnc(test_path))
    else:
        print(fnc(real_path))


def prep(fp):
    with open(fp, 'r') as f:
        lines = [line.strip() for line in f.readlines()]
        fishes = [int(x) for x in lines[0].split(',')]
        return fishes


def solve_p1(fp):
    fishes = prep(fp)
    fish_map = map_fish_count(fishes)
    print(f'0: {fish_map}')
    next_map = {0: 6, 1: 0, 2: 1, 3: 2, 4: 3, 5: 4, 6: 5, 7: 6, 8: 7}
    cycles = 256
    for cycle in range(cycles):
        new_map = {i: 0 for i in range(9)}
        for fish in range(8, -1, -1):
            new_map[next_map[fish]] += fish_map[fish]
            # print(new_map)
        new_map[8] = fish_map[0]
        fish_map = new_map
    print(f'{cycle + 1}: {fish_map}')
    return fish_count(fish_map)


def solve_p2(fp):
    coords = prep(fp)
    pass


def map_fish_count(fishes: List[int]) -> Dict[int, int]:
    result = {i: 0 for i in range(9)}
    for fish in fishes:
        result[fish] += 1
    return result


def fish_count(fish_map: Dict[int, int]) -> int:
    result = 0
    for _, count in fish_map.items():
        result += count
    return result


if __name__ == '__main__':
    solve()
