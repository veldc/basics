'''
Write a script that takes a string from the user and creates a list of tuples with each word.
For example:

input = "hello world"
result_list = [('h', 'e', 'l', 'l', 'o'), ('w', 'o', 'r', 'l', 'd')]

'''

sent = []
sent = input("Enter a sentence: ")
sent = sent.split(' ', len(sent))
for i in range(len(sent)):
    sent[i] = tuple(sent[i])
print(sent)

