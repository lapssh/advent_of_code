def load_data(filename='test.txt'):
    with open(filename) as f:
        data = list(f.readline().strip())
    return data


def calc_way(data):
    way = []
    for i in data:
        if i == 'L' and 'R' in way:
            index = way.index('R')
            way.pop(index)
        elif i == 'R' and 'L' in way:
            index = way.index('L')
            way.pop(index)
        elif i == 'U' and 'D' in way:
            index = way.index('D')
            way.pop(index)
        elif i == 'D' and 'U' in way:
            index = way.index('U')
            way.pop(index)
        else:
            way.append(i)

    way.sort()
    way = ''.join(way)
    return way


data = load_data('advent_6.test.txt')
print(calc_way(data))
