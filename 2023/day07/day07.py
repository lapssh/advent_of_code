def load(file='input.txt'):
    with open(file, "rt") as f:
        return list(line.strip() for line in f.readlines())

ranked_cards = []
type_ranks = {
    'High': 1,
    'Pare': 2,
    'TwoPare': 3,
    'Three': 4,
    'FullHouse': 5,
    'Care': 6,
    'Five': 7,
}

type_cards = {
    'A': 13,
    'K': 12,
    'Q': 11,
    'J': 10,
    'T': 9,
    '9': 8,
    '8': 7,
    '7': 6,
    '6': 5,
    '5': 4,
    '4': 3,
    '3': 2,
    '2': 1,
}

def get_card_type(card):
    # print(card)
    card = card.split()[0]
    # print('Определяем раздачу:', card)
    # card = list(card)
    # 5-одинаковых
    if len(set(card)) == 1:
        # print(f'{card=} === !!!FIVE!!!')
        return ('Five')
    elif len(set(card)) == 5:
        # print(f'{card=} === High Card')
        return ('High')
    # проверям Full House и Каре
    elif len(set(card)) == 2:
        _ = list(card)
        _.sort()
        if _[0] == _[3] or _[1] == _[4]:
            # print('Care', _)
            return 'Care'
        else:
            # print('Full House', _)
            return 'FullHouse'
    # проверяем пару
    elif len(set(card)) == 4:
        # print('Pare')
        return 'Pare'
    # проверяем тройку
    elif len(set(card)) <= 4:
        _ = list(card)
        _.sort()
        # print(_)
        if _[0] == _[2] or _[2] == _[4]:
            # print('Tree', _)
            return 'Three'
        elif len(set(card)) == 3:
            # print('TwoPare', card)
            return 'TwoPare'
        else:
            # print('TwoPare', card)
            return 'TwoPare'



def get_stronger(card, _card):
    # print(f'Равные карты {card=} {_card=}')
    for symbol in range(len(card)):
        if type_cards[card[symbol]] > type_cards[_card[symbol]]:
            # print(f' {card=} > {_card=} {card[symbol]} > {_card[symbol]}')
            return '>'
        elif type_cards[card[symbol]] < type_cards[_card[symbol]]:
            # print(f' {card=} < {_card=} {card[symbol]} < {_card[symbol]}')
            return '<'


def card_is_higher(card, _card):
    # print(f'Сравниваем {card=} и {_card=}')
    type_card1 = get_card_type(card)
    if type_card1 == None:
        print(card, type_card1, _card, 'Ошибка')
        exit()
    # print(type_card1, card)
    type_card2 = get_card_type(_card)
    # проверяем чья раздача лучше
    if type_ranks[type_card1] == type_ranks[type_card2]:
        # Необходимо определить старшую букву
        return(get_stronger(card, _card))
        # print(f'{type_ranks[type_card1]} = {type_ranks[type_card2]}')
        return '>'
    if type_ranks[type_card1] > type_ranks[type_card2]:
        # print(f'{type_ranks[type_card1]} > {type_ranks[type_card2]}')
        return '>'
    elif type_ranks[type_card1] < type_ranks[type_card2]:
        # print(f'{type_ranks[type_card1]} < {type_ranks[type_card2]}')
        return '<'
    else:
        print('Карты равны')
        exit()
        return None
def insert_card(card):
    # если карта первая - просто добавляем
    if ranked_cards == []:
        ranked_cards.append(card.split())
    else:
        idx = 0
        while True:
            if idx == len(ranked_cards):
                # print(f'КОНЕЦ Шаг {idx} {card=} ')
                ranked_cards.append(card.split())
                break
            card2 = ranked_cards[idx]
            ans = card_is_higher(card.split()[0], card2[0])
            if ans == '<':
                # ranked_cards.insert(idx, card.split())
                # print(f'Шаг {idx} {card=} {ans=} {card2=}')
                ranked_cards.insert(idx, card.split())
                break
            elif ans == '>':
                # print(f'Шаг {idx} {card=} {ans=} {card2=}')
                idx += 1

def calc_bid():
    total = 0
    for mult, card in enumerate(ranked_cards):
        bid = int(card[1])
        total += (mult + 1) * bid
        # print(f'{bid=}  {mult+1} {total=}')
    return total


def part1(data):
    for card in data:
        insert_card(card)
    print(ranked_cards)
    return calc_bid()


data = load()
# data = load('test.txt')
# data = load('test2.txt')
print(data)

print('Part1 result:', part1(data)) # 250597026 - error (too high)
