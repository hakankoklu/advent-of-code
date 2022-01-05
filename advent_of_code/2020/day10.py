from typing import List, Set


def take_input(filepath):
    with open(filepath, 'r') as f:
        lines = f.readlines()
        return [int(line) for line in lines]


def puzzle1(filepath):
    adapters = take_input(filepath)
    adapters_sorted = sorted(adapters)
    diffs = [0, 0, 0, 0]
    prev = 0
    for i in range(len(adapters)):
        diffs[adapters_sorted[i] - prev] += 1
        prev = adapters_sorted[i]
    diffs[3] += 1
    print(diffs)
    return diffs[1] * diffs[3]


def puzzle2(filepath):
    adapters = take_input(filepath)
    adapters.append(0)
    adapters = sorted(adapters)
    adap_set = set(adapters)
    return get_path_count(adapters[-1], adapters, adap_set)


cache = {}


def get_path_count(jolt: int, adapters: List[int], adap_set: Set[int]) -> int:
    if jolt not in adap_set:
        return 0
    if jolt == 0:
        return 1
    if cache.get(jolt):
        return cache[jolt]
    result = 0
    for j in range(jolt - 3, jolt):
        result += get_path_count(j, adapters, adap_set)
    cache[jolt] = result
    return result


filepath = '/Users/hkoklu/personal/advent_of_code/2020/day10.txt'
print(puzzle1(filepath))
print(puzzle2(filepath))
