from typing import Dict, List


def take_input(filepath):
    cmds = []
    with open(filepath, 'r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            if line[:4] == 'mask':
                cmds.append(('m', line.split(' = ')[1]))
            else:
                line = line.strip('mem[')
                # print(line)
                address, value = [int(x) for x in line.split('] = ')]
                cmds.append((address, value))
    return cmds


def puzzle1(filepath):
    cmds = take_input(filepath)
    IP = InitProgram(cmds)
    IP.run()


def puzzle2(filepath):
    cmds = take_input(filepath)
    IP = InitProgram2(cmds)
    IP.run()


def mask_to_bits(mask: str) -> Dict[int, int]:
    mask_bitmap = {}
    for i in range(len(mask)):
        mask_bit = mask[-1 - i]
        if mask_bit != 'X':
            mask_bitmap[i] = int(mask_bit)
    return mask_bitmap


def dec_to_bin(number: int) -> List[int]:
    num_bin = bin(number)
    bin_digits = []
    for i in range(len(num_bin) - 2):
        bin_digits.append(int(num_bin[-1 - i]))
    return bin_digits


class InitProgram:

    def __init__(self, cmds):
        self.cmds = cmds
        self.mask = {}
        self.memory = {}
        self.bit_len = 36

    def mask_value(self, value: int) -> int:
        bin_digits = dec_to_bin(value)
        bin_digits = bin_digits + [0] * (self.bit_len - len(bin_digits))
        for i in range(self.bit_len):
            if i in self.mask:
                bin_digits[i] = self.mask[i]
        bin_digits.reverse()
        return int(''.join([str(x) for x in bin_digits]), 2)

    def process_write(self, address, value):
        self.memory[address] = self.mask_value(value)

    def run(self):
        for cmd, value in self.cmds:
            if cmd == 'm':
                self.mask = mask_to_bits(value)
            else:
                self.process_write(cmd, value)
        print(sum(self.memory.values()))


class InitProgram2:

    def __init__(self, cmds):
        self.cmds = cmds
        self.floats = []
        self.ones = []
        self.memory = {}
        self.bit_len = 36

    def mask_address(self, address: int) -> List[int]:
        addresses = []
        bin_digits = dec_to_bin(address)
        bin_digits += [0] * (self.bit_len - len(bin_digits))
        # print('1', bin_digits)
        for dig in self.ones:
            bin_digits[dig] = 1
            # print('2', bin_digits)
        for i in range(2 ** len(self.floats)):
            replacement_digits = dec_to_bin(i)
            replacement_digits += [0] * (len(self.floats) - len(replacement_digits))
            # print('r', i, replacement_digits)
            for float_i, floaty in enumerate(self.floats):
                bin_digits[floaty] = replacement_digits[float_i]
            # print('3', bin_digits)
            temp = bin_digits[::-1]
            addresses.append(int(''.join([str(x) for x in temp]), 2))
        return addresses

    def update_mask(self, mask):
        self.floats = []
        self.ones = []
        for i in range(len(mask)):
            if mask[i] == 'X':
                self.floats.append(self.bit_len - 1 - i)
            elif mask[i] == '1':
                self.ones.append(self.bit_len - 1 - i)

    def process_write(self, address, value):
        addresses = self.mask_address(address)
        # print(addresses)
        for a in addresses:
            self.memory[a] = value

    def run(self):
        for cmd, value in self.cmds:
            # print(self.floats, self.ones)
            if cmd == 'm':
                self.update_mask(value)
            else:
                self.process_write(cmd, value)
        print(sum(self.memory.values()))


filepath = '/Users/hkoklu/personal/advent_of_code/2020/day14.txt'
puzzle1(filepath)
puzzle2(filepath)
# print(puzzle4(filepath))
