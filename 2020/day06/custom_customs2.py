def get_input(filename):
    with open(filename) as f:
        data = f.read()
    return data


def prepare_data(data):
    data2 = data.split('\n\n')
    data3 = []
    for i in data2:
        j = i.strip().split('\n')

        data3.append(j)


    print(len(data3), 'длинна')
    print(data3)
    return data3


def get_count(data):
    # identify the questions to which everyone answered "yes"
    answer_count = 0
    num_of_groups = len(data)
    print(f'{num_of_groups=}')
    for group in data:
        result = set(group[0])
        person_count = len(group)
        print(f'В группе {group=} {person_count=} человек')


        for answer in range(1, person_count):
            result.intersection_update(group[answer])
            if len(result) == 0:
                break
        answer_count += len(result)
    print(f'{answer_count=}')

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
data = get_input('input2.txt')
# data = test01()
# data = test02()
data = prepare_data(data)
get_count(data)
# print(test01())
# 3447 - wrong
# 3375 - wrong
# 3382 - right
