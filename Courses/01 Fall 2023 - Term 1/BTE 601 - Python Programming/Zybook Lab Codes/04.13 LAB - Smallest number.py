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

# Get three integer inputs
x = int(input())
y = int(input()) 
z = int(input())

# Check which value is smallest
if (x <= y and x <= z):
  # If x is smallest, print x
  print(x) 

elif (y <= x and y <= z):
  # If y is smallest, print y
  print(y)

else:
  # Otherwise z must be smallest, print z
  print(z)