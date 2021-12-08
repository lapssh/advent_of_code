def load_data(filename='test-input.txt'):
    with open(filename) as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
    # print(lines)
    return lines


def get_output_data(data):
    output_data = []
    # print(data)
    for i in data:
        tmp = i.split('|')
        code = tmp[0].strip()
        answer = tmp[1].strip()
        output_data.append((code, answer))
    return output_data


def get_mask_numbers(line):
    code = line[0]
    print(code)
    tmp = code.split()
    # print(tmp)
    res = []
    for i in tmp:
        res.append(set(i))
    # print(res)
    numbers = dict()
    for num in res:
        # print(len(num))
        if len(num) == 2:
            # отлично, мы нашли 1!
            numbers['1'] = num
        elif len(num) == 3:
            # отлично, мы нашли 7!
            numbers['7'] = num
        elif len(num) == 4:
            # отлично, мы нашли 4!
            numbers['4'] = num
        elif len(num) == 5:
            # отлично, мы нашли 2,3 или 5!
            if numbers.get('235'):
                numbers['235'].append(num)
            else:
                numbers['235'] = [num]
        elif len(num) == 6:
            # отлично, мы нашли 6,9 или 0!
            if numbers.get('690'):
                numbers['690'].append(num)
            else:
                numbers['690'] = [num]
        # elif len(num) == 7:
        #     # отлично, мы нашли 8!
        #     numbers['8'] = num
    numbers['8'] = {'a', 'b', 'c', 'd', 'e', 'f', 'g'}
    # print(numbers)
    """Попробуем достать 3 из 1"""
    if '1' in numbers:
        numbers['right'] = numbers['1']
        for item in numbers['235']:
            # print('нашли 235:')
            if len(item.intersection(numbers['1'])) == 2:
                # нашли 3!
                # print('3 из 1 =', item)
                numbers['3'] = item
    """Попробуем достать 3 из 7"""
    if '7' in numbers:
        for item in numbers['235']:
            # print('нашли 235:')
            if len(item.intersection(numbers['7'])) == 3:
                # нашли 3!
                # print('3 из 7 =', item)
                numbers['3'] = item
    """Ищем left из 3"""
    numbers['left'] = numbers['8'].difference(numbers['3'])
    # print('left=', numbers['left'])
    # теперь найдём mid
    for num in numbers['690']:
        # print(len(num.intersection(numbers['left'])))
        if len(num.intersection(numbers['left'])) == 2 and len(num.intersection(numbers['right'])) == 2:
            numbers['0'] = num
    numbers['mid'] = numbers['8'].difference(numbers['0'])
    # print('mid=', numbers['mid'])
    # теперь найдём цифру 6
    numbers['69'] = numbers['690']
    numbers['69'].remove(numbers['0'])
    # print('number 69', numbers['69'])
    for num in numbers['690']:
        # print(num.intersection(numbers['left']))
        if len(num.intersection(numbers['left'])) == 2:
            # print(num.intersection(numbers['left']))
            numbers['6'] = num
            numbers['69'].remove(num)
            numbers['9'] = numbers['69'][0]

    numbers['235'].remove(numbers['3'])
    numbers['25'] = numbers['235']
    # print('numbers 25=', numbers['25'])
    # теперь найдём цифру 5
    for num in numbers['25']:
        if len(num.intersection(numbers['6'])) == 5:
            numbers['5'] = num
        else:
            numbers['2'] = num

    # теперь найдём цифру 7: 7=4-
    numbers['1'] = numbers['right']
    # print(numbers)
    # пробуем найти top из 1 и 7
    try:
        top = numbers['7'].difference(numbers['1'])
        # print(f'{top=}')
    except:
        print('ERROR - TOP not found')
    return numbers

def get_set_value(line):
    tmp = line.split()
    print(tmp)
    res = []
    for i in tmp:
        res.append(set(i))
    return res

def find_eight(code):
    for j in code:
        len_tmp = len(j)
        # print(f'{j=} {len_tmp=}')
        if len_tmp == 7:
            return j


def decode_data(line):
    """Задача 1 - декодировать символы в первой части данных и сопоставить с цифрами"""
    code = line[0].split()
    return code




test_one = ['acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf',
            'acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf']
# x = get_output_data(test_one)
# line = x[0]
# print(line)
# code = line[0]
# res = get_mask_numbers(code)
# print(f'{res=}')
lines = load_data()
# print(lines)
data = get_output_data(lines)
print(f'{data=}')
for line in data:
    print(line)
    mask = get_mask_numbers(line[0])
    # values = get_mask_numbers(line[1])
    # print((line[1]))
    # print(line[1])
    # get_mask_numbers(line[0])
# print(data)
# for line in data:
#     get_mask_numbers(lines)
# codes_as_set = []
# for i in data:
#     print(i[0])
#     tmp = i[0].split()
#     print(tmp)
#     for j in tmp:
#         my_key = set(j)
#         print(my_key)
#         for key, value in data:
#             if value == j:
#                 print(f'{value=} {key}')

# decoded_line = decode_data(x[0])
# print(decoded_line)
# print(find_eight(decoded_line))
