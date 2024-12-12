from traceback import print_tb


def load(file='day_test.txt'):
    with open(file, "rt") as f:
        lines = list(x.replace('\n', '') for x in f.readlines())
        # print(lines)
        data = []
        for item in lines:
            _ = list(item)
            # print(f'{_=}')
        _ = [int(x) for x in _]
        data.append(_)
        # res = [x.split(',') for x in lines]

        return data


def part1(src_data):
    def is_file(idx):
        if idx % 2 == 0:
            return True
        else:
            return False

    data = src_data[0]
    print(data)
    fs_map = []
    file_id = 0
    for idx,i in enumerate(data):
        # print(idx, is_file(idx))
        if is_file(idx):
            for j in range(i):
                fs_map.append(file_id)
            file_id += 1
        else:
            for j in range(i):
                fs_map.append('.')


    # print(f'{fs_map=}')
    x1 = 0
    x2 = len(fs_map)-1
    hvost = []
    len_map = len(fs_map)
    while '.' in fs_map:
        # print(f'{x1=} {x2=} {fs_map=}')
        # print(f'{fs_map[x1]=} ')
        print(fs_map[x1])
        if fs_map[x1] == '.':
            # print('первая проверка')
            # hvost.append('.')
            if fs_map[-1] == '.':
                hvost.append(fs_map.pop())
                continue
            else:
                fs_map[x1] = fs_map.pop()
        else:
            x1 += 1
    # print('end')
    # print(fs_map)
    # print(f'{len_map=}')

    # считаем контрольную сумму
    ctrl_sum = 0
    for idx, num in enumerate(fs_map):
        ctrl_sum += idx * num
    print(ctrl_sum)
    return ctrl_sum


def part2(src_data):
    return src_data


def show_results(answer1, answer2):
    print(f'Result part1: {answer1}')
    # print(f'Result part2: {answer2}')


if __name__ == '__main__':
    # data = load('day09-test1.txt')
    # data = load('day09-test2.txt')
    data = load('day09-input.txt')
    part1_result = part1(data)
    part2_result = part2(data)
    show_results(part1_result, part2_result)
