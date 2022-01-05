from typing import List, Tuple


def puzzle1(filepath):
    with open(filepath, 'r') as f:
        numbers = [int(a) for a in f.readlines()]
        num1, num2 = get_summing_two(numbers, 2020)
        return num1 * num2


def puzzle2(filepath):
    with open(filepath, 'r') as f:
        numbers = [int(a) for a in f.readlines()]
        num1, num2, num3 = get_summing_three(numbers, 2020)
        return num1 * num2 * num3


def get_summing_two(nums: List[int], target: int) -> Tuple[int, int]:
    nums_set = set(nums)
    for num in nums:
        if target - num in nums_set:
            return num, target - num
    return 0, 0


def get_summing_three(nums: List[int], target: int) -> Tuple[int, int, int]:
    for num in nums:
        num1, num2 = get_summing_two(nums, target - num)
        if num1 == 0 and num2 == 0:
            continue
        return num, num1, num2


filepath = '/Users/hkoklu/personal/advent_of_code/2020/day01.txt'
print(puzzle1(filepath))
print(puzzle2(filepath))
