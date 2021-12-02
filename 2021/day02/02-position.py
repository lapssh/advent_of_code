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


filename = 'test_input.txt'
print(load_data(filename))
print('new coordinates multiply:', calculate_position(load_data(filename)))

filename = 'input.txt'
print('new coordinates multiply:', calculate_position(load_data(filename)))
