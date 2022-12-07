def load_data(filename='input.txt'):
    with open(filename) as f:
        data = f.readlines()
    cleaned_data = [x.strip() for x in data]
    return cleaned_data


def build_fs(data):
    root = []
    for line in data:
        pass
        # print(f'{line=}')
    return 1, root


data = load_data('test.txt')
print(data)
commands, fs = build_fs(data)


class directory():
    def __init__(self, name):
        self.name = name
        self.content = []
        self.size = 0


root = directory('/')
print(root.name)

root = []
obj1 = {'name': 'a', 'type': 'dir', 'size': 0, 'content': []}
obj2 = {'name': 'b.txt', 'type': 'file', 'size': 14848514, 'content': None}
obj3 = {'name': 'c.dat', 'type': 'file', 'size': 8504156, 'content': None}
obj4 = {'name': 'd', 'type': 'dir', 'size': 0, 'content': []}
obj5 = {'name': 'd.log', 'type': 'file', 'size': 8033020, 'content': None}

root.append(obj1)
root.append(obj2)
root.append(obj3)
root.append(obj4)
root[3]['content'].append(obj5)

print(root)




