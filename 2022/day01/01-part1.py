filename = 'input.txt'
# filename = 'test.txt'
def load_data(filename):
    data = []
    with open(filename) as f:
        lines = f.readlines()
        tmp = []
        for line in lines:
            if line != '\n':
                tmp.append(int(line.strip()))
            else:
                data.append(tmp)
                tmp = []
        return data


def part1(data):
    calories = []
    for i in data:
        calories.append(sum(i))
    # print(calories)
    result = max(calories)
    return result


def part2(data):
    calories = []
    for i in data:
        calories.append(sum(i))
    # print(calories)
    data = sorted(calories)
    # print('сортировка', data)
    result = data[-3:]
    # print(result)
    result = sum(result)
    return result


data = load_data(filename)
result1 = part1(data)
print('ответ на задачу №1: ', result1)
result2 = part2(data)
print('ответ на задачу №1: ', result2)
