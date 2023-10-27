"""
2.12 LAB: Convert to dollars
Given three input values representing counts of nickels, dimes, and quarters, output the total amount as dollars and cents.

Output each floating-point value with two digits after the decimal point using the following statement:
print(f'Amount: ${dollars:.2f}')

Ex: If the input is:

3
1
4
where 3 is the number of nickels (at $0.05 each), 1 is the number of dimes (at $0.10 each), and 4 is the number of quarters (at $0.25 each), the output is:

Amount: $1.25
For simplicity, assume input is non-negative.
"""

# Get number of nickels
n = int(input())  

# Get number of dimes
d = int(input())

# Get number of quarters
q = int(input())

# Calculate total value 
# Nickels are 5 cents each
# Dimes are 10 cents each
# Quarters are 25 cents each
dollars = (.25 * q) + (.10 * d) + (.05 * n) 

# Print total formatted as currency
print(f'Amount: ${dollars:.2f}')