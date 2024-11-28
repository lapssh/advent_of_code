def load(file='day03_input.txt'):
    with open(file, "rt") as f:
        lines = list(x.replace('\n', '') for x in f.readlines())
        print(lines)
        res = [x.split(',') for x in lines]
        print(f'{res=}')
        return res


def part1(src_data):
    x1, y1, x2, y2 = 0, 0, 0, 0

    print(f'{src_data[0]=}')
    coords1 = []
    coords2 = []
    for i in src_data[0]:
        match i[0]:
            case 'R':
                target = int(i[1:])
                [coords1.append((x, y1)) for x in range(x1, target + 1)]
                x1 += target
            case 'L':
                target = int(i[1:])
                [coords1.append((x, y1)) for x in range(x1 - 1, x1 - target - 1, -1)]
                x1 -= target
            case 'U':
                target = int(i[1:])
                [coords1.append((x1, y)) for y in range(y1, target + 1)]
                y1 += target
            case 'D':
                target = int(i[1:])
                [coords1.append((x1, y)) for y in range(y1, y1 - target - 1, -1)]
                y1 -= target
    for i in src_data[1]:
        match i[0]:
            case 'R':
                target = int(i[1:])
                [coords2.append((x, y2)) for x in range(x2, target + 1)]
                x2 += target
            case 'L':
                target = int(i[1:])
                print(f'LEFT {target=}')
                print(f'{list(range(x2-1, x2-target-1, -1))=}')
                [coords2.append((x, y2)) for x in range(x2 - 1, x2 - target - 1, -1)]
                x2 -= target
            case 'U':
                target = int(i[1:])
                [coords2.append((x2, y)) for y in range(y2, target + 1)]
                y2 += target
            case 'D':
                target = int(i[1:])
                [coords2.append((x2, y)) for y in range(y2, y2 - target - 1, -1)]
                y2 -= target

    print(f'{coords1=}, {coords2=}')
    coords1 = set(coords1)
    coords2 = set(coords2)
    print(f'{coords1=}, {coords2=}')
    result = coords1.intersection(coords2)
    print(f'{result=}')
    result = sorted(list(result))
    result.remove((0, 0))
    print(f'{result=}')
    # ищем манхэтенское расстояние
    min_dist = 100000000
    for point in result:
        manheten_dist = abs(point[0] - 0) + abs(point[1] - 0)
        if manheten_dist < min_dist:
            min_dist = manheten_dist
    print(f'{min_dist=}')

    return result


def part2(src_data):
    result = src_data
    return result


def show_results(answer1, answer2):
    print(f'Result part1: {answer1}')
    print(f'Result part2: {answer2}')


if __name__ == '__main__':
    # data = load()
    # data = load('test-day03-1.txt')
    data = load('test-day03-2.txt')
    part1_result = part1(data)
    part2_result = part2(data)
    show_results(part1_result, part2_result)
