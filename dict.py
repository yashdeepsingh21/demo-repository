# problem number one

test_dict = {'Gfg': 4, 'best': 9}
test_list = [8, 2]

result_dict = {}
count = 0
for key, value in test_dict.items():
    result_dict[test_list[count]] = {key: value}
    count += 1

print(result_dict)
