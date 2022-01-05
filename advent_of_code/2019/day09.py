from collections import defaultdict

opcode_jumps = {1: 4, 2: 4, 3: 2, 4: 2, 5: 3, 6: 3, 7: 4, 8: 4, 9: 2}


def proc_code(code):
    p = [0, 0, 0]
    if len(code) >= 2:
        opcode = code[-2] + code[-1]
    else:
        opcode = code
    if len(code) == 3:
        p = [int(code[0]), 0, 0]
    if len(code) == 4:
        p = [int(code[1]), int(code[0]), 0]
    if len(code) == 5:
        p = [int(code[2]), int(code[1]), int(code[0])]
    return opcode, p


def get_commands(filepath):
    with open(filepath, 'r') as f:
        line = f.readline()
        return line.split(',')


def execute_command(com_ind, input_list, inp, relative_base):
    opcode, params = proc_code(input_list[com_ind])
    intopcode = int(opcode)
    if opcode == '99':
        return -1, (opcode), 0
    if intopcode in [1, 2, 7, 8]:
        first_ind = int(input_list[com_ind + 1])
        first_relative_ind = first_ind + relative_base if params[0] == 2 else first_ind
        first_val = first_ind if params[0] == 1 else int(input_list[first_relative_ind])
        second_ind = int(input_list[com_ind + 2])
        second_relative_ind = second_ind + relative_base if params[1] == 2 else second_ind
        second_val = second_ind if params[1] == 1 else int(input_list[second_relative_ind])
        result_ind = int(input_list[com_ind + 3])
        result_relative_ind = result_ind + relative_base if params[2] == 2 else result_ind
        # print(first_relative_ind, second_relative_ind, result_relative_ind)
        # print(first_val, second_val)
    elif intopcode in [5, 6]:
        first_ind = int(input_list[com_ind + 1])
        first_relative_ind = first_ind + relative_base if params[0] == 2 else first_ind
        first_val = first_ind if params[0] == 1 else int(input_list[first_relative_ind])
        second_ind = int(input_list[com_ind + 2])
        second_relative_ind = second_ind + relative_base if params[1] == 2 else second_ind
        second_val = second_ind if params[1] == 1 else int(input_list[second_relative_ind])
        # print(first_relative_ind, second_relative_ind)
        # print(first_val, second_val)
    else:
        first_ind = int(input_list[com_ind + 1])
        first_relative_ind = first_ind + relative_base if params[0] == 2 else first_ind
        first_val = first_ind if params[0] == 1 else int(input_list[first_relative_ind])
        # print(first_relative_ind)
        # print(first_val)
    if intopcode == 1:
        input_list[result_relative_ind] = first_val + second_val
        input_list[result_relative_ind] = str(input_list[result_relative_ind])
        return com_ind + opcode_jumps[intopcode], 0, relative_base
    if intopcode == 2:
        input_list[result_relative_ind] = first_val * second_val
        input_list[result_relative_ind] = str(input_list[result_relative_ind])
        return com_ind + opcode_jumps[intopcode], 0, relative_base
    if intopcode == 3:
        input_list[first_relative_ind] = inp
        input_list[first_relative_ind] = str(input_list[first_relative_ind])
        return com_ind + opcode_jumps[intopcode], 0, relative_base
    if intopcode == 4:
        return com_ind + opcode_jumps[intopcode], first_val, relative_base
    if intopcode == 5:
        new_com_ind = second_val if first_val else com_ind + opcode_jumps[intopcode]
        return new_com_ind, 0, relative_base
    if intopcode == 6:
        new_com_ind = second_val if first_val == 0 else com_ind + opcode_jumps[intopcode]
        return new_com_ind, 0, relative_base
    if intopcode == 7:
        input_list[result_relative_ind] = '1' if first_val < second_val else '0'
        return com_ind + opcode_jumps[intopcode], 0, relative_base
    if intopcode == 8:
        input_list[result_relative_ind] = '1' if first_val == second_val else '0'
        return com_ind + opcode_jumps[intopcode], 0, relative_base
    if intopcode == 9:
        return com_ind + opcode_jumps[intopcode], 0, first_val + relative_base


filepath = '/Users/hkoklu/personal/advent_of_code_2019/day09.txt'
cmds = get_commands(filepath)
cmds_d = defaultdict(lambda: '0', enumerate(cmds))
print(len(cmds))
newind = current = 0
rb = 0
while newind != -1:
    current = newind
    current_opcode, _ = proc_code(cmds[current])
    current_rb = rb
    # print(f'{current} > opcode: {current_opcode}, rb: {current_rb}')
    # print(cmds_d[63])
    if int(current_opcode) == 3:
        out = execute_command(current, cmds_d, 2, current_rb)
    else:
        out = execute_command(current, cmds_d, 0, current_rb)
    # print(cmds[current: current + 4], out)
    if int(current_opcode) == 4:
        print(out[1])
    newind = out[0]
    rb = out[2]
