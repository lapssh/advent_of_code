def load(file='day01_test.txt'):
    with open(file, "rt") as f:
        lines = list(x.replace('\n', '') for x in f.readlines())
        # print(lines)
        for item in lines:
            _ = item.split()
        res = lines
        # res = [x.split(',') for x in lines]
        # print(f'{res=}')
        return res

def reverse_list_items(normal_list):
    reversed_list =  []
    for i in normal_list:
        reversed_list.append(i[::-1])
    return reversed_list

def part1(src_data):
    horizontal  = src_data
    horizontal = horizontal + reverse_list_items(horizontal)
    print('horizontal =', horizontal)
    vertical = []
    idx = 0

    for j, letter in enumerate(src_data[0]):
        _ = ''
        for i, line in enumerate(src_data):
            _ += line[idx]
        vertical.append(_)
        idx += 1
    vertical = vertical + reverse_list_items(vertical)
    print('vertical =', vertical)
    return 1


def part2(src_data):
    result = 1
    return result


def show_results(answer1, answer2):
    print(f'Result part1: {answer1}')
    print(f'Result part2: {answer2}')


if __name__ == '__main__':
    data = load('day04-test1.txt')
    # data = load('day-input.txt')
    part1_result = part1(data)
    part2_result = part2(data)
    show_results(part1_result, part2_result)
