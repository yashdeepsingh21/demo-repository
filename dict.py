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

test_list = ["Gfg", "is", "Good", "for", "Geeks"]
test_dict = {"Gf": 5, "Best": 6}
K = "Gfg"


def get_keys_value(test_list, test_dict, K):
    test_list = test_list
    test_dict = test_dict
    K = K
    result = None
    for value in test_list:
        if K == value:
            test_list = True
            break

    if test_list == True:
        for key in test_dict.keys():
            if K == key:
                result = test_dict[K]
                break
        if result:
            return f"{K} is present in list and has value {result}"
        else:
            return f"{K} is present in list but not in dict"
    else:
        return f"{K} is not present in list"


print(get_keys_value(test_list, test_dict, K))
