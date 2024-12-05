import numpy as np


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
    reversed_list = []
    for i in normal_list:
        reversed_list.append(i[::-1])
    return reversed_list


def part1(data):
    lines = data[:]
    print(lines)
    lines.extend(["".join([row[i] for row in data]) for i in range(len(data[0]))])
    print(lines)

    def find_diagonals(grid):
        rows, cols = len(grid), len(grid[0])

        # from top-left to bottom-right
        main_diagonals = {}

        # from top-right to bottom-left
        anti_diagonals = {}

        for r in range(rows):
            for c in range(cols):
                key_main = r - c
                if key_main not in main_diagonals:
                    main_diagonals[key_main] = []
                main_diagonals[key_main].append(grid[r][c])

                key_anti = r + c
                if key_anti not in anti_diagonals:
                    anti_diagonals[key_anti] = []
                anti_diagonals[key_anti].append(grid[r][c])

        return main_diagonals, anti_diagonals

    main_diagonals, anti_diagonals = find_diagonals(data)
    print(lines)
    print(lines)
    lines.extend(["".join(i) for i in main_diagonals.values()])
    lines.extend(["".join(i) for i in anti_diagonals.values()])
    print(lines)

    return sum(line.count("XMAS") + line.count("SAMX") for line in lines)


def part2(data):
    rows, cols = len(data), len(data[0])
    count = 0
    _set = {"M", "S"}
    # find A as center of the cross, then check the diagonals
    for r in range(1, rows - 1):
        for c in range(1, cols - 1):
            if data[r][c] == "A":
                if {data[r - 1][c - 1], data[r + 1][c + 1]} == _set and {data[r - 1][c + 1],
                                                                         data[r + 1][c - 1]} == _set:
                    count += 1
    return count


def show_results(answer1, answer2):
    print(f'Result part1: {answer1}')
    print(f'Result part2: {answer2}')


if __name__ == '__main__':
    # data = load('day04-test1.txt')
    # data = load('day04-test2.txt')
    data = load('day04-input.txt')
    part1_result = part1(data)
    part2_result = part2(data)
    show_results(part1_result, part2_result)
