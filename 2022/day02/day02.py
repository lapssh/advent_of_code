filename = 'input.txt'
# filename = 'test.txt'
data = ['A Y', 'B X', 'C Z']
def load_data(filename):
    data = []
    with open(filename) as f:
        lines = f.readlines()
        for line in lines:
            if line != '\n':
                data.append(line.strip())
        return data


def calc_match_score(match):
    score = 0
    elf = match[0]
    santa = match[2]
    print(elf, santa)
    if elf == 'A':
        if santa == 'X':
            score = 4
        elif santa == 'Y':
            score = 8
        elif santa == 'Z':
            score = 3
    if elf == 'B':
        if santa == 'X':
            score = 1
        elif santa == 'Y':
            score = 5
        elif santa == 'Z':
            score = 9
    if elf == 'C':
        if santa == 'X':
            score = 7
        elif santa == 'Y':
            score = 2
        elif santa == 'Z':
            score = 6
    print(score)
    return score


def calc_match_score_for_part2(match):
    score = 0
    elf = match[0]
    result = match[2]
    print(elf, result)
    # A - Rock (1)    B - Paper (2)     C - Scissors
    # X - lose      Y - draw        Z - win
    if elf == 'A':
        if result == 'X':
            score = 3
        elif result == 'Y':
            score = 4
        elif result == 'Z':
            score = 8
    if elf == 'B':
        if result == 'X':
            score = 1
        elif result == 'Y':
            score = 5
        elif result == 'Z':
            score = 9
    if elf == 'C':
        if result == 'X':
            score = 2
        elif result == 'Y':
            score = 6
        elif result == 'Z':
            score = 7
    print(score)
    return score


def part1(data):
    # A - Rock (1)    B - Paper (2)     C - Scissors
    # X - Rock (1)    Y - Paper (2)     Z - Scissors
    # Win - 6       Draw - 3        Lose - 0
    score = 0
    for match in data:
        score += calc_match_score(match)
    return score


def part2(data):
    # A - Rock (1)    B - Paper (2)     C - Scissors
    # X - Rock (1)    Y - Paper (2)     Z - Scissors
    # Win - 6       Draw - 3        Lose - 0
    score = 0
    for match in data:
        score += calc_match_score_for_part2(match)
    return score


data = load_data(filename)
print(data)
print('part1 resut = ', part1(data))
print('part2 resut = ', part2(data))
