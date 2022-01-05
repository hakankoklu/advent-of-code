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
    elif intopcode in [5, 6]:
        first_ind = int(input_list[com_ind + 1])
        first_relative_ind = first_ind + relative_base if params[0] == 2 else first_ind
        first_val = first_ind if params[0] == 1 else int(input_list[first_relative_ind])
        second_ind = int(input_list[com_ind + 2])
        second_relative_ind = second_ind + relative_base if params[1] == 2 else second_ind
        second_val = second_ind if params[1] == 1 else int(input_list[second_relative_ind])
    else:
        first_ind = int(input_list[com_ind + 1])
        first_relative_ind = first_ind + relative_base if params[0] == 2 else first_ind
        first_val = first_ind if params[0] == 1 else int(input_list[first_relative_ind])
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


def get_direction(cur_coor, cur_dir, turn_signal):
    x = cur_coor[0]
    y = cur_coor[1]
    if cur_dir == 'up':
        if turn_signal == 0:
            return (x - 1, y), 'left'
        elif turn_signal == 1:
            return (x + 1, y), 'right'
    elif cur_dir == 'down':
        if turn_signal == 0:
            return (x + 1, y), 'right'
        elif turn_signal == 1:
            return (x - 1, y), 'left'
    elif cur_dir == 'left':
        if turn_signal == 0:
            return (x, y - 1), 'down'
        elif turn_signal == 1:
            return (x, y + 1), 'up'
    elif cur_dir == 'right':
        if turn_signal == 0:
            return (x, y + 1), 'up'
        elif turn_signal == 1:
            return (x, y - 1), 'down'


def run_robot(cmds_d):
    painted = defaultdict(int)
    painted[(0, 5)] = 1
    newind = current = 0
    rb = 0
    new_coor = current_coor = (0, 5)
    out_count = 0
    new_dir = current_dir = 'up'
    while newind != -1:
        current = newind
        current_rb = rb
        current_coor = new_coor
        current_dir = new_dir
        current_paint = painted[current_coor]
        current_opcode, _ = proc_code(cmds[current])
        print(f'Coor: {current_coor}, Dir: {current_dir}, Color: {current_paint}')
        print(f'{current} > opcode: {current_opcode}, rb: {current_rb}')
        if int(current_opcode) == 3:
            out = execute_command(current, cmds_d, current_paint, current_rb)
        else:
            out = execute_command(current, cmds_d, 0, current_rb)
        print(cmds[current: current + 4], out)
        print(f'NewInd: {out[0]}, Output: {out[1]}, NewBase: {out[2]}')
        print('-----------------------------------')
        if int(current_opcode) == 4 and out_count == 0:
            painted[current_coor] = out[1]
            out_count += 1
        elif int(current_opcode) == 4 and out_count == 1:
            out_count = 0
            new_coor, new_dir = get_direction(current_coor, current_dir, out[1])
        newind = out[0]
        rb = out[2]
    return painted


filepath = '/Users/hkoklu/personal/advent_of_code_2019/day11.txt'
cmds = get_commands(filepath)
cmds_d = defaultdict(lambda: '0', enumerate(cmds))
result = run_robot(cmds_d)
print(result, '\n', len(result))

row = [' ']*43
plate = []
for y in range(6):
    plate.append(row[:])
for x in range(43):
    for y in range(6):
        plate[y][x] = ' ' if result[(x, y)] == 0 else '*'

plate.reverse()
for row in plate:
    print(''.join([str(a) for a in row]))
