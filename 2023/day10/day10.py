data = open('test1.txt').readlines()
data = [x.strip() for x in data]
print(data)


def find_s_coord():
    for y, line in enumerate(data):
        for x, val in enumerate(line):
            if val == 'S':
                s_x, s_y = x, y
    return s_x, s_y

def possible_directions(x, y):
    pd = []
    print(f'{x=} {y=}')
    if y > 0:
        if data[y-1][x] in ('|', '7', 'F'):
            pd.append((x, y-1, 'down'))
    if x > 0:
        if data[y][x-1] in ('-', 'L', 'F'):
            pd.append((x-1, y, 'right'))
    if x < len(data[0])-1:
        if data[y][x+1] in ('-', 'J', '7'):
            pd.append((x+1, y, 'left'))
    if y < len(data)-1:
        if data[y+1][x] in ('|', 'L', 'J'):
            pd.append((x, y+1, 'up'))
    return pd[0], pd[1]

def lets_go(pd):
    position = 0
    x, y = pd[0], pd[1]
    arrow = pd[2]
    while position != 'S':
        position = data[y][x]
        print(position)
        if position == '|':
            if arrow == 'down':
                 
def part1():
    # ищем координаты стартовой позиции S
    s_x, s_y = find_s_coord()
    # определяем возможные направления
    pd = possible_directions(s_x, s_y)
    # отправляемся по первой линии пока не встретим S
    number_of_steps = lets_go(pd[0])
    print(number_of_steps)




print(f'Part1: {part1()}')