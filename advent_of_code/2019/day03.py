def get_path_points(start, segment):
    x = start[0]
    y = start[1]
    direction = segment[0]
    path_len = int(segment[1:])
    points = []
    if direction == 'R':
        for i in range(1, path_len + 1):
            points.append((x + i, y))
    elif direction == 'L':
        for i in range(1, path_len + 1):
            points.append((x - i, y))
    elif direction == 'U':
        for i in range(1, path_len + 1):
            points.append((x, y + i))
    else:
        for i in range(1, path_len + 1):
            points.append((x, y - i))
    return points


def get_all_path_points(segments):
    start = (0, 0)
    path = [start]
    for segment in segments:
        temp_start = path[-1]
        temp_path = get_path_points(temp_start, segment)
        path.extend(temp_path)
    print(len(path))
    return path


def get_inputs(filepath):
    with open(filepath, 'r') as f:
        lines = f.readlines()
    return [line.split(',') for line in lines]


def get_intersections_of_point_lists(l1, l2):
    result = []
    count = 1
    set1 = set(l1)
    set2 = set(l2)
    for p1 in set1:
        # print(f'checking point {count}')
        count += 1
        if p1 in set2:
            result.append(p1)
    return result


def get_intersection_segments(s1, s2):
    return get_intersections_of_point_lists(
        get_all_path_points(s1),
        get_all_path_points(s2)
    )


def get_min_distance_of_points(points):
    distance = 10000000
    for point in points:
        dist = abs(point[0]) + abs(point[1])
        if dist < distance and dist != 0:
            distance = dist
    return distance


def get_total_min_steps_to_intersection(s1, s2):
    path1 = get_all_path_points(s1)
    path2 = get_all_path_points(s2)
    points = get_intersections_of_point_lists(
        path1, path2)
    distance = 1000000000
    for point in points:
        dist = get_point_location(point, path1) + get_point_location(point, path2)
        if dist < distance and dist != 0:
            distance = dist
    return distance


def get_point_location(point, l):
    for i in range(len(l)):
        if l[i] == point:
            return i


def get_result(s1, s2):
    points = get_intersection_segments(s1, s2)
    return get_min_distance_of_points(points)


filepath = '/Users/hkoklu/personal/advent_of_code_2019/day3.txt'
print(get_total_min_steps_to_intersection(
    *get_inputs(filepath)
    ))
