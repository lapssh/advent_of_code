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
    print(f'Число: {digit=} {x1=} {x2=} ')
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
        print('сверху - пусто')
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
        print('слева - пусто')
        left = {'.'}
    # проверка справа
    print(f'{x1=} {x2=}  {r=} ')
    if x2 == len(data[y]):
        right = {'.'}
    else:
        right = data[y][x2 + 1:]
        print(f'{right=}')
    right = right[0]
    print(f'{right=}')
    right = right[0]
    res = set(left) | set(right) | set(up) | set(down)
    print(f'{res=}')
    if res != {'.'}:
        # print(f'Число {digit} прошло проверку {up=} {down=} {left=} {right=}')
        return True
    print(f'!Число {digit} НЕ ПРОШЛО проверку {up=} {down=} {left=} {right=}')
    return False

def find(data):
    nums = []
    for y, line in enumerate(data):
        digit = ''
        for x, _ in enumerate(line):
            if _.isdigit():
                print(_, 'найдено число')
                if digit == '':
                    x1 = x
                digit += _
                x2 = x
                y = y
            else:
                if not _.isdigit():
                    print(f'Надёно число: {digit=} с координатами {x1=} {x2=} {y=}')
                    nums.append(digit)
                    digit = ''
    print(nums)

def find_numbers_and_coords(data):
    print(data)
    nums = []
    for y, line in enumerate(data):
        digit = None
        for x, symbol in enumerate(line):
            # print(f'{symbol=} ')
            if symbol.isdigit():
                if digit == None:
                    digit = symbol
                    x1, y1 = x, y
                    x2 = x1
                else:
                    digit += symbol
                    x2 = x
            else:
                if digit != None:
                    print(f'Мы нашли число: {digit=}')
                    print(f'Значит координаты числа {digit=} {x1=} {x2=} {y=} ')
                    nums.append([digit, (x1, x2, y)])
                    digit = None
                    x1, x2 = 0, 0
    return nums


def part1(data):
    nums = find(data)
    # nums = find_numbers_and_coords(data)
    exit()
    true_numbers = []
    test = nums[0]

    for num in nums:
        # print(f'{test=} число: {test[0]=} x1={test[1][0]} x2={test[1][1]} y={test[1][2]}')
        if check_borders(data, num[1][0], num[1][1], num[1][2], num[0]):
            true_numbers.append(num[0])
    print(nums)
    return sum([int(x) for x in true_numbers])


# data = load()
# data = load('test.txt')  # 4361
data = load('test2.txt')
# data = build_matrix(data)
result = part1(data)
print(part1(data))  # не верно  503142(two low)
# assert result == 4361
