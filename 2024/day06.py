from importlib.metadata import pass_none


def load(file='day01_test.txt'):
    with open(file, "rt") as f:
        lines = list(x.replace('\n', '') for x in f.readlines())
        # print(lines)
        labirint = []
        for item in lines:
            _ = list(item)
            # print(_)
            labirint.append(_)

        # res = [x.split(',') for x in lines]
        print(f'{labirint=}')
        # for line in labirint:
        #     print(line)
        return labirint


def part1(labirint_map):
    def create_map(data):
        block_map=[]
        lab_map = []
        for y, i in enumerate(data):
            for x, j in enumerate(i):
                lab_map.append((x, y))
                if data[y][x] == '^':
                    point = (x,y)
                    print(x,y, '^')
                elif data[y][x] == '#':
                    block_map.append((x,y))
        print(block_map)
        return point, block_map, lab_map


    way = []
    point, block_map, lab_map = create_map(labirint_map)
    print(f'{block_map=}')
    direction = {
        'up': (0, -1),
        'down': (0, 1),
        'left': (-1, 0),
        'right': (1, 0)}
    current_direction = 'up'
    while point in lab_map:
        # вычисляем следующий шаг
        new_point = (point[0]+direction[current_direction][0], point[1]+direction[current_direction][1])
        print(f'{point=} {new_point=}')
        # проверка, можем ли сделать шаг
        if new_point not in block_map:
            point = new_point
            way.append(point)
        else:
            print(f'Проверка {new_point=} воткнулся в блок {block_map=}')
            if current_direction == 'up':
                current_direction = 'right'
            elif current_direction == 'down':
                current_direction = 'left'
            elif current_direction == 'left':
                current_direction = 'up'
            elif current_direction == 'right':
                current_direction = 'down'
        print(f'{point=} {lab_map=}')
        print(way)  # выход за пределы лабиринта
        print(len(set(way))-1)





def part2(src_data):
    pass


def show_results(answer1, answer2):
    print(f'Result part1: {answer1}')
    print(f'Result part2: {answer2}')


if __name__ == '__main__':
    # data = load('day06-test.txt')
    data = load('day06-input.txt')
    part1_result = part1(data)
    part2_result = part2(data)
    show_results(part1_result, part2_result)
