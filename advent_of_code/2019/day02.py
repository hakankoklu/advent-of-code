def day2_1(filepath):
    cmds = get_commands(filepath)
    return calculate_output(cmds, 12, 2)


def day2_2(filepath, target):
    cmds = get_commands(filepath)
    for i in range(100):
        for j in range(100):
            temp = cmds[:]
            out = calculate_output(temp, i, j)
            if out == target:
                return i, j


def calculate_output(cmds, noun, verb):
    execute_commands_with_inputs(cmds, noun, verb)
    return cmds[0]


def execute_commands_with_inputs(cmds, noun, verb):
    cmds[1] = noun
    cmds[2] = verb
    for i in range(0, len(cmds), 4):
        res = execute_command(i, cmds)
        if not res:
            break


def execute_commands(cmds):
    print(cmds)
    for i in range(0, len(cmds), 4):
        res = execute_command(i, cmds)
        if not res:
            break


def get_commands(filepath):
    with open(filepath, 'r') as f:
        line = f.readline()
        return [int(x) for x in line.split(',')]


def execute_command(com_ind, input_list):
    if input_list[com_ind] == 99:
        return False
    first_ind = input_list[com_ind + 1]
    second_ind = input_list[com_ind + 2]
    result_ind = input_list[com_ind + 3]
    if input_list[com_ind] == 1:
        input_list[result_ind] = input_list[first_ind] + input_list[second_ind]
        return True
    if input_list[com_ind] == 2:
        input_list[result_ind] = input_list[first_ind] * input_list[second_ind]
        return True


filepath = '/Users/hkoklu/personal/advent_of_code_2019/day2.txt'
cmds = get_commands(filepath)
execute_commands_with_inputs(cmds, 76, 10)
print(cmds)
print(day2_2(filepath, 19690720))
