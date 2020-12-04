import collections
c = collections.Counter


def get_passports_data(filename, ignore_params=0):
    pattern = ':'
    regex = '(\w+):(.+)'
    passport = {}
    base_of_passports = []
    with open(filename) as f:
        for line in f:
            if line == '\n':
                base_of_passports.append(passport)
                #print('добавлен', passport)
                passport = {}
                continue
            line1 = line.replace('\n', '').split(' ')
            for item in line1:
                tmp_ = item.split(':')
                tmp_key = tmp_[0]
                tmp_value = tmp_[1]
                passport[tmp_key] = tmp_value
    return base_of_passports

def byr_validate(byr):
    try:
        if len(byr) != 4:
            print(byr)
        else:
            pass
            # c['byr'] += 1
        byr = int(byr)
        if byr >= 1920 and byr <= 2002:
            return True
        else:
            pass
            # c['byr'] += 1
            # print(byr, ' - не валидный')
    except Exception as err:
        # c['byr'] += 1
        print(err)


def iyr_validate(iyr):
    try:
        if len(iyr) != 4:
            print(iyr)
        iyr = int(iyr)
        if iyr >= 2010 and iyr <= 2020:
            return True
        return False
    except Exception as err:
        print(iyr, ' - не валидный')
        return False

def eyr_validate(eyr):
    try:
        if len(eyr) != 4:
            print(eyr)
        eyr = int(eyr)
        if eyr >= 2020 and eyr <= 2030:
            return True
        return False
    except Exception as err:
        print(eyr, ' - не валидный')
        return False

def hgt_validate(hgt):
    if 'cm' in hgt:
        hgt_ = hgt.replace('cm', '')
        # print(hgt_)
        if (int(hgt_) >=150) and (int(hgt_)<=193):
            # print('Норм! СМ')
            return True
    elif 'in' in hgt:
        hgt_ = hgt.replace('in', '')
        if int(hgt_) >=59 and int(hgt_)<=76:
            # print('Норм! Дюймы')
            return True
    else:
        print(hgt, 'Не валидный')
        return False

def hcl_validate(hcl):
    if hcl[0] == '#':
        if len(hcl) == 7:
            for i in range(1,8):
                if hcl[i] in '0123456789abcdef':
                    return True
    return False

def ecl_validate(ecl):
    if ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return True
    return False

def pid_validate(pid):
    if len(pid) == 9:
        try:
            pid_is_number = int(pid)
            if isinstance(pid_is_number, int):
                return True
        except:
            print('ошибка', pid)


def passport_validator(passport_list):
    # принимает список паспортов, и возвращает колличество правильных (все поля кроме CID)
    valid_passport_count = 0
    byr_err_count = 0
    iyr_err_count = 0
    eyr_err_count = 0
    hgt_err_count = 0
    hcl_err_count = 0
    ecl_err_count = 0
    pid_err_count = 0

    for passport in passport_list:
        try:
            if passport['byr']:
                if byr_validate(passport['byr']):
                    if passport['iyr']:
                        if iyr_validate(passport['iyr']):
                            if passport['eyr']:
                                if eyr_validate(passport['eyr']):
                                    if passport['hgt']:
                                        if hgt_validate(passport['hgt']):
                                            if passport['hcl']:
                                                if hcl_validate(passport['hcl']):
                                                    if passport['ecl']:
                                                        if ecl_validate(passport['ecl']):
                                                            if passport['pid']:
                                                                if pid_validate(passport['pid']):
                                                                    valid_passport_count += 1
                                                                else:
                                                                    pid_err_count += 1
                                                        else:
                                                            ecl_err_count += 1
                                                else:
                                                    hcl_err_count += 1
                                        else:
                                            hgt_err_count += 1
                                else:
                                    eyr_err_count += 1
                        else:
                            iyr_err_count += 1
                else:
                    byr_err_count += 1

        except Exception as ex:
            pass
    print('Невалидных byr:', byr_err_count)
    print('Невалидных iyr:', iyr_err_count)
    print('Невалидных eyr:', eyr_err_count)
    print('Невалидных hgt:', hgt_err_count)
    print('Невалидных hcl:', hcl_err_count)
    print('Невалидных ecl:', ecl_err_count)
    print('Невалидных pid:', pid_err_count)
            # print('ошибка', ex)

    print('Проверено ', len(passport_list), 'паспортов. Число валидных:', valid_passport_count)
    return valid_passport_count

data = get_passports_data('input.txt')
print('Всего загружено - ', len(data), 'паспортов.')
passport_validator(data)
