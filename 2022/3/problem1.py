# Input contains backpacks with items
# Backpacks have to be split in half and we need to find the common item between the splits
# Then add scores based on letter found

backpacks = []
with open('input.txt', 'r') as f:
    backpacks = list(map(lambda x: x.strip(), f.readlines()))


def get_common_items(set_left, set_right):
    return set_left.intersection(set_right)

def get_priority(letter):
    if ord(letter) >= 97:
        return ord(letter) - 96
    else:
        return ord(letter) - 64 + 26

sum = 0
for backpack in backpacks:
    print(backpack)
    count = backpack.__len__()
    half = int(count/2)

    set_items_left = set(list(backpack[0:half]))
    set_items_right = set(list(backpack[half:count]))

    common = get_common_items(set_items_left, set_items_right)
    sum += get_priority(common.pop())


print(sum)