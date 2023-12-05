def load(file='input.txt'):
    with open(file, "rt") as f:
        return list(line.strip() for line in f.readlines())


def make_int(raw_list):
    # print(raw_list)
    norm_list = []
    for el in raw_list:
        _ = el.split()
        norm_list.append([int(x) for x in _])
    # print(norm_list)
    return norm_list
def parse_data(raw):
    seeds = list([int(x) for x in raw[0].split(':')[1].split()])
    # print(f'{seeds=}')
    raw = raw[2:]
    # print(raw)
    idx_seed_to_soil = raw.index('seed-to-soil map:')
    idx_soil_to_fertilizer = raw.index('soil-to-fertilizer map:')
    # print(idx_seed_to_soil, idx_soil_to_fertilizer)
    seed_to_soil = raw[idx_seed_to_soil+1:idx_soil_to_fertilizer-1]
    seed_to_soil = make_int(seed_to_soil)
    # print(f'{seed_to_soil=}')
    idx_fertilizer_to_water = raw.index('fertilizer-to-water map:')
    fertilizer_to_water = raw[idx_soil_to_fertilizer+1:idx_fertilizer_to_water-1]
    fertilizer_to_water = make_int(fertilizer_to_water)
    # print(f'{fertilizer_to_water=}')
    idx_water_to_light = raw.index('water-to-light map:')
    idx_light_to_temperature = raw.index('light-to-temperature map:')
    water_to_light = raw[idx_water_to_light+1:idx_light_to_temperature-1]
    water_to_light = make_int(water_to_light)
    # print(f'{water_to_light=}')
    idx_temperature_to_humidity = raw.index('temperature-to-humidity map:')
    light_to_temperature = raw[idx_light_to_temperature+1:idx_temperature_to_humidity-1]
    light_to_temperature = make_int(light_to_temperature)
    # print(f'{light_to_temperature=}')
    idx_humidity_to_location = raw.index('humidity-to-location map:')
    temperature_to_humidity = raw[idx_temperature_to_humidity+1:idx_humidity_to_location-1]
    temperature_to_humidity = make_int(temperature_to_humidity)
    # print(f'{temperature_to_humidity=}')
    humidity_to_location = raw[idx_humidity_to_location+1:]
    humidity_to_location = make_int(humidity_to_location)
    # print(f'{humidity_to_location=}')
    result = {
        'seeds': seeds,
        'seed_to_soil': seed_to_soil,
        'fertilizer_to_water': fertilizer_to_water,
        'water_to_light': water_to_light,
        'light_to_temperature': light_to_temperature,
        'temperature_to_humidity': temperature_to_humidity,
        'humidity_to_location': humidity_to_location
    }
    return result


def map_generator(src, seeds):
    # print(src)
    ranges_src = []
    result = []
    for el in src:
        # print(f'{el=}')
        start_dst = el[0]
        start_src = el[1]
        lenght = el[2]
        range_src, range_dst = range(start_src, start_src+lenght), range(start_dst, start_src+lenght-1)
        ranges_src.append((range_src, range_dst))
        def seed_in_list(seed, lists):
            # print('!', lists)
            for _ in lists:
                if seed in _[0]:
                    print(f'{seed} in {_[0]} второй {_[1]=}')
                    idx_seed = _[0].index(seed)
                    print(f'Индекс {idx_seed=} ')
                    print(f'{_[1]}')
                    print(f'по этому индексу {_[1][idx_seed]=} ')
                    return _[1][idx_seed]
            else:
                return seed
    for seed in seeds:
        # проверка на вхождение
        print(ranges_src)
        val = seed_in_list(seed, ranges_src)
        print(f'{seed=} {range_src=} соответствует номеру почвы', val)
        # flag, _ = seed_in_list(seed, ranges_src)
        # if flag:
        #     # print(f'{seed=} {range_src=} соответствует номеру почвы {range_src.index(seed)=}')
        #     val = _.index(seed)
        #     # val = range_dst[range_src.index(seed)]
        # else:
        #     val = seed
        result.append(val)
    return result



data = load('test.txt')
# data = load()
data= parse_data(data)
seeds_to_soil_map = map_generator(data['seed_to_soil'], seeds=data['seeds'])
print(f'{data['seeds']=}')
print(f'{seeds_to_soil_map=}')
fertilizer_to_water_map = map_generator(data['fertilizer_to_water'], seeds=seeds_to_soil_map)
print(fertilizer_to_water_map)
# print(data)