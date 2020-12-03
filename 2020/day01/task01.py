def get_data_from_file():
    with open('nums.txt', 'r') as f:
        nums = f.readlines()
        result = [int(item) for item in nums]
        return result
# ищем пару чисел, сумма которой равна 2020, и выводим произведение
nums  =get_data_from_file()
pairs2020 = []
print(nums)
while nums:
    first = nums.pop(0)
    for num in nums:
        if first+num == 2020:
            pairs2020.append([first, num])

print(pairs2020)
print(pairs2020[0][0] * pairs2020[0][1])

# теперь ищем тройкиу таких числе
nums = get_data_from_file()
while nums:
    first = nums.pop(0)
    for i in nums:
        for j in nums:
            if first + i + j == 2020:
                pairs2020.append([first,i , j])
                break
print(pairs2020)
print(pairs2020[1][0] * pairs2020[1][1] * pairs2020[1][2])