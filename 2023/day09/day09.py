data = open('input.txt').readlines()
# data = open('test.txt').readlines()
# data = open('test2.txt').readlines()
data = [[int(a) for a in line.strip().split()] for line in data]


def get_sequence(arr):
    result = []
    for idx, num2 in enumerate(arr):
        if idx == 0:
            num1 = num2
        else:
            result.append(num2-num1)
            num1 = num2
    return result


def get_shift_arr(data):
    shift_arr = []
    # вычисляем последовательность для каждой строки
    for arr in data:
        line = arr
        _ = []
        while True:
            shift = get_sequence(line)
            # Если элементы не равны 0, то сохраняем результат в массиве сдвигов
            if set(shift) != {0}:
                _.append(shift)
                line = shift
            else:
                break
        shift_arr.append(_)
    return (shift_arr)

def calc_next_value(idx, shift_arr):
    shift_arr = shift_arr[::-1]
    # print(idx, data[idx], shift_arr)
    _ = 0
    for shift in shift_arr:
        next = shift[-1] + _
        _ = next
        # print(f'{next=}')
    res = data[idx][-1] + next
    # print(f'{data[idx][-1]} + {next} = {res}')
    return res


def calc_prev_value(idx, shift_arr):
    shift_arr = shift_arr[::-1]
    # print(idx, data[idx], shift_arr)
    _ = 0
    for shift in shift_arr:
        prev = shift[0] - _
        _ = prev
        # print(f'{prev=}')
    res = data[idx][0] - prev
    # print(f'{data[idx][-1]} - {prev} = {res}')
    return res


def part1(data):
    vals = []
    shift_arr = get_shift_arr(data)
    for idx, val in enumerate(shift_arr):
        next_value = calc_next_value(idx, val)
        vals.append(next_value)
    return (sum(vals))

def part2(data):
    vals = []
    shift_arr = get_shift_arr(data)
    for idx, val in enumerate(shift_arr):
        prev_value = calc_prev_value(idx, val)
        vals.append(prev_value)
    return (sum(vals))


print(f'Part1: {part1(data)}')
print(f'Part2: {part2(data)}')
