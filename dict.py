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

# test_dict = {'a': {'b': {}}, 'd': {'e': {}}, 'f': {'g': {}}}
#
# result_dict = {}
#
# for key, value in test_dict.items():
#     result_dict[list(value.keys())[0]] = {key: list(value.values())[0]}
#
# print(result_dict)

# Python – Extract Key’s Value, if Key Present in List and Dictionary
#
# test_list = ["Gfg", "is", "Good", "for", "Geeks"]
# test_dict = {"Gf": 5, "Best": 6}
# K = "Gfg"
#
#
# def get_keys_value(test_list, test_dict, K):
#     test_list = test_list
#     test_dict = test_dict
#     K = K
#     result = None
#     for value in test_list:
#         if K == value:
#             test_list = True
#             break
#
#     if test_list == True:
#         for key in test_dict.keys():
#             if K == key:
#                 result = test_dict[K]
#                 break
#         if result:
#             return f"{K} is present in list and has value {result}"
#         else:
#             return f"{K} is present in list but not in dict"
#     else:
#         return f"{K} is not present in list"
#
#
# print(get_keys_value(test_list, test_dict, K))


# Python – Remove keys with Values Greater than K ( Including mixed values )

# test_dict = {'Gfg': 3, 'is': 7, 'best': 10, 'for': 6, 'geeks': 'CS'}
#
# K = 6
#
#
# def remove_key_greater_than_K(test_dict, K):
#     result = {}
#     for key, value in test_dict.items():
#         print(type(value), value)
#         if type(value) != type(K):
#             result[key] = value
#         elif value <= K:
#             result[key] = value
#     return result
#
#
# print(remove_key_greater_than_K(test_dict, K))

# Python – Remove keys with substring values

# test_dict = {1: 'Gfg is git ', 2: 'Gfg is stash'}
# sub_list = ['git', 'stash']
#
#
# def remove_keys(test_dict, sub_list):
#     result = {}
#     for key, value in test_dict.items():
#         list_value = value.split(" ")
#         flag = False
#         for i in sub_list:
#             print(i, list_value)
#             if i in list_value:
#                 flag = True
#                 break
#         if flag == False:
#             result[key] = value
#
#     return result
#
#
# print(remove_keys(test_dict, sub_list))

# Python – Dictionary with maximum count of pairs

# test_list = [{'gfg': 2, 'best': 4}, {'gfg': 2, 'is': 3, 'best': 4, 'CS': 9, "abc": 1}, {'gfg': 2}]
#
# max = len(test_list[0])
# for i in test_list:
#     if len(i) > max:
#         max = len(i)
#
# print(max)

# Python – Append Dictionary Keys and Values ( In order ) in dictionary

# test_dict = {"Gfg": 1, 'is': 2, 'Best': 3}
#
# all_keys = []
# all_values = []
#
# for key, value in test_dict.items():
#     all_keys.append(key)
#     all_values.append(value)
#
# print(all_keys+all_values)


# Python – Extract Unique values dictionary values

# test_dict = {'gfg': [5, 6, 7, 8], 'is': [10, 11, 7, 5], 'best': [6, 12, 10, 8], 'for': [1, 2, 5]}
#
# result = []
#
# for value in test_dict.values():
#     result += value
#
# result_set = set(result)
#
# print(list(result_set))

# Python – Keys associated with Values in Dictionary

test_dict = {'gfg': [1, 2, 3], 'is': [1, 4], 'best': [4, 2]}

result = []

for value in test_dict.values():
    result += value

data = list(set(result))

data.sort()

# print(data)

output = {}

for value in data:
    list_value = []
    for key, values in test_dict.items():
        if value in values:
            list_value.append(key)
            output[value] = list_value

print(output)
