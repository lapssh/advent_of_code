def validate_inn(inn):
    inn = int(inn)
    if inn > 0:
        while inn:
            if (inn % 10) in range(0, 10):
                inn = inn // 10
            else:
                return False
        return True
    else:
        return False



inn = input('Введите ИНН организации: ')
valid = validate_inn(inn)
print(f'ИНН {inn} является {('не является') if not valid else 'является'} корректным.')
