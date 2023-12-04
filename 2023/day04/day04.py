def load(file='input.txt'):
    with open(file, "rt") as f:
        return list(line.strip() for line in f.readlines())


def parse_cards(cards):
    data = {}
    for card in cards:
        left, right = card.split('|')
        card_number = int(left.split(':')[0].split()[1])
        win_nums = [int(x) for x in (left.split(':')[1].split())]
        pool_nums = [int(x) for x in right.split()]
        # print(f'{left=} {right=} {card_number=} {win_nums=}')
        # print(f'{pool_nums=}')
        data[card_number] = {
            'win_nums': win_nums,
            'pool_nums': pool_nums,
        }
    return data


def calc_score_for_card(win_nums, pool_nums):
    print(win_nums, pool_nums)
    res = [x for x in win_nums if x in pool_nums]
    print(f'{res=}')
    score = 0
    if len(res) > 0:
        score = 1
        for i in range(len(res)-1):
            score = score * 2
    print(f'{score=}')
    return score
def calc_total_score_all_cards(cards):
    total = 0
    print(cards)
    for card in range(1, len(cards)+1):
        print(cards[card])
        print(cards[card]['win_nums'])
        card_score = calc_score_for_card(cards[card]['win_nums'], cards[card]['pool_nums'])
        total += card_score
    return total

def part1(data):
    cards = parse_cards(data)
    result = calc_total_score_all_cards(cards)
    return result


# data = load(file='test.txt')
data = load()
print(data)
result1 = part1(data)
print('part1:', result1)
