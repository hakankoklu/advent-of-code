def is_increasing(num):
    prev = int(num[0])
    for n in num:
        if int(n) < prev:
            return False
        prev = int(n)
    return True


def has_double(num):
    prev = num[0]
    for n in num[1:]:
        if n == prev:
            return True
        prev = n
    return False


def has_double_only(num):
    counts = {}
    for n in num:
        if n in counts:
            counts[n] += 1
        else:
            counts[n] = 1
    for _, v in counts.items():
        if v == 2:
            return True
    return False


def is_valid(num):
    return is_increasing(num) and has_double(num)


def is_valid2(num):
    return is_increasing(num) and has_double_only(num)


result = []
for num in range(183564, 657474):
    if is_valid2(str(num)):
        result.append(num)
print(len(result))
print(result[:10])
