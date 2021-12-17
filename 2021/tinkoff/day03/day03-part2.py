def load_data(filename='test2.test'):
    with open(filename) as f:
        lines_count, order = f.readline().strip().split()
        passwords = f.readlines()
        passwords = [x.strip() for x in passwords]
        new_passwords = []
        for i in passwords:
            if len(i) == 1:
                new_passwords.append(int(i))
            else:
                tmp = i.split()
                tmp = [int(x) for x in tmp]
                new_passwords.append(tmp)
    print(lines_count, order, new_passwords)
    return lines_count, new_passwords


def generate_passwords(passwords):
    combinations = [0]
    for line in passwords:
        if type(line) != int:
            numbers = list(line)
            print(numbers)
            for num in numbers:
                print(f'{num=} {combinations=}')
                new_combinations = []
                for pwd in combinations:
                    pwd2 = str(pwd)+str(num)
                    new_combinations.append(pwd2)
                combinations = new_combinations
                # combinations.append(_)
            print(f'{combinations=}')



lines_count, passwords = load_data()
generate_passwords(passwords)