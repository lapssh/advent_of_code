from itertools import cycle

# instr, data = open('test.txt').read().split('\n\n')
instr, data = open('input.txt').read().split('\n\n')
# print(instr, data)
data = [x.split(' = ') for x in data.splitlines()]
print(data)
data = {a: b[1:-1].split(', ') for a, b in data}
print(data)

curr = 'AAA'
for count, d in enumerate(cycle(instr), start=1):
    curr = data[curr][d == "R"]
    if curr == "ZZZ":
        print(count)
        break