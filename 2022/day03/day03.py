def load_data(filename):
    with open(filename) as f:
        data = f.readlines()
    clean_data = [x.strip() for x in data]
    return clean_data


def split_rucksack(items):
    # print((len(items)//2))
    item1 = items[0:(len(items)//2)]
    item2 = items[len(items)//2:]
    # print(f'{item1=}, {item2=}')
    return item1, item2


def find_error(data):
    score = 0
    for rucksack in data:
        item1, item2 = split_rucksack(rucksack)
        item1 = set(item1)
        item2 = set(item2)
        item = item1 & item2
        item = list(item)[0]
        # print(item)
        letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        # enum_letters = list(enumerate(letters, 1))
        # print(enum_letters)
        inx_letter = letters.index(item)+1
        # print(f'{inx_letter=}')
        # print(f'{letters.index("Z")=}')
        score += inx_letter
    return score


def part2(data):
    """Разобьем все строки в списке на блоки по 3 шт"""
    tripple_data = []
    score = 0
    while len(data) > 0:
        # tmp = data.pop(0), data.pop(0), data.pop(0)
        tmp = set(data.pop(0)), set(data.pop(0)), set(data.pop(0))
        # print(tmp)
        result = list(tmp[0] & tmp[1] & tmp[2])[0]
        # print('пересечение: ', result)
        letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        inx_letter = letters.index(result) + 1
        # print(inx_letter)
        score += inx_letter
    return score
        # tripple_data.append(data.pop(0))

# filename = 'test.txt'
filename = 'input.txt'
data = load_data(filename)
# print(data)
# print(split_rucksack(data[0]))
print('part1 result:', find_error(data))
# print(data)
print('part2 result:', part2(data))