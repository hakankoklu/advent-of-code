def day1_1(filepath):
    with open(filepath, 'r') as f:
        modules = [int(a) for a in f.readlines()]
        result = sum([counter_upper(x) for x in modules])
    return result


def day1_2(filepath):
    with open(filepath, 'r') as f:
        modules = [int(a) for a in f.readlines()]
        result = sum([get_module_fuel(x) for x in modules])
    return result


def counter_upper(x):
    return int(x/3) - 2


def get_module_fuel(weight):
    result = 0
    temp = counter_upper(weight)
    while temp > 0:
        result += temp
        temp = counter_upper(temp)
    return result


filepath = '/Users/hkoklu/personal/advent_of_code_2019/day1.txt'
print(day1_1(filepath))
print(day1_2(filepath))
