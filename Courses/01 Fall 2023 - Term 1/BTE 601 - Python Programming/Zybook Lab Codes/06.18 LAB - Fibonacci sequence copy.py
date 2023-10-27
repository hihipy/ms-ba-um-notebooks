"""
6.18 LAB: Fibonacci sequence
The Fibonacci sequence begins with 0 and then 1 follows. All subsequent values are the sum of the previous two, ex: 0, 1, 1, 2, 3, 5, 8, 13. Complete the fibonacci() function, which has an index, n (starting at 0), as a parameter and returns the nth value in the sequence. Any negative index values should return -1.

Ex: If the input is:

7
the output is:

fibonacci(7) is 13
"""

# Recursive function to find nth Fibonacci number
def fibonacci(n):
  
  # Base case 1: Negative input
  if n < 0: 
    return -1
  
  # Base case 2: 0th Fibonacci number  
  elif n == 0:
    return 0

  # Base case 3: 1st Fibonacci number
  elif n == 1:
    return 1

  # Initialize previous 2 numbers  
  prev_prev = 0
  prev = 1
  
  # Initialize current Fibonacci number 
  current = 0

  # Loop to calculate next Fibonacci numbers
  for _ in range(2, n + 1):
    current = prev + prev_prev
    prev_prev = prev
    prev = current

  # Return nth Fibonacci number
  return current

if __name__ == '__main__':

  # Take index as user input
  index = int(input())
  
  # Call fibonacci function
  result = fibonacci(index)

  # Print final result
  print(f'fibonacci({index}) is {result}')