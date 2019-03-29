'''
Write a script that takes a string of words and a letter from the user.
Find the index of first occurrence of the letter in the string. For example:

String input: hello world
Letter input: o
Result: 4

'''

st = input("Enter sentence: ")
letter = input("Enter letter: ")
occ = st.find(letter)
print(occ)