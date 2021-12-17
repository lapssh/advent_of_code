def load_data(filename='test.test'):
    with open(filename) as f:
        blades_count = int(f.readline().strip())
        blades = f.readline().strip().split()
        blades = [int(x) for x in blades]
    # print(blades_count, blades)
    return blades, blades_count


def find_password(blades, blades_count):
    unic_slide = set()
    blades = tuple(blades)
    for i in range(blades_count):
        blades = blades[1:] + blades[:1]
        # print(blades)
        unic_slide.add(blades)
    # print(unic_slide)
    return len(unic_slide)



# blades, blades_count = load_data()
blades, blades_count = load_data('advent_4.test.txt')
res = find_password(blades, blades_count)
print(res)
