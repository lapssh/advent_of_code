def load(file='day01_test.txt'):
    with open(file, "rt") as f:
        lines = list(x.replace('\n', '') for x in f.readlines())
        print(lines)
        arr1, arr2 = [], []
        for item in lines:
            _ = item.split()

        # res = [x.split(',') for x in lines]
        res = [sorted(arr1), sorted(arr2)]
        print(f'{res=}')
        return res


def part1(src_data):
    return result


def part2(src_data):
    return result


def show_results(answer1, answer2):
    print(f'Result part1: {answer1}')
    print(f'Result part2: {answer2}')


if __name__ == '__main__':
    data = load('day-test.txt')
    # data = load('day-input.txt')
    part1_result = part1(data)
    part2_result = part2(data)
    show_results(part1_result, part2_result)
