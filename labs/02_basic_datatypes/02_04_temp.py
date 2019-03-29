'''
Fahrenheit to Celsius:

Write the necessary code to read a degree in Fahrenheit from the console
then convert it to Celsius and print it to the console.

    C = (F - 32) * (5 / 9)

Output should read like - "81.32 degrees fahrenheit = 27.4 degrees celsius"


'''

Farh = float(input("Enter degree Farh: "))
Celsius = (Farh-32)*(5/9)
print (Farh, "degress fahrenheid = ",Celsius, "degress celsius")