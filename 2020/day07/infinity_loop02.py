def acc(index_program, accumulator, arg):
    accumulator += arg
    index_program += 1
    return index_program, accumulator


def nop(index_program):
    index_program += 1
    return index_program


def jmp(index_program, accumulator, arg):
    index_program += arg
    return index_program, accumulator


def print_result(accumulator, index_program):
    print(f'Решение {accumulator=} {index_program=}')


def save_state(program, index_program, accumulator):
    global program_tmp, index_tmp, accumulator_tmp
    program_tmp = program
    index_tmp = index_program
    accumulator_tmp = accumulator
    print(f'Сохраняю {program=}  {program_tmp=}')


def load_state():
    global program_tmp, index_tmp, accumulator_tmp
    print('Начинаю восстановление......')
    program = program_tmp
    index_program = index_tmp
    accumulator = accumulator_tmp
    print(f'Во времянке хранится {program=}  {index_program=}  {accumulator=}')
    return program, index_program, accumulator

program_tmp = 0
index_tmp = 0
accumulator_tmp = 0

data = ['nop +0',
        'acc +1',
        'jmp +4',
        'acc +3',
        'jmp -3',
        'acc -99',
        'acc +1',
        'jmp -4',
        # 'nop -4',
        'acc +6'
        ]
print(data)


def get_input(filename):
    # return list programm
    with open(filename, 'r', encoding='utf-8') as f:
        data = f.read()
    data = list(data.strip().split('\n'))
    return data


# data = get_input('input.txt')
program = data
history_program = []
index_program = 0
accumulator = 0

debug_flag = True

while True:

    while index_program not in history_program:
        if index_program >= len(data):
            print('Мы дошли, всем спасибо')
            print(f'{accumulator=}')
            exit()
        history_program.append(index_program)  # кладем значение в историю
        get_instruction = data[index_program][:3]
        arg = program[index_program].split()
        agr = arg[1]
        arg = int(arg[1])

        if get_instruction == 'nop':
            if debug_flag:
                debug_flag = False
                # print(f'{program[index_program]=}')
                save_state(program, index_program+1, accumulator)
                program[index_program] = program[index_program].replace('nop', 'jmp')
                print(f'Теперь {program[index_program]=}')
                index_program, accumulator = jmp(index_program, accumulator, arg)
                # exit()
            else:
                index_program = nop(index_program)
        elif get_instruction == 'acc':
            index_program, accumulator = acc(index_program, accumulator, arg)
        elif get_instruction == 'jmp':
            if debug_flag:
                debug_flag = False
                print(f'{program[index_program]=}')
                save_state(program, index_program+1, accumulator)
                program[index_program] = program[index_program].replace('jmp', 'nop')
                print(f'Теперь {program[index_program]=}')
                index_program = nop(index_program)
            else:
                index_program, accumulator = jmp(index_program, accumulator, arg)
    print('-' * 40)
    print(f'Программа зациклилась при {program[index_program]=}')
    print(history_program)
    history_program.pop()
    program, index_program, accumulator = load_state()
    debug_flag = True
    print(print_result(accumulator, index_program))
