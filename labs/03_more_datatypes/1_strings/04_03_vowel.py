'''
Write a script prints the number of times a vowel is used in a user inputted string.

'''

count = 0
counta = 0
#counte, countu, counto, counti = 0

st = input("Enter a sentence: ").lower()
for char in st:
    if char in 'aeuoi':
        count += 1
    if char in 'a':
        counta += 1
print(count)
print(counta)

