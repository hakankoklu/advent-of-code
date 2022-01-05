opcode_jumps = {1: 4, 2: 4, 3: 2, 4: 2, 5: 3, 6: 3, 7: 4, 8: 4}


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


def execute_command(com_ind, input_list, inp):
    opcode, params = proc_code(input_list[com_ind])
    intopcode = int(opcode)
    if opcode == '99':
        return 0, (opcode), 0
    if intopcode in [1,2,7,8]:
        first_ind = int(input_list[com_ind + 1])
        first_val = first_ind if params[0] else int(input_list[first_ind])
        second_ind = int(input_list[com_ind + 2])
        second_val = second_ind if params[1] else int(input_list[second_ind])
        result_ind = int(input_list[com_ind + 3])
        result_val = result_ind if params[2] else int(input_list[result_ind])
    elif intopcode in [5,6]:
        first_ind = int(input_list[com_ind + 1])
        first_val = first_ind if params[0] else int(input_list[first_ind])
        second_ind = int(input_list[com_ind + 2])
        second_val = second_ind if params[1] else int(input_list[second_ind])
    else:
        first_ind = int(input_list[com_ind + 1])
        first_val = first_ind if params[0] else int(input_list[first_ind])
    if intopcode == 1:
        input_list[result_ind] = first_val + second_val
        input_list[result_ind] = str(input_list[result_ind])
        return com_ind + opcode_jumps[intopcode], input_list[com_ind:com_ind + opcode_jumps[intopcode]], 0
    if intopcode == 2:
        input_list[result_ind] = first_val * second_val
        input_list[result_ind] = str(input_list[result_ind])
        return com_ind + opcode_jumps[intopcode], input_list[com_ind:com_ind + opcode_jumps[intopcode]], 0
    if intopcode == 3:
        input_list[first_ind] = inp
        input_list[first_ind] = str(input_list[first_ind])
        return com_ind + opcode_jumps[intopcode], input_list[com_ind:com_ind + opcode_jumps[intopcode]], 0
    if intopcode == 4:
        return com_ind + opcode_jumps[intopcode], input_list[com_ind:com_ind + opcode_jumps[intopcode]], first_val
    if intopcode == 5:
        new_com_ind = second_val if first_val else com_ind + opcode_jumps[intopcode]
        return new_com_ind, input_list[com_ind:com_ind + opcode_jumps[intopcode]], 0
    if intopcode == 6:
        new_com_ind = second_val if first_val == 0 else com_ind + opcode_jumps[intopcode]
        return new_com_ind, input_list[com_ind:com_ind + opcode_jumps[intopcode]], 0
    if intopcode == 7:
        input_list[result_ind] = '1' if first_val < second_val else '0'
        return com_ind + opcode_jumps[intopcode], input_list[com_ind:com_ind + opcode_jumps[intopcode]], 0
    if intopcode == 8:
        input_list[result_ind] = '1' if first_val == second_val else '0'
        return com_ind + opcode_jumps[intopcode], input_list[com_ind:com_ind + opcode_jumps[intopcode]], 0


filepath = '/Users/hkoklu/personal/advent_of_code_2019/day5.txt'
cmds = get_commands(filepath)
print(len(cmds))
current = 0
print(current)
out = execute_command(current, cmds, 5)
print(out)
newind = out[0]
while newind != 0:
    current = newind
    print(current)
    out = execute_command(current, cmds, 0)
    print(out)
    newind = out[0]
