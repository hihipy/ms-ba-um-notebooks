"""
4.14 LAB: Leap year
A year in the modern Gregorian Calendar consists of 365 days. In reality, the earth takes longer to rotate around the sun. To account for the difference in time, every 4 years, a leap year takes place. A leap year is when a year has 366 days: An extra day, February 29th. The requirements for a given year to be a leap year are:

1) The year must be divisible by 4

2) If the year is a century year (1700, 1800, etc.), the year must be evenly divisible by 400; therefore, both 1700 and 1800 are not leap years

Some example leap years are 1600, 1712, and 2016.

Write a program that takes in a year and determines whether that year is a leap year.

Ex: If the input is:

1712
the output is:

1712 - leap year
Ex: If the input is:

1913
the output is:

1913 - not a leap year
"""
# This program determines whether a given year is a leap year according to the Gregorian calendar rules.
# A leap year is a year with an extra day, February 29th, added to keep the calendar year synchronized
# with the astronomical year.

# Prompt the user to input a year and store the value as an integer.
input_year = int(input("Enter a year to check if it's a leap year: "))

# A year is a leap year if it is divisible by 4, except for end-of-century years, which must be divisible by 400.
# This means that the year must be divisible by 4 and not divisible by 100 unless it is also divisible by 400.
if (input_year % 4 == 0 and input_year % 100 != 0) or (input_year % 400 == 0):
    # If the conditions are met, print that the year is a leap year.
    print(f"{input_year} - leap year")
else:
    # If the conditions are not met, print that the year is not a leap year.
    print(f"{input_year} - not a leap year")
