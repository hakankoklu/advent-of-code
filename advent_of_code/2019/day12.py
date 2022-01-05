def get_initial_state(filepath):
    positions = {}
    count = 0
    with open(filepath, 'r') as f:
        for line in f.readlines():
            positions[count] = tuple(int(a.split('=')[1]) for a in line.strip('<>\n').split(','))
            count += 1
    return positions


def get_velocity_change_single(own, others):
    change = 0
    for other in others:
        if other > own:
            change += 1
        elif other < own:
            change -= 1
    return change


def get_velocity_change_all(own, others):
    change_x = get_velocity_change_single(own[0], [others[0][0], others[1][0], others[2][0]])
    change_y = get_velocity_change_single(own[1], [others[0][1], others[1][1], others[2][1]])
    change_z = get_velocity_change_single(own[2], [others[0][2], others[1][2], others[2][2]])
    return change_x, change_y, change_z


def get_others(moon, moon_vectors):
    result = {}
    for other in moon_vectors:
        if other != moon:
            result[other] = moon_vectors[other]
    return result


def sum_vectors(v1, v2):
    return tuple(v1[i] + v2[i] for i in range(len(v1)))


def get_updated_velocities(positions, velocities):
    new_velocities = {}
    for moon in positions:
        # print(f'current moon: {moon}')
        # print(f'current vel: {velocities[moon]}')
        other_positions = get_others(moon, positions)
        velocity_change = get_velocity_change_all(positions[moon], list(other_positions.values()))
        # print(f'vel change: {velocity_change}')
        new_velocities[moon] = sum_vectors(velocities[moon], velocity_change)
        # print(f'new vel: {new_velocities}')
    return new_velocities


def get_updated_positions(positions, velocities):
    new_positions = {}
    for moon in positions:
        new_positions[moon] = sum_vectors(positions[moon], velocities[moon])
    return new_positions


def get_energy(position, velocity):
    return sum([abs(c) for c in position]) * sum([abs(c) for c in velocity])


filepath = '/Users/hkoklu/personal/advent_of_code_2019/day12.txt'
current_pos = new_pos = get_initial_state(filepath)
current_vel = new_vel = {0: (0, 0, 0), 1: (0, 0, 0), 2: (0, 0, 0), 3: (0, 0, 0)}
print(current_pos)
print(current_vel)
steps = 1000
for step in range(steps):
    current_vel = new_vel
    current_pos = new_pos
    new_vel = get_updated_velocities(current_pos, current_vel)
    new_pos = get_updated_positions(current_pos, new_vel)
    print(f'After {step + 1} steps')
    print(f'Pos: {new_pos}')
    print(f'Vel: {new_vel}')

total_energy = sum([get_energy(x, y) for x, y in zip(list(new_pos.values()), list(new_vel.values()))])
print(total_energy)
