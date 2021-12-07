def load_data(filename='input-test.txt'):
    with open(filename) as f:
        data = f.readline()
        data = data.strip()
        data = data.split(',')
        data = [int(x) for x in data]
    return data


def horizontal_pozition(data):
    uniq_pozitions = set(data)
    uniq_pozitions = list(uniq_pozitions)
    unics = uniq_pozitions[:]
    print(uniq_pozitions)
    fuel_kpi = []
    while len(uniq_pozitions) > 0:
        current_pos = uniq_pozitions.pop(0)
        print('текущая позиция ', current_pos)
        for position in uniq_pozitions:
            fuel = abs(current_pos - position)
            print(f'для смены {current_pos=} на {position} будет потрачено {fuel=} топлива')
            fuel_kpi.append((current_pos, position, fuel))
    # print(fuel_kpi)
    result = []
    fuel_kpi = []
    print('Уникальные ', unics)
    for base in unics:
        fuel_kpi = []
        print('base', base)
        for i in data:
            fuel = abs(base - i)
            fuel_kpi.append(fuel)
        result.append((fuel_kpi, base))
    result2 = []
    for i in result:
        print('for base=', i[1], i)
        print('sum=', sum(i[0]))
        result2.append((sum(i[0]), i[1]))
    print(result2)
    result3 = sorted(result2)
    print('result3 = ', result3)
    result4 = result3[0]
    print(result4)
    # print([min(x[0]) for x in result2])
    # print(sorted.result2)



data = load_data('input.txt')
print(data)
horizontal_pozition(data)
