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
        signals = [line.split(' | ')[0].split() for line in lines]
        displays = [line.split(' | ')[1].split() for line in lines]
        return signals, displays


def solve_p1(fp):
    signals, displays = prep(fp)
    target_digit_lengths = {2, 3, 4, 7}
    count = 0
    for display in displays:
        for digit in display:
            if len(digit) in target_digit_lengths:
                count += 1
    return count


def solve_p2(fp):
    signals, displays = prep(fp)
    return sum(get_display(signal, display) for signal, display in zip(signals, displays))


def get_display(signal, display):
    signal = [''.join(sorted(sign)) for sign in signal]
    display = [''.join(sorted(sign)) for sign in display]
    digit_segment_map = {i: None for i in range(10)}
    segment_digit_map = {}
    length_signal_map = {}
    for sign in signal:
        length_signal_map.setdefault(len(sign), [])
        length_signal_map[len(sign)].append(sign)
    # 1
    digit_segment_map[1] = length_signal_map[2].pop()
    segment_digit_map[digit_segment_map[1]] = 1
    # 4
    digit_segment_map[4] = length_signal_map[4].pop()
    segment_digit_map[digit_segment_map[4]] = 4
    # 7
    digit_segment_map[7] = length_signal_map[3].pop()
    segment_digit_map[digit_segment_map[7]] = 7
    # 8
    digit_segment_map[8] = length_signal_map[7].pop()
    segment_digit_map[digit_segment_map[8]] = 8
    # 3
    for segment in length_signal_map[5]:
        if contains(segment, digit_segment_map[1]):
            digit_segment_map[3] = segment
            segment_digit_map[digit_segment_map[3]] = 3
            length_signal_map[5].remove(segment)
    # 9
    for segment in length_signal_map[6]:
        if contains(segment, digit_segment_map[4]):
            digit_segment_map[9] = segment
            segment_digit_map[digit_segment_map[9]] = 9
            length_signal_map[6].remove(segment)
    # 0
    for segment in length_signal_map[6]:
        if contains(segment, digit_segment_map[1]):
            digit_segment_map[0] = segment
            segment_digit_map[digit_segment_map[0]] = 0
            length_signal_map[6].remove(segment)
    # 6
    digit_segment_map[6] = length_signal_map[6].pop()
    segment_digit_map[digit_segment_map[6]] = 6
    # 5
    for segment in length_signal_map[5]:
        if contains(digit_segment_map[6], segment):
            digit_segment_map[5] = segment
            segment_digit_map[digit_segment_map[5]] = 5
            length_signal_map[5].remove(segment)
    # 2
    digit_segment_map[2] = length_signal_map[5].pop()
    segment_digit_map[digit_segment_map[2]] = 2

    return int(''.join([str(segment_digit_map[d]) for d in display]))


def contains(str1, str2):
    return set(list(str2)).intersection(set(list(str1))) == set(list(str2))


if __name__ == '__main__':
    solve()
