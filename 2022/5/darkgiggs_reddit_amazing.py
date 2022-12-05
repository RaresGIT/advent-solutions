input = open('input.txt').read().split('\n\n')    
h_stacks = input[0].splitlines()
instructions = input[1].strip().splitlines()

def move(n,s,d, over_9000):
    temp, s = s[:n], s[n:]
    return (s, temp+d) if over_9000 else (s, temp[::-1]+d)

def rearrange(inst, over_9000):
    stack = [[h_stacks[i][j] for i in range(len(h_stacks)-1) if h_stacks[i][j] != ' '] for j in range(1, len(h_stacks[0]), 4)]
    print(stack)
    for instruction in inst:
        _, n, _, source, _, dest = instruction.split(' ')
        n, source, dest = map(int,(n, source, dest))
        stack[source-1], stack[dest-1] = move(n, stack[source-1], stack[dest-1], over_9000)
    return ''.join([stack[i][0] for i in range(len(stack))])

print(rearrange(instructions, False),
      rearrange(instructions, True))