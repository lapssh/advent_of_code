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


def part1(rules, pages):
    for line in pages:
        program = []
        nums = [int(x) for x in line.split(',')]
        correctly_lines = []
        for num in nums:
            program.append(num)
            for rule in rules:
                num1, num2 = rule.split('|')
                num1 = int(num1)
                num2 = int(num2)
                if num in (num1, num2) and num2 in program:
                    num_idx = program.index(num)
                    if num1 in program:
                        num1_idx = program.index(num1)
                    num2_idx = program.index(num2)
                    print(f'{num=} {num1=} {num2=} {num_idx=}')
                    if num == num1:
                        if num_idx < num2_idx:
                            correctly_lines.append(rule)

        print(correctly_lines)
    return 1


def part2(src_data):
    return result


def show_results(answer1, answer2):
    print(f'Result part1: {answer1}')
    print(f'Result part2: {answer2}')


if __name__ == '__main__':
    rules, pages = load('day05-test.txt')
    # data = load('day-input.txt')
    part1_result = part1(rules, pages)
    part2_result = part2(rules, pages)
    show_results(part1_result, part2_result)
