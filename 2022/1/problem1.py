# Read from input, empty line = new elf. 
# Sum up calories for each elf and determined the one with the most calories
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

print(max(elves))