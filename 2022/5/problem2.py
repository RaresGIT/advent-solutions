from pprint import pprint
import re


#### read stack diagram and create stacks
file_lines = []
with open('input.txt', 'r') as f:
    file_lines = f.readlines()

# pprint(file_lines)
stack_diagram = []
for line in file_lines:
    if line == '\n':
        break
    # line = re.sub(' +', ' ', line)
    stack_diagram.append(line)

pprint(stack_diagram)
stack_diagram.pop()
stacks = [[], [], [], [], [], [], [], [], []]

def edit_list(list: list):
    empty_spaces = int(list.count('') /4)
    
    for i in range(empty_spaces):
        empty_space = list.index('')
        list[empty_space] = '|'
        for i in range(3):
            list.remove('')

    return list

# for i in range(9):
for line in reversed(list(stack_diagram)):
    elements = line.split(' ')
    
    if '' in elements:
        elements = edit_list(elements)
    for i, element in enumerate(elements):
        if element.strip() != '|':
            stacks[i].append(element.strip())

pprint(stacks)

#### read steps and parse input

def parse_move(line: str):
    line = line.replace(' ','')
    count = line[line.find('move') + 4 : line.find('from')]
    from_index = line[line.find('from') + 4]
    to_index = line[line.find('to') + 2]
    return (int(count), int(from_index) - 1, int(to_index) - 1)
moves = []
START_READ = False
for line in file_lines:
    if START_READ:
        tuple = parse_move(line)
        moves.append(tuple)
    if line == '\n':
        START_READ = True
    
# pprint(moves)
#### calculate end state of stacks and form the output (string containing top of each stack)

def move(count, from_stack_index, to_stack_index):
    
    for i in range(count):
        element = stacks[from_stack_index].pop()
        stacks[to_stack_index].append(element)

def move_arranged(count, from_stack_index, to_stack_index):
    buffer = []
    # pprint(stacks)
    for i in range(count):
        element = stacks[from_stack_index].pop()
        buffer.append(element)
        
    buffer.reverse()
    for item in buffer:
        stacks[to_stack_index].append(item)

for tuple in moves:
    move_arranged(tuple[0], tuple[1], tuple[2])

tops = []
for stack in stacks:
    formatted = stack.pop().replace('[', '').replace(']', '')
    tops.append(formatted)

print("".join(tops))