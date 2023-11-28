from typing import Sequence


def load(file):
    with open(file, "rt") as f:
        return list(int(x) for x in f.readline().split(','))


def run_program():
    for command in range(0, len(data), 4):
        operator = data[command]
        idx_first = data[command + 1]
        idx_second = data[command + 2]
        idx_result = data[command + 3]
        # print('индексы', operator, idx_first, idx_second, idx_result)
        if operator == 1:
            calc_sum(idx_first, idx_second, idx_result)
        elif operator == 2:
            calc_multi(idx_first, idx_second, idx_result)
        elif operator == 99:
            break
    return data
    # print(data[command], command)


def calc_sum(idx_first, idx_second, idx_result):
    # print(f'+ {idx_first=} {data[idx_first]=} + {idx_second=} {data[idx_second]=}')
    data[idx_result] = data[idx_first] + data[idx_second]
    # print(f'+ {a=} {data[a]=} + {b=} {data[b]=}')
    # print(f'+ {a=} {data[a]=} + {b=} {data[b]=}')
    # data[result] = data[a] + data[b]


def calc_multi(a, b, result):
    data[result] = data[a] * data[b]


def part1():
    run_program()


if __name__ == '__main__':
    data = load('input.txt')
    data[1] = 12
    data[2] = 2
    # data = [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]
    run_program()
    print(f"Part 1 : {data[0]}")
    # print(data)
