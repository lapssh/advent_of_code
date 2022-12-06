def load_data(filename='input.txt'):
    with open(filename) as f:
        data = f.readlines()
    cleaned_data = [x.strip() for x in data]
    return cleaned_data[0]


def check_uniq(s):
    s_list = list(s)
    s_set = set(s)
    # print(f'{len(s_list)=}  {len(s_set)=}')
    if len(s_list) == len(s_set):
        return True


def find_packet(packet, length=4):
    for i in range(len(packet)):
        s = packet[i:length + i]
        if not check_uniq(s):
            continue
        else:
            # print('нашёл!', i+length)
            return i + length


signal = load_data()
print('Result part 1:', find_packet(signal))
print('Result part 2:', find_packet(signal, length=14))
