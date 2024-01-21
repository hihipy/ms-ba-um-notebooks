"""
4.13 LAB: Smallest number
Write a program whose inputs are three integers, and whose output is the smallest of the three values.

Ex: If the input is:

7
15
3
the output is:

3
"""
# This program takes three integers as input and outputs the smallest of the three values.

# Request and store the first integer input from the user.
x = int(input("Enter the first number: "))

# Request and store the second integer input from the user.
y = int(input("Enter the second number: "))

# Request and store the third integer input from the user.
z = int(input("Enter the third number: "))

# Compare the integers to determine which is the smallest.
# If x is less than or equal to both y and z, it is the smallest.
if (x <= y and x <= z):
  # Output x as it is the smallest integer among the three.
  print(x)

# If y is not greater than x or z, then y is the smallest.
elif (y <= x and y <= z):
  # Output y as it is the smallest integer among the three.
  print(y)

# If neither x nor y is the smallest, z must be the smallest.
else:
  # Output z as it is the smallest integer among the three.
  print(z)