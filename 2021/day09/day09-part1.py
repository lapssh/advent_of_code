def load_list_of_lines(filename):
    with open(filename) as f:
        numbers = []
        lines = f.readlines()
        lines = [line.strip() for line in lines]
        row = []
        for line in lines:
            for num in line:
                row.append(int(num))
            numbers.append(row)
            row = []
        print(numbers)
        return numbers


def find_lowest_points(lines):
    res = []
    first_row, first_point = 0, 0
    last_row = len(lines)
    last_point = len(lines[0]) - 1
    print(f'{first_row=} {last_row=} {last_point=}')
    for row in range(0, last_row):
        for index in range(last_point + 1):
            point = lines[row][index]
            if row == first_row:
                # print('первая строка')
                # case for first item
                if index == first_point:
                    # print('первый итем')
                    if point < lines[row][index + 1] and point < lines[row + 1][index]:
                        res.append(point)
                # case for last item
                elif index == last_point:
                    # print('последний итем')
                    if point < lines[row][index - 1] and point < lines[row + 1][index]:
                        res.append(point)
                else:
                    # case for other
                    # print('остальное')
                    if point < lines[row][index - 1] and point < lines[row][index + 1] and point < lines[row + 1][
                        index]:
                        res.append(point)
            elif row == last_row - 1:
                # print('последняя строка')
                # case for first item
                if index == first_point:
                    # print('первый итем')
                    if point < lines[row][index + 1] and point < lines[row - 1][index]:
                        res.append(point)
                # case for last item
                elif index == last_point:
                    # print('последний итем')
                    if point < lines[row][index - 1] and point < lines[row - 1][index]:
                        res.append(point)
                else:
                    # case for other
                    # print('остальное')
                    if point < lines[row][index - 1] and point < lines[row][index + 1] and point < lines[row - 1][
                        index]:
                        res.append(point)
            else:
                # case for first item
                if index == first_point:
                    # print('первый итем')
                    if (point < lines[row][index + 1] and point < lines[row - 1][index] and point < lines[row + 1][
                        index]):
                        res.append(point)
                # case for last item
                elif index == last_point:
                    # print('последний итем')
                    if (point < lines[row][index - 1] and point < lines[row - 1][index] and point < lines[row + 1][
                        index]):
                        res.append(point)
                else:
                    # case for other
                    # print('остальное')
                    if (point < lines[row][index - 1] and point < lines[row][index + 1] and point < lines[row - 1][
                        index] and point < lines[row + 1][index]):
                        res.append(point)

    return res


filename = 'test-input.txt'
# filename = 'input.txt'
lines = load_list_of_lines(filename)


# res_part_one = find_lowest_points(lines)
# print(res_part_one)
# res_with_risk_level = sum([x + 1 for x in res_part_one])
# print(res_with_risk_level)



def part_two(data):
    max_y = len(data)
    max_x = len(data[0])
    pool_coordinates = []
    print(f'{max_x=} {max_y=}')
    start_point = (2, 1)
    pool_coordinates.append(start_point)
    x = 2
    y = 1

    while True:
        print(pool_coordinates)
        try:
            # пробуем вправо
            # проверим границу x
            print(f'{y=} {len(data)-1=}')
            print(f'{x=}')
            if x != len(data[0])-1:
                if (data[y][x + 1] and data[y][x + 1] != 9) and (x + 1, y) not in pool_coordinates:
                    x += 1
                    print(f'{x=} {y=} {data[y][x]=}')
                    pool_coordinates.append((x, y))
            # пробуем вниз
            # проверим нижнюю границу
            if y != len(data)-1:
                # print('проверку нижней границы прошли')
                    # print(f'{y=} {max_y=}')
                if (data[y + 1][x] and data[y + 1][x] != 9) and (x, y + 1) not in pool_coordinates:
                    y += 1
                    print(f'{x=} {y=}  {data[y][x]=}')
                    pool_coordinates.append((x, y))
            # пробуем влево
            # проверим левую границу
            if x != 0:
                if (data[y][x - 1] and data[y][x - 1] != 9) and (x - 1, y):
                    x -= 1
                    print(f'{x=} {y=} {data[y][x]=}')
                    if (x, y) not in pool_coordinates:
                        pool_coordinates.append((x, y))
            # пробуем вверх
            # проверим потолок
            if y != 0:
                if data[y - 1][x] and data[y - 1][x] != 9:
                    # and (x, y-1):
                    y -= 1
                    print(f'{x=} {y=} {data[y][x]=}')
                    if (x, y) not in pool_coordinates:
                        pool_coordinates.append((x, y))
            else:
                print('зациклилось')
                if x == 2 and y == 1:
                    print('приплыли')
                    exit()
        except Exception as error:
            print(f'{x=} {y=} {data[y][x]=} ')
            print('УПС! НЕЖДАНЧИК!', error)
            exit()
        print('hz')
        print(f'{x=} {y=} {data[y][x]=} ')
        print(pool_coordinates)
        exit()

    # print('Pool complite!')
    # print(pool_coordinates)
    return data



""" Part two """
print(lines)
part_two(lines)
