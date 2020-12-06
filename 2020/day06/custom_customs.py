def get_input(filename):
    with open(filename) as f:
        data = f.read()
    return data


def prepare_data(data):
    # print(f'{data=}')
    data2 = data.split('\n\n')
    # print(f'{data2=}')
    data3 = [x.replace('\n', '') for x in data2]
    # print(f'{data3=}')
    return data3


def get_count(data):
    count_ = 0
    # print(f'{data=}')
    for item in data:
        tmp_set = set(item)
        count_ += len(tmp_set)
        # print(f'для {tmp_set=} увечиливаем на {len(tmp_set)}  = {count_}')
    #
    print(count_)


data = get_input('input.txt')
data = prepare_data(data)
get_count(data)
