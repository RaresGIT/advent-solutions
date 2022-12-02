# Rock paper scissors
# Column 1: what opponents play
# Column 2: what I play in response

# Score: 1 Rock 2 Paper 3 Scissors + outcome (0,3,6)

# A/X = Rock, B/Y = Paper, C/Z = Scissors
WIN = 6
DRAW = 3
LOSE = 0
ROCK = 1
SCISSORS = 3
PAPER = 2
SCORES = {
    'A': 1,
    'X': 1,
    'B': 2,
    'Y': 2,
    'C': 3,
    'Z': 3
}
# define a way to easily track counters
WIN_ORDER = [ROCK, SCISSORS, PAPER, ROCK]

def determine_win(me, opponent):
    if me == opponent:
        return DRAW

    if me == ROCK and opponent == PAPER:
        return LOSE
    
    index_me = WIN_ORDER.index(me)
    if WIN_ORDER[index_me + 1] == opponent:
        return WIN
    elif WIN_ORDER[index_me - 1] == opponent:
        return LOSE

strategies = []
with open('input.txt', 'r') as f:
    strategies = list(map(lambda x: x.strip(), f.readlines()))

score = 0
for strategy in strategies:
    opponent = SCORES.get(strategy[0])
    me = SCORES.get(strategy[2])
    
    local_score = determine_win(me, opponent) + me
    print(me, opponent, local_score)
    score += local_score
print(score)
    
            