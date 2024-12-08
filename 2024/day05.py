def load(file='day05_test.txt'):
    with open(file, "rt") as f:
        lines = list(x.replace('\n', '') for x in f.readlines())
        print(lines)
        idx = lines.index('')
        rules = lines[:21]
        print(f'{rules=}')
        updates = lines[22:]
        print(f'{updates=}')
        updates = [list(map(int, i.split(","))) for i in updates]
        print(f'{updates=}')
        return rules, updates


def part1(rules, updates):
    def is_valid(rules, update):
        for i in range(len(update)):
            for j in range(i + 1, len(update)):
                if update[j] not in rules[update[i]]:
                    return False
        return True
    add_up = 0
    for update in updates:
        if is_valid(rules, update):
            add_up += update[len(update) // 2]
    return add_up


def part2(src_data):
    return result


def show_results(answer1, answer2):
    print(f'Result part1: {answer1}')
    print(f'Result part2: {answer2}')


if __name__ == '__main__':
    rules, updates = load('day05-test.txt')
    # data = load('day-input.txt')
    part1_result = part1(rules, updates)
    part2_result = part2(rules, updates)
    show_results(part1_result, part2_result)
