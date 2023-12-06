def load(file='input.txt'):
    with open(file, "rt") as f:
        return list(line.strip() for line in f.readlines())


# time, distance = load('test.txt')[0].split(':')[1], load('test.txt')[1].split(':')[1]
time, distance = load()[0].split(':')[1], load()[1].split(':')[1]
time = [int(x) for x in time.split()]  # 7 15 30
distance = [int(x) for x in distance.split()]  # 9 40 200
# print(time, distance)


def min_time_for_race(race):
    t = race[0]
    d = race[1]  # record
    # print(t, d)
    count_wins = 0
    for seconds in range(t+1):
        speed = seconds
        other_time = t-seconds
        dist = speed * other_time
        # print(f'{seconds=} {speed=} {other_time=} {dist=}')
        if dist > d:
            count_wins += 1
    # print(f'{count_wins=}')
    return count_wins

def part1(time, distance):
    # высчитываем оптимальное время для каждой гонки
    race = 0
    race01 = (7, 9)
    count_wins = 1
    # print(min_time_for_race(race01))
    for race in range(len(distance)):
        count_wins *= min_time_for_race((time[race], distance[race]))
        pass
    # print(count_wins)
    return count_wins
print(f'Part result: {part1(time, distance)}')
