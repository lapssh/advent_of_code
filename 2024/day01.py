from os.path import split


def load(file='day01_test.txt'):
    with open(file, "rt") as f:
        lines = list(x.replace('\n', '') for x in f.readlines())
        print(lines)
        arr1, arr2 = [], []
        for item in lines:
            _ = item.split()
            arr1.append(int(_[0]))
            arr2.append(int(_[1]))
            print(arr1, arr2)

        # res = [x.split(',') for x in lines]
        res = [sorted(arr1), sorted(arr2)]
        print(f'{res=}')
        return res


def part1(src_data):
    arr1 = src_data[0]
    arr2 = src_data[1]
    arr_dist = []
    for i in range(len(arr1)):
        dist = abs(arr1[i] - arr2[i])
        print(dist)
        arr_dist.append(dist)
    result = sum(arr_dist)
    return result


def part2(src_data):
    arr1 = src_data[0]
    arr2 = src_data[1]
    arr_dist = []
    for i in range(len(arr1)):
        _ = arr1[i]
        item_cnt = arr2.count(_)
        dist = _ * item_cnt
        print(dist)
        arr_dist.append(dist)
    result = sum(arr_dist)
    return result
    return result


def show_results(answer1, answer2):
    print(f'Result part1: {answer1}')
    print(f'Result part2: {answer2}')


if __name__ == '__main__':
    # data = load()
    # data = load('day01-test.txt')
    data = load('day01-input.txt')
    part1_result = part1(data)
    part2_result = part2(data)
    show_results(part1_result, part2_result)
