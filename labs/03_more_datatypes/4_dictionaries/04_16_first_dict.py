'''
Write a script that creates a dictionary of keys, n and values n*n for numbers 1-10. For example:

result = {1: 1, 2: 4, 3: 9, ...and so on}

'''


result = {}
for i in range(1,10):
    result[i] = i*i
print(result)