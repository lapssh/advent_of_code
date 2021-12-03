def analyse_deep(data):
    deep = data[0]
    deep_inc_count = 0
    for i in data:
        if deep < i:
            # print('current deep=', deep,'new depp=', i, 'count=', deep_inc_count)
            deep = i
            deep_inc_count += 1
        deep = i

    return deep_inc_count


def analyse_adv_deep(data):
    increased_count = 0
    decreased_count = 0
    no_change_count = 0
    while len(data) > 3:
        a = data[0:3]
        print('in block ', a, 'summ=', sum(a))
        b = data[1:4]
        print('in block ', b, 'summ=', sum(b))
        data = data[1:]
        if sum(a) < sum(b):
            print('deep is increased')
            increased_count += 1
        elif sum(a) > sum(b):
            print('deep is decreased')
            decreased_count += 1
        else:
            print('deep is no change')
            no_change_count += 1
    return increased_count


with open('01-data.txt') as file:
    lines = file.readlines()
test_data = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
lines = [line.rstrip() for line in lines]
lines = [int(line) for line in lines]

print('measurements are larger count in test:', analyse_deep(test_data))
print('measurements are larger count:', analyse_deep(lines))

print('measurements are larger count in adv_test:', analyse_adv_deep(test_data))
print('measurements are larger count in task 2:', analyse_adv_deep(lines))
