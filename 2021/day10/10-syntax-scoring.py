import re

def load_lines(filename='test-input.txt'):
    with open(filename) as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
        return lines


def analyze_line(line):
    print('Analyze - ', line)
    cropped_line = line
    opens = ['(', '[', '{']
    closed = [')', ']', '}']
    # print(')' in cropped_line)
    flag_loop = len(cropped_line)
    while ')' in cropped_line or ']' in cropped_line or '}' in cropped_line or '>' in cropped_line:
        # print(cropped_line)
        before = len(cropped_line)
        cropped_line = cropped_line.replace('()', '')
        cropped_line = cropped_line.replace('[]', '')
        cropped_line = cropped_line.replace('{}', '')
        cropped_line = cropped_line.replace('<>', '')
        after = len(cropped_line)
        # print(cropped_line)
        if before == after:
            print('Loop detected! - return!')
            return (line, cropped_line)
    # return (line, cropped_line)


def calc_bug_points(lines):
    pattern = ('}|\)|\]|\>')
    result = 0
    for line in lines:
        answer = analyze_line(line)
        print(answer)
        if answer != None:
            print(answer)
            bug_index = re.search(pattern, answer[1]).start()
            print(re.search(pattern, answer[1]).start())
            print(bug_index, answer[1][bug_index])
            if answer[1][bug_index] == ')':
                result += 3
            elif answer[1][bug_index] == ']':
                result += 57
            elif answer[1][bug_index] == '}':
                result += 1197
            elif answer[1][bug_index] == '>':
                result += 25137
    return result

lines = load_lines('input.txt')
incomplite_line = lines[0]
bad_line = lines[2]
# print(incomplite_line, 'Неполная строка')
# print(bad_line, 'сломанная строка')
analyze_line(incomplite_line)
analyze_line(bad_line)

print(calc_bug_points(lines))
# bad = analyze_line(bad_line)



