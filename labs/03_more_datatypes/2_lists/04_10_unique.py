'''
Write a script that creates a list of all unique values in a list. For example:

list_ = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]
unique_list = [55, 'hi', 4, 13]


'''

unique_list = []
start_list = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]
for i in range(len(start_list)):
    count = start_list.count(start_list[i])
    if count == 1:
        unique_list.append(start_list[i])
print(start_list)
print(unique_list)
