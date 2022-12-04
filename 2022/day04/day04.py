def load_data(filename):
    with open(filename) as f:
        data = f.readlines()
    cleaned_data = [x.strip() for x in data]
    return cleaned_data


def part1(data):
    score = 0
    for elf in data:
        elf1, elf2 = elf.split(',')
        elf1_1, elf1_2 = elf1.split('-')
        elf2_1, elf2_2 = elf2.split('-')
        if int(elf1_1) <= int(elf2_1):
            if int(elf1_2) >= int(elf2_2):
                score += 1
                print(f'{elf1=} {elf2=} {score=}')
        else:
            if int(elf2_1) <= int(elf1_1):
                if int(elf2_2) >= int(elf1_2):
                    score += 1
                    print(f'{elf1=} {elf2=} {score=}')
    return score


# filename = 'test.txt'
filename = 'input.txt'
clean_data = load_data(filename)
print(clean_data)
part1_result = part1(clean_data)
print('part1 result: ', part1_result)
