'''
11.7 LAB: Average exam scores (NumPy arrays basic)
Write a program that reads two sets of exam scores of five students from user input and stores the scores into two NumPy arrays (exam1 and exam2). The program then calculates the average of the two exams for each of the five students and outputs the average scores as a NumPy array. The program finally counts the number of average scores that are 80 or higher and outputs the count.

Ex: If the input of the two sets of scores are:

75 80 65 82 92
88 85 75 95 73
where [75 80 65 82 92] is stored in NumPy array exam1, and [88 85 75 95 73] is stored in NumPy array exam2. The program then outputs:

Average scores: [81.5 82.5 70.  88.5 82.5]
Number of students who received 80 and above: 4
'''
import numpy as np  # Importing NumPy library

# Read two sets of exam scores of five students from user input and store the scores into two NumPy arrays
exam1 = np.array(input().split(), dtype=float)
exam2 = np.array(input().split(), dtype=float)

# Compute the average scores for each of the five students
average_scores = (exam1 + exam2) / 2

# Output "Average scores: " followed by the NumPy array of the average scores
print(f'Average scores: {average_scores}')

# Count the number of average scores that are >= 80
count_80_above = np.sum(average_scores >= 80)

# Output "Number of students who received 80 and above: " followed by the count
print(f'Number of students who received 80 and above: {count_80_above}')
