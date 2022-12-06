def load_data(filename='input.txt'):
    with open(filename) as f:
        data = f.readlines()
    # cleaned_data = [x.strip() for x in data]
    # return cleaned_data
    return data


def split_data(raw_data):
    cargo = []
    commands = []
    for line in raw_data:
        if line[0] != '1' and line[0] != 'm':
            cargo.append(line)
        else:
            if line[0] == 'm':
                commands.append(line)
    cargo.pop()
    cargo.pop()
    print('cargo:', cargo)
    print('commands:', commands)
    return cargo, commands


def create_cargo_stack(cargo):
    print('Создаём стек грузов')
    result = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: []}
    # result = {1: [], 2: [], 3: []}
    count = 1
    cargo.reverse()
    for line in cargo:
        # print(line)
        _ = line.replace('[', ' ')
        _ = _.replace(']', ' ')
        # _ = _.replace(' ', ' ')
        _ = _.replace('\n', '')
        _ = _[1:]
        _ = _[:-1]
        # print(_)
        print(_)
        # index = iter(range(0, 9, 4))
        index = iter(range(0, 33, 4))
        for i in range (1, 10):
        # for i in range(1, 3):
            current_index = next(index)
            if _[current_index] != ' ':
                result[i].append(_[current_index])
        # print(result)
    return result


def move_crate(cargo_stack, number_of_crates, _from, _to):
    print(f'Запрос на перенос {number_of_crates} ящиков из {_from} в {_to}')
    for i in range(0, number_of_crates):
        # print(f'{cargo_stack[_from]=}')
        stack = cargo_stack[_from].pop()
        print(f'{stack=}')
        cargo_stack[_to].append(stack)
    print('после сортировки: ', cargo_stack)
    return cargo_stack


def move_crate2(cargo_stack, number_of_crates, _from, _to):
    print(f'Запрос на перенос {number_of_crates} ящиков из {_from} в {_to}')
    # print(f'{cargo_stack[_from]=}')
    stack = cargo_stack[_from][-number_of_crates:]
    cargo_stack[_from] = cargo_stack[_from][:-number_of_crates]
    print(f'{stack=}')
    cargo_stack[_to] = cargo_stack[_to] + stack
    print('после сортировки: ', cargo_stack)
    return cargo_stack

def cargo_sort(cargo_stack, commmands):
    for command in commmands:
        # print(command)
        command = command.replace('move ', '')
        command = command.replace('from ', '')
        command = command.replace('to ', '')
        # print(command)
        command = command.split()
        # print(command)
        number_crates = int(command[0])
        crate_from = int(command[1])
        crate_to = int(command[2])
        cargo_stack = move_crate2(cargo_stack, number_crates, crate_from, crate_to)
        # cargo_stack = move_crate(cargo_stack, number_crates, crate_from, crate_to)
    return cargo_stack


def part1(cargo):
    result = ''
    for i in range(1,len(cargo)+1):
        result = result + (cargo[i][-1])
    return result

tmp = load_data()
# tmp = load_data('test.txt')
print(tmp)
# tmp = ['[Z] [P] [S] [F] [F] [T] [N] [P] [W]']
# for line in
# for i in range(1, 35, 4):
#     print(tmp[0][i], end='')
cargo, commands = split_data(tmp)
cargo_stack = create_cargo_stack(cargo)
print(cargo_stack)
new_cargo_stack = cargo_sort(cargo_stack, commands)
print(new_cargo_stack)
print('part2 result:', part1(new_cargo_stack))
