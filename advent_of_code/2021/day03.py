import os
from enum import Enum
from typing import List, Tuple

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
        return lines


def solve_p1(fp):
    cmds = prep(fp)
    sb = Submarine()
    sb.diagnostic_report.load_report(cmds)
    gamma, epsilon = sb.diagnostic_report.get_gamma_epsilon_rate()
    return gamma * epsilon


def solve_p2(fp):
    cmds = prep(fp)
    sb = Submarine()
    sb.diagnostic_report.load_report(cmds)
    oxy = sb.diagnostic_report.get_oxy_gen_rating()
    co2 = sb.diagnostic_report.get_co2_scrubber_rating()
    return oxy * co2


class Direction(Enum):
    FORWARD = 'forward'
    UP = 'up'
    DOWN = 'down'


class Submarine:

    def __init__(self):
        self.aim = 0
        self.depth = 0
        self.distance = 0
        self.diagnostic_report = DiagnosticReport()

    def step(self, direction: Direction, amount: int) -> None:
        if direction == Direction.FORWARD:
            self.distance += amount
            self.depth += self.aim * amount
        elif direction == Direction.DOWN:
            self.aim += amount
        elif direction == Direction.UP:
            self.aim -= amount

    def navigate(self, cmds: List[Tuple[Direction, int]]) -> None:
        for cmd in cmds:
            self.step(cmd[0], cmd[1])


class DiagnosticReport:

    def __init__(self):
        self.report = []

    def load_report(self, report: List[str]):
        self.report = report

    def get_gamma_epsilon_rate(self) -> Tuple[int, int]:
        mcb, lcb = self.get_most_least_common_bits(self.report)
        return int(''.join([str(i) for i in mcb]), 2), int(''.join([str(i) for i in lcb]), 2)

    def get_one_count(self, report):
        one_bits = [0] * len(report[0])
        for line in report:
            for pos, bit in enumerate(line):
                one_bits[pos] += int(bit)
        return one_bits

    def get_most_least_common_bits(self, report):
        report_length = len(report)
        one_bits = self.get_one_count(report)
        mcb = []
        lcb = []
        for one_bit in one_bits:
            if one_bit >= report_length / 2:
                mcb.append(1)
                lcb.append(0)
            else:
                mcb.append(0)
                lcb.append(1)
        return mcb, lcb

    def get_oxy_gen_rating(self):
        return int(self.filter_report(self.report, True), 2)

    def get_co2_scrubber_rating(self):
        return int(self.filter_report(self.report, False), 2)

    def filter_report(self, report: List[str], filter_bit: bool, bit_loc: int = 0):
        if len(report) == 1:
            return report[0]
        mcb, lcb = self.get_most_least_common_bits(report)
        bit_freq = mcb if filter_bit else lcb
        new_report = []
        for line in report:
            if bit_freq[bit_loc] == int(line[bit_loc]):
                new_report.append(line)
        return self.filter_report(new_report, filter_bit, bit_loc + 1)


if __name__ == '__main__':
    solve()
