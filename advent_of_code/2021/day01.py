import os
from typing import List


def prep(fp):
    with open(fp, 'r') as f:
        numbers = [int(a) for a in f.readlines()]
        return numbers


def solve_p1(fp):
    numbers = prep(fp)
    return count_increase(numbers)


def solve_p2(fp):
    numbers = prep(fp)
    return count_increase(sliding_window(numbers, 3))


def count_increase(numbers: List[int]) -> int:
    inc_count = 0
    for i in range(1, len(numbers)):
        if numbers[i] > numbers[i-1]:
            inc_count += 1
    return inc_count


def sliding_window(numbers: List[int], window: int) -> List[int]:
    result = []
    for i in range(len(numbers) - window + 1):
        result.append(sum(numbers[i:i + window]))
    return result


filepath_test = os.path.join(os.getcwd(), f'{__file__.split(".")[0]}_test.txt')
filepath = os.path.join(os.getcwd(), f'{__file__.split(".")[0]}.txt')
print(solve_p2(filepath))
