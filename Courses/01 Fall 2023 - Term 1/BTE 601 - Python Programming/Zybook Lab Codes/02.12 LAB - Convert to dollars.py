"""
2.12 LAB: Convert to dollars
Given three input values representing counts of nickels, dimes, and quarters, output the total amount as dollars and cents.

Output each floating-point value with two digits after the decimal point using the following statement:
print(f'Amount: ${dollars:.2f})

Ex: If the input is:

3
1
4
where 3 is the number of nickels (at $0.05 each), 1 is the number of dimes (at $0.10 each), and 4 is the number of quarters (at $0.25 each), the output is:

Amount: $1.25
For simplicity, assume input is non-negative.
"""
# This program calculates the total dollar amount based on the number of coins input by the user.
# It considers nickels, dimes, and quarters, then outputs the total in dollars and cents.

# Prompt the user for the number of nickels and store the input as an integer.
# A nickel is worth 5 cents.
nickels = int(input("Enter the number of nickels: "))

# Prompt the user for the number of dimes and store the input as an integer.
# A dime is worth 10 cents.
dimes = int(input("Enter the number of dimes: "))

# Prompt the user for the number of quarters and store the input as an integer.
# A quarter is worth 25 cents.
quarters = int(input("Enter the number of quarters: "))

# Calculate the total dollar value by converting each count of coins to its value in dollars.
# The total is the sum of the values of nickels, dimes, and quarters.
# We multiply the number of each type of coin with its respective value in dollars:
# - Each nickel is 0.05 dollars
# - Each dime is 0.10 dollars
# - Each quarter is 0.25 dollars
total_dollars = (0.25 * quarters) + (0.10 * dimes) + (0.05 * nickels)

# Output the total amount formatted as a currency with two digits after the decimal point.
# The formatting directive :.2f limits the float to two decimal places.
print(f'Amount: ${total_dollars:.2f}')
