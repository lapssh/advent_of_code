from collections import Counter


def load_data(filename):
    with open(filename) as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
        coordinates = [line.split(' -> ') for line in lines]
        points = []
        for nums in coordinates:
            point_one = nums[0].split(',')
            point_two = nums[1].split(',')
            point_one = [int(x) for x in point_one]
            point_two = [int(x) for x in point_two]
            points.append((point_one, point_two))
            # nums = (int(nums[0]), int(nums[1]))

    return points


def create_map(points):
    # size = 10
    size = 999
    water_map = [0] * size
    for i in range(size):
        water_map[i] = [0] * size
    return water_map


def draw_map(points):
    # print(f'Получены точки: {points}')
    for point in points:
        water_map[point[1]][point[0]] += 1
    # print_map(water_map)



def calculate_points_horizontal(line):
    points = []
    # для горизонтальных линий
    # print('Высчитаем точки для горизонтального отрезка ',line )
    if line[0][0] > line [1][0]:
        line[0][0], line [1][0] = line [1][0], line [0][0]
    for i in range(line[0][0],line[1][0]+1):
        # print('Новая точка ',i,  line[0][1])
        points.append((i,line[0][1]))
    # print(f' {points=}')
    draw_map(points)

def calculate_points_vertical(line):
    points = []
    # для вертикальных линий
    # print('Высчитаем точки для вертикального отрезка ',line )
    if line[0][1] > line [1][1]:
        line[0][1], line [1][1] = line [1][1], line [0][1]
    for i in range(line[0][1],line[1][1]+1):
        # print('Новая точка ',i,  line[0][1])
        points.append((line[0][0], i))
    # print(f' {points=}')
    draw_map(points)


def calc_hydrotermal(points):
    for line in points:
        if line[0][1] == line[1][1]:
            # print(f'Horizontal {line=} {line[0][1]=} {line[0][1]=}')
            calculate_points_horizontal(line)
        elif line[0][0] == line[1][0]:
            calculate_points_vertical(line)
            # print(f'Vertical {line=} {line[0][0]=} {line[1][0]=}')
        else:
            pass
            # print(f'N/A {line=}')



def print_map(water_map):
    for line in water_map:
        for coord in line:
            print(coord, end='  ')
        print()


# filename = 'test-input.txt'
filename = 'input.txt'
data = load_data(filename)
print(data)
water_map = create_map(data)
print_map(water_map)
result = calc_hydrotermal(data)
print(water_map)
my_count = 0
for line in water_map:
    for val in line:
        if val >=2:
            my_count += 1
print(my_count)
