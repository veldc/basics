'''
Write a script that "flattens" a list. For example:

starting_list = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
flattened_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

'''
flattened_list = []
starting_list = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
for i in range(len(starting_list)):
    temp_list = starting_list[i]
    flattened_list.extend(temp_list)
print(flattened_list)

