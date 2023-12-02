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
    for res in game:
        red = 0
        green = 0
        blue = 0
        red += res[0]
        green += res[1]
        blue += res[2]
        if red > RED or green > GREEN or blue > BLUE:
            return False
    return True

def game_is_valid2(game):
    # дастём игру по ID
    game = games[game]['results']
    max_red = 0
    max_green = 0
    max_blue = 0
    for res in game:
        # print(res)
        if res[0] > max_red:
            max_red = res[0]
        if res[1] > max_green:
            max_green = res[1]
        if res[2] > max_blue:
            max_blue = res[2]
        # print(f'{max_red=} {max_green=} {max_blue=}')
    multi = max_red * max_green * max_blue
    return multi


def part1(games):
    # необходимо посчиать сумму ID возможных игры.
    acc = 0
    # print(f'Всего было сыграно {len(games)} игр')
    for game in games:
        # print(game)
        if game_is_valid(game):
            # print(game, ' - ', games[game]['results'])
            acc += game
    # print(f'{acc=}')
    return acc

def part2(games):
    acc = 0
    for game in games:
        acc += game_is_valid2(game)
    return acc

data = load()
# data = load(file='test.txt')
games = adv_load(data)
print('Part1 result:', part1(games))  # 2551
print('Part2 result:', part2(games))  # 62811
