import re
def get_dict(filename):
    with open(filename) as f:
        passwords = f.readlines()
    passwords2 = [x.replace('\n', '') for x in passwords]
    return passwords2

#print(get_dict('input.txt'))
valid_count = 0
passwords = get_dict('input.txt')
for password in passwords:
    pattern = '(\d+)-(\d+) (\w+): (\w+)'
    #regex = re.compile(pattern='(\d+-\d+) (\w+:) (\w+)')
    tmp = re.findall(pattern, password)
    #print(tmp)
    from_num = int(tmp[0][0])
    to_num = int(tmp[0][1])
    letter = tmp[0][2]
    word = tmp[0][3]
    print(from_num, to_num, letter, word)
    tmp_count = word.count(letter)
    if (tmp_count >= from_num) and (tmp_count <= to_num):
        valid_count += 1
print('Всего правильных паролей: ', valid_count) # 548
