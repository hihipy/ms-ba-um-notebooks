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
# This program converts a positive integer to its binary representation in reverse order.
# It follows an algorithm that repeatedly divides the number by 2 and records the remainder.

# Request and store a positive integer from the user.
num = int(input("Enter a positive integer: "))

# Initialize an empty string to hold the reverse binary digits.
reverse_binary = ''

# The loop will continue until the number is reduced to zero.
while num > 0:
    # Calculate the remainder (0 or 1) when the current number is divided by 2.
    remainder = num % 2

    # Add the string representation of the remainder to the reverse binary string.
    reverse_binary += str(remainder)

    # Update the number by integer division by 2, which discards any fractional part.
    num //= 2

# Once the loop completes, output the string of binary digits in reverse order.
print(reverse_binary)
