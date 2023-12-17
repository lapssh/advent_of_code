import re

lines = open("input.txt").read().splitlines()
ans = 0
for i, line in enumerate(lines):
    for m in re.finditer(r"\d+", line):
        # idx contains neighbours
        idxs = [(i, m.start() - 1), (i, m.end())]  # left, right
        idxs += [(i - 1, j) for j in range(m.start() - 1, m.end() + 1)]  # row above
        idxs += [(i + 1, j) for j in range(m.start() - 1, m.end() + 1)]  # row below
        count = sum(0 <= a < len(lines) and 0 <= b < len(lines[a]) and lines[a][b] != "." for a, b in
                    idxs)  # special char nearby within bounds
        if count > 0:
            ans += int(m.group())
print(ans)
