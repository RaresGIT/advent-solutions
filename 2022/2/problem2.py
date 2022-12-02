# Rock paper scissors
# Column 1: what opponents play
# Column 2: what I play in response

# Score: 1 Rock 2 Paper 3 Scissors + outcome (0,3,6)

# X/Y/Z = outcome
WIN = 6
DRAW = 3
LOSE = 0
ROCK = 1
SCISSORS = 3
PAPER = 2
SCORES = {
    'A': 1,
    'B': 2,
    'C': 3,
}

OUTCOMES = {
    'X': LOSE,
    'Y': DRAW,
    'Z': WIN
}
# define a way to easily track counters
WIN_ORDER = [ROCK, SCISSORS, PAPER, ROCK]

def find_play(opponent, outcome):
    if outcome == DRAW:
        return opponent
    index_opponent = WIN_ORDER.index(opponent)
    if outcome == WIN:
        if opponent == ROCK:
            return PAPER
        return WIN_ORDER[index_opponent - 1]
    if outcome == LOSE:
        return WIN_ORDER[index_opponent + 1]


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
wins = 0
draws = 0
loses = 0
for strategy in strategies:
    opponent = SCORES.get(strategy[0])
    outcome = OUTCOMES.get(strategy[2])

    if outcome == WIN:
        wins += 1
    elif outcome == DRAW:
        draws += 1
    else: loses += 1

    me = find_play(opponent, outcome)
    local_score = determine_win(me, opponent) + me
    print(me, opponent, outcome, local_score)
    score += local_score
print({
    'WINS': wins,
    'LOSES': loses,
    'DRAWS': draws
})
print(score)
    
            