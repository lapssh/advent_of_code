import itertools
from itertools import permutations, product


def load(file):
    with open(file, "rt") as f:
        lines = list(x.replace('\n', '') for x in f.readlines())
        data = []
        for item in lines:
            result, numbers = item.split(':')
            numbers = numbers[1:]
            result = int(result)
            numbers = list(map(int, numbers.split(' ')))
            data.append((result, numbers))
        # res = [x.split(',') for x in lines]
        # print(f'{data=}')
        return data


def part1(data):
    total = 0

    def is_valid(result, nums, opers):
        # print(f'Для {opers=} мы должны выполнить {len(opers)} цикла')
        etalon_nums = nums[:]
        trigger = sum(etalon_nums)
        for i in range(len(opers)):
            # print(f'В {nums=} нужно вставить {opers[i]}')
            for znak in opers:
                example = nums.pop(0)
                # print(example, end='')
                znak = list(znak)
                while nums:
                    _oper = znak.pop(0)
                    if _oper == '+':
                        # print('+', nums[0], sep='', end='')
                        example += nums.pop(0)
                    elif _oper == '*':
                        # print('*', nums[0], sep='', end='')
                        example = example * nums.pop(0)
                    _res = example
                # print('=', _res)
                # print(f' {_res=} а  результат {result}  ')
                if _res == result:
                    # print()
                    # print()
                    # print(f'Верная строка! {result}: {etalon_nums}')
                    return True
                _res = 0
                example = ''
                _oper = ''
                nums = etalon_nums[:]
        return False

    for line in data:

        # operators = ['+', '*']
        operators = '+*'
        result = line[0]
        nums = line[1]
        if sum(nums) > result:
            continue
        else:
            len_operators = len(nums) - 1
            # print(f'Для чисел {nums=} доступно {len_operators=} {result=}')
            # operators = list(itertools.permutations(operators, len_operators))
            operators = list(product(operators, repeat=len_operators))
            # print(f'{operators=}')
            if is_valid(result, nums, operators):
                total += result
    return total


def part2(src_data):
    pass


def show_results(answer1, answer2):
    print(f'Result part1: {answer1}')
    print(f'Result part2: {answer2}')


if __name__ == '__main__':
    # data = load('day07-test.txt')
    data = load('day07-input.txt')
    part1_result = part1(data)
    part2_result = part2(data)
    show_results(part1_result, part2_result)
