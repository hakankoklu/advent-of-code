import os
from enum import Enum
from typing import List, Tuple, Optional
from pprint import pprint

import click


@click.command()
@click.option('--part', required=True, type=int)
@click.option('--test', is_flag=True)
def solve(part, test):
    solve_map = {1: solve_p1, 2: solve_p2}
    fnc = solve_map[part]
    file_root = f'{__file__.split(".")[0]}'
    real_path = os.path.join(os.getcwd(), f'{file_root}.txt')
    test_path = os.path.join(os.getcwd(), f'{file_root}_test.txt')
    if test:
        print(fnc(test_path))
    else:
        print(fnc(real_path))


def prep(fp):
    with open(fp, 'r') as f:
        lines = [line.strip() for line in f.readlines()]
        numbers = [int(i) for i in lines[0].split(',')]
        card_count = int((len(lines) - 1) / 6)
        cards = []
        for i in range(card_count):
            card = []
            for line in lines[i * 6 + 2:i * 6 + 7]:
                card.append([int(num) for num in line.split()])
            cards.append(card)
        return numbers, cards


def solve_p1(fp):
    numbers, cards = prep(fp)
    bingo_cards = [BingoCard(card) for card in cards]
    bingo = Bingo(bingo_cards)
    winner, last = bingo.run(numbers)
    return winner.sum_unmarked() * last


def solve_p2(fp):
    numbers, cards = prep(fp)
    bingo_cards = [BingoCard(card) for card in cards]
    bingo = Bingo(bingo_cards)
    loser, last = bingo.run_full(numbers)
    return loser.sum_unmarked() * last


class BingoCard:

    def __init__(self, lines: List[List[int]]) -> None:
        self.lines = lines
        self.width = len(lines[0])
        self.length = len(lines)
        self.number_indices = {}
        self.index_numbers()

    def index_numbers(self):
        for i in range(self.length):
            for j in range(self.width):
                self.number_indices[self.lines[i][j]] = (i, j)

    def cross_number(self, number: int):
        try:
            i, j = self.number_indices[number]
            self.lines[i][j] = -1
        except KeyError:
            pass

    def check_bingo(self) -> bool:
        for line in self.lines:
            if all(num == -1 for num in line):
                return True
        for i in range(self.width):
            if all(num == -1 for num in [line[i] for line in self.lines]):
                return True
        return False

    def sum_unmarked(self):
        result = 0
        for i in range(self.length):
            for j in range(self.width):
                if self.lines[i][j] != -1:
                    result += self.lines[i][j]
        return result


class Bingo:

    def __init__(self, cards: List[BingoCard]):
        self.cards = cards

    def run(self, numbers: List[int]) -> Optional[Tuple[BingoCard, int]]:
        for number in numbers:
            for card in self.cards:
                card.cross_number(number)
                if card.check_bingo():
                    return card, number

    def run_full(self, numbers: List[int]):
        unfinished_cards = set(range(len(self.cards)))
        last = 0
        for number in numbers:
            for i, card in enumerate(self.cards):
                if i in unfinished_cards:
                    card.cross_number(number)
                    if card.check_bingo():
                        last = i
                        unfinished_cards.remove(i)
            if len(unfinished_cards) == 0:
                return self.cards[last], number


if __name__ == '__main__':
    solve()
