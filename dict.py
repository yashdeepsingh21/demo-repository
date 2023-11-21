# problem number one
#
# test_dict = {'Gfg': 4, 'best': 9}
# test_list = [8, 2]
#
# result_dict = {}
# count = 0
# for key, value in test_dict.items():
#     result_dict[test_list[count]] = {key: value}
#     count += 1
#
# print(result_dict)

# Python – Swapping Hierarchy in Nested Dictionaries

# test_dict = {'Gfg': {'best' : [1, 3, 4]}}
#
# result_dict = {}
#
# key = None
#
# value = None
#
# for keys , values in test_dict.items():
#     key = keys
#     value = values
#     break
#
# for keys, values in value.items():
#     result_dict[keys] = {key: values}
#
# print(result_dict)

# Python – Inversion in nested dictionary ~~~~important~~~~

test_dict = {'a': {'b': {}}, 'd': {'e': {}}, 'f': {'g': {}}}

result_dict = {}

for key, value in test_dict.items():
    result_dict[list(value.keys())[0]] = {key: list(value.values())[0]}

print(result_dict)
