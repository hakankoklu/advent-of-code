from typing import List, Tuple


def puzzle1(filepath):
    with open(filepath, 'r') as f:
        valid_passes = 0
        for line in f.readlines():
            interval, letter, password = line.split()
            interval = tuple([int(x) for x in interval.split('-')])
            letter = letter.strip(':')
            if is_password_valid1(interval, letter, password):
                valid_passes += 1
        return valid_passes


def puzzle2(filepath):
    with open(filepath, 'r') as f:
        valid_passes = 0
        for line in f.readlines():
            interval, letter, password = line.split()
            interval = tuple([int(x) for x in interval.split('-')])
            letter = letter.strip(':')
            if is_password_valid2(interval, letter, password):
                valid_passes += 1
        return valid_passes


def get_letter_freq(word: str, letter: str) -> int:
    count = 0
    for let in word:
        if let == letter:
            count += 1
    return count


def is_password_valid1(freq_interval: Tuple[int, int], letter: str, password: str) -> bool:
    letter_freq = get_letter_freq(password, letter)
    return freq_interval[0] <= letter_freq <= freq_interval[1]


def is_password_valid2(place_indices: Tuple[int, int], letter: str, password: str) -> bool:
    if (password[place_indices[0] - 1] == letter and password[place_indices[1] - 1] != letter) \
            or (password[place_indices[0] - 1] != letter and password[place_indices[1] - 1] == letter):
        return True
    return False


filepath = '/Users/hkoklu/personal/advent_of_code/2020/day02.txt'
print(puzzle1(filepath))
print(puzzle2(filepath))
