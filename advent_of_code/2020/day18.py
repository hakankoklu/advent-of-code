from typing import Dict, List, Tuple
from collections import defaultdict


def take_input(filepath):
    with open(filepath, 'r') as f:
        lines = [line.strip() for line in f.readlines()]
        return lines


def puzzle1(filepath):
    eqs = take_input(filepath)
    result = 0
    for eq in eqs:
        eq_result = solve(eq)
        print(eq_result)
        result += eq_result
    return result


def puzzle2(filepath):
    eqs = take_input(filepath)
    result = 0
    for eq in eqs:
        eq_result = solve2(eq)
        print(eq_result)
        result += eq_result
    return result


def solve(eq):
    par_stack = []
    ptr1 = 0
    cur_result = None
    current_operation = None
    while ptr1 < len(eq):
        # print(cur_result)
        # print(current_operation)
        if eq[ptr1] not in ' ()+*':
            cur_number = int(eq[ptr1])
            if cur_result is None:
                cur_result = cur_number
            else:
                if current_operation == '+':
                    cur_result += cur_number
                else:
                    cur_result *= cur_number
        elif eq[ptr1] in '+*':
            current_operation = eq[ptr1]
        elif eq[ptr1] == '(':
            par_stack.append('(')
            ptr2 = ptr1 + 1
            while par_stack:
                if eq[ptr2] == '(':
                    par_stack.append(')')
                elif eq[ptr2] == ')':
                    par_stack.pop()
                ptr2 += 1
            cur_number = solve(eq[ptr1 + 1: ptr2])
            if cur_result is None:
                cur_result = cur_number
            else:
                if current_operation == '+':
                    cur_result += cur_number
                else:
                    cur_result *= cur_number
            ptr1 = ptr2
            continue
        ptr1 += 1
    return cur_result


def solve2(eq):
    par_stack = []
    ptr1 = 0
    current_operation = None
    eq_parsed = []
    while ptr1 < len(eq):
        # print(cur_result)
        # print(current_operation)
        # print(eq_parsed)
        if eq[ptr1] not in ' ()+*':
            cur_number = int(eq[ptr1])
            if not eq_parsed:
                eq_parsed.append(cur_number)
            else:
                if current_operation == '+':
                    eq_parsed[-1] += cur_number
                else:
                    eq_parsed.append(cur_number)
        elif eq[ptr1] in '+*':
            current_operation = eq[ptr1]
        elif eq[ptr1] == '(':
            par_stack.append('(')
            ptr2 = ptr1 + 1
            while par_stack:
                if eq[ptr2] == '(':
                    par_stack.append(')')
                elif eq[ptr2] == ')':
                    par_stack.pop()
                ptr2 += 1
            cur_number = solve2(eq[ptr1 + 1: ptr2])
            if not eq_parsed:
                eq_parsed.append(cur_number)
            else:
                if current_operation == '+':
                    eq_parsed[-1] += cur_number
                else:
                    eq_parsed.append(cur_number)
            ptr1 = ptr2
            continue
        ptr1 += 1
    result = 1
    for num in eq_parsed:
        result *= num
    # print(eq_parsed)
    return result


filepath = '/Users/hkoklu/personal/advent_of_code/2020/day18.txt'
# print(puzzle1(filepath))
print(puzzle2(filepath))

# print(solve2('1 + 2 * 3 + 4 * 5 + 6'))
# print(solve2('1 + (2 * 3) + (4 * (5 + 6))'))
