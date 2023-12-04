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
    # print(win_nums, pool_nums)
    res = [x for x in win_nums if x in pool_nums]
    # print(f'{res=}')
    score = 0
    if len(res) > 0:
        score = 1
        for i in range(len(res) - 1):
            score = score * 2
    # print(f'{score=}')
    return score


def calc_total_score_all_cards(cards):
    total = 0
    # print(cards)
    for card in range(1, len(cards) + 1):
        # print(cards[card])
        # print(cards[card]['win_nums'])
        card_score = calc_score_for_card(cards[card]['win_nums'], cards[card]['pool_nums'])
        total += card_score
    return total


def calc_score_for_scratch_card(win_nums, pool_nums, card_num):
    """
    возвращает номера Scratch-карт
    """
    # print(win_nums, pool_nums)
    cards = []
    win_cards = {}
    flag = False
    # if win_nums != []:
    #     cards.append(card_num)
    for card_number, val in enumerate(win_nums):
        if val in pool_nums:
            print(win_cards)
            # cards.append(card_number + 1)
    # print(cards)
    return cards


def get_count_card(card_num):
    """
    Возвращает колличество следующих карт по числу совпадений
    """
    win_nums, pool_nums = cards[card_num]['win_nums'], cards[card_num]['pool_nums']
    # print(win_nums, pool_nums)
    card_count = 0
    print('выигрышные карты: ', end=' ')
    for card_number, val in enumerate(win_nums):
        if val in pool_nums:
            card_count += 1
            print(card_count, end=' ')
    return card_count
    exit()
    scratch_cards = calc_score_for_scratch_card(win_nums, pool_nums, card_num)
    # print(scratch_cards)
    return scratch_cards

def card_is_win(win_nums, pool_nums, card_num):
    for i in win_nums:
        if i in pool_nums:
            return True
    return False


def part1(data):
    cards = parse_cards(data)
    result = calc_total_score_all_cards(cards)
    return result


def part2(data):
    cards = parse_cards(data)
    win_cards = {}
    for i in cards:
        win_cards[i] = 0
    # print(win_cards)
    result = 0
    for card in range(1, len(cards) + 1):
        print(f'Карта с номером {card}', end=' ')
        # Определяем выигрышная ли это карта
        if card_is_win(cards[card]['win_nums'], cards[card]['pool_nums'], card):
            print(' - Выигрышная')
            win_cards[card] += 1
            # Если карта выигрышная - получаем колличество карт дальше
            next_card_count = get_count_card(card)
            print('необходимо добавить к выигрышу ', next_card_count, 'карты.')
            currernt_card = card
            for el in range(1, next_card_count+1):
                print(f'Добавляем Win-карту {el+currernt_card}')
                win_cards[el+currernt_card] += 1
            print(f'{win_cards=}')
        # print(scratch_cards)
        # for i in scratch_cards:
            # print(i)
            # result += i
    print('карты', win_cards)
    # print(f'{result=}')

def part2_adv():
    data = open("input.txt").read().splitlines()
    data = [x.split('|') for x in data]

    win = [x[0][10:] for x in data]
    win = [x.strip().split() for x in win]

    elf = [x[1] for x in data]
    elf = [x.strip().split() for x in elf]

    dups = []
    for _ in elf:
        dups.append(1)

    for i, card in enumerate(elf):
        hitcount = 0
        for num in card:
            if num in win[i]:
                hitcount += 1
                dups[i + hitcount] += dups[i]
    return sum(dups)

# data = load(file='test.txt')
data = load()
# print(data)
cards = parse_cards(data)
result1 = part1(data)
result2 = part2(data)
print('part1:', result1)
print('part2:', part2_adv())
