from os.path import split


def load(file='day02-test.txt'):
    with (open(file, "rt") as f):
        lines = list(x.replace('\n', '') for x in f.readlines())
        # print(lines)
        res = []
        for line in lines:
            _ = line.split()
            _ = [int(x) for x in _]
            res.append(_)
        # res = [x.split(' ') for x in lines]
        # print(f'{res=}')
        return res


def part1(src_data):
    result = 0
    for line in src_data:
        # print(line)
        result += if_safe(line)
        # print(f'{line=} {result=} ')
    return result


def if_safe(line):
    first = line[0]
    second = line[1]
    line2 = line[1:]
    if first == second:
        return 0
    elif first < second:  ## возрастает
        for x in line2:
            if (x - first) in [1, 2, 3]:
                # print(f'{x=} {x-first=}')
                first = x
                continue
            else:
                # print('return 0')
                return 0
        # print(f'return1')
        return 1
    elif first > second:
        # print(f'{first} > {second}')
        for x in line2:
            # print(line2)
            if first - x in [1, 2, 3]:
                # print(f'{first - x in [1, 2, 3]=}')
                first = x
                continue
            else:
                return 0
        return 1


def if_safe2(line):
    count_errors = 0
    first = line[0]
    second = line[1]
    line2 = line[1:]
    if first == second:
        count_errors += 1
        print(f'{count_errors=}')
        if count_errors == 2: return 0
    elif first < second:  ## возрастает
        for x in line2:
            if (x - first) in [1, 2, 3]:
                # print(f'{x=} {x-first=}')
                first = x
                continue
            else:
                count_errors += 1
                print(f'{count_errors=}')
                if count_errors == 2: return 0
        # print(f'return1')
        return 1
    elif first > second:
        # print(f'{first} > {second}')
        for x in line2:
            # print(line2)
            if first - x in [1, 2, 3]:
                # print(f'{first - x in [1, 2, 3]=}')
                first = x
                continue
            else:
                count_errors += 1
                print(f'{count_errors=}')
                if count_errors == 2: return 0
        return 1
    print(f'аномалия {count_errors=} {line=}')
    return 0

def part2(src_data):
    result = 0
    for line in src_data:
        # print(line)
        result += if_safe2(line)
        # print(f'{line=} {result=} ')
    return result


def show_results(answer1, answer2):
    print(f'Result part1: {answer1}')
    print(f'Result part2: {answer2}')


if __name__ == '__main__':
    # data = load()
    # data = load('day02-test.txt')
    data = load('day02-input.txt')
    part1_result = part1(data)
    part2_result = part2(data)
    show_results(part1_result, part2_result)
