from typing import Dict, List, Tuple
from collections import defaultdict


def take_input(filepath):
    fields = {}
    my_ticket = []
    tickets = []
    with open(filepath, 'r') as f:
        lines = f.readlines()
        read_mine = False
        read_others = False
        for line in lines:
            line = line.strip()
            if 'your ticket' in line:
                read_mine = True
            elif 'nearby tickets' in line:
                read_others = True
            elif read_mine:
                my_ticket = [int(x) for x in line.split(',')]
                read_mine = False
            elif read_others:
                tickets.append([int(x) for x in line.split(',')])
            elif 'or' in line:
                field, constraints = line.split(': ')
                constraints = constraints.split(' or ')
                constraints = [[int(y) for y in x.split('-')] for x in constraints]
                fields[field] = constraints
    return fields, tickets, my_ticket


def puzzle1(filepath):
    fields, tickets, my_ticket = take_input(filepath)
    invalids = []
    for ticket in tickets:
        invalid, value = check_ticket_invalid(ticket, fields)
        if invalid:
            invalids.append(value)
    return sum(invalids)


def puzzle2(filepath):
    fields, tickets, my_ticket = take_input(filepath)
    valid_tickets = []
    for ticket in tickets:
        invalid, value = check_ticket_invalid(ticket, fields)
        if not invalid:
            valid_tickets.append(ticket)
    tickets_trans = []
    for i in range(len(my_ticket)):
        tickets_trans.append([])
    for ticket in valid_tickets:
        for ind, value in enumerate(ticket):
            tickets_trans[ind].append(value)
    ticket_field_cand = defaultdict(set)
    for ind, field_values in enumerate(tickets_trans):
        ticket_field_cand[ind].update(check_fields(field_values, fields))
    field_ind_name = {}
    while len(field_ind_name) < len(my_ticket):
        for ind, cands in ticket_field_cand.items():
            if len(cands) == 1:
                field_name = cands.pop()
                field_ind_name[ind] = field_name
                for _, cands2 in ticket_field_cand.items():
                    cands2.remove(field_name) if field_name in cands2 else None
    result = 1
    for ind, ff in field_ind_name.items():
        if 'departure' in ff:
            result *= my_ticket[ind]
    return result


def check_fields(values: List[int], fields: Dict[str, List[List[int]]]) -> List[str]:
    result = []
    for field, field_limits in fields.items():
        state = True
        for value in values:
            if not check_value_field(value, field_limits):
                state = False
        if state:
            result.append(field)
    return result


def check_value_field(value, field_limits):
    for field_limit in field_limits:
        if field_limit[0] <= value <= field_limit[1]:
            return True
    return False


def check_ticket_invalid(ticket: List[int], fields: Dict[str, List[List[int]]]) -> Tuple[bool, int]:
    for value in ticket:
        valid = False
        for _, field_limits in fields.items():
            for field_limit in field_limits:
                if field_limit[0] <= value <= field_limit[1]:
                    valid = True
        if not valid:
            return True, value
    return False, 0


filepath = '/Users/hkoklu/personal/advent_of_code/2020/day16.txt'
print(puzzle1(filepath))
print(puzzle2(filepath))

