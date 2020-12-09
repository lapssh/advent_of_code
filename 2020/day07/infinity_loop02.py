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

def parse_line(line):
    comm = line[:3]
    arg = line.split()
    agr = arg[1]
    arg = int(arg[1])
    return comm, arg

def get_command(program, index_program):
    print(f' Get comand {index_program=}')
    line = program[index_program]
    comm, arg = parse_line(line)
    print(f'{comm=} {arg=}')
    return comm, arg

def run_command(comm, arg, accumulator, index_program):
    print(f'Поулчена команда {comm=} {arg=} {accumulator=} {index_program=}')
    if comm == 'nop':
        print(f'[NOP] {arg=}')
        index_program = nop(index_program)
    elif comm == 'acc':
        index_program, accumulator = acc(index_program, accumulator, arg)
    elif comm == 'jmp':
        index_program, accumulator = jmp(index_program, accumulator, arg)
    print(f'Возврат {accumulator=} {index_program=}')
    return accumulator, index_program



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

while index_program <= len(program): # повторять, пока не завершится ОК
    while index_program not in history_program:
        history_program.append(index_program)
        comm, arg = get_command(program, index_program)
        # проба запуска в режиме дебага
        while debug_flag:
            if comm == 'nop':
                comm = 'jmp'
                debug_flag = False
                # tmp_index = index_program
            elif comm == 'jmp':
                comm = 'nop'
                debug_flag = False
            accumulator, index_program = run_command(comm, arg, accumulator, index_program)
    else:
        print(f'Зациклилась на {index_program=} с {accumulator=}' )
        debug_flag = True



print_result(accumulator, index_program)
