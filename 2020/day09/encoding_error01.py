PREAMBLE = 25
data = [
    35,
    20,
    15,
    25,
    47,
    40,
    62,
    55,
    65,
    95,
    102,
    117,
    150,
    182,
    127,
    219,
    299,
    277,
    309,
    576
]

def get_data(filename):
    with open(filename, 'r') as f:
        data = list(f.readlines())
    data = [int(x.replace('\n', '')) for x in data]
    return data

def get_preamble(data, index):
    preamble = data[index-PREAMBLE:index]
    return preamble

def is_valid(number, preamble):
    flag = False
    for num in preamble:
        for num2 in preamble:
            if num != num2:
                if num + num2 == number:
                    # print(f'{num=} + {num2=} = {number} --->>> True')
                    flag = True
        # if flag == True:
            # print(f'{num} + {num2} = {number} --->>> True')
        # else:
            # print(f'{num} + {num2} ни разу не равно {number} --->>> False')
    # print(f'{flag=}')
    return flag



data = get_data('input.txt')
index = PREAMBLE
preamble = get_preamble(data,index)
while index < len(data):
    not_valid = is_valid(data[index], preamble)
    if not not_valid:
        print(f'Result: {data[index]} by {index=}')
        exit()
    index += 1
    preamble = get_preamble(data, index)
