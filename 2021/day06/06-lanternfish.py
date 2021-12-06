def load_data(filename):
    with open(filename) as f:
        data = f.readline()
        data = data.strip()
        data = data.split(',')
        data = [int(x) for x in data]
        return data


def genearte_fishes(data, days=256):
    print('Initial state: ', data)
    yung_fishes_index = []
    for i in range(days):
        for fish in range(len(data)):
            if data[fish] == 0:
                data[fish] = 6
                data.append(8)
            else:
                # print(f'yes {data[fish]=}')
                data[fish] -= 1
        # print('After', i + 1, ' day:', data)
    return data


# filename = 'test-input.txt'
filename = 'input.txt'

data = load_data(filename)
data2 = genearte_fishes(data)
print(len(data2))
