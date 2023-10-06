'''
11.8 LAB: Curve student scores
Given the name of a text file that is read from user input and contains student scores, complete a program to perform the following tasks:

Load student scores from the text file into a NumPy array.
Calculate the median and average of the student scores.
Curve the student scores by adding the difference of 100 and the maximum score (100 - max) to each score. As a result, the new maximum score would become 100.
Output the median and average scores with two digits after the decimal point.
Output the curved scores as a NumPy array. End the last output with a newline.
Follow the output format as shown in the example below.
Note: Different input text files will be used by the auto-grader. The number of student scores in each file may vary.

Ex: If the input of the program is:

scores.txt

the output is:

Median = 73.00
Average = 73.32
Curved scores = [ 70  95  84  68  98  73  67  88  73 100  79  92 100  83  98  85 100  85 77  95  99  81  69  74  75]

Note: Download scores.txt to view the text file's contents.
'''
import numpy as np  # Importing NumPy library

file_name = input()

# Load student scores from file_name into a NumPy array
scores = np.loadtxt(file_name, dtype=int)

# Calculate the median and average of student scores
median_score = np.median(scores)
average_score = np.mean(scores)

# Curve student scores
curving_value = 100 - np.max(scores)
curved_scores = scores + curving_value

# Output the median, average, and curved scores
print(f'Median = {median_score:.2f}')
print(f'Average = {average_score:.2f}')
print(f'Curved scores = {curved_scores}')