def get_input(filename):
    with open(filename) as f:
        data = f.read()
    return data


def prepare_data(data):
    # print(f'{data=}')
    data2 = data.split('\n\n')
    # print(f'{data2=}')
    data3 = []
    for i in data2:
        i_ = i.replace('\n', ' ')
        j = i_.split(' ')
        # print(f'{i=} {i_=} {j=}')
        data3.append(j)
    # print(f'{data3=}')
    return data3


def get_count(data):
    # identify the questions to which everyone answered "yes"
    count_ = 0
    num_of_groups = len(data)
    print(f'{num_of_groups=}')
    for item in data:
        person_count = len(item)
        # print(f'В группе {item=} {person_count=} человек')
        result = set(item[0])
        # print(result)
        count2 = 0
        for i in item:
            tmp_set = set(i)
            set_diff = result.intersection(tmp_set)
            # print(item, ' ', end='')
        count_ += len(set_diff)
        count2 = len(set_diff)
        print('\nВ группе ',item, count2, 'совпадений')

    print(f'{count_=}')

def test01():
    # must return 6
    data = '''abc

a
b
c

ab
ac

a
a
a
a

b'''
    return data

def test02():
    # must return 2
    data = '''pe
kpes

a
a
a
tv
'''
    return data
#
data = get_input('input.txt')
# data = test01()
# data = test02()
data = prepare_data(data)
get_count(data)
# print(test01())
# 3447 - wrong
