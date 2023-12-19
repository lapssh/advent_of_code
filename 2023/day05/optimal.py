seeds, *mappings = open('input.txt').read().split('\n\n')
seeds = seeds.split(": ")[1]
seeds = [int(x) for x in seeds.split()]

for m in mappings:
    _, *ranges = m.splitlines()
    ranges = [[int(x) for x in r.split()] for r in ranges]
    ranges = [(range(a, a + c), range(b, b + c)) for a, b, c in ranges]


    def translate(x):
        for a, b in ranges:
            if x in b:
                return a.start + x - b.start
        return x


    seeds = [translate(x) for x in seeds]

print(min(seeds))
