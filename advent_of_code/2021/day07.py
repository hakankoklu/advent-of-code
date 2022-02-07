import os
from enum import Enum
from typing import List, Tuple, Optional, Dict, Callable
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
        crabs = [int(x) for x in lines[0].split(',')]
        return crabs


def solve_p1(fp):
    crabs = prep(fp)
    return find_min(crabs, calculate_fuel)


def solve_p2(fp):
    crabs = prep(fp)
    return find_min(crabs, calculate_fuel2)


def calculate_fuel(coordinates: List[int], center: int) -> int:
    return sum(abs(center - coordinate) for coordinate in coordinates)


def calculate_fuel2(coordinates: List[int], center: int) -> int:
    return sum(abs(center - coordinate) * (abs(center - coordinate) + 1) / 2 for coordinate in coordinates)


def get_median(coordinates: List[int]) -> int:
    if len(coordinates) % 2 == 1:
        return coordinates[len(coordinates) // 2]
    else:
        return sum(coordinates[len(coordinates) // 2 - 1: len(coordinates) // 2 + 1]) // 2


def find_min(coordinates: List[int], cost_fnc: Callable) -> int:
    sc = sorted(coordinates)
    median = get_median(sc)
    print(median)
    fuel_at_median = cost_fnc(sc, median)
    new_fuel = fuel_at_median
    current_fuel = fuel_at_median
    down = median - 1
    while new_fuel <= current_fuel:
        new_fuel = cost_fnc(sc, down)
        if new_fuel < current_fuel:
            current_fuel = new_fuel
        down -= 1

    if current_fuel < fuel_at_median:
        print(f'Down: {down}')
        return current_fuel

    new_fuel = fuel_at_median
    current_fuel = fuel_at_median
    up = median + 1
    while new_fuel <= current_fuel:
        new_fuel = cost_fnc(sc, up)
        if new_fuel < current_fuel:
            current_fuel = new_fuel
        up += 1

    if current_fuel < fuel_at_median:
        print(f'Up: {up}')
        return current_fuel
    return fuel_at_median


if __name__ == '__main__':
    solve()
