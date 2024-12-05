def load(file='day05_test.txt'):
    with open(file, "rt") as f:
        lines = list(x.replace('\n', '') for x in f.readlines())
        print(lines)
        idx = lines.index('')
        rules = lines[:21]
        print(f'{rules=}')
        pages = lines[22:]
        print(f'{pages=}')



        return rules, pages


def part1(src_data):
    rules, pages = src_data
    return 1


def part2(src_data):
    return result


def show_results(answer1, answer2):
    print(f'Result part1: {answer1}')
    print(f'Result part2: {answer2}')


if __name__ == '__main__':
    data = load('day05-test.txt')
    # data = load('day-input.txt')
    part1_result = part1(data)
    part2_result = part2(data)
    show_results(part1_result, part2_result)
