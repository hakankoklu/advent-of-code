from typing import Dict, Tuple

def take_input(filepath):
    with open(filepath, 'r') as f:
        lines = f.readlines()
        my_time = int(lines[0])
        buses = lines[1].strip()
        buses = [int(x) for x in buses.split(',')
                 if x != 'x']
    return my_time, buses


def puzzle1(filepath):
    my_time, buses = take_input(filepath)
    earliest = 1000000000000
    earliest_wait = 0
    earliest_bus = 0
    for bus in buses:
        late = my_time % bus
        next_time = my_time + bus - late
        if next_time < earliest:
            earliest = next_time
            earliest_wait = bus - late
            earliest_bus = bus
    print(earliest, earliest_wait, earliest_bus)
    print(earliest_bus * earliest_wait)


def puzzle2(filepath):
    with open(filepath, 'r') as f:
        lines = f.readlines()
    buses = lines[1].strip()
    buses = [int(x) if x != 'x' else 0 for x in buses.split(',')]
    bus_minutes = {bus: ind for ind, bus in enumerate(buses)
                   if bus != 0}
    print(bus_minutes)
    for i in range(buses[0], 10000000000, buses[0]):
        found = True
        for bus, minute in bus_minutes.items():
            if (i + minute) % bus != 0:
                found = False
                break
        if found:
            print(i)


def puzzle3(filepath):
    with open(filepath, 'r') as f:
        lines = f.readlines()
    buses = lines[1].strip()
    buses = [int(x) if x != 'x' else 0 for x in buses.split(',')]
    bus_minutes = {bus: ind for ind, bus in enumerate(buses)
                   if bus != 0}
    bus_minutes[buses[0]] = buses[0]
    print(bus_minutes)
    buses_des = sorted([bus for bus, _ in bus_minutes.items()], reverse=True)
    print(buses_des)
    buses_des_tup = [(bus, bus - bus_minutes[bus] % bus) for bus in buses_des]
    print(buses_des_tup)
    while len(buses_des_tup) >= 2:
        first = buses_des_tup.pop(0)
        second = buses_des_tup.pop(0)
        new_rem = find_x(first[0], first[1], second[0], second[1])
        new_bus = first[0] * second[0]
        buses_des_tup.insert(0, (new_bus, new_rem))
    print(buses_des_tup)


def puzzle4(filepath):
    with open(filepath, 'r') as f:
        lines = f.readlines()
    buses = lines[1].strip()
    buses = [int(x) if x != 'x' else 0 for x in buses.split(',')]
    bus_minutes = {bus: ind for ind, bus in enumerate(buses)
                   if bus != 0}
    buses_only = list(bus_minutes.keys())
    print(bus_minutes)
    bus_minutes_other = {bus: bus - minute % bus for bus, minute in bus_minutes.items()}
    bus_minutes_other[buses[0]] = 0
    print(bus_minutes_other)
    prod = multiply_buses(bus_minutes)
    print(prod)
    pp = [prod // bus for bus, _ in bus_minutes.items()]
    print(pp)
    inverses = [pow(pp_bus, -1, bus) for bus, pp_bus in zip(buses_only, pp)]
    print(inverses)
    return sum([rem * pp_bus * inverse
                for rem, pp_bus, inverse in zip(bus_minutes_other.values(), pp, inverses)]) % prod


def find_x(num1, rem1, num2, rem2):
    for i in range(1000000):
        if (num1 * i + rem1) % num2 == rem2:
            return num1 * i + rem1


def multiply_buses(bus_minutes):
    res = 1
    for bus in bus_minutes:
        res *= bus
    return res


filepath = '/Users/hkoklu/personal/advent_of_code/2020/day13.txt'
# puzzle1(filepath)
# puzzle3(filepath)
print(puzzle4(filepath))
