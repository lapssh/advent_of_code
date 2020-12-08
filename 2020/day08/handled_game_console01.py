def acc(program, index_program, accumulator, arg):
    print(f'[ACC] {index_program=} {accumulator=}')
    accumulator += arg
    index_program += 1
    print(f'[ACC] - после обработки {index_program=} {accumulator=}')
    return index_program, accumulator


def nop(index_program):
    print(f'[NOP] {index_program=}')
    index_program += 1
    print(f'[NOP] после сложения {index_program=}')
    return index_program


def jmp(program, index_program, accumulator, arg):
    print(f'Сейчас {index_program=} и пришла инструкция JMP с аргументом {arg=}')
    index_program += arg
    print(f'Теперь пора отправляться на {index_program=} и выполнить {program[index_program]}')
    return index_program, accumulator


def print_result(accumulator, index_program):
    print(f'Решение {accumulator=} {index_program=}')


data = ['nop +0',
        'acc +1',
        'jmp +4',
        'acc +3',
        'jmp -3',
        'acc -99',
        'acc +1',
        'jmp -4',
        'acc +6'
        ]
print(data)
def get_input(filename):
    # return list programm
    with open(filename, 'r', encoding='utf-8') as f:
        data = f.read()
    data = list(data.strip().split('\n'))
    return data

data = get_input('input.txt')
program = data
history_program = []
index_program = 0
accumulator = 0

while index_program not in history_program:
    history_program.append(index_program)  # кладем значение в историю
    get_instruction = data[index_program][:3]
    arg = data[index_program].split()
    agr = arg[1]
    print(f' {arg=}')
    arg = int(arg[1])
    print(f' {arg=}')
    print(f'{get_instruction=}   {arg=}')
    if get_instruction == 'nop':
        print('Вызов nop')
        index_program = nop(index_program)
        print(index_program)
        # accumulator, index_program = nop(program, index_program, accumulator, arg)
        print(f'Вернуло {accumulator=}, {index_program=}')
    elif get_instruction == 'acc':
        index_program, accumulator = acc(program, index_program, accumulator, arg)
        print(f'Вернуло {accumulator=}, {index_program=}')
    elif get_instruction == 'jmp':
        index_program, accumulator = jmp(program, index_program, accumulator, arg)
print('-' * 40)
print(print_result(accumulator, index_program))

# result 1782