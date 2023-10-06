"""
6.18 LAB: Fibonacci sequence
The Fibonacci sequence begins with 0 and then 1 follows. All subsequent values are the sum of the previous two, ex: 0, 1, 1, 2, 3, 5, 8, 13. Complete the fibonacci() function, which has an index, n (starting at 0), as a parameter and returns the nth value in the sequence. Any negative index values should return -1.

Ex: If the input is:

7
the output is:

fibonacci(7) is 13
"""

def fibonacci(n):
    if n < 0:
        return -1
    elif n == 0:
        return 0
    elif n == 1:
        return 1

    prev_prev = 0
    prev = 1
    current = 0
    for _ in range(2, n + 1):
        current = prev + prev_prev
        prev_prev = prev
        prev = current

    return current

if __name__ == '__main__':
    index = int(input())
    result = fibonacci(index)
    print(f'fibonacci({index}) is {result}')