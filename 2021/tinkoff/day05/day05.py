def load_data(filename='test.txt'):
    with open(filename) as f:
        data = f.readline().strip()
        return data


def calc_code(data):
    _ = data
    _ = _.replace('222', 'c')
    _ = _.replace('22', 'b')
    _ = _.replace('2', 'a')
    _ = _.replace('333', 'f')
    _ = _.replace('33', 'e')
    _ = _.replace('3', 'd')
    _ = _.replace('444', 'i')
    _ = _.replace('44', 'h')
    _ = _.replace('4', 'g')
    _ = _.replace('555', 'l')
    _ = _.replace('55', 'k')
    _ = _.replace('5', 'j')
    _ = _.replace('666', 'o')
    _ = _.replace('66', 'n')
    _ = _.replace('6', 'm')
    _ = _.replace('7777', 's')
    _ = _.replace('777', 'r')
    _ = _.replace('77', 'q')
    _ = _.replace('7', 'p')
    _ = _.replace('888', 'v')
    _ = _.replace('88', 'u')
    _ = _.replace('8', 't')
    _ = _.replace('9999', 'z')
    _ = _.replace('999', 'y')
    _ = _.replace('99', 'x')
    _ = _.replace('9', 'w')
    return _


def new_calc_code(data):
    new_code = []
    count = 1
    for letter in data:
        if new_code == []:
            new_code.append([letter, 1])
        elif letter == new_code[-1][0]:
            new_code[-1][1] += 1
        else:
            new_code.append([letter, 1])
    return new_code


def decode_data(data):
    s = ''
    res = []
    for i in data:
        if i[1] == 3:
            # print(i)
            res.append((i[0], (1, 2), (2, 1)))
        elif i[1] == 4:
            res.append((i[0], (1, 3), (3, 1), (2, 2)))
        elif i[1] == 5:
            res.append((i[0], (2, 3), (3, 2), (1, 4), (4, 1)))
        elif i[1] == 2:
            res.append((i[0], 2))
        else:
            res.append((i[0], 1))
    return res
# data = load_data()
data = load_data('advent_8.test.txt')
data2 = new_calc_code(data)
data3 = decode_data(data2)
print(data3)
res = ''
codes = {'2': 'ABC', '3': 'DEF', '4': 'GHI', '5': 'JKL', '6': 'MNO', '7': 'PQRS', '8': 'TUV', '9': 'WXYZ'}
for i in data3:
    # print(i, len(i),codes[i[0]])
    if len(i) == 2:
        pass
        # print(codes[i[0]][i[1]-1])
    else:
        print(i)
        num = i[0]
        vars = i[1:]
        for var in vars:
            print(f'Для варианта {var=} символа {num}')
            mask = codes[num]
            print(f'{mask=} {var[0]=} {var[1]=}')
            num1, num2 = var[0]-1, var[1]-1
            print(f'{num} {mask=} {mask[num1]}')


        # tmp = i
        # sym = i[0]
        # tmp = tmp[1:]
        # for j in tmp:
        #     print(codes[sym][j[0]-1], codes[sym][j[1]-1])


