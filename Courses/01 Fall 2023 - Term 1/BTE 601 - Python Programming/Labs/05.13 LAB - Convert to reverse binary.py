"""
5.13 LAB: Convert to reverse binary
Write a program that takes in a positive integer as input, and outputs a string of 1's and 0's representing the integer in reverse binary. For an integer x, the algorithm is:

As long as x is greater than 0
   Output x modulo 2 (remainder is either 0 or 1)
   Assign x with x divided by 2
Note: The above algorithm outputs the 0's and 1's in reverse order.

Ex: If the input is:

6
the output is:

011
6 in binary is 110; the algorithm outputs the bits in reverse.
"""

# Input a positive integer
num = int(input())

# Initialize an empty string to store the reverse binary representation
reverse_binary = ''

# Perform the reverse binary conversion
while num > 0:
    remainder = num % 2  # Calculate the remainder when dividing by 2
    reverse_binary += str(remainder)  # Append the remainder (0 or 1) to the string
    num //= 2  # Divide num by 2, discarding the fractional part

# Output the reverse binary representation
print(reverse_binary)