'''
Write a script that takes a string of words and a symbol from the user.
Replace all occurrences of the first letter with the symbol. For example:

String input: more python programming please
Symbol input: #
Result: #ore python progra##ing please

'''


OrgInput = input("Enter a sentence: ")
Charac = input("Enter charactar to replace")
SymbolInput = input("Enter symbol to replace")
ModInput = OrgInput.replace(Charac, SymbolInput)
print(ModInput)