def to_jaden_case(string):
    new_str = []
    my_str = string.split(' ')
    for word in my_str:
        new_str.append(word.capitalize())
    jaden_say = ' '.join(new_str)
    return jaden_say


a = to_jaden_case('hell how are you?')
print(a)
