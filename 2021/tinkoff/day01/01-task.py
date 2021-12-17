def gcd(x, y):
    """
         Евклидов алгоритм для нахождения наибольшего общего делителя двух чисел
         : параметр х: первое число
         : param y: второе число
         : return: наибольший общий делитель
    """
    # Держите большие числа первыми
    if y > x:
        x, y = y, x
    if y == 0:
        return x
        # Рекурсивный вызов, формула: gcd (a, b) = gcd (b, a% b) {a> b}
    return gcd(y, x % y)


def lcm(x, y):
    """
    Вычислить наименьшее общее кратное из двух чисел
         : параметр х: первое число
         : param y: второе число
         : return: наименее распространенный кратный
    """
    # Формула: наименьшее общее кратное a, b равно наибольшему общему делителю a * b, деленному на a, b
    return int(x * y / gcd(x, y))


up_button = 61429526
down_button = 61430729

all = (up_button + down_button)
dif_1 = all + up_button
dif_2 = all + down_button
if dif_1 < dif_2:
    print(dif_1)
else:
    print(dif_2)
# print(f'{dif_1=} {dif_2=}')

window_lenght = 945747
point = 130713

first_car_time = (window_lenght) * 2

second_car_time = (window_lenght - point) * 2
print(f'{first_car_time=} {second_car_time=}')


print(lcm(first_car_time, second_car_time))

# while True:
#     if first_car_time % second_car_time == 0:
#         print(first_car_time)
#         exit()
#     first_car_time += second_car_time
#     second_car_time += second_car_time

# 200498364
