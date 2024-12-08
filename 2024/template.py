def load(file='day01_test.txt'):
    with open(file, "rt") as f:
        lines = list(x.replace('\n', '') for x in f.readlines())
        print(lines)
        labirint = []
        for item in lines:
            _ = list(item)
            print(_)
        labirint.append(_)

        # res = [x.split(',') for x in lines]
        print(f'{labirint=}')
        for line in labirint:
            print(line)
        return labirint


def part1(src_data):
    return result


def part2(src_data):
    return result


def show_results(answer1, answer2):
    print(f'Result part1: {answer1}')
    print(f'Result part2: {answer2}')


if __name__ == '__main__':
    data = load('day06-test.txt')
    # data = load('day06-input.txt')
    part1_result = part1(data)
    part2_result = part2(data)
    show_results(part1_result, part2_result)
