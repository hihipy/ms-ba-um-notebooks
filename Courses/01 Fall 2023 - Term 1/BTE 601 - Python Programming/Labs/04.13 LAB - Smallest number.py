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

x = int(input())
y = int(input())
z = int(input())

if (x <= y and x <= z):
    print(x)

elif (y <= x and y <= z):
    print(y)

else:
    print(z)