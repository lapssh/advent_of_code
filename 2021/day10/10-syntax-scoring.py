import re


def load_lines(filename='test-input.txt'):
    with open(filename) as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
        return lines


def analyze_line(line):
    # print('Analyze - ', line)

    cropped_line = line
    while ')' in cropped_line or ']' in cropped_line or '}' in cropped_line or '>' in cropped_line:
        before = len(cropped_line)
        cropped_line = cropped_line.replace('()', '')
        cropped_line = cropped_line.replace('[]', '')
        cropped_line = cropped_line.replace('{}', '')
        cropped_line = cropped_line.replace('<>', '')
        after = len(cropped_line)
        if before == after:
            # print('Loop detected! - return!')
            return (line, cropped_line)
    print(cropped_line)
    incomplite_lines.append(cropped_line)

    # return (line, cropped_line)


def calc_bug_points(lines):
    pattern = ('}|\)|\]|\>')
    result = 0
    for line in lines:
        answer = analyze_line(line)
        # print(answer)
        if answer != None:
            # print(answer)
            bug_index = re.search(pattern, answer[1]).start()
            # print(re.search(pattern, answer[1]).start())
            # print(bug_index, answer[1][bug_index])
            if answer[1][bug_index] == ')':
                result += 3
            elif answer[1][bug_index] == ']':
                result += 57
            elif answer[1][bug_index] == '}':
                result += 1197
            elif answer[1][bug_index] == '>':
                result += 25137
    return result


def replace_incomplite_lines(lines):
    new_lines = []
    for line in lines:
        line = line.replace('[', ']')
        line = line.replace('(', ')')
        line = line.replace('{', '}')
        line = line.replace('<', '>')
        line = line[::-1]
        new_lines.append(line)
    return new_lines


def part_two(lines):
    score = 0
    score_lines = []
    points = {')': 1,
              ']': 2,
              '}': 3,
              '>': 4}
    for line in lines:
        for symbol in line:
            score *= 5
            tmp = str(symbol)
            score += points[tmp]
        print(score)
        score_lines.append(score)
        score = 0

    return score_lines


def my_sort(lines):
    lines = sorted(lines)
    index_mediana = (len(lines) // 2)
    print(lines[index_mediana])


incomplite_lines = []
# lines = load_lines()
lines = load_lines('input.txt')
# incomplite_line = lines[0]
# bad_line = lines[2]
# print(incomplite_line, 'Неполная строка')
# print(bad_line, 'сломанная строка')
# analyze_line(incomplite_line)
# analyze_line(bad_line)

print(calc_bug_points(lines))
print(incomplite_lines)
incomplite_lines = replace_incomplite_lines(incomplite_lines)
mask = ['])}>']
my_data = part_two(incomplite_lines)
print(my_data)
# bad = analyze_line(bad_line)
my_sort(my_data)
