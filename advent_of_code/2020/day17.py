from typing import Dict, List, Tuple
from collections import defaultdict

CYCLES = 6


def take_input(filepath):
    with open(filepath, 'r') as f:
        lines = [line.strip() for line in f.readlines()]
        return [list(line) for line in lines]


def puzzle1(filepath):
    start_area = take_input(filepath)
    mid_slice = get_empty_slice(len(start_area) + 2 * CYCLES, len(start_area[0]) + 2 * CYCLES)
    for i in range(len(start_area)):
        for j in range(len(start_area[0])):
            mid_slice[CYCLES + i][CYCLES + j] = start_area[i][j]
    # print_slice(mid_slice)
    full_pocket = [mid_slice]
    for i in range(CYCLES):
        full_pocket.insert(0, get_empty_slice(len(mid_slice), len(mid_slice[0])))
        full_pocket.append(get_empty_slice(len(mid_slice), len(mid_slice[0])))
    for i in range(CYCLES):
        print(f'cycle {i}')
        run_cycle(full_pocket)

    return sum_pocket(full_pocket)


def puzzle2(filepath):
    start_area = take_input(filepath)
    mid_cube = get_empty_cube(2 * CYCLES + 1, len(start_area) + 2 * CYCLES, len(start_area[0]) + 2 * CYCLES)
    for i in range(len(start_area)):
        for j in range(len(start_area[0])):
            mid_cube[CYCLES][CYCLES + i][CYCLES + j] = start_area[i][j]
    # print_slice(mid_slice)
    full_pocket = [mid_cube]
    for i in range(CYCLES):
        full_pocket.insert(0, get_empty_cube(len(mid_cube), len(mid_cube[0]), len(mid_cube[0][0])))
        full_pocket.append(get_empty_cube(len(mid_cube), len(mid_cube[0]), len(mid_cube[0][0])))
    for i in range(CYCLES):
        print(f'cycle {i}')
        run_cycle_4d(full_pocket)

    return sum_pocket_4d(full_pocket)


def run_cycle(pocket):
    # print(sum_pocket(pocket))
    print_slice(pocket[6])
    to_activate = []
    to_deactivate = []
    for i in range(len(pocket)):
        for j in range(len(pocket[0])):
            for k in range(len(pocket[0][0])):
                act_count = count_active_neighbors(i, j, k, pocket)
                current = pocket[i][j][k]
                if current == '#' and act_count not in [2, 3]:
                    to_deactivate.append((i, j, k))
                if current == '.' and act_count == 3:
                    to_activate.append((i, j, k))
    for i, j, k in to_deactivate:
        pocket[i][j][k] = '.'
    for i, j, k in to_activate:
        pocket[i][j][k] = '#'


def run_cycle_4d(pocket):
    to_activate = []
    to_deactivate = []
    for i in range(len(pocket)):
        for j in range(len(pocket[0])):
            for k in range(len(pocket[0][0])):
                for l in range(len(pocket[0][0][0])):
                    act_count = count_active_neighbors_4d(i, j, k, l, pocket)
                    current = pocket[i][j][k][l]
                    if current == '#' and act_count not in [2, 3]:
                        to_deactivate.append((i, j, k, l))
                    if current == '.' and act_count == 3:
                        to_activate.append((i, j, k, l))
    for i, j, k, l in to_deactivate:
        pocket[i][j][k][l] = '.'
    for i, j, k, l in to_activate:
        pocket[i][j][k][l] = '#'


def count_active_neighbors(i, j, k, pocket):
    act_count = 0
    for x in range(-1, 2):
        for y in range(-1, 2):
            for z in range(-1, 2):
                if x != 0 or y != 0 or z != 0:
                    try:
                        if i + x >= 0 and j + y >= 0 and k + z >= 0:
                            neighbor = pocket[i + x][j + y][k + z]
                            if neighbor == '#':
                                act_count += 1
                    except:
                        pass
    return act_count


def count_active_neighbors_4d(i, j, k, l, pocket):
    act_count = 0
    for x in range(-1, 2):
        for y in range(-1, 2):
            for z in range(-1, 2):
                for w in range(-1, 2):
                    if x != 0 or y != 0 or z != 0 or w != 0:
                        try:
                            if i + x >= 0 and j + y >= 0 and k + z >= 0 and l + w >= 0:
                                neighbor = pocket[i + x][j + y][k + z][l + w]
                                if neighbor == '#':
                                    act_count += 1
                        except:
                            pass
    return act_count


def sum_pocket(pocket: List[List[List[int]]]) -> int:
    res = 0
    for i in pocket:
        for j in i:
            for k in j:
                if k == '#':
                    res += 1
    return res


def sum_pocket_4d(pocket: List[List[List[List[int]]]]) -> int:
    res = 0
    for i in pocket:
        for j in i:
            for k in j:
                for l in k:
                    if l == '#':
                        res += 1
    return res


def get_empty_slice(row_c, col_c):
    result = []
    for _ in range(row_c):
        r = []
        for _ in range(col_c):
            r.append('.')
        result.append(r)
    return result


def get_empty_cube(slice_c, row_c, col_c):
    result = []
    for _ in range(slice_c):
        s = []
        for _ in range(row_c):
            r = []
            for _ in range(col_c):
                r.append('.')
            s.append(r)
        result.append(s)
    return result


def print_slice(sl):
    for row in sl:
        print(''.join(row))



filepath = '/Users/hkoklu/personal/advent_of_code/2020/day17.txt'
print(puzzle1(filepath))
print(puzzle2(filepath))
