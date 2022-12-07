def load_data(filename='input.txt'):
    with open(filename) as f:
        data = f.readlines()
    cleaned_data = [x.strip() for x in data]
    return cleaned_data


def build_fs(data):
    root = []
    for line in data:
        print(f'{line=}')
    return 1, fs


data = load_data('test.txt')
print(data)
commands, fs = build_fs(data)

# root = []
# a = {'type': 'dir', 'content': []}
# e = {'type': 'dir', 'content': []}
# i = {'type': 'file', 'size': 584}
#
# root.append(a)
# root[0]['content'].append(i)
# print(root[0]['content'])

