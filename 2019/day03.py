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
                x1 += target
            case 'L':
                target = int(i[1:])
                x1 -= target
            case 'U':
                target = int(i[1:])
                y1 += target
            case 'D':
                target = int(i[1:])
                y1 -= target
        coords1.append((x1, y1))
    print(f'{x1=}, {y1=}')
    for i in src_data[1]:
        match i[0]:
            case 'R':
                x2 += int(i[1:])
            case 'L':
                x2 -= int(i[1:])
            case 'U':
                y2 += int(i[1:])
            case 'D':
                y2 -= int(i[1:])
        coords2.append((x2, y2))
    print(f'{coords1=}, {coords2=}')
    pull1 = build_pull(coords1)
    print(f'{pull1=}')
    result = src_data
    return result


def build_pull(coords: list) -> set:
    start = coords[0]
    coords = coords[1:]
    for i in coords:
        x1, y1 = start
        print(f'{x1=}, {y1=}')
        x2, y2 = i[0], i[1]
        if x2 > x1:
            for i in range(x1 + 1, x2 + 1):
                coords.append((i, y2))
        else:
            for i in range(x2 - 1, x1, -1):
                coords.append((i, y2))
        if y2 > y1:
            for i in range(y1 + 1, y2 + 1):
                coords.append((x2, i))
        else:
            for i in range(y2 - 1, y1, -1):
                coords.append((x2, i))
        start = (x2, y2)
    return set(coords)


def part2(src_data):
    result = src_data
    return result


def show_results(answer1, answer2):
    print(f'Result part1: {answer1}')
    print(f'Result part2: {answer2}')


if __name__ == '__main__':
    # data = load()
    data = load('test-day03-1.txt')
    part1_result = part1(data)
    part2_result = part2(data)
    show_results(part1_result, part2_result)
