from typing import Dict, Tuple


def take_input(filepath):
    with open(filepath, 'r') as f:
        lines = f.readlines()
        instructions = []
        for line in lines:
            line = line.strip()
            instructions.append((line[0], int(line[1:])))
        return instructions


degree_to_orient = {
    0: 'N',
    90: 'E',
    180: 'S',
    270: 'W',
}

orient_to_degree = {
    'N': 0,
    'E': 90,
    'S': 180,
    'W': 270,
}


class Navigator:

    def __init__(self, commands):
        self.commands = commands
        self.position = [0, 0]
        self.orientation = 'E'

    def turn(self, direction, degrees):
        cur_angle = orient_to_degree[self.orientation]
        if direction == 'R':
            cur_angle += degrees
        elif direction == 'L':
            cur_angle -= degrees
        cur_angle %= 360
        self.orientation = degree_to_orient[cur_angle]

    def move(self, direction, distance):
        if direction == 'N':
            self.position[1] += distance
        if direction == 'S':
            self.position[1] -= distance
        if direction == 'E':
            self.position[0] += distance
        if direction == 'W':
            self.position[0] -= distance

    def process_command(self, cmd):
        if cmd[0] == 'F':
            self.move(self.orientation, cmd[1])
        elif cmd[0] in ['L', 'R']:
            self.turn(cmd[0], cmd[1])
        else:
            self.move(cmd[0], cmd[1])

    def run(self):
        for cmd in self.commands:
            self.process_command(cmd)
        print(self.position)
        print(abs(self.position[0]) + abs(self.position[1]))


def puzzle1(filepath):
    cmds = take_input(filepath)
    N = Navigator(cmds)
    N.run()


class Navigator2:

    def __init__(self, commands, waypoint):
        self.commands = commands
        self.position = [0, 0]
        self.waypoint = waypoint

    def turn(self, direction, degrees):
        if direction == 'L':
            degrees = 360 - degrees
        if degrees == 90:
            self.waypoint = [self.waypoint[1], -1 * self.waypoint[0]]
        if degrees == 180:
            self.waypoint = [-1 * self.waypoint[0], -1 * self.waypoint[1]]
        if degrees == 270:
            self.waypoint = [-1 * self.waypoint[1], self.waypoint[0]]

    def move_waypoint(self, direction, distance):
        if direction == 'N':
            self.waypoint[1] += distance
        if direction == 'S':
            self.waypoint[1] -= distance
        if direction == 'E':
            self.waypoint[0] += distance
        if direction == 'W':
            self.waypoint[0] -= distance

    def move(self, distance):
        self.position[0] += distance * self.waypoint[0]
        self.position[1] += distance * self.waypoint[1]

    def process_command(self, cmd):
        if cmd[0] == 'F':
            self.move(cmd[1])
        elif cmd[0] in ['L', 'R']:
            self.turn(cmd[0], cmd[1])
        else:
            self.move_waypoint(cmd[0], cmd[1])

    def run(self):
        for cmd in self.commands:
            self.process_command(cmd)
        print(self.position)
        print(abs(self.position[0]) + abs(self.position[1]))


def puzzle2(filepath):
    cmds = take_input(filepath)
    N = Navigator2(cmds, [10, 1])
    N.run()


filepath = '/Users/hkoklu/personal/advent_of_code/2020/day12_test.txt'
puzzle1(filepath)
puzzle2(filepath)
