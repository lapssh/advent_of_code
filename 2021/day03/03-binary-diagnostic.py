def load_data(file):
    with open(file) as f:
        data = f.readlines()
        data = [line.strip() for line in data]  # убираем переносы строк
        return data


def binary_diagnostic(data):
    result = []
    print(f'{data[0]=}')
    print(f'{len(data[0])=}')
    len_data = (len(data[0]))
    mediana = len(data) // 2
    print(f'{mediana=}')
    for i in range(len_data):
        result.append(((sum([int(x[i]) for x in data]))))
    print(f'{result=}')
    inversed_result = []
    for i in range (len_data):
        if result[i] > mediana:
            result[i] = 1
            inversed_result.append(0)
        else:
            result[i] = 0
            inversed_result.append(1)
    print(f'{result=}')
    print(f'{inversed_result=}')
    gamma_rate = [''.join(map(str, result))]
    epsilon_rate = [''.join(map(str, inversed_result))]
    print(f'{gamma_rate=}')
    gamma_rate_dec = int(gamma_rate[0], base=2)
    epsilon_rate_dec = int(epsilon_rate[0], base=2)
    print(f'{gamma_rate_dec=}')
    print(f'{epsilon_rate_dec=}')
    gamma_rate_bin =bin(gamma_rate_dec)
    print(f'{gamma_rate_bin=}')
    # gamma_rate_bin = ~(gamma_rate_bin)
    print('aswer = ', gamma_rate_dec * epsilon_rate_dec)

#                       E T A L O N
#     counters = [Counter(bits) for bits in zip(*lines)]
#     gamma, epsilon = [int(''.join(c.most_common()[pos][0] for c in counters), base=2) for pos in [0, -1]]



data = load_data('test_input.txt')
print(data)
binary_diagnostic(data)

data = load_data('input.txt')
print(data)
binary_diagnostic(data)
