# This time, find common item between "groups" of 3 backpacks, then add the scores as pb1

backpacks = []
with open('input.txt', 'r') as f:
    backpacks = list(map(lambda x: x.strip(), f.readlines()))

def get_common_items_group(set1, set2, set3):
    return set1.intersection(set2.intersection(set3))


def get_priority(letter):
    if ord(letter) >= 97:
        return ord(letter) - 96
    else:
        return ord(letter) - 64 + 26

sum = 0
for i in range(0, backpacks.__len__(), 3):
    set1 = set(backpacks[i])
    set2 = set(backpacks[i+1])
    set3 = set(backpacks[i+2])

    common = get_common_items_group(set1,set2,set3)

    sum+= get_priority(common.pop())

print(sum)


