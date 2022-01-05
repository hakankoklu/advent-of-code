from typing import List, Set


def take_input(filepath):
    with open(filepath, 'r') as f:
        lines = f.readlines()
        answers = []
        current_answers = []
        for line in lines:
            line = line.strip()
            if not line:
                answers.append(current_answers)
                current_answers = []
                continue
            current_answers.append(line)
        answers.append(current_answers)
        return answers


def puzzle1(filepath):
    answers = take_input(filepath)
    count = 0
    for answer in answers:
        count += len(get_group_answers1(answer))
    return count


def puzzle2(filepath):
    answers = take_input(filepath)
    count = 0
    for answer in answers:
        count += len(get_group_answers2(answer))
    return count


def get_group_answers1(answers: List[str]) -> Set[str]:
    result = set()
    for answer in answers:
        for let in answer:
            result.add(let)
    return result


def get_group_answers2(answers: List[str]) -> Set[str]:
    qs = 'qwertyuiopasdfghjklzxcvbnm'
    result = set()
    for q in qs:
        yes = True
        for answer in answers:
            if q not in answer:
                yes = False
                break
        if yes:
            result.add(q)
    return result


filepath = '/Users/hkoklu/personal/advent_of_code/2020/day06.txt'
print(puzzle1(filepath))
print(puzzle2(filepath))
