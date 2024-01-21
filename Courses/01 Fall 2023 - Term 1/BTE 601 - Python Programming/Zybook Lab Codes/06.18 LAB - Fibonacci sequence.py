"""
6.18 LAB: Fibonacci sequence
The Fibonacci sequence begins with 0 and then 1 follows. All subsequent values are the sum of the previous two, ex: 0, 1, 1, 2, 3, 5, 8, 13. Complete the fibonacci() function, which has an index, n (starting at 0), as a parameter and returns the nth value in the sequence. Any negative index values should return -1.

Ex: If the input is:

7
the output is:

fibonacci(7) is 13
"""
# This program computes the nth value in the Fibonacci sequence where n is provided by the user.
# The Fibonacci sequence starts with 0, 1, and each subsequent number is the sum of the previous two.


def fibonacci(n):
    """
    Calculate the nth Fibonacci number.

    Args:
    n (int): The index (starting at 0) to compute in the Fibonacci sequence.

    Returns:
    int: The nth Fibonacci number, or -1 for negative index.
    """
    # If the index is negative, return -1 as it is not a valid position in the sequence.
    if n < 0:
        return -1
    # The first number in the Fibonacci sequence is 0.
    elif n == 0:
        return 0
    # The second number in the Fibonacci sequence is 1.
    elif n == 1:
        return 1

    # Initialize variables to store the two previous Fibonacci numbers and the current one.
    prev_prev = 0  # Represents F(n-2)
    prev = 1       # Represents F(n-1)
    current = 0    # Represents F(n)

    # Loop to calculate Fibonacci from the 3rd term onwards.
    for _ in range(2, n + 1):
        current = prev + prev_prev  # Current Fibonacci number is the sum of the previous two.
        prev_prev = prev            # Update F(n-2) to F(n-1) for the next iteration.
        prev = current              # Update F(n-1) to F(n) for the next iteration.

    # Return the nth Fibonacci number.
    return current


# The main part of the script that gets executed when the script is run directly.
if __name__ == '__main__':
    # Prompt the user for the index n and convert the input to an integer.
    index = int(input("Enter the index for the Fibonacci sequence: "))

    # Call the fibonacci function and store the result.
    result = fibonacci(index)

    # Print the result in the format "fibonacci(n) is result".
    print(f'fibonacci({index}) is {result}')
