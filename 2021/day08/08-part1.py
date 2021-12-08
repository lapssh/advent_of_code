def load_data(filename = 'test-input.txt'):
    with open(filename) as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
    print(lines)
    return lines


def get_output_data(data):
    output_data = []
    print(data)
    for i in data:
        tmp = i.split('|')
        tmp = tmp[1].strip()
        output_data.append(tmp)
    return output_data


def calc_uniq_values(data):
    uniq_count = 0
    lines_with_eight = 0
    for output in data:
        tmp = output.split()
        for i in tmp:
            len_tmp = len(i)
            print(f'{i=} {len_tmp=}')
            if len_tmp == 2 or len_tmp == 3 or len_tmp == 4 or len_tmp == 7:
                uniq_count += 1
    print(uniq_count)
    print(f'{lines_with_eight=}')

# source = load_data()
source = load_data('input.txt')
print(source)
output_values = get_output_data(source)
print(output_values)
calc_uniq_values(output_values)