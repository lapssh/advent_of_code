# Each policy actually describes two positions in the password, where 1 means the first character,
# 2 means the second character, and so on. (Be careful; Toboggan Corporate Policies have no concept of "index zero"!)
# Exactly one of these positions must contain the given letter. Other occurrences of the letter are irrelevant for the
# purposes of policy enforcement.
#
# Given the same example list from above:
#
# 1-3 a: abcde is valid: position 1 contains a and position 3 does not.
# 1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
# 2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.
# How many passwords are valid according to the new interpretation of the policies?


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
    from_num = int(tmp[0][0])
    to_num = int(tmp[0][1])
    letter = tmp[0][2]
    word = tmp[0][3]
    tmp_count = word.count(letter)
    # if (tmp_count >= from_num) and (tmp_count <= to_num):
    if str(word[from_num-1]) != str(word[to_num-1]):
        if letter == str(word[from_num-1]) or letter == str(word[to_num-1]):
            print(f'{(word[from_num-1])=}, " != " ,  {str(word[to_num-1])=}')
            valid_count += 1
            print(valid_count, ' - ', from_num, to_num, letter, word, )
print('Всего паролей: ', len(passwords))
print('Всего правильных паролей: ', valid_count) # 375 714 - не верные ответы
# Solution 502
