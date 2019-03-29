'''
Take in the following three values from the user:
    - investment amount
    - interest rate in percentage
    - number of years to invest

Print the future values to the console.

'''
import math

UserInvestAmount = float(input("Enter your investment amount: "))
UserInterestRate = float(input("Enter your interest rate in percentage: "))/100
UserInvestYears = int(input("Enter number of years to invest: "))

for i in range(UserInvestYears+1):

    print ("Year ", i, ": ", UserInvestAmount*pow((1+UserInterestRate),i))
