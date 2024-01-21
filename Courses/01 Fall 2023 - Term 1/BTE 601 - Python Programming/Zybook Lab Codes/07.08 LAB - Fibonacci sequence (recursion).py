"""
7.8 LAB: Fibonacci sequence (recursion)
The Fibonacci sequence begins with 0 and then 1 follows. All subsequent values are the sum of the previous two, for example: 0, 1, 1, 2, 3, 5, 8, 13. Complete the fibonacci() function, which takes in an index, n, and returns the nth value in the sequence. Any negative index values should return -1.

Ex: If the input is:

7
the output is:

fibonacci(7) is 13
Note: Use recursion and DO NOT use any loops.
"""


def fibonacci(n):
	"""
	Recursive function to calculate the nth Fibonacci number.
	:param n: The index in the Fibonacci sequence.
	:return: The nth Fibonacci number.
  """
	# Base case for 0 and 1
	if n in [0, 1]:
		return n

	# Recursive case for positive indices
	elif n > 1:
		return fibonacci(n - 1) + fibonacci(n - 2)

	# Error case for negative indices
	else:
		return -1


if __name__ == "__main__":
	# Get user input
	start_num = int(input("Enter the index for the Fibonacci sequence: "))

	# Call the fibonacci function and store the result
	result = fibonacci(start_num)

	# Print the result
	print(f'fibonacci({start_num}) is {result}')
