def get_map(filename):
    with open(filename) as f:
        passwords = f.readlines()
    passwords2 = [x.replace('\n', '') for x in passwords]
    return passwords2

def look_trees(right, down):
    forest_map = get_map('input.txt')
    len_line = len(forest_map[0])  # 31
    finish_line = len(forest_map)  # 323
    x, y = 0, 0  # start point
    forest_count = 0


    while y != finish_line - 1:
        if x + right >= len_line:
            x = (x + right) - (len_line)
        else:
            x = x + right
        y += down
        if forest_map[y][x] == '#':
            forest_count += 1
            forest_map[y] = forest_map[y][:x] + 'X' + forest_map[y][x + 1:]
        else:
            forest_map[y] = forest_map[y][:x] + 'O' + forest_map[y][x + 1:]
        #print(forest_map[y], y)
    print('При шаге Right =', right, 'Down =', down, 'Олени словили', forest_count, 'деревьев.')

look_trees(1, 1)
look_trees(3, 1)
look_trees(5, 1)
look_trees(7, 1)
look_trees(1, 2)

# Solution 61*257*64*47*37 = 1744787392
