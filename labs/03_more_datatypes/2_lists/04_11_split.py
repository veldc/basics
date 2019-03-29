'''
Write a script that takes in a string from the user. Using the split() method,
create a list of all the words in the string and print the word with the most
occurrences.

'''

sent = input("Enter a sentence: ")
sent_list = sent.split()
sorted_list = sorted(sent_list, key=len)
print(sorted_list[0])
