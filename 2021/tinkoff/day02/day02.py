class SetWithSum:
    def __init__(self, s):
        self._items = list(s)
        self._sum = sum(s)

    def add(self, x):
        self._items.append(x)
        self._sum += x
        return self

    def clone(self):
        return SetWithSum(self.items())

    def items(self):
        return self._items

    def sum(self):
        return self._sum

    def __repr__(self):
        return f"<{self._sum},{self._items}>"

def load_data(filename='test.test'):
    with open(filename) as f:
        rope_count, height = f.readline().strip().split()
        ropes = f.readline().strip().split()
        ropes = [int(x) for x in ropes]
    print(rope_count, height)
    print(ropes)
    return ropes, int(height)


def find_sum(s, T, eps):
    s = list(sorted(s))
    L = [SetWithSum([s[0]])]
    n = len(s)
    delta = eps*T/n
    for x in s[1:]:
        U = L
        U.extend([ l.clone().add(x) for l in L])
        U = sorted(U, key=SetWithSum.sum)
        y = U[0]
        L = [y]
        for z in U:
            if (y.sum()+delta) < z.sum() and z.sum() <= T:
                y = z
                L.append(y)
    return max(L, key=SetWithSum.sum)

def find_sum2(ropes, height):
    ropes = sorted(ropes, reverse=True)
    # print(ropes)
    total = 0
    knots = 0
    for rope in ropes:
        if total >= height:
            print(f'{total} >= {height}')
            break
        print(f'{total} < {height}')
        total += rope
        knots += 1
    print(f'{total=} {knots=}')

ropes, height = load_data('advent_3.test')
find_sum2(ropes, height)
# print(find_sum(ropes, height, 1))



