'''
Write a script that takes three strings from the user and prints the one with the most characters.

'''

st1 = input("Enter a sentence: ")
count = len(st1)
st2 = input("Enter a second sentence: ")
if len(st2) > count:
    count = len(st2)
st3 = input("Enter a third sentence: ")
if len(st3) > count:
    count = len(st3)

print (count)