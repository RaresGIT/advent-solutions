

ranges_raw = []
with open('input.txt', 'r') as f:
    ranges_raw = list(map(lambda x: x.strip(), f.readlines()))

ranges = []
for line in ranges_raw:
    split = line.split(',')
    ranges.append((split[0], split[1]))

def create_range(string_input: str):
    # Takes in smth like 1-3 and returns [1,2,3]
    edges = string_input.split('-')
    print(edges)
    return list(range(int(edges[0]), int(edges[1]) + 1))

def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3

def indentify_elf_pair(range0, range1):
    intersection_local = intersection(range0,range1)
    if intersection_local == range0 or intersection_local == range1:
        return 1
    else:
        return 0

count = 0
for tuple in ranges:
    range0 = create_range(tuple[0])
    range1 = create_range(tuple[1])

    count += indentify_elf_pair(range0, range1)

print(count)

