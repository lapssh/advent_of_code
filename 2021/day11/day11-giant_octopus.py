def load_data(filename='test-input.txt'):
    with open(filename) as f:
        data = f.readlines()
        data = [x.strip() for x in data]
        data2 = []
        for el in data:
            tmp = list(el)
            tmp = [int(x) for x in tmp]
            data2.append(tmp)
    return data2


def print_octopus(data):
    for i, x in enumerate(data):
        # print(f'{i=} {x=}')
        for j, y in enumerate(x):
            # print(f'{j=} {y=}')
            print(data[i][j], end='  ')
        print()


def calc_flashes(data, steps=1):
    for i, x in enumerate(data):
        for j, y in enumerate(x):
            # если 9 - взрываем всех
            if data[i][j] == 9:
                data[i][j] = 0
                # взрываем LT
                if i-1 >= 0 and j-1 >=0:
                    data[i-1][j-1] += 1

            elif data[i][j] ==0:
                continue
            else:
                data[i][j] += 1
            # меняем
    return data


octopuses = load_data('test-input2.txt')
print_octopus(octopuses)
result = calc_flashes(octopuses)
print(14 * '+ ')
print_octopus(result)
