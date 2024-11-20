def load(file='day03_input.txt'):
    with open(file, "rt") as f:
        return list(int(x) for x in f.readline().split(','))


def part1(data):
    print(data)


if __name__ == '__main__':
    data = load()
    part1(data)
