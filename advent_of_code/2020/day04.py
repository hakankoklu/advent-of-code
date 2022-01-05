from typing import Dict


def hgt_validation(hgt: str) -> bool:
    return (hgt[-2:] == 'in' and 59 <= int(hgt[:-2]) <= 76) \
           or (hgt[-2:] == 'cm' and 150 <= int(hgt[:-2]) <= 193)


def hcl_validation(hcl:str) -> bool:
    if hcl[0] != '#':
        return False
    for ch in hcl[1:]:
        if ch not in '1234567890abcdef':
            return False
    return True


REQUIRED_FIELDS = {
    'byr': lambda x: 1920 <= int(x) <= 2002,
    'iyr': lambda x: 2010 <= int(x) <= 2020,
    'eyr': lambda x: 2020 <= int(x) <= 2030,
    'hgt': hgt_validation,
    'hcl': hcl_validation,
    'ecl': lambda x: x in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
    'pid': lambda x: len(x) == 9,
}


def take_input(filepath):
    with open(filepath, 'r') as f:
        lines = f.readlines()
        passports = []
        current_pass = {}
        for line in lines:
            line = line.strip()
            if not line:
                passports.append(current_pass)
                current_pass = {}
                continue
            for pair in line.split():
                key, val = pair.split(':')
                current_pass[key] = val
        passports.append(current_pass)
        return passports


def puzzle1(filepath):
    passports = take_input(filepath)
    valid_count = 0
    for passport in passports:
        if is_valid_passport1(passport):
            valid_count += 1
    return valid_count


def puzzle2(filepath):
    passports = take_input(filepath)
    valid_count = 0
    for passport in passports:
        if is_valid_passport2(passport):
            valid_count += 1
    return valid_count


def is_valid_passport1(passport: Dict[str, str]):
    for f in REQUIRED_FIELDS:
        if f not in passport:
            return False
    return True


def is_valid_passport2(passport: Dict[str, str]):
    for f, fun in REQUIRED_FIELDS.items():
        if f not in passport or not fun(passport[f]):
            return False
    return True


filepath = '/Users/hkoklu/personal/advent_of_code/2020/day04.txt'
print(puzzle1(filepath))
print(puzzle2(filepath))
