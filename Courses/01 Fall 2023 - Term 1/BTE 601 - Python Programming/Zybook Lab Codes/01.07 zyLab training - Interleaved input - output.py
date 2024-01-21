"""
1.7 zyLab training: Interleaved input / output
Auto-graded programming assignments have numerous advantages, but have some challenges too. Students commonly struggle with realizing that example input / output provided in an assignment's specification interleaves input and output, but the program should only output the output parts. If a program should double its input, an instructor might provide this example:

Enter x: 
5
x doubled is: 10
Students often incorrectly create a program that outputs the 5. Instead, the program should only output the output parts:

Enter x: 
x doubled is: 10
The instructor's example is showing both the output of the program, AND the user's input to that program, assuming the program is developed in an environment where a user is interacting with a program. But the program itself doesn't output the 5 (or the newline following the 5, which occurs when the user types 5 and presses enter).

Also, if the instructor configured the test cases to observe whitespace, then according to the above example, the program should output a newline after Enter x: (and possibly after the 10, if the instructor's test case expects that).

The program below incorrectly echoes the user's input to the output.

Try submitting it for grading (click "Submit mode", then "Submit for grading"). Notice that the test cases fail. The first test case's highlighting indicates that output 3 and newline were not expected. In the second test case, the -5 and newline were not expected.
Remove the code that echoes the user's input back to the output, and submit again. Now the test cases should all pass.
"""
# The program is designed to prompt the user for an integer input and output double that integer.
# It is important to note that the program should not echo the user's input, only provide the expected output.

# Output a prompt to the user; no newline is needed after this prompt because input() will follow.
print('Enter x: ', end='')

# Get input from the user and convert it to an integer.
# The input function automatically adds a newline after the user presses "Enter".
x = int(input())

# Output the description of the next value that will be printed. This is part of the expected output.
print('x doubled is:')

# Calculate x doubled by multiplying x by 2 and print the result.
# No additional text is printed here, just the result.
print(2 * x)
