def get_passports_data(filename, ignore_params=0):
    pattern = ':'
    regex = '(\w+):(.+)'
    passport = {}
    base_of_passports = []
    with open(filename) as f:
        for line in f:
            if line == '\n':
                base_of_passports.append(passport)
                print('добавлен', passport)
                passport = {}
                continue
            line1 = line.replace('\n', '').split(' ')
            for item in line1:
                tmp_ = item.split(':')
                tmp_key = tmp_[0]
                tmp_value = tmp_[1]
                passport[tmp_key] = tmp_value
    return base_of_passports


def passport_validator(passport_list):
    # принимает список паспортов, и возвращает колличество правильных (все поля кроме CID)
    valid_passport_count = 0
    for passport in passport_list:
        try:
            if passport['byr']:
                if passport['iyr']:
                    if passport['eyr']:
                        if passport['hgt']:
                            if passport['hcl']:
                                if passport['ecl']:
                                    if passport['pid']:
                                        valid_passport_count += 1
        except Exception as ex:
            print('ошибка', ex)

    print('Проверено ', len(passport_list), 'паспортов. Число валидных:', valid_passport_count)
    return valid_passport_count

data = get_passports_data('input.txt')
print('Всего загружено - ', len(data), 'паспортов.')
passport_validator(data)
