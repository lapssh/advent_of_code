# How many bag colors can eventually contain at least one shiny gold bag?
import re

MY_BAG = 'shiny gold'

top_count = 0
colors_bags = []

def get_input(filename):
    # return list of rules
    with open(filename, 'r', encoding='utf-8') as f:
        data = f.read()
    data = list(data.strip().split('\n'))
    return data


def get_test_input():
    data = [
        'light red bags contain 1 bright white bag, 2 muted yellow bags.',
        'dark orange bags contain 3 bright white bags, 4 muted yellow bags.',
        'bright white bags contain 1 shiny gold bag.',
        'muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.',
        'shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.',
        'dark olive bags contain 3 faded blue bags, 4 dotted black bags.',
        'vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.',
        'faded blue bags contain no other bags.',
        'dotted black bags contain no other bags.']
    return data


def parse_rule(rule):
    # делим правило на две части
    result = re.split(' bags contain ', rule)

    key_color = result[0]  # получаем ключ-значение по цвету
    if result[1] == 'no other bags.':
        val_color = 'STOP'
        parsed_rule = {key_color: val_color}
        return parsed_rule
    else:
        # если сумка может содержать другие
        val_list = []
        val_color = result[1].split(',')
        if len(val_color) == 1:  # если внутри только одно правило
            val_color = val_color[0]
            pattern = '(\d+) (\w+ \w+) bag'
            reresult = re.match(pattern, val_color)
            bag_count = reresult.group(1)
            bag_color = reresult.group(2)
            parsed_rule = {key_color: [{bag_color: int(bag_count)}]}
            return parsed_rule
        else:  # если внутри несколько правил
            for bag in val_color:
                pattern = '(\d+) (\w+ \w+) bag'
                bag = bag.strip()
                reresult = re.match(pattern, bag)
                bag_count = reresult.group(1)
                bag_color = reresult.group(2)
                bag_dict = {bag_color: int(bag_count)}
                val_list.append(bag_dict)

            parsed_rule = {key_color: val_list}
            return parsed_rule


def create_rules(list_of_rules):
    # создаем список правил, формата : [цвет: [{цвет: счётчик}]]
    advanced_rules = []
    for rule in list_of_rules:
        parsed_rule = parse_rule(rule)
        # print(parsed_rule)
        advanced_rules.append(parsed_rule)
    return advanced_rules


def calculate_my_bag_count(count, rules):
    for rule in rules:
        print(f'Пришло правило: {rule}')
        if rule.values() != 'STOP':
            for i in rule.keys():
                tmp_key = i  # достаём ключ
                print(f'{tmp_key=}')
                if tmp_key == MY_BAG:
                    count += 1
                    calculate_my_bag_count(count, [])

    return print(f'{count=}')


def calculate_how_many(count, rules, bag_list):
    global top_count
    global colors_bags
    # Сколько внутри цветов? Должно вернуть 4

    if isinstance(rules, list): # Если мы получили список правил
        print('Вот пришёл список правил', rules)
        print(f'Мы будем искать список {bag_list}')
        for bag in bag_list:
            for rule in rules:
                if bag in rule:
                    items_count = len(rule.values())
                    print(f'В {rule.values()=} находится {items_count=}')

                    print()
                    print(f'Ага, в {rule=} имеется сумка {bag=} ')
                    tmp_ = rule.values()
                    bag_list = []
                    for v in tmp_:
                        print(f'{v=}', type(v))
                        for bag2 in v:
                            if v == 'STOP':
                                break
                            # if isinstance(bag, str):
                            #     print(bag, 'пришло в Bag - >>> Exit')
                            #     break
                            # print(bag2)
                            bag3 = list(bag2.keys())[0]
                            # print(f'{bag3=}')
                            bag_list.append(bag3)
                            count += 1
                            print(f'увеличиваем счетчик на 1 и теперь он {count=}')
                            colors_bags.append(bag3)
                            print(f'{bag_list=}')
                    calculate_how_many(count, rules,bag_list)
                # print(f'{count=}')
    else:
        print('А вот пришёл словарик')
    print('Финальный count', count)
    if top_count < count:
        top_count = count
    return count

def collect_colors(adv_rules, bag_list):
    global colors_bags
    for bag in bag_list:
        for rule in adv_rules:
            if bag in rule:
                print(f'{bag=}  {rule=}')
                tmp_ = rule.values()
                print(f'{tmp_=}')
                for v in tmp_:
                    print(f'{v=}')
                    for bag2 in v:
                        if v == 'STOP':
                            break
                        bag_list = []
                        print(bag2)
                        bag3 = list(bag2.keys())
                        print(f'{bag3=}')
                        colors_bags.append(bag3[0])
                        print(f'Добавлена {bag3[0]=} в список')
                        bag_list.append(bag3[0])
                        collect_colors(adv_rules, bag_list)


            # print(f'{rule=} {bag=}')
            # try:
            #     if bag in rule:
            #         print(f'{rule=} тут есть {bag=}')
            #         tmp_ = list(rule.values())
            #         print(tmp_[0])
            #         bag_list = []
            #         for t in tmp_[0]:
            #             bag_list.append(list(t.keys()))
            #             colors_bags.append(list(t.keys()))
            #         print(bag_list)
            #
            #         return collect_colors(adv_rules, bag_list)
            # except Exception as err:
            #     print(err, rule)


data = get_input('input.txt')

# test rules:
# data = get_test_input()

adv_rules = create_rules(data)
# calculate_my_bag_count(0, adv_rules)
# calculate_how_many(0, adv_rules)
print(adv_rules)
print(len(adv_rules), ' - вот сколько у нас правил')
# for rule in adv_rules:
#     if rule.get(MY_BAG):
#         my_bag_contain = rule.get(MY_BAG)
# print(my_bag_contain)
# answer = calculate_how_many(0, adv_rules, [MY_BAG])
# print(f'{answer=}, {top_count=}')
# print('Я заглянул в стеклянных шар, и увидел что ответ:', top_count)
# print(colors_bags)
# only_colors = []
# for color in colors_bags:
#     tmp_ = color.split()[1]
#     only_colors.append(tmp_)
# # only_colors = set(only_colors)
# print(only_colors)
# print(len(only_colors))



# only_color = [color[0] for color.split() in colors_bags]
collect_colors(adv_rules, [MY_BAG])
print(colors_bags)
print(len(colors_bags))
colors_bags = set(colors_bags)
print(len(colors_bags))


# wrong 116, 33