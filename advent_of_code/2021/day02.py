import os
from enum import Enum
from typing import List, Tuple

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
    cmds = []
    with open(fp, 'r') as f:
        for a in f.readlines():
            inp = a.split(' ')
            cmds.append((Direction(inp[0]), int(inp[1])))
        return cmds


def solve_p1(fp):
    sb = Submarine()
    cmds = prep(fp)
    sb.navigate(cmds)
    return sb.depth * sb.distance


def solve_p2(fp):
    sb = Submarine2()
    cmds = prep(fp)
    sb.navigate(cmds)
    return sb.depth * sb.distance


class Direction(Enum):
    FORWARD = 'forward'
    UP = 'up'
    DOWN = 'down'


class Submarine:

    def __init__(self):
        self.depth = 0
        self.distance = 0

    def step(self, direction: Direction, amount: int) -> None:
        if direction == Direction.FORWARD:
            self.distance += amount
        elif direction == Direction.DOWN:
            self.depth += amount
        elif direction == Direction.UP:
            self.depth -= amount

    def navigate(self, cmds: List[Tuple[Direction, int]]) -> None:
        for cmd in cmds:
            self.step(cmd[0], cmd[1])


class Submarine2:

    def __init__(self):
        self.aim = 0
        self.depth = 0
        self.distance = 0

    def step(self, direction: Direction, amount: int) -> None:
        if direction == Direction.FORWARD:
            self.distance += amount
            self.depth += self.aim * amount
        elif direction == Direction.DOWN:
            self.aim += amount
        elif direction == Direction.UP:
            self.aim -= amount

    def navigate(self, cmds: List[Tuple[Direction, int]]) -> None:
        for cmd in cmds:
            self.step(cmd[0], cmd[1])


if __name__ == '__main__':
    solve()
