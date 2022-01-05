from typing import Any, Dict, List, Tuple
from collections import defaultdict


def take_input(filepath):
    rules = {}
    messages = []
    with open(filepath, 'r') as f:
        lines = [line.strip() for line in f.readlines()]
        for line in lines:
            if not line:
                continue
            if ':' in line:
                rule_no, rule_text = line.split(': ')
                rule_no = int(rule_no)
                if '"' in rule_text:
                    rule_text = rule_text.strip('"')
                    rules[rule_no] = rule_text
                elif '|' not in rule_text:
                    rules[rule_no] = [int(x) for x in rule_text.split(' ')]
                else:
                    rule_text_split = rule_text.split(' | ')
                    rules[rule_no] = [
                        [int(x) for x in rt.split(' ')]
                        for rt in rule_text_split
                     ]
            else:
                messages.append(line)
    return rules, messages


def puzzle1(filepath):
    rules, messages = take_input(filepath)
    # print(check_rule(messages[0], rules[0], rules))
    print(simple_expand(0, rules))
    return rules, messages


def expand_rule(rule_list, rules):
    if check_reduction(rule_list, rules):
        return rule_list
    expanded = False
    while not expanded:
        result = []
        for rule in rule_list:
            result.extend(rules[rule])
        rule_list = result
        if check_reduction(rule_list, rules):
                return rule_list
        else:
            pass


def simple_expand(rule, rules):
    print(rules[rule])
    if type(rules[rule]) == str:
        return rules[rule]
    result = []
    for r in rules[rule]:
        if
        result.append(simple_expand(r, rules))
    return result


def check_branching(rule: List[Any]):
    for i in rule:
        if type(rule[i]) == list:
            return True
    return False


def check_reduction(reduced_rule, rules):
    for i in reduced_rule:
        if type(rules[i]) != str:
            return False
    return True


filepath = '/Users/hkoklu/personal/advent_of_code/2020/day19.txt'
# print(puzzle1(filepath))
puzzle1(filepath)
# print(puzzle2(filepath))
