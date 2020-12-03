def get_map(filename):
    with open(filename) as f:
        passwords = f.readlines()
    passwords2 = [x.replace('\n', '') for x in passwords]
    return passwords2

forest_map = get_map('input.txt')
len_line = forest_map[0] #31
finish_line = len(forest_map) #323
x, y = 0, 0 # start point
forest_count = 0
print(forest_map[y])
while y != 322:
    if x == 28:
        x = 0
    elif x == 29:
        x = 1
    elif x == 30:
        x = 2
    else:
        x = x + 3
    y += 1
    if forest_map[y][x] == '#':
        forest_count += 1
        forest_map[y] = forest_map[y][:x] + 'X' + forest_map[y][x+1:]
    else:
        forest_map[y] = forest_map[y][:x] + 'O' + forest_map[y][x + 1:]
    print(forest_map[y], y)
print('Олени словили', forest_count, 'деревьев.')