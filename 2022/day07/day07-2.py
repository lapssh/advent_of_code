from collections import defaultdict

sizes_dict = defaultdict(int)
path = []

# part1
with open("input.txt", "r") as file:
    # with open("test.txt", "r") as file:
    for line in file.readlines():
        line = line.strip()
        part = line.split(' ')
        print(f'Строка {part=}')
        if part[1] == 'cd':
            if part[2] == '..':
                path.pop()
            else:
                path.append(part[2])
                print(f'{path=}')
        elif part[1] == 'ls':
            continue
        elif part[0] == 'dir':
            continue
        else:
            size = int(part[0])
            print('У нас файл размером', size)
            for i in range(1, len(path) + 1):
                sizes_dict['/'.join(path[:i])] += size
                print(sizes_dict)

total = sizes_dict['/']
print(f'{total=}')
print(f'{sizes_dict=}')
part1 = 0
for k, v in sizes_dict.items():
    if v <= 100000:
        part1 = part1 + v

print(part1)

# part2

max_used = 70000000 - 30000000
to_free_up = total - max_used
part2 = 1000000000

for k, v in sizes_dict.items():
    if v > to_free_up:
        part2 = min(part2, v)

print(part2)
