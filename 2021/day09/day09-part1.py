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
    last_point = len(lines[0])-1
    print(f'{first_row=} {last_row=} {last_point=}')
    for row in range(0, last_row):
        # print(lines[row])
        for index in range(last_point+1):
            point = lines[row][index]
            # case for first row
            if row == first_row:
                print('первая строка')
                # case for first item
                if index == first_point:
                    print('первый итем')
                    if (point < lines[row][index+1] and point < lines[row+1][index]):
                        res.append(point)
                # case for last item
                elif index == last_point:
                    print('последний итем')
                    if (point < lines[row][index-1] and point < lines[row+1][index]):
                        res.append(point)
                else:
                    # case for other
                    print('остальное')
                    if (point < lines[row][index-1] and point < lines[row][index+1] and point < lines[row+1][index]):
                        res.append(point)
            elif row == last_row-1:
                print('последняя строка')
                # case for first item
                if index == first_point:
                    print('первый итем')
                    if (point < lines[row][index+1] and point < lines[row-1][index]):
                        res.append(point)
                # case for last item
                elif index == last_point:
                    print('последний итем')
                    if (point < lines[row][index-1] and point < lines[row-1][index]):
                        res.append(point)
                else:
                    # case for other
                    print('остальное')
                    if (point < lines[row][index-1] and point < lines[row][index+1] and point < lines[row-1][index]):
                        res.append(point)
            else:
                # case for first item
                if index == first_point:
                    print('первый итем')
                    if (point < lines[row][index+1] and point < lines[row-1][index] and point < lines[row+1][index]):
                        res.append(point)
                # case for last item
                elif index == last_point:
                    print('последний итем')
                    if (point < lines[row][index-1] and point < lines[row-1][index] and point < lines[row+1][index]):
                        res.append(point)
                else:
                    # case for other
                    print('остальное')
                    if (point < lines[row][index - 1] and point < lines[row][index + 1] and point < lines[row - 1][index] and point < lines[row + 1][index]):
                        res.append(point)


            # print(f'{index=} {point=}')
    # for row in range(0, len(lines)):
    #     for point in range(0, len(lines[row])):
    #         print(lines[row][point], end='')
    #         # case for first row
    #         if row == 0:
    #             # case for firs num
    #             if point == 0:
    #                 if (lines[row][point] < lines[row][point+1]) and (lines[row][point] < lines[row+1][point]):
    #                     print('строка 0 point =', lines[row][point])
    #                     res.append(lines[row][point])
    #             elif point == len(lines[row]):
    #                 print('последний')
    #             else:
    #                 if (lines[row][point] < lines[row][point-1]) and (lines[row][point] < lines[row][point+1]) and  (lines[row+1][point] < lines[row][point]):
    #                     res.append(lines[row][point])


    return res

# filename = 'test-input.txt'
filename = 'input.txt'
lines = load_list_of_lines(filename)
res_part_one = find_lowest_points(lines)
print(res_part_one)
res_with_risk_level = sum([x+1 for x in res_part_one])
print(res_with_risk_level)