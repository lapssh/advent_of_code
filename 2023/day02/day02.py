import re

RED = 12
GREEN = 13
BLUE = 14


def load(file='input.txt'):
    with open(file, "rt") as f:
        return list(line.strip() for line in f.readlines())


def adv_load(data):
    games = {
    }
    for game in data:
        line = game.split(':')
        game_number = int(line[0].split()[1])
        # print(f'Game {game_number}: \n=============================')
        games[game_number] = 'test'
        games[game_number] = {'results': []}
        # print(f'{games=}')
        # print(line[1])
        casts = line[1].split(';')
        # print(casts)
        # раскрываем броски в одной игре

        for cast in casts:
            # print(cast)
            tmp_casts = cast.split(',')
            # print(f'{tmp_casts=}')
            red, green, blue = 0, 0, 0
            for tmp_cast in tmp_casts:
                _ = tmp_cast.split()
                line_color = _[1]
                line_value = int(_[0])
                match line_color:
                    case 'red':
                        red += line_value
                    case 'green':
                        green += line_value
                    case 'blue':
                        blue += line_value
                # print(f'{tmp_cast=}')
                # print(f'{red=}  {green=}   {blue=}')
            # сохраняем результаты броскa
            games[game_number]['results'].append([red, green, blue])
            # print(games[game_number]['results'])
    return games

def game_is_valid(game):
    # дастём игру по ID
    game = games[game]['results']
    red = 0
    green = 0
    blue = 0
    # print(game)
    for res in game:
        red = 0
        green = 0
        blue = 0
        # print(res)
        red += res[0]
        green += res[1]
        blue += res[2]
        if red > RED or green > GREEN or blue > BLUE:
            return False
    # print(f'{red=}  {green=}  {blue=}')
    # if red > RED or green > GREEN or blue > BLUE:
    #     # print('FALSE')
    #     return False
    # elif green > GREEN:
    #     # print('FALSE')
    #     return False
    # elif blue > BLUE:
    #     # print('FALSE')
    #     return False
    return True
def part1(games):
    # необходимо посчиать сумму ID возможных игры.
    acc = 0
    print(f'Всего было сыграно {len(games)} игр')
    for game in games:
        # print(game)
        if game_is_valid(game):
            print(game, ' - ', games[game]['results'])
            acc += game
    # print(f'{acc=}')
    return acc

data = load()
# data = load(file='test.txt')
games = adv_load(data)
print('Part1:', part1(games))  # 101 - не парвильно
