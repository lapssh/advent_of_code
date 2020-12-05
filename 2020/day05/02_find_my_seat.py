def get_input(filename):
    with open(filename) as f:
        data = f.readlines()
    data2 = []
    for item in data:
        data2.append(item.replace('\n', ''))
    return data2


def get_row(row_code):
    seat_row = [0, 127]
    for i in range(7):
        if row_code[i] == 'F':
            min_ = seat_row[0]
            max_ = (seat_row[0] + seat_row[1]) // 2
            seat_row[0], seat_row[1] = min_, max_
            # print(i, '-я итерация', seat_row)
        else:
            min_ = (seat_row[0] + seat_row[1]) // 2 + 1
            max_ = seat_row[1]
            seat_row[0], seat_row[1] = min_, max_
            # print(i, '-я итерация', seat_row)

    return seat_row


def get_col(col_code):
    seat_col = [0, 7]
    for i in range(3):
        if col_code[i] == 'L':
            min_ = seat_col[0]
            max_ = (seat_col[0] + seat_col[1]) // 2
            seat_col[0], seat_col[1] = min_, max_
            # print(i, '-я итерация', seat_col)
        else:
            min_ = (seat_col[0] + seat_col[1]) // 2 + 1
            max_ = seat_col[1]
            seat_col[0], seat_col[1] = min_, max_
            # print(i, '-я итерация', seat_col)
    return seat_col


def find_seat(boarding_code):
    row = get_row(boarding_code[0:7])
    col = get_col(boarding_code[-3:])
    # print(str(row[0]) + '  ' + str(col[0]))
    seat_id = row[0] * 8 + col[0]
    return seat_id


def test_find_seat(boarding_code, answer):
    print('Получен талон', boarding_code)
    print('Расчетный ID:', find_seat(boarding_code))
    print('Проверочный ID:', answer)


def get_max_seat_id(data):
    max_seat = 0
    for x in data:
        seat = find_seat(x)
        if max_seat < seat:
            max_seat = seat
    return max_seat


def get_min_seat_id(data):
    min_seat = 1000
    for x in data:
        seat = find_seat(x)
        if min_seat > seat:
            min_seat = seat
    return min_seat


def get_all_seat_id(data):
    seat_list = []
    for x in data:
        seat = find_seat(x)
        seat_list.append(seat)
    return seat_list


def get_my_seat(all_seat_id):
    my_seat_id = 0
    print(all_seat_id)
    return my_seat_id


data = get_input('input.txt')
# 128 rows (0-127)  F - lower half 0-63     B - upper half 64-127
# 8 column (0-7)    L - lower half 0-3      R - upper half 4-7
example = 'FBFBBFFRLR'  # right answer = 44 row and 5 column | Solution: 44 * 8 + 5 = 357
print(find_seat(example))
test_find_seat('BFFFBBFRRR', 567)
test_find_seat('FFFBBBFRRR', 119)
test_find_seat('BBFFBBFRLL', 820)
print('Highest seat ID=', get_max_seat_id(data))
all_seat_id = get_all_seat_id(data)
# print(get_my_seat(all_seat_id))
min_seat=get_min_seat_id(data)
max_seat=get_max_seat_id(data)
print('минимальное место', min_seat)
print('мaксимальное место', max_seat)

# сгенерируем множество min-max
set_of_seats = {seat for seat in range(min_seat,max_seat+1)}
real_set_of_seats = set(all_seat_id)
# print(set_of_seats)
hidden_seats = set_of_seats - real_set_of_seats
print(hidden_seats)
