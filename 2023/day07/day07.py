def load(file='input.txt'):
    with open(file, "rt") as f:
        return list(line.strip() for line in f.readlines())

ranked_cards = []

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
    # проверяем тройку
    elif len(set(card)) <= 4:
        _ = list(card)
        _.sort()
        # print(_)
        if _[0] == _[2] or _[2] == _[4]:
            # print('Tree', _)
            return 'Three'
        elif len(set(card)) == 3:
            return 'TwoPare'
        else:
            print('Two', card)
            return 'Two'
    else:
        print('Two', card)
        return 'Two'
    # проверяем пару



def card_is_higher(card, _card):
    # print(f'Сравниваем {card=} и {_card=}')
    type_card1 = get_card_type(card)
    if type_card1 == None:
        print(card, type_card1, 'Ошибка')
        exit()
    print(type_card1, card)
    type_card2 = get_card_type(_card)
def insert_card(card):
    # если карта первая - просто добавляем
    if ranked_cards == []:
        ranked_cards.append(card.split())
    else:
        for _card in ranked_cards:
            if card_is_higher(card.split()[0], _card[0]):
                pass
               # print(f'{card=} Больше, чем {_card=}')



def part1(data):
    for card in data:
        insert_card(card)
    print(ranked_cards)

# data = load()
data = load('test.txt')
print(data)

print(part1(data))
