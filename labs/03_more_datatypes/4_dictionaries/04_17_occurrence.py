'''
Write a script that takes a string from the user and creates a dictionary of letter that exist
in the string and the number of times they occur. For example:

user_input = "hello"
result = {"h": 1, "e": 1, "l": 2, "o": 1}

'''

str = list(input("Enter sentence: "))
print(str)
undouble_list = list(set(str))
print(undouble_list)
result = {}
for i in undouble_list:
    result[i] = str.count(i)
print(result)
