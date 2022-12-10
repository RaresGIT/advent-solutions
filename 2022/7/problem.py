from functools import reduce
from pprint import pprint
from anytree import Node, RenderTree, PreOrderIter
from anytree.exporter import DotExporter
from anytree.resolver import Resolver

file_lines = []
with open('input.txt', 'r') as f:
    file_lines = f.readlines()

file_lines = list(map(lambda x: x.strip(), file_lines))
# pprint(file_lines)

def alreadyExists(str: str, list_input: list[str]):
    isInList = len(list(filter(lambda x: x.name == str, list_input)))
    if isInList > 0:
        return True
    else:
        return False

def getIndexOf(str: str, list_input: list[str], start_from: int):
    for index, node in enumerate(list_input[start_from:]):
        if node.name == str:
            return index + start_from

    return None

def parseCommands(list : list[str]):
    
    start_dir = list[0].split().pop().__str__()
    tree = [Node(start_dir)]
    active_dir = 0
    path = [('/', 0)]
    for line in list[1:]:
        if any(char.isdigit() for char in line):
            new_file = Node(line, parent=tree[path[-1][1]])
            
        if line.__contains__('dir'):
            _ = line.split().pop()
            new_dir = Node(_, parent=tree[path[-1][1]])
            tree.append(new_dir)

        if line.__contains__('$'):
            if line.__contains__('cd'):
                # get rid of command and get only the dir name
                _ = line.split().pop()
                # print(_)
                if _ == '..':
                    path.pop()
                    # print(path)

                else:
                    active_dir = path[-1][1]
                    path.append((_ , getIndexOf(_, tree, active_dir)))
                    # print(path)
        
    return tree
tree = parseCommands(file_lines)
size_dict = {}

dirs = []
output_1 = 0
for node in tree:
    dir_name = "".join(list(map(lambda x: x.name + '/', node.path)))
    dir_size = 0
    if len(node.children) > 0:
        for child in node.children:
            if any(char.isdigit() for char in child.name):
                dir_size += int(child.name.split()[0])
    # if dir_size > 0:
    dirs.append([dir_name, dir_size])
pprint(list(sorted(dirs)))

dir_sizes = {}
for index, path in enumerate(list(sorted(dirs))):
    for path_to_check in dirs[index:]:
        if path[0] in path_to_check[0]:
            # print(path, path[1], path_to_check, path_to_check[1], path in path_to_check)
            path[1] += path_to_check[1]     
    if path[1] < 100000:
        output_1 += path[1]

    
def select_print(str: str):
    for path in dirs:
        if str in path[0]:
            print(path)
pprint(list(sorted(dirs)))
# select_print('//dtqvbspj/')
print(output_1)


# for pre, fill, node in RenderTree(tree[0]):
#     print("%s%s" % (pre, node.name))

# DotExporter(tree[0],
#              nodeattrfunc=lambda node: "fixedsize=true, width=1, height=1, shape=diamond",
#              edgeattrfunc=lambda parent, child: "style=bold").to_picture("tree.png")