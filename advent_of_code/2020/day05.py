from typing import Dict, Tuple

FRONT = 'F'
BACK = 'B'
RIGHT = 'R'
LEFT = 'L'


def take_input(filepath):
    with open(filepath, 'r') as f:
        lines = f.readlines()
        return [line.strip() for line in lines]


def puzzle1(filepath):
    boarding_passes = take_input(filepath)
    max_seat = 0
    for boarding_pass in boarding_passes:
        row, column = decode_boarding_pass(boarding_pass)
        cur_seat = row * 8 + column
        max_seat = max(max_seat, cur_seat)
    return max_seat


def puzzle2(filepath):
    boarding_passes = take_input(filepath)
    seat_ids = []
    for boarding_pass in boarding_passes:
        row, column = decode_boarding_pass(boarding_pass)
        cur_seat = row * 8 + column
        seat_ids.append(cur_seat)
    seat_ids.sort()
    for ind, seat in enumerate(seat_ids[:-1]):
        if seat + 1 != seat_ids[ind+1]:
            return seat + 1


def decode_boarding_pass(pass_code: str) -> Tuple[int, int]:
    row_code = pass_code[:7]
    column_code = pass_code[7:]
    row = binary_convert(row_code, FRONT, BACK)
    column = binary_convert(column_code, LEFT, RIGHT)
    return row, column


def binary_convert(text: str, zero: str, one: str) -> int:
    degree = 0
    digits = reversed(list(text))
    result = 0
    for d in digits:
        value = 0 if d == zero else 1
        result += value * (2 ** degree)
        degree += 1
    return result


row, column = decode_boarding_pass('BFFFBBFRRR')
print(row, column, row *8 + column)


filepath = '/Users/hkoklu/personal/advent_of_code/2020/day05.txt'
print(puzzle1(filepath))
print(puzzle2(filepath))
