def load_data(filename='input.txt'):
    with open(filename) as f:
        data = f.readlines()
    cleaned_data = [x.strip() for x in data]
    return cleaned_data


def create_matrix(data):
    width = len(data[0])
    height = len(data)
    print(f'Ширина леса: {width}    Высота леса: {height}')
    forest = []

    for y in range(height):
        line = []
        for x in range(width):
            line.append(int(data[y][x]))
        forest.append(line)
    return forest


def print_forest(forest):
    for y in forest:
        for x in y:
            print(str(x)+'  ', end='')
        print()


def find_tall_tree(forest):
    # line - линия, tree - дерево
    tall_tree_sum = 0
    for i_line, line in enumerate(forest):
        for i_tree, tree in enumerate(line):
            # проверим есть ли слева или справа дерево?
            if i_tree == 0 or i_tree ==len(line)-1:
                print(f'{tree=} по бокам пусто')
                tall_tree_sum += 1
            # проверим есть ли сверху или снизу дерево?
            elif i_line == 0 or i_line == len(forest)-1:
                print(f'{tree=} сверху или снизу пусто')
                tall_tree_sum += 1
            else:
                # проверим есть ли деревья по бокам выше
                left = line[:i_tree]
                right = line[i_tree+1:]
                # print(f'{"".join(map(str, left))} +[{tree}]+ {"".join(map(str, right))}')
                if tree > max(left) or tree > max(right):
                    tall_tree_sum += 1
                    print(f'$ {"".join(map(str, left))} +[{tree}]+ {"".join(map(str, right))}')
                    print(f'{tree=}   {max(left)=}     {max(right)=}')
                    # print('Моё деревце выше!')
                    continue
                else:
                    # проверим есть ли деревья по вертикали выше
                    vertical =[]
                    for _ in forest:
                        vertical.append(_[i_tree])
                    # print('Вертикаль ', vertical, tree, i_line, i_tree)
                    up = vertical[:i_line]
                    down = vertical[i_line:]
                    # print(f'сверху {up}  +[{tree}]+   {down} снизу')
                    if tree > max(up) or tree > max(down):
                        tall_tree_sum += 1
                        # print(f'$ {"".join(map(str, up))} +[{tree}]+ {"".join(map(str, down))}')
            # if x
            # pos = x, y
        print()
    return tall_tree_sum


# print(load_data('test.txt'))
# data =load_data('test.txt')
# data =load_data('test2.txt')
data =load_data('input.txt')
forest = create_matrix(data)
# print(forest)
# print_forest(forest)
print('Деревьев в лесу:', find_tall_tree(forest))
