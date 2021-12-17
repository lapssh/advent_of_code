from typing import List, Tuple
import os


def solution(data: str) -> int:
    n, index, numbers = _parse_input(data)

    combinations = 1
    for digits in numbers:
        combinations *= len(digits)

    code = [0] * n
    start = 1

    for i in range(n):
        partition = combinations / len(numbers[i])
        end = start + partition - 1

        for j in range(len(numbers[i])):
            if start <= index <= end:
                code[i] = numbers[i][j]
                break
            start += partition
            end += partition

        combinations = partition

    return int("".join([str(x) for x in code]))


def _parse_input(data: str) -> Tuple[int, int, List[List[int]]]:
    numbers = []

    for line in data.split('\n'):
        if not line:
            continue

        numbers.append([int(x) for x in line.split()])

    return numbers[0][0], numbers[0][1], numbers[1:]
        

def test(expected, actual):
    assert expected == actual, f'Expected: {expected}, Actual: {actual}'


test(12945, solution("""
5 5
1
2
3 6 9
4
5 6
"""))


file_path = os.path.join(os.path.dirname(__file__), 'advent_5.test.txt')
with open(file_path, 'r') as f:
    input_data = f.read()
    print('Advent 05: %r' % (solution(input_data)))
