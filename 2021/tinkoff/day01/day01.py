def part1(up: int, down: int) -> int:
    total = up + down
    return min(up, down) + total


def part2(window_len: int, point: int) -> int:
    left_time = point * 2
    right_time = (window_len - point) * 2

    if left_time == right_time:
        return left_time

    return _lcm(left_time, right_time)


def _gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def _lcm(a, b):
    return a * b // _gcd(a, b)  


#---------------------------------------------------------------------------------------


def test(expected, actual):
    assert expected == actual, f'Expected: {expected}, Actual: {actual}'


test(3, part1(up=1, down=1))
test(6, part2(window_len=4, point=1))


print('Day 01, part 1: %r' % (part1(up=61429526, down=61430729)))
print('Day 01, part 2: %r' % (part2(window_len=945747, point=130713)))
