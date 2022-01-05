from typing import List, Set


def take_input(filepath):
    with open(filepath, 'r') as f:
        lines = f.readlines()
        bags = {}
        contained_bags = {}
        for line in lines:
            line = line.strip()
            bag, contents = line.split(' bags contain ')
            if contents == 'no other bags.':
                bags['faded blue'] = []
                continue
            contents = contents.strip('.')
            contents = contents.split(', ')
            for content in contents:
                content = content.strip('s')
                bag_type = content[2:-4]
                bag_count = int(content[0])
                if bags.get(bag):
                    bags[bag].append((bag_type, bag_count))
                else:
                    bags[bag] = [(bag_type, bag_count)]
                if contained_bags.get(bag_type):
                    contained_bags[bag_type].add(bag)
                else:
                    contained_bags[bag_type] = {bag}
        # print(bags, contained_bags)
        return bags, contained_bags


def puzzle1(filepath):
    _, contained_bags = take_input(filepath)
    result = set()
    q = ['shiny gold']
    visited = set()
    while q:
        current = q.pop(0)
        if current in visited:
            continue
        if contained_bags.get(current):
            result.update(contained_bags[current])
            q.extend(contained_bags[current])
            visited.add(current)
    return len(result)


def puzzle2(filepath):
    bags, _ = take_input(filepath)
    return inside_bags('shiny gold', bags)


def inside_bags(bag_type, bags):
    contents = bags.get(bag_type)
    if contents:
        total = 1
        for content in contents:
            total += content[1] * inside_bags(content[0], bags)
        return total
    else:
        return 1


filepath = '/Users/hkoklu/personal/advent_of_code/2020/day07.txt'
print(puzzle1(filepath))
print(puzzle2(filepath))
