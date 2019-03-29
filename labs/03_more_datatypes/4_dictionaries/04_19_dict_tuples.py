'''
Write a script that sorts a dictionary into a list of tuples based on values. For example:

input_dict = {"item1": 5, "item2": 6, "item3": 1}
result_list = [("item3", 1), ("item1", 5), ("item2", 6)]

'''

result_list = []
input_dict = {"item1": 5, "item2": 6, "item3": 1}
t = ()
for key, value in input_dict.items():
     t = (key, value)
     result_list.append(t)

result_list.sort(key=lambda result_list: result_list[1])

print(result_list)