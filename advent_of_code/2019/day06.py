filepath = '/Users/hkoklu/personal/advent_of_code_2019/day6.txt'
with open(filepath, 'r') as f:
    lines = f.readlines()

childs = {}
parents = {}
for line in lines:
    foc, pla = line.strip('\n').split(')')
    if foc in childs:
        childs[foc].add(pla)
    else:
        childs[foc] = set([pla])
    parents[pla] = foc

levels = {}

queue = [('COM', 0)]
while queue:
    center, level = queue.pop(0)
    levels[center] = level
    kids = childs.get(center)
    if kids:
        for kid in kids:
            queue.append((kid, level + 1))

total = 0
for planet, level in levels.items():
    total += level

print(total)

def get_path_to_COM(planet):
    parent = planet
    result = []
    while parent != 'COM':
        result.append(parent)
        parent = parents[parent]
    result.append('COM')
    return result

line1 = get_path_to_COM('YOU')
line2 = get_path_to_COM('SAN')
print(line1)
print(line2)

i = 0
found = False
while not found:
    i -= 1
    if line1[i] == line2[i]:
        prev = line1[i]
        continue
    else:
        found = True
print(prev)
print(line1.index(prev))
print(line2.index(prev))
print(line1.index(prev) + line2.index(prev) - 2)