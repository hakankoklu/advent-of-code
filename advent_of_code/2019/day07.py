from itertools import permutations

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
        return -1, (opcode), 0
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


def run_software(inps, input_list, pos):
    inp_index = 0
    newind = current = pos
    output = None
    while newind != -1:
        current = newind
        current_opcode, _ = proc_code(input_list[current])
        if int(current_opcode) == 3:
            if inp_index >= len(inps):
                return current, input_list[:], output
            out = execute_command(current, input_list, inps[inp_index])
            inp_index += 1
        else:
            out = execute_command(current, input_list, 0)
        if int(current_opcode) == 4:
            print(out)
            output = out[2]
        newind = out[0]
    return newind, [], output


def run_thruster_amp(input_list, phases, inp):
    for phase in phases:
        temp = input_list[:]
        inp = run_software([phase, inp], temp)
    return inp


def run_thruster_amp_loop(input_list, phases, inp):
    amp_lists = [input_list[:], input_list[:], input_list[:], input_list[:], input_list[:]]
    amp_list_pos = [0, 0, 0, 0, 0]
    count = 0
    while inp is not None:
        cur = count % 5
        count += 1
        # if count == 10:
        #     break
        phase = phases[cur]
        if count < 6:
            amp_list_pos[cur], amp_lists[cur], inp = run_software([phase, inp], amp_lists[cur], amp_list_pos[cur])
        else:
            amp_list_pos[cur], amp_lists[cur], inp = run_software([inp], amp_lists[cur], amp_list_pos[cur])
        if amp_list_pos[cur] == -1:
            print(f'{cur} halted')
            if cur == 4:
                break
    return inp


filepath = '/Users/hkoklu/personal/advent_of_code_2019/day7.txt'
cmds = get_commands(filepath)
print(run_thruster_amp_loop(cmds, [9, 8, 7, 6, 5], 0))

all_perms = permutations([5, 6, 7, 8, 9])
maxx = 0
for perm in all_perms:
    maxx = max(maxx, run_thruster_amp_loop(cmds, perm, 0))
    print(maxx)
