'''

Demonstrate how to:

    1) Convert an int to a float
    2) Convert a float to an int
    3) Perform floor division using a float and an int.
    4) Use two user inputted values to perform multiplication.

    Take note of what information is lost when some conversions take place.

'''
# int to float
Num = 8
Div = float(Num)
print(Div)

# float to int
Num = 8
Div = 10
devision = int(Num/Div)
print(devision)

#Floor division
NumInt = 30
NumFl = 9.3
print(NumInt//NumFl)

'''#user input int
InputUser1 = int(input("Enter number: "))
InputUser2 = int(input("Enter another number: "))
Multi=(InputUser1*InputUser2)
print(Multi)'''

#user input float
InputUser1 = float(input("Enter number: "))
InputUser2 = float(input("Enter another number: "))
Multi=int((InputUser1*InputUser2))
print(Multi)