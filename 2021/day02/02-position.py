def load_data(file):
    with open(file) as f:
        data = f.readlines()
        data = [line.strip() for line in data]  # убираем переносы строк
        data = [x.rsplit() for x in data]  # разбиваем линию на команду и шаг
        data = [(x[0], int(x[1])) for x in data]  # приводим элементы к кортежам
        return data


def calculate_position(data):
    x, y = 0, 0
    for i in data:
        if i[0] == 'forward':
            x = x + i[1]
        elif i[0] == 'down':
            y = y + i[1]
        elif i[0] == 'up':
            y = y - i[1]
        else:
            print('error data!')
    print('position is ', x, y)
    return x * y


def calculate_with_aim(data):
    x, depth = 0, 0
    aim = 0
    for i in data:
        if i[0] == 'forward':
            x = x + i[1]
            depth = depth + (i[1] * aim)
        elif i[0] == 'down':
            aim = aim + i[1]
        elif i[0] == 'up':
            aim = aim - i[1]
        else:
            print('error data!')
    print('position with aim is ', x, depth)
    return x * depth


test_file = 'test_input.txt'
filename = 'input.txt'
print(load_data(test_file))
print('\n', 'Task #1')
print('new coordinates multiply:', calculate_position(load_data(test_file)))
print()
print('new coordinates multiply:', calculate_position(load_data(filename)))
print('\n', 'Task #2')
print('coordinates with aim test:', calculate_with_aim(load_data(test_file)))
print('coordinates with aim:', calculate_with_aim(load_data(filename)))
