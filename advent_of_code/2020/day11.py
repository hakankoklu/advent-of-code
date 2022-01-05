from typing import Dict, Tuple


def take_input(filepath):
    with open(filepath, 'r') as f:
        lines = f.readlines()
        return [list(line.strip()) for line in lines]


def puzzle1(filepath):
    rows = take_input(filepath)
    print_map(rows)
    changed = True
    count = 0
    while changed:
        to_empty = []
        to_fill = []
        changed = False
        for i in range(len(rows)):
            for j in range(len(rows[0])):
                e, o = check_adjacents(rows, i, j)
                if rows[i][j] == 'L' and o == 0:
                    to_fill.append((i, j))
                    changed = True
                if rows[i][j] == '#' and o >= 4:
                    to_empty.append((i, j))
                    changed = True
        for i, j in to_fill:
            rows[i][j] = '#'
        for i, j in to_empty:
            rows[i][j] = 'L'
        print_map(rows)
    return count_occupied(rows)


def puzzle2(filepath):
    rows = take_input(filepath)
    print_map(rows)
    changed = True
    count = 0
    while changed:
        to_empty = []
        to_fill = []
        changed = False
        cache = {}
        for i in range(len(rows)):
            for j in range(len(rows[0])):
                occ_count = 0
                for direction in directions:
                    if check_occupied_as_seen(rows, i, j, direction, cache):
                        occ_count += 1
                if rows[i][j] == 'L' and occ_count == 0:
                    to_fill.append((i, j))
                    changed = True
                if rows[i][j] == '#' and occ_count >= 5:
                    to_empty.append((i, j))
                    changed = True
        for i, j in to_fill:
            rows[i][j] = '#'
        for i, j in to_empty:
            rows[i][j] = 'L'
        print_map(rows)
    return count_occupied(rows)


def count_occupied(rows):
    c = 0
    for row in rows:
        for seat in row:
            if seat == '#':
                c += 1
    return c


def print_map(rows):
    print('New map\n')
    for row in rows:
        print(''.join(row))
    print('\n')


def check_adjacents(rows, r: int, c: int):
    empty_count = 0
    occupied_count = 0
    # left
    if c > 0:
        if rows[r][c - 1] in ['L', '.']:
            empty_count += 1
        else:
            occupied_count += 1
    # left - up
    if c > 0 and r > 0:
        if rows[r - 1][c - 1] in ['L', '.']:
            empty_count += 1
        else:
            occupied_count += 1
    # up
    if r > 0:
        if rows[r - 1][c] in ['L', '.']:
            empty_count += 1
        else:
            occupied_count += 1
    # up - right
    if c < len(rows[0]) - 1 and r > 0:
        if rows[r - 1][c + 1] in ['L', '.']:
            empty_count += 1
        else:
            occupied_count += 1
    # right
    if c < len(rows[0]) - 1:
        if rows[r][c + 1] in ['L', '.']:
            empty_count += 1
        else:
            occupied_count += 1
    # bottom - right
    if c < len(rows[0]) - 1 and r < len(rows) - 1:
        if rows[r + 1][c + 1] in ['L', '.']:
            empty_count += 1
        else:
            occupied_count += 1
    # bottom
    if r < len(rows) - 1:
        if rows[r + 1][c] in ['L', '.']:
            empty_count += 1
        else:
            occupied_count += 1
    # bottom - left
    if c > 0 and r < len(rows) - 1:
        if rows[r + 1][c - 1] in ['L', '.']:
            empty_count += 1
        else:
            occupied_count += 1
    return empty_count, occupied_count


directions = [
    'left',
    'left-up',
    'up',
    'right-up',
    'right',
    'right-down',
    'down',
    'left-down',
]


def check_occupied_as_seen(
        rows, r: int, c: int, direction: str, cache: Dict[Tuple[int, int, str], bool]):
    if (r, c, direction) in cache:
        return cache[(r, c, direction)]
    if direction == 'left':
        if c == 0 or rows[r][c - 1] == 'L':
            return False
        if rows[r][c - 1] == '#':
            return True
        result = check_occupied_as_seen(rows, r, c - 1, direction, cache)
    if direction == 'left-up':
        if c == 0 or r == 0 or rows[r - 1][c - 1] == 'L':
            return False
        if rows[r - 1][c - 1] == '#':
            return True
        result = check_occupied_as_seen(rows, r - 1, c - 1, direction, cache)
    if direction == 'up':
        if r == 0 or rows[r - 1][c] == 'L':
            return False
        if rows[r - 1][c] == '#':
            return True
        result = check_occupied_as_seen(rows, r - 1, c, direction, cache)
    if direction == 'right-up':
        if c == len(rows[0]) - 1 or r == 0 or rows[r - 1][c + 1] == 'L':
            return False
        if rows[r - 1][c + 1] == '#':
            return True
        result = check_occupied_as_seen(rows, r - 1, c + 1, direction, cache)
    if direction == 'right':
        if c == len(rows[0]) - 1 or rows[r][c + 1] == 'L':
            return False
        if rows[r][c + 1] == '#':
            return True
        result = check_occupied_as_seen(rows, r, c + 1, direction, cache)
    if direction == 'right-down':
        if c == len(rows[0]) - 1 or r == len(rows) - 1 or rows[r + 1][c + 1] == 'L':
            return False
        if rows[r + 1][c + 1] == '#':
            return True
        result = check_occupied_as_seen(rows, r + 1, c + 1, direction, cache)
    if direction == 'down':
        if r == len(rows) - 1 or rows[r + 1][c] == 'L':
            return False
        if rows[r + 1][c] == '#':
            return True
        result = check_occupied_as_seen(rows, r + 1, c, direction, cache)
    if direction == 'left-down':
        if c == 0 or r == len(rows) - 1 or rows[r + 1][c - 1] == 'L':
            return False
        if rows[r + 1][c - 1] == '#':
            return True
        result = check_occupied_as_seen(rows, r + 1, c - 1, direction, cache)
    cache[(r, c, direction)] = result
    return result


filepath = '/Users/hkoklu/personal/advent_of_code/2020/day11.txt'
print(puzzle1(filepath))
print(puzzle2(filepath))
