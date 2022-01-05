from typing import List, Tuple


def take_input(filepath):
    with open(filepath, 'r') as f:
        lines = f.readlines()
        return [list(line.strip()) for line in lines]


def puzzle1(filepath):
    terrain = take_input(filepath)
    return count_trees(terrain, 3, 1)


def puzzle2(filepath):
    terrain = take_input(filepath)
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    m = 1
    for slope in slopes:
        m *= count_trees(terrain, slope[0], slope[1])
    return m


def count_trees(terrain: List[List[str]], x: int, y: int) -> int:
    cur_x = 0
    cur_y = 0
    tree_count = 0
    while cur_y < len(terrain):
        if terrain[cur_y][cur_x] == '#':
            tree_count += 1
        #     terrain[cur_y][cur_x] = 'X'
        # else:
        #     terrain[cur_y][cur_x] = 'O'
        cur_y += y
        cur_x += x
        cur_x %= len(terrain[0])
    return tree_count


filepath = '/Users/hkoklu/personal/advent_of_code/2020/day03.txt'
print(puzzle1(filepath))
print(puzzle2(filepath))
