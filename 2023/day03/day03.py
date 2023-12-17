def load(file='input.txt'):
    with open(file, "rt") as f:
        return list(line.strip() for line in f.readlines())


def build_matrix(data):
    schematic = []
    for line in data:
        line_arr = []
        for symbol in line:
            # if symbol == '.':
            line_arr.append(symbol)
            # line_arr.append(None)
            # else:
            #     line_arr.append(symbol)
        schematic.append(line_arr)
    print(schematic)
    return schematic


def check_borders(data, x1, x2, y, digit):
    # обозначем границы проверки
    print(f'Число: {digit=} {x1=} {x2=} {y=}')
    left = {'.'}
    right = {'.'}
    if x1 > 0:
        l = x1 - 1
    else:
        l = x1
    if x2 == len(data[0]):
        r = x2
    else:
        r = x2 + 1
    if y != 0:
        up = data[y - 1][l:r + 1]
        print(f'{up=}')
    else:
        # print('сверху - пусто')
        up = {'.'}

    # проверка снизу
    if y != len(data) - 1:
        # print(f'{y1=} {len(data)=}')
        # print(data[y + 1])
        down = data[y + 1][l:r + 1]
        print(f'{down=}')
    else:
        down = {'.'}

        # проверка слева
    if x1 > 0:
        print(f'{left=}')
        if data[y][x1 - 1] == '.':
            left = {'.'}
    elif x1 == 0:
        # print('слева - пусто')
        left = {'.'}
    # проверка справа
    # print(f'{x1=} {x2=}  {r=} ')
    if x2 == len(data[y])-1:
        # print(f'{x2=} всё равно {len(data[y])=}')
        right = {'.'}
    else:
        # print(f'{x2=} всё равно {len(data[y])=}')
        # print(f'{x2+1=}')
        right = data[y][x2 + 1]
        print(f'{right=}')
    # print(f'{type(right)=} {right=} ')
    # right = right[0]
    print(f'{right=}')
    res = set(left) | set(right) | set(up) | set(down)
    print(f'{res=}')
    if res != {'.'}:
        # print(f'Число {digit} прошло проверку {up=} {down=} {left=} {right=}')
        return True
    print(f'!Число {digit} НЕ ПРОШЛО проверку {up=} {down=} {left=} {right=}')
    return False

def find(data):
    print(data)
    nums = []
    for y, line in enumerate(data):
        digit = ''
        for x, _ in enumerate(line):
            if _.isdigit():
                if digit == '':
                    x1, y1 = x, y
                digit += _
                x2 = x
            else:
                if not _.isdigit() and digit != '':
                    # print(f'Надёно число: {digit=} с координатами {x1=} {x2=} {y1=}')
                    nums.append((digit, (x1, x2, y1)))
                    digit = ''
        if digit != '':
            # print(f'Надёно число: {digit=} с координатами {x1=} {x2=} {y1=}')
            nums.append((digit, (x1, x2, y1)))
            digit = ''
        digit = ''
    return nums


def part1(data):
    nums = find(data)
    true_numbers = []

    for num in nums:
        if check_borders(data, num[1][0], num[1][1], num[1][2], num[0]):
            true_numbers.append(num[0])
    print(true_numbers)
    return sum([int(x) for x in true_numbers])


data = load()
# data = load('test.txt')  # 4361
# data = load('test2.txt')
# data = build_matrix(data)
result = part1(data)
print(part1(data))  # не верно  (two low) 504721  win -  540212
# assert result == 4361
