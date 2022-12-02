# Read from input, empty line = new elf. 
# Sum up calories for each elf and determined the one with the most calories

# Instead of getting only max, determine top 3 elves
calories = []

with open('input.txt', 'r') as f:
    calories = f.readlines()

elves_count = calories.count('\n')
print(elves_count)
elves = [0] * (elves_count + 1)
elf_index = 0
for entry in calories:
    if entry != '\n':
        elves[elf_index] += int(entry.strip())
    else:
        elf_index += 1

# sort and get only top 3
sorted_elves = sorted(elves, reverse=True)[:3]

# print sum of these 3
print(sum(sorted_elves))