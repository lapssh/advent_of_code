def load(file='day_test.txt'):
    with open(file, "rt") as f:
        lines = list(x.replace('\n', '') for x in f.readlines())
        print(lines)
        data = []
        for item in lines:
            _ = list(item)
            print(_)
        data.append(_)

        # res = [x.split(',') for x in lines]
        print(f'{data=}')
        for line in data:
            print(line)
        return data


def part1(src_data):
    return result


def part2(src_data):
    return result


def show_results(answer1, answer2):
    print(f'Result part1: {answer1}')
    print(f'Result part2: {answer2}')


if __name__ == '__main__':
    data = load('day09-test1.txt')
    # data = load('day09-input.txt')
    part1_result = part1(data)
    part2_result = part2(data)
    show_results(part1_result, part2_result)
