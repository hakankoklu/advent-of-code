def get_pixels(filepath):
    with open(filepath, 'r') as f:
        line = [int(x) for x in f.readline()]
        return line


def make_layers(pixels, width, height):
    area = width * height
    layers = [pixels[area * i: area * (i + 1)] for i in range(int(len(pixels)/area))]
    return layers


def count_digits(layer, digit):
    count = 0
    for pix in layer:
        if pix == digit:
            count += 1
    return count


def make_pixel(layered_pixels):
    for pix in layered_pixels:
        if pix == 0 or pix == 1:
            return pix
    return 2


filepath = '/Users/hkoklu/personal/advent_of_code_2019/day08.txt'
pixels = get_pixels(filepath)
layers = make_layers(pixels, 25, 6)
# zero_min_count = 151
# zero_min_layer = 0
# for i, l in enumerate(layers):
#     temp = count_digits(l, 0)
#     print(temp)
#     if temp < zero_min_count:
#         zero_min_count = temp
#         zero_min_layer = i

# one_count = count_digits(layers[zero_min_layer], 1)
# two_count = count_digits(layers[zero_min_layer], 2)
# print(one_count, two_count, one_count * two_count)


def combine_layers(layers):
    result = []
    for i in range(len(layers[0])):
        layered_pixels = []
        for j in range(len(layers)):
            layered_pixels.append(layers[j][i])
        pix = make_pixel(layered_pixels)
        result.append(pix)
    return result


def convert_pix(pix):
    res = '8'
    if pix == 0:
        res = ' '
    return res


def print_picture(line, width):
    area = [line[width * i: width * (i + 1)] for i in range(int(len(line)/width))]
    print(area)
    for l in area:
        print(''.join([convert_pix(p) for p in l]))

c = combine_layers(layers)
print(c)
print_picture(combine_layers(layers), 25)