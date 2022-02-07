import os
from enum import Enum
from typing import List, Tuple, Optional
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
        coords_text = [line.split(' -> ') for line in lines]
        coords = [
            [
                (int(coor[0].split(',')[0]), int(coor[0].split(',')[1])),
                (int(coor[1].split(',')[0]), int(coor[1].split(',')[1])),
            ] for coor in coords_text
        ]
        return coords


def solve_p1(fp):
    coords = prep(fp)
    vents = [Vent(*[Point(*c) for c in coord]) for coord in coords]
    all_coverage = {}
    for vent in vents:
        for point in vent.coverage:
            if point in all_coverage:
                all_coverage[point] += 1
            else:
                all_coverage[point] = 1
    count = 0
    for point, num in all_coverage.items():
        count += int(num >= 2)
    return count


def solve_p2(fp):
    coords = prep(fp)
    vents = [Vent(*([Point(*c) for c in coord] + [True])) for coord in coords]
    all_coverage = {}
    for vent in vents:
        for point in vent.coverage:
            if point in all_coverage:
                all_coverage[point] += 1
            else:
                all_coverage[point] = 1
    count = 0
    for point, num in all_coverage.items():
        count += int(num >= 2)
    return count


@dataclass(eq=True, frozen=True)
class Point:
    x: int
    y: int


class Vent:

    def __init__(self, start: Point, end: Point, diag: bool = False) -> None:
        self.start = start
        self.end = end
        self.diag = diag
        self.coverage = []
        self.cover()

    def cover(self) -> None:
        unit_vector = self.unit_vector()
        if unit_vector:
            current = self.start
            self.cover_point(self.start)
            while current != self.end:
                current = Point(current.x + unit_vector.x, current.y + unit_vector.y)
                self.cover_point(current)

        # if self.start.y == self.end.y:
        #     incr = int((self.end[0] - self.start[0]) / abs(self.end[0] - self.start[0]))
        #     for i in range(self.start[0], self.end[0] + incr, incr):
        #         self.coverage.append((i, self.start[1]))
        # # vertical
        # elif self.start[0] == self.end[0]:
        #     incr = int((self.end[1] - self.start[1]) / abs(self.end[1] - self.start[1]))
        #     for i in range(self.start[1], self.end[1] + incr, incr):
        #         self.coverage.append((self.start[0], i))

    def cover_point(self, point: Point) -> None:
        self.coverage.append(point)

    def unit_vector(self) -> Optional[Point]:
        x_diff = self.end.x - self.start.x
        y_diff = self.end.y - self.start.y
        if self.start.y == self.end.y:
            return Point(int(x_diff / abs(x_diff)), 0)
        if self.start.x == self.end.x:
            return Point(0, int(y_diff / abs(y_diff)))
        if abs(x_diff) == abs(y_diff) and self.diag:
            return Point(int(x_diff / abs(x_diff)), int(y_diff / abs(y_diff)))
        return None


if __name__ == '__main__':
    solve()
