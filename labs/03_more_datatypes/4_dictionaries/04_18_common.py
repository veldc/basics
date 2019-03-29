'''
Write a script that takes the following two dictionaries and creates a new dictionary by combining
the common keys and adding the values of duplicate keys together. For example:

dict_1 = {"a": 1, "b": 2, "c": 3}
dict_2 = {"a": 2, "c": 4 , "d": 2}

result = {"a": 3, "b": 2, "c": 7 , "d": 2}

'''

dict_1 = {"a": 1, "b": 2, "c": 3}
dict_2 = {"a": 2, "c": 4, "d": 2}

dist_3 = {}
for key in (dict_1.keys() | dict_2.keys()):
    if key in dict_1:
        dict_3.setdefault(key, []).extend(dict_1[key])
    if key in dict_2:
        dict_3.setdefault(key, []).extend(dict_2[key])
print(dict_3)


# dict1 = {'key1':['value11','value12','value13'] , 'key2':['value21','value22','value23']}
# dict2 = {'key1':['value14','value15'] , 'key2':['value24','value25']}
#
# dict3 = {}
# for key in (dict1.viewkeys() | dict2.keys()):
#     if key in dict1: dict3.setdefault(key, []).extend(dict1[key])
#     if key in dict2: dict3.setdefault(key, []).extend(dict2[key])
#
# print dict3