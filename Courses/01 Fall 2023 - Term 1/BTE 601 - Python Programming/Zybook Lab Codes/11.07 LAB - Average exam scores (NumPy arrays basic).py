"""
11.7 LAB: Average exam scores (NumPy arrays basic)
Write a program that reads two sets of exam scores of five students from user input and stores the scores into two NumPy arrays (exam1 and exam2). The program then calculates the average of the two exams for each of the five students and outputs the average scores as a NumPy array. The program finally counts the number of average scores that are 80 or higher and outputs the count.

Ex: If the input of the two sets of scores are:

75 80 65 82 92
88 85 75 95 73
where [75 80 65 82 92] is stored in NumPy array exam1, and [88 85 75 95 73] is stored in NumPy array exam2. The program then outputs:

Average scores: [81.5 82.5 70.  88.5 82.5]
Number of students who received 80 and above: 4
"""
import numpy as np


def read_exam_scores():
    """
    Reads two sets of exam scores from user input and stores them in NumPy arrays.
    :return: Two NumPy arrays containing exam scores.
    """
    exam1 = np.array(input("Enter exam 1 scores: ").split(), dtype=float)
    exam2 = np.array(input("Enter exam 2 scores: ").split(), dtype=float)
    return exam1, exam2


def calculate_average_scores(exam1, exam2):
    """
    Calculates the average of two sets of exam scores.
    :param exam1: NumPy array of the first set of exam scores.
    :param exam2: NumPy array of the second set of exam scores.
    :return: NumPy array of average scores.
    """
    return (exam1 + exam2) / 2


def count_high_scores(average_scores, threshold=80):
    """
    Counts the number of scores that are equal to or above a threshold.
    :param average_scores: NumPy array of average scores.
    :param threshold: The threshold value to count scores above (default is 80).
    :return: Count of scores above the threshold.
    """
    return np.sum(average_scores >= threshold)


def main():
    """
    Main function to execute the program.
    """
    exam1, exam2 = read_exam_scores()
    average_scores = calculate_average_scores(exam1, exam2)

    print(f'Average scores: {average_scores}')

    count_80_above = count_high_scores(average_scores)
    print(f'Number of students who received 80 and above: {count_80_above}')


if __name__ == "__main__":
    main()
