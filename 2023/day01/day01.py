import re

nums = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}
def load(file='input.txt'):
    with open(file, "rt") as f:
        return list(line.strip() for line in f.readlines())


def calibrate_line(line):
    # print(f'line:', line, end='')
    res = re.findall(r'\d+', line)
    # print(f'nums: ', res)
    if len(res) == 1:
        # print('last')
        line = res[0][0] + res[0][-1]
    else:
        line = res[0][0] + res[-1][-1]
    # print()
    # print(f'result for line: ', line)
    # print()
    return int(line)


def search_nums(part):
    word = ''
    while len(part) > 1:
        for letter in part:
            # print(f'{letter=} {part=}')
            word += letter
            # print(f'{word=}')
            if word in nums:
                # print(f'Найдено слово ', word)
                return word
        # print('перебрали - не нашли')
        word = ''
        part = part[1:]
        # print(f'отрезаем {part=}')


def search_nums2(part):
    word = ''
    part = str(part[::-1])
    # print(f'{part=}')
    while len(part) > 1:
        for letter in part:
            # print(f'{letter=} {part=}')
            word = letter + word
            # print(f'{word=}')
            if word in nums:
                # print(f'Найдено слово ', word)
                return word
        # print('перебрали - не нашли')
        word = ''
        part = part[1:]
        # print(f'отрезаем {part=}')


def parse_block(block):
    # print('===========ИЩЕМ СЛЕВА============')
    # print(f'{block=}')
    while True:
        if block[0].isdigit():
            return block
        word = search_nums(block)
        # print(f'{block=} {word=}')
        if not word: break
        # print(f'в {block=} найдено {word=}')
        block = str(block).replace(word, nums[word])
        return block
    return block

def parse_block2(block):
    # print('===========ИЩЕМ СПРАВА============')
    # print(f'{block=}')
    while True:
        if block[-1].isdigit():
            return block
        word = search_nums2(block)
        # print(f'{block=} {word=}')
        if not word: break
        # print(f'в {block=} найдено {word=}')
        block = str(block).replace(word, nums[word])
        return block
    return block


def calibrate_line_advanced(line):
    # print(f'src-line:', line)
    # разбиваем строку на блоки текста
    res = re.findall(r'\D+', line)
    # print(f'{res=}')
    if res != []:
        # парсим каждый блок на цифры
        for i in res:
            # проход слева
            left = parse_block(line)
            # print(f'После прохода слева {left=}')
            # проход справа
            right = parse_block2(line)
            # print(f'После прохода справа {right=}')
            # print(left+right)
            return calibrate_line(left+right)
    else:
        return calibrate_line(line)
    exit()



def part1(data):
    acc = 0
    for line in data:
        acc += calibrate_line(line)
    return acc


def part2(data):
    acc = 0
    for line in data:
        n = calibrate_line_advanced(line)
        # print(f'{n=}')
        if 9 > n > 99:
            print('ERROR')
            exit()
        acc += n
    return acc


data = load()
# data = data[0:5]
# data = ['1abc2',     'pqr3stu8vwx',     'a1b2c3d4e5f',     'treb7uchet' ]
# data = ['twone',     'pqr3stu8vwx',     'a1b2c3d4e5f',     'treb7uchet' ]
# data = ['1abc2',     'pqr3stu8vwx',     'a1b2c3d4e5f',     'treb7uchet' ]
# data = ['two1nine',  'abcone2threexyz', '9one1two']
# data = ['eightwothree', 'two1nine',  'abcone2threexyz', 'xtwone3four', '4nineeightseven2', 'zoneight234', '7pqrstsixteen']
# data = ['twoneighthree', 'eightwothree']
# print(f'test: ', calibrate_line(data[0]))
print(f'part1: ', part1(data))
print(f'part2: ', part2(data))  # 54594
