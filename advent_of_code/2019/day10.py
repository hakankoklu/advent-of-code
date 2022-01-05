from pprint import pprint
import math


def get_asts(filepath):
    with open(filepath, 'r') as f:
        lines = f.readlines()
        asteroids = []
        for y, line in enumerate(lines):
            for x, let in enumerate(line):
                if let == '#':
                    asteroids.append((x, y))
    return asteroids


def get_coordinate_diff(ast1, ast2):
    return (ast1[0] - ast2[0], ast1[1] - ast2[1])


def get_distance_sq(ast1, ast2):
    return (ast1[0] - ast2[0]) ** 2 + (ast1[1] - ast2[1]) ** 2


def get_all_ast_diffs(ast, asteroids):
    diffs = {}
    for asteroid in asteroids:
        diff = get_coordinate_diff(ast, asteroid)
        if diff != (0, 0):
            diffs[asteroid] = diff
    return diffs


def check_obstruction(diff1, diff2):
    return diff1[0] * diff2[1] == diff1[1] * diff2[0] and diff1[0] * diff2[0] >= 0 and diff1[1] * diff2[1] >= 0 and diff1 != diff2


def get_unobstructed(ast, asteroids):
    diffs = get_all_ast_diffs(ast, asteroids)
    obstructed = set()
    asts = list(diffs.keys())
    for i in range(len(asts)):
        for j in range(i + 1, len(asts)):
            if check_obstruction(diffs[asts[i]], diffs[asts[j]]):
                if get_distance_sq(ast, asts[i]) < get_distance_sq(ast, asts[j]):
                    obstructed.add(asts[j])
                else:
                    obstructed.add(asts[i])
    return set(diffs) - obstructed


def get_all_unobstructed(asteroids):
    result = {}
    for ast in asteroids:
        result[ast] = get_unobstructed(ast, asteroids)
    return result


def get_angle(ast1, ast2):
    x1 = ast1[0]
    y1 = ast1[1]
    x2 = ast2[0]
    y2 = ast2[1]
    angle = math.atan2(abs(x1 - x2), abs(y1 - y2))
    if x1 <= x2 and y1 > y2:
        return angle
    elif x1 < x2 and y1 <= y2:
        return math.pi - angle
    elif x1 >= x2 and y1 < y2:
        return math.pi + angle
    elif x1 > x2 and y1 >= y2:
        return 2 * math.pi - angle


filepath = '/Users/hkoklu/personal/advent_of_code_2019/day10.txt'
asts = get_asts(filepath)
# pprint(asts)
# diffs = get_all_ast_diffs((4, 2), asts)
# pprint(diffs)
# unobs = get_unobstructed((4, 2), asts)
# pprint(unobs)
all_unobs = get_all_unobstructed(asts)
# pprint(all_unobs)
maxx = 0
best = None
for ast, un in all_unobs.items():
    maxx = max(maxx, len(un))
    if maxx == len(un):
        best = ast
    # print(ast, len(un))
print(maxx, best)
# print(all_unobs[(26, 29)])
print(len(all_unobs[best]))
detected = all_unobs[best]
angles = [(ast, get_angle(best, ast)) for ast in detected]
pprint(angles)
new_angles = sorted(angles, key=lambda ast: ast[1])
for i in range(len(new_angles)):
    print(i, new_angles[i])
