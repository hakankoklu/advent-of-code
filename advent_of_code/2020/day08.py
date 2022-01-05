from typing import List, Set


def take_input(filepath):
    with open(filepath, 'r') as f:
        lines = f.readlines()
        commands = []
        for line in lines:
            command = line[:3]
            arg = int(line[4:])
            commands.append((command, arg))
        return commands


def puzzle1(filepath):
    cmds = take_input(filepath)
    BC = BootCode(cmds)
    BC.run()


def puzzle2(filepath):
    cmds = take_input(filepath)
    nops = [ind for ind in range(len(cmds))
            if cmds[ind][0] == 'nop']
    jmps = [ind for ind in range(len(cmds))
            if cmds[ind][0] == 'jmp']
    for nop in nops:
        temp_cmds = cmds[:]
        temp_cmds[nop] = ('jmp', temp_cmds[nop][1])
        bc = BootCode(temp_cmds)
        result = bc.run()
        if result == 1:
            print(f'Program fixed, nop -> jmp was needed at index {nop}')
            break

    for jmp in jmps:
        temp_cmds = cmds[:]
        temp_cmds[jmp] = ('nop', temp_cmds[jmp][1])
        bc = BootCode(temp_cmds)
        result = bc.run()
        if result == 1:
            print(f'Program fixed, jmp -> nop was needed at index {jmp}')
            break


class BootCode:

    def __init__(self, cmds):
        self.cmds = cmds
        self.current = 0
        self.accumulator = 0
        self.executed = set()

    def step(self):
        if self.current >= len(self.cmds):
            print(f'Accumulator is {self.accumulator}, program finished!')
            return 1
        if self.current in self.executed:
            print(f'Accumulator is {self.accumulator}, entering infinite loop...')
            return 2
        self.executed.add(self.current)
        cmd = self.cmds[self.current][0]
        arg = self.cmds[self.current][1]
        if cmd == 'nop':
            self.current += 1
            return 0
        if cmd == 'acc':
            self.accumulator += arg
            self.current += 1
            return 0
        if cmd == 'jmp':
            self.current += arg
            return 0

    def run(self):
        output = 0
        while output == 0:
            output = self.step()
        return output


filepath = '/Users/hkoklu/personal/advent_of_code/2020/day08.txt'
puzzle1(filepath)
puzzle2(filepath)
