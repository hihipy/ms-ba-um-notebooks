'''
7.8 LAB: Fibonacci sequence (recursion)
The Fibonacci sequence begins with 0 and then 1 follows. All subsequent values are the sum of the previous two, for example: 0, 1, 1, 2, 3, 5, 8, 13. Complete the fibonacci() function, which takes in an index, n, and returns the nth value in the sequence. Any negative index values should return -1.

Ex: If the input is:

7
the output is:

fibonacci(7) is 13
Note: Use recursion and DO NOT use any loops.
'''

# Recursive function to calculate nth Fibonacci number
def fibonacci(n):

  # Base case
  if n == 1 or n == 0:  
    return n
  
  # Recursive case
  elif n > 1:
    return (fibonacci(n-1) + fibonacci(n-2))

  # Error case  
  else: 
    return -1 # Return -1 for any negative index
  
if __name__ == "__main__":

  # Get user input
  start_num = int(input())  

  # Call fibonacci function
  result = fibonacci(start_num)

  # Print result
  print(f'fibonacci({start_num}) is {result}')