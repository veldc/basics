'''

Write a script that removes all duplicates from a list.

'''

List = ['A', 'A', 'B']
List = list(dict.fromkeys(List))
print(List)

#Sets are unordered collections of distinct objects. T

ListB = [1, 2, 3, 4, 2, 3, 4]
NewListB = list(set(ListB))
print(NewListB)
